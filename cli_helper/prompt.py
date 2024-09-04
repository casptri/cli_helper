import os
import inquirer

def nested_prompt(data: dict, parent: any = None) -> any:
    ret = data
    while type(ret) == dict:
        selection = [("<-- back", parent) ]
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
        #ret = answer["template"]
        ret = nested_prompt(answer["template"])
        #print(ret)
        #if type(ret) is dict:
        #    ret = nested_prompt(ret)
        #    print(ret)
    return ret
