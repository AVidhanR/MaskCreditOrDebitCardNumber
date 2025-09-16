# Credit/Debit Card Number Masker

A simple Python utility to mask credit and debit card numbers for security purposes, showing only the last 4 digits while replacing the rest with asterisks or custom characters.

## 🌟 Features

- **Secure Masking**: Masks all digits except the last 4 for privacy and security
- **Customizable**: Configure the number of digits to keep visible and the masking character
- **Simple Interface**: Easy-to-use command-line interface
- **Simple Input**: Accepts 16-digit card numbers (without spaces or dashes)
- **Validation**: Basic validation for 16-digit card numbers

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AVidhanR/MaskCreditOrDebitCardNumber.git
   cd MaskCreditOrDebitCardNumber
   ```

2. No additional dependencies required - uses only Python standard library!

## 📖 Usage

### Command Line Interface

Run the script interactively:

```bash
python3 credit.py
```

Then enter your card number when prompted:
```
Enter any Credit Card number: 1234567890123456
************3456
```

### As a Python Module

**Note**: Due to the current code structure, importing the module will prompt for input. This is a known issue that needs fixing.

For now, you can copy the `mask_cc_number` function to use it in your own code:

```python
import re

def mask_cc_number(cc_string, digits_to_keep=4, mask_char='*'):
    cc_string_total = sum(map(str.isdigit, cc_string))
    
    if len(cc_string) != 16:
        print("Invalid Credit Card number.")
        return None
    
    digits_to_mask = cc_string_total - digits_to_keep
    masked_cc_string = re.sub(r'\d', mask_char, cc_string, digits_to_mask)
    
    return masked_cc_string

# Usage
card_number = "1234567890123456"
masked = mask_cc_number(card_number)
print(masked)  # Output: ************3456
```

## 🔧 Function Parameters

### `mask_cc_number(cc_string, digits_to_keep=4, mask_char='*')`

- **cc_string** (str): The credit card number to mask
- **digits_to_keep** (int, optional): Number of digits to keep visible at the end. Default: 4
- **mask_char** (str, optional): Character to use for masking. Default: '*'

**Returns**: Masked credit card number as a string

## 📝 Examples

### Different Masking Characters

```python
card = "1234567890123456"

print(mask_cc_number(card))                    # ************3456
print(mask_cc_number(card, mask_char='#'))     # ############3456
print(mask_cc_number(card, mask_char='X'))     # XXXXXXXXXXXX3456
```

### Different Numbers of Visible Digits

```python
card = "1234567890123456"

print(mask_cc_number(card, digits_to_keep=2))  # **************56
print(mask_cc_number(card, digits_to_keep=4))  # ************3456
print(mask_cc_number(card, digits_to_keep=6))  # **********123456
```

### Handling Different Card Formats

```python
# Currently works with 16-digit numbers only
card = "1234567890123456"
print(mask_cc_number(card))  # ************3456

# Note: Formatted cards with dashes/spaces need preprocessing
formatted_card = "1234-5678-9012-3456"
clean_card = formatted_card.replace('-', '').replace(' ', '')
print(mask_cc_number(clean_card))  # ************3456
```

## ⚠️ Important Notes

- **Security**: This tool is for display purposes only. Never store or transmit sensitive card information
- **Validation**: The script performs basic length validation for 16-digit cards
- **Privacy**: Always ensure proper handling of sensitive financial data
- **Testing**: Use test card numbers (like 4111111111111111) for development

## 🛡️ Security Best Practices

When using this tool:

1. **Never log actual card numbers** - always mask before logging
2. **Use in secure environments** - ensure your development environment is secure
3. **Comply with regulations** - follow PCI DSS and other relevant standards
4. **Test thoroughly** - validate masking works correctly before production use

## 🐛 Known Issues

- Regex warning for escape sequences (uses `\d` pattern)
- Currently only supports 16-digit cards (no spaces or dashes)
- Limited input validation
- Code runs immediately when imported (needs `if __name__ == "__main__"` guard)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Here are some ways you can contribute:

- Fix the regex warning issue
- Add `if __name__ == "__main__"` guard for proper module importing
- Add support for different card number lengths (13, 15, 19 digits)
- Add support for formatted input (with spaces/dashes)
- Improve input validation
- Add unit tests
- Enhance error handling
- Add more formatting options

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test your changes
5. Commit: `git commit -am 'Add some feature'`
6. Push: `git push origin feature-name`
7. Submit a pull request

## 📋 Test Card Numbers

For testing purposes, you can use these standard test card numbers:

- Visa: `4111111111111111`
- Visa: `4012888888881881`
- Mastercard: `5555555555554444`
- Mastercard: `5105105105105100`

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**AVidhanR**

- GitHub: [@AVidhanR](https://github.com/AVidhanR)

## 🙏 Acknowledgments

- Thanks to the Python community for the excellent standard library
- Inspired by the need for simple, secure card number masking utilities

---

⭐ **Star this repository if you find it helpful!** ⭐
