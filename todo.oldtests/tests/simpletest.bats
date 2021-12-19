load $BATS_LIB/bats-support/load.bash
load $BATS_LIB/bats-assert/load.bash
@test "called with }die 42" {
    run blessed.foo }die 42
    [ $status = 42 ]
}
@test "sourced with }die 42" {
    run . blessed.foo }die 42
    [ $status = 42 ]
}

