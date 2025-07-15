from rich import print
from rich.panel import Panel


def main():
##### Doc
    """
    Archive main

    Returns:
        None
    """
##### Doc
    text = "[bold white]Choose a option:[/bold white]\n1- [green]Bin[/green] to [red]Dec[/red]\n2- [red]Dec[/red] to [green]Bin[/green]" # Use rich

    print(Panel(text, title="[bold]Convert[/bold] [bold green]Bin[/bold green]/[bold red]Dec[/bold red]", border_style="white"))
    choose = int(input("Enter a option: "))

    if choose == 1:
        to_dec()
    elif(choose == 2):
        to_bin()
    else:
        print("Please, enter a valid option.")

def to_bin():
##### Doc
    """
    Convert Binary to Decimal

    Returns:
        None
    """
##### Doc
    try:
        decimal = int(input("Decimal number: "))
    except ValueError:
        print("Only use numbers!")
        return


    binary = ""
    while decimal > 0:
        remainder = decimal % 2 # give the remainder
        binary = str(remainder) + binary #add the left
        decimal = decimal // 2

    print(binary)

def to_dec():
##### Doc
    """
    Convert Decimal to Binary

    Returns:
        None
    """
##### Doc

    try:
        binary = int(input("Binary number: "))
    except ValueError:
        print("Only use base 2 numbers!")
        return

    bit_arr = [int(i) for i in str(binary)]
    

    decimal = 0

    #Conversion
    for i in range(len(bit_arr)):

        bit = bit_arr[i]
        decimal += bit * 2 ** (len(bit_arr) - 1 - i)
    print(decimal)

main()