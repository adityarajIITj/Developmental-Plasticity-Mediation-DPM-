#include "dpm/core.hpp"

#include <cassert>

int main() {
    assert(dpm::CoreScaffold::project_name()[0] == 'D');
    return 0;
}
