#!/usr/bin/env python3
# Authors: Trittibach Caspar
#
# Helper class to create awesome cli's

import inspect


class TermCreater:
    history = []

    def __init__(self, cl):
        self.cl = cl
        self.inst = cl()

    def print_help(self):
        function_list = inspect.getmembers(self.cl, predicate=inspect.isfunction)
        for name, func in function_list:
            if name.startswith("_"):
                continue
            if name != "__init__":
                doc = inspect.getdoc(func)
                sig = inspect.signature(func)
                print(f"{name}: {doc}\n    {sig}\n")

    def clear_history(self):
        self.history.clear()

    def print_history(self):
        for e in self.history:
            print(e)

    def run(self, value=""):
        arg = value.split("--")
        cmd_dict = {}
        for a in arg[1:]:
            c = a.split(" ")
            cmd_dict.update({c[0]: c[1]})
        cmd = arg[0].split(" ")[0]
        if not hasattr(self.cl, cmd):
            self.print_help()
            return
        self.history.append(value)
        func = getattr(self.cl, cmd)
        result = func(self.inst, **cmd_dict)
        if result:
            print(result)
