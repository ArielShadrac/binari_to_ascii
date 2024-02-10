from rich.console import Console

console = Console()

def binary_to_ascii(bin):
    try:
        binary = int(bin, base=2)
        ascii = binary.to_bytes((binary.bit_length()+7)//8, 'big').decode()
        return ascii
    except ValueError:
        return console.print("⚠️- Enter binary number", style="bold red")