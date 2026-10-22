.PHONY: help protocol-test protocol-check cpp-configure cpp-build cpp-test check

help:
	@printf '%s\n' \
	  'protocol-check  Validate the draft protocol YAML' \
	  'protocol-test   Run protocol validator regression tests' \
	  'cpp-configure   Configure the C++ project' \
	  'cpp-build      Build the C++ project' \
	  'cpp-test       Run CTest' \
	  'check          Run protocol checks and native tests'

protocol-check:
	python scripts/validate_protocol.py configs/protocol.yaml

protocol-test:
	python -m unittest discover -s tests -p 'test_protocol_validator.py' -v

cpp-configure:
	cmake -S . -B build -DCMAKE_BUILD_TYPE=Release

cpp-build: cpp-configure
	cmake --build build --parallel

cpp-test: cpp-build
	ctest --test-dir build --output-on-failure

check: protocol-check protocol-test cpp-test
