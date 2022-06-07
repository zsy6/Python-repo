from email.policy import default
from pydoc import cli
import click

@click.command()

#prompt 获取用户输入

def hello():
    count = click.prompt("input a int",type=int)
    click.secho(count,fg='yellow')
    click.echo("hello click")
    if click.confirm("continue?"):
        print("over")
    else:
        exit()
 

if __name__ == "__main__":
    hello()