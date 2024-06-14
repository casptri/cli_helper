from cli_helper.cliHelper import TermCreater

class GoldenClass:
    def _privat_func(self):
        pass

    def func0(self):
        return True

    def func_with_param(self, name: str):
        return name

def test_funcs():
    term = TermCreater(GoldenClass)
    funcs = term._get_func_list()
    assert len(funcs) == 2
    assert funcs[0]['name'] == "func0"
    assert funcs[1]['name'] == "func_with_param"
