import click
from pathlib import Path

from cli_helper.cliHelper import TermCreater, ClassWatcher

from sample import SampleClass

@click.group("cli")
@click.pass_context
def cli(ctx):
    """
    Knob measurement

    Example:
        ./knobCli.py -i 10 test -e ro
    """
    term = TermCreater(SampleClass)
    ctx.obj = term

@cli.command()
@click.pass_context
def term(ctx):
    """
    Open evaulation terminal
    """
    term = ctx.obj
    while True:
        value = click.prompt("")
        if value == "close":
            break
        if value == "help":
            term.print_help()
            continue
        if value == "history":
            term.print_history()
            continue
        term.run(value)
    click.echo("Closing")

@cli.command()
@click.pass_context
def watch(ctx):
    #path = Path("sample.py")
    path = Path()
    watcher = ClassWatcher(path)
    click.confirm("exit\n", default=True)
    watcher.close()



if __name__ == "__main__":
    cli()

