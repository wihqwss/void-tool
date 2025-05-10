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
import platform
import sys
import os

# title
def set_terminal_title(title):
    if platform.system() == "Windows":
        os.system(f'title {title}')
    else:
        sys.stdout.write(f"\33]0;{title}\a")
        sys.stdout.flush()

con = Console()

import requests

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
    dsc_gradient = Gradient(
        "dsc.gg/voidtool",
        colors=["red", "blue", "pink"],
    )
    gradient_text = Gradient(
        text,
        colors=["#bababa", "gray"],
    )
    con.print(Align(gradient_text, align="center"))
    con.print(Align(dsc_gradient, align="center"))
    con.line(2)

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
                requests.post(webhook_url, json={"content": ".gg/voidtool" + message})
                con.print(f"[green][+] Message sent[/green]")
                sleep(0.5)
    except KeyboardInterrupt:
        exit()
    

# Function to delete webhook
def delete_webhook():
    con.clear()
    webhook_url = Prompt.ask("[#bababa]Webhook URL")
    con.print(f"[red]Deleting webhook...[/red]")
    
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        con.print(f"[green][+] Webhook deleted successfully[/green]")
    else:
        con.print(f"[red]Failed to delete webhook[/red]")
    sleep(1)
    exit()

# Function to validate webhook
def valid_webhook():
    con.clear()
    webhook_url = Prompt.ask("[#bababa]Webhook URL")
    
    response = requests.get(webhook_url)
    if response.status_code == 200:
        con.print(f"[green][+] Webhook is working[/green]")
    else:
        con.print(f"[red][-]Unknown webhook/Deleted webhook[/red]")
    sleep(1)
    exit()

if __name__ == "__main__":
    menu()
    set_terminal_title("dsc.gg/voidtool")
    option = Prompt.ask("[#bababa]Choose an option")
    if option == "1":
        spam_webhook()
    elif option == "2":
        delete_webhook()
    elif option == "3":
        valid_webhook()
    elif option == "4":
        con.print("[red]Not implemented yet[/red]")
    else:
        con.print("[red]Invalid option[/red]")