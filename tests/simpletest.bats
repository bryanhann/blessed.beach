load $BATS_LIB/bats-support/load.bash
load $BATS_LIB/bats-assert/load.bash

@test "this is a test" {
    run FOO }die 3
    assert_failure
}
