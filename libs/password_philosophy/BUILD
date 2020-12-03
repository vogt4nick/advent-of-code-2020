load("@rules_python//python:defs.bzl", "py_library", "py_test")

py_library(
    name = "lib",
    srcs = ["__init__.py"],
    visibility = ["//:password_philosophy"],
)

py_test(
    name = "test",
    timeout = "short",
    srcs = ["tests/test_password_philosophy.py"],
    local = True,
    main = "tests/test_password_philosophy.py",
    deps = [":lib"],
)
