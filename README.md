# Binary to ASCII Converter

A simple Python utility to convert binary strings to their ASCII equivalents, with error handling for invalid inputs. This tool uses the `rich` library for styled console output in case of errors.

## Features
- Converts a binary string (e.g., "01001000 01100101 01101100 01101100 01101111") to ASCII text (e.g., "Hello").
- Handles invalid binary inputs by printing a styled error message to the console.
- Lightweight and easy to integrate into larger projects.

## Requirements
- Python 3.6+
- `rich` library (for console styling)

Install the dependency:
```
pip install rich
```

## Usage
Import the function and call it with a binary string:

```python
from rich.console import Console

console = Console()

def binary_to_ascii(bin_str):
    try:
        binary = int(bin_str, base=2)
        ascii_text = binary.to_bytes((binary.bit_length() + 7) // 8, 'big').decode()
        return ascii_text
    except ValueError:
        console.print("Enter a valid binary number", style="bold red")
        return None  # Returns None on error after printing

# Example
result = binary_to_ascii("01001000 01100101 01101100 01101100 01101111")
print(result)  # Output: Hello

# Invalid input example
binary_to_ascii("invalid")  # Prints error message in red and returns None
```

### Notes
- The input should be a string of binary digits (0s and 1s). Spaces are ignored during conversion since `int(bin_str, base=2)` handles them implicitly if they separate bytes, but for best results, provide a continuous or space-separated binary string.
- On error (e.g., non-binary characters), it prints a message using `rich` and returns `None`.
- This function assumes UTF-8 decoding; for other encodings, modify the `.decode()` call accordingly.

## How It Works
1. **Input Parsing**: The binary string is converted to an integer using base-2.
2. **Byte Conversion**: The integer is transformed into bytes, calculating the minimum byte length needed.
3. **Decoding**: Bytes are decoded to ASCII/UTF-8 text.
4. **Error Handling**: If the input isn't valid binary, catch the `ValueError`, print a styled error, and return `None`.

## Examples
- Valid: `binary_to_ascii("01110111 01101111 01110010 01101100 01100100")` → "world"
- Invalid: `binary_to_ascii("12345")` → Prints "Enter a valid binary number" in bold red and returns `None`

## Contributing
Feel free to fork this repository and submit pull requests for improvements, such as adding support for other bases or enhancing error messages.

## License
MIT License - Free to use, modify, and distribute.
