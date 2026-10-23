#!/usr/bin/env python3
"""Validate structural invariants in the draft DPM protocol YAML.

This checks configuration shape only. It does not certify scientific validity,
and the current protocol is not consumed by an experiment runner.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def _construct_unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in mapping
        except TypeError:
            fail("mapping keys must be hashable scalars")
        if duplicate:
            fail(f"duplicate YAML mapping key: {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


REQUIRED_TOP_LEVEL = {
    "seed",
    "episodes",
    "interventions",
    "splits",
    "metrics",
    "notes",
}
ALLOWED_TOP_LEVEL = REQUIRED_TOP_LEVEL


def fail(message: str) -> None:
    print(f"protocol validation error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("configs/protocol.yaml")
    try:
        with path.open("r", encoding="utf-8") as stream:
            config = yaml.load(stream, Loader=UniqueKeyLoader)
    except (OSError, yaml.YAMLError) as exc:
        fail(f"cannot read valid YAML from {path}: {exc}")

    if not isinstance(config, dict):
        fail("top-level YAML value must be a mapping")

    missing = REQUIRED_TOP_LEVEL - config.keys()
    unexpected = config.keys() - ALLOWED_TOP_LEVEL
    if missing:
        fail(f"missing top-level keys: {', '.join(sorted(missing))}")
    if unexpected:
        fail(f"unknown top-level keys: {', '.join(sorted(unexpected))}")

    seed = config["seed"]
    if isinstance(seed, bool) or not isinstance(seed, int):
        fail("seed must be an integer")

    episodes = config["episodes"]
    if not isinstance(episodes, dict):
        fail("episodes must be a mapping")
    if set(episodes) != {"train", "evaluation"}:
        fail("episodes must contain exactly train and evaluation")
    for key in ("train", "evaluation"):
        value = episodes.get(key)
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            fail(f"episodes.{key} must be a positive integer")

    interventions = config["interventions"]
    clamp = interventions.get("mediator_clamp") if isinstance(interventions, dict) else None
    if not isinstance(interventions, dict) or set(interventions) != {"mediator_clamp"}:
        fail("interventions must contain only mediator_clamp")
    if not isinstance(clamp, dict) or set(clamp) != {"enabled", "values"}:
        fail("interventions.mediator_clamp must contain exactly enabled and values")
    if not isinstance(clamp.get("enabled"), bool):
        fail("interventions.mediator_clamp.enabled must be boolean")
    values = clamp.get("values")
    if not isinstance(values, list) or len(values) < 2:
        fail("interventions.mediator_clamp.values must contain at least two levels")
    if not all(
        isinstance(value, (str, int, float)) and not isinstance(value, bool)
        for value in values
    ):
        fail("mediator clamp values must be non-null scalar strings or numbers")
    if len({(type(value).__name__, value) for value in values}) != len(values):
        fail("mediator clamp values must be unique")

    splits = config["splits"]
    contexts = splits.get("contexts") if isinstance(splits, dict) else None
    if not isinstance(splits, dict) or set(splits) != {"contexts"}:
        fail("splits must contain only contexts")
    if not isinstance(contexts, dict) or set(contexts) != {"train", "held_out"}:
        fail("splits.contexts must contain exactly train and held_out")
    train = contexts.get("train")
    held_out = contexts.get("held_out")
    if not isinstance(train, list) or not isinstance(held_out, list):
        fail("splits.contexts.train and held_out must be lists")
    if not all(isinstance(item, str) and item.strip() for item in train + held_out):
        fail("context identifiers must be non-empty strings")
    if len(set(train)) != len(train) or len(set(held_out)) != len(held_out):
        fail("context identifiers must be unique within each split")
    overlap = set(train) & set(held_out)
    if overlap:
        fail(f"train and held-out contexts overlap: {', '.join(sorted(overlap))}")

    metrics = config["metrics"]
    if not isinstance(metrics, list) or not metrics:
        fail("metrics must be a non-empty list")
    if not all(isinstance(metric, str) and metric.strip() for metric in metrics):
        fail("each metric must be a non-empty string")
    if len(set(metrics)) != len(metrics):
        fail("metric names must be unique")

    notes = config["notes"]
    if not isinstance(notes, list) or not all(isinstance(note, str) for note in notes):
        fail("notes must be a list of strings")

    print(f"Protocol structure valid: {path}")
    print("Note: this validates file structure, not scientific readiness or model behavior.")


if __name__ == "__main__":
    main()
