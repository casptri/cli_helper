import os
import inquirer

def nested_prompt(data: dict) -> any:
    ret = None
    while not ret:
        selection = [("<-- back", None) ]
        for key, value in data.items():
            if type(value) is dict:
                sel = ("--> " + key, value)
                selection.append(sel)
            else:
                sel = (" * " + key, value)
                selection.append(sel)
        question = [
            inquirer.List(
                "template", message="Template Menu", choices=selection, carousel=True
            ),
        ]
        answer = inquirer.prompt(question)
        ret = answer["template"]
        if type(ret) is dict:
            ret = nested_prompt(ret)
    return sel
