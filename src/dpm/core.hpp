#pragma once

namespace dpm {

// Initial public API placeholder. Scientific update rules are intentionally
// unspecified until the experimental protocol is finalized.
struct CoreScaffold {
    [[nodiscard]] static constexpr const char* project_name() noexcept {
        return "Developmental Plasticity Mediation";
    }
};

}  // namespace dpm
