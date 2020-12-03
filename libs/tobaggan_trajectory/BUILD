load("@rules_python//python:defs.bzl", "py_library", "py_test")

py_library(
    name = "lib",
    srcs = ["__init__.py"],
    data = ["data/input.txt"],
    visibility = ["//:tobaggan_trajectory"],
)

py_test(
    name = "test",
    timeout = "short",
    srcs = ["tests/test_tobaggan_trajectory.py"],
    local = True,
    main = "tests/test_tobaggan_trajectory.py",
    deps = [":lib"],
)

py_test(
    name = "test_solutions",
    timeout = "short",
    srcs = ["tests/test_solutions.py"],
    local = True,
    main = "tests/test_solutions.py",
    deps = [":lib"],
)
