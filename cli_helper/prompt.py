import os
import inquirer

def nested_prompt(data: dict, parent: any = None, level = 0) -> any:
    level += 1
    selection = data
    while type(selection) == dict:
        options = []
        if parent:
            options.append(("<-- back", None))
        for key, value in data.items():
            if type(value) is dict:
                sel = ("--> " + key, value)
                options.append(sel)
            else:
                sel = (" * " + key, value)
                options.append(sel)
        question = [
            inquirer.List(
                "template", message="Template Menu", choices=options, carousel=True
            ),
        ]
        answer = inquirer.prompt(question)
        if answer["template"] == None:
            return None
        nest = nested_prompt(answer["template"], data, level)
        if nest != None:
            selection = nest
    return selection
