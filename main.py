# Traceback system
from rich.traceback import install
install(show_locals=True)

# Importing necessary libraries
from rich_gradient import Gradient
from rich.console import Console
from rich.prompt import Prompt
from rich.align import Align
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from time import sleep
con = Console()

from requests import post

# Menu
def menu():
    logo = """
    
██╗   ██╗ ██████╗ ██╗██████╗ ████████╗ ██████╗  ██████╗ ██╗     
██║   ██║██╔═══██╗██║██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║   ██║██║   ██║██║██║  ██║   ██║   ██║   ██║██║   ██║██║     
╚██╗ ██╔╝██║   ██║██║██║  ██║   ██║   ██║   ██║██║   ██║██║     
 ╚████╔╝ ╚██████╔╝██║██████╔╝██╗██║   ╚██████╔╝╚██████╔╝███████╗
  ╚═══╝   ╚═════╝ ╚═╝╚═════╝ ╚═╝╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                
  
    """

    text = Text(logo)
    gradient_text = Gradient(
        text,
        colors=["#bababa", "gray"],
    )
    con.print(Align(gradient_text, align="center"))

    table = Table(box=None)
    table.add_column("[0]", style="#bababa")
    table.add_column("[Option]", style="#bababa")
    table.add_row("[1]", "Spam webhook", style="#bababa")
    table.add_row("[2]", "Delete webhook", style="#bababa")
    table.add_row("[3]", "Valid webhook", style="#bababa")
    table.add_row("[4]", "Spam with bots (IN DEV)", style="#bababa")

    choose_panel = Panel(
        table,
        title="Choose your option",
        border_style="#bababa",
    )

    con.print(choose_panel)

# Function to spam webhook
def spam_webhook():

    try:
        con.clear()
        webhook_url = Prompt.ask("[#bababa]Webhook URL")
        message = Prompt.ask("[#bababa]Enter the message to spam:")
        con.clear()
        while True:
                post(webhook_url, json={"content": ".gg/voidtool" + message})
                con.print(f"[green][+] Message sent[/green]")
                sleep(0.5)
    except KeyboardInterrupt:
        exit()
    



if __name__ == "__main__":
    menu()
    option = Prompt.ask("[#bababa]Choose an option")
    if option == "1":
        spam_webhook()
    elif option == "2":
        con.print("[red]Not implemented yet[/red]")
    elif option == "3":
        con.print("[red]Not implemented yet[/red]")
    elif option == "4":
        con.print("[red]Not implemented yet[/red]")
    else:
        con.print("[red]Invalid option[/red]")