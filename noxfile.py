from nox_poetry import session


@session
def lint(session):
    session.install('flake8','black')
    session.run('black', '--check', "cli_helper", 'tests')
    session.run('flake8', "cli_helper", 'tests')

@session(python=["3.10", "3.11", "3.12"])
def tests(session):
    session.install("pytest", ".")
    session.run("pytest")

@session
def format(session):
    session.install("black", "isort")
    session.run("black", "cli_helper/", "tests/")
    session.run("isort", "cli_helper/", "tests/")

@session
def docs(session):
    session.install("mkdocs")
    session.run('mkdocs','build')
