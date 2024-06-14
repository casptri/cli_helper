#!/usr/bin/env python3
# Authors: Trittibach Caspar
#
# Helper class to create awesome cli's

import inspect
import logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class EventHandler(PatternMatchingEventHandler):
    def __init__(self):
        super(EventHandler, self).__init__(patterns=["*.py"],ignore_patterns=["*.swp","*~"])

    #def on_any_event(self, event):
    #    print(event)

    #def on_deleted(self, event):
    #    print(event)

    def on_modified(self, event):
        print(event)

class ClassWatcher:
    def __init__(self, path):
        self.obs = Observer()
        event_handler = EventHandler()
        #self.obs.schedule(EventHandler, path)
        self.obs.schedule(event_handler, path, recursive=True)
        self.obs.start()

    def close(self):
        self.obs.stop()

class TermCreater:
    history = []

    def __init__(self, cl):
        self.cl = cl
        self.inst = cl()

    def _get_func_list(self):
        funcs = []
        function_list = inspect.getmembers(self.cl, predicate=inspect.isfunction)
        for name, func in function_list:
            if name.startswith("_"):
                continue
            doc = inspect.getdoc(func)
            sig = inspect.signature(func)
            funcs.append({'name': name, 'doc': doc, 'sig': sig})
        return funcs

    def print_help(self):
        funcs = self._get_func_list()
        for f in funcs:
            name = f['name']
            doc = f['doc']
            sig = f['sig']
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
