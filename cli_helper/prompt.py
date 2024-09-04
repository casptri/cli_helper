import os
import inquirer

def prompt_dict(data: dict):
    #os.system("clear")
    selection = []
    for key, value in data.items():
        print(type(value))
        if type(value) is dict:
            sel = ("--> " + key, key)
            selection.append(sel)
        else:
            sel = (" * " + key, key)
            selection.append(sel)
    print(selection)
    question = [
        inquirer.List(
            "template", message="Template Menu", choices=selection, carousel=True
        ),
    ]
    answer = inquirer.prompt(question)
    ret = answer["template"]
    return ret
