#include "dpm/core.hpp"

#include <iostream>
#include <string_view>

int main() {
    constexpr std::string_view expected = "Developmental Plasticity Mediation";
    const std::string_view actual = dpm::CoreScaffold::project_name();

    if (actual != expected) {
        std::cerr << "Unexpected project name: " << actual << '\n';
        return 1;
    }

    return 0;
}
