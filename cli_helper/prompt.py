import os
from pathlib import Path
import inquirer


def nested_prompt(data: dict, _root: bool = True) -> any:
    os.system("clear")
    selection = data
    while type(selection) == dict:
        opt_dict = []
        opt_any = []
        for key, value in data.items():
            if type(value) is dict:
                sel = ("--> " + key, value)
                opt_dict.append(sel)
            else:
                sel = (" * " + key, value)
                opt_any.append(sel)
        options = opt_dict + opt_any
        if not _root:
            options.append(("<-- back", None))
        question = [
            inquirer.List(
                "template", message="Template Menu", choices=options, carousel=True
            ),
        ]
        answer = inquirer.prompt(question)
        if answer["template"] == None:
            return None
        nest = nested_prompt(answer["template"], False)
        if nest != None:
            selection = nest
    return selection

def file_select_prompt(data: Union[str, Path]) -> Path:
    pass
