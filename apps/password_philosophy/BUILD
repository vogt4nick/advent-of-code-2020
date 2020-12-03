load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "bin",
    srcs = ["__main__.py"],
    data = ["data/input.txt"],
    main = "__main__.py",
    deps = ["//libs/password_philosophy:lib"],
)
