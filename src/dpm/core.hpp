#pragma once

namespace dpm {

// Stable identity for the initial scaffold. This is not a model interface.
struct CoreScaffold {
    [[nodiscard]] static constexpr const char* project_name() noexcept {
        return "Developmental Plasticity Mediation";
    }
};

}  // namespace dpm
