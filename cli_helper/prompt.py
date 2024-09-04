import os
import inquirer

def nested_prompt(data: dict) -> any:
    selection = [("<-- back", data) ]
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
    print(ret)
    for e in ret:
        print(type(e))
    if type(ret[1]) is dict:
        sel = nested_prompt(ret[1])
    return sel
