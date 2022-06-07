from turtle import bgcolor
import click

@click.command()
@click.argument('count',type=int)
@click.option('--count1',type=int,default=1)

def hello(count,count1):
    click.echo(count)
    click.echo(count1)
    #click.echo不能写以下这种中文+变量打印的echo
    #click.echo("count1的值为"+count1)
    click.echo("hello click")
    click.secho("test color",bg="green")
    click.secho("test color",fg="red")

if __name__ == "__main__":
    hello()