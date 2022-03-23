#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""Examines modules for the presence of similar functions or methods"""

import sys
from importlib import import_module
import inspect
import textwrap
import ast
from difflib import SequenceMatcher

RATIO_LEVEL = 0.95


def module_parser(module, name):
    res = {}
    all_memb = inspect.getmembers(module)
    for name0, value in all_memb:
        if inspect.isclass(value) and not name0.startswith("__"):
            res.update(module_parser(value, f"{name}.{name0}"))
        if inspect.isfunction(value):
            code = inspect.getsource(value)
            if "." in name:
                code = textwrap.dedent(code)
            tree = ast.parse(code)
            for node in ast.walk(tree):
                for attr in ["name", "id", "arg", "attr"]:
                    if hasattr(node, attr):
                        setattr(node, attr, "_")

            prepared_text = ast.unparse(tree)
            res.update({f"{name}.{name0}": prepared_text})
    return res


def main():
    functions = {}
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Incorrect number of arguments")
        return 1
    for i in range(1, len(sys.argv)):
        module = import_module(sys.argv[i])
        tmp = module_parser(module, sys.argv[i])
        functions.update(tmp)
    funcs_name = sorted(functions.keys())

    for i, f1 in enumerate(funcs_name):
        for f2 in funcs_name[i + 1 :]:
            if SequenceMatcher(None, functions[f1], functions[f2]).ratio() > RATIO_LEVEL:
                print(f1, ":", f2)
    print(functions, sep="\n")


if __name__ == "__main__":
    sys.exit(main())
