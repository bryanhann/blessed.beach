#!/bin/bash
@test "mul result" {
    .bl.beach-demo maths mul 2 3  | grep "result: 5"
}

@test "maths doc" {
    .bl.beach-demo maths -h | grep "mul - undocumented"
}

