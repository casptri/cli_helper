import os
import inquirer

def nested_prompt(data: dict) -> any:
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
        if parent:
            options.append(("<-- back", None))
        question = [
            inquirer.List(
                "template", message="Template Menu", choices=options, carousel=True
            ),
        ]
        answer = inquirer.prompt(question)
        if answer["template"] == None:
            return None
        nest = nested_prompt(answer["template"])
        if nest != None:
            selection = nest
    return selection
