# E-commerce Invoice Generator

This project is a simple e-commerce invoice generator built using Python and the `ReportLab` library. It allows you to dynamically generate invoices with seller details, billing details, item details, and tax calculations. You can also add a signature image to the invoice.

# Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [How to Use](#how-to-use)

# Features

- Dynamic input handling for seller details, billing details, and item details.
- Automatic calculation of CGST, SGST, and IGST taxes.
- Generates PDF invoices using the `ReportLab` library.
- Supports adding a custom signature image to the invoice.
- Error handling for missing files and incorrect paths.

# Prerequisites

- Python 3.x installed on your system.
- `ReportLab` library installed. You can install it via pip:

```bash
pip install reportlab
```

# How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Vivek92503/ecommerce-invoice-generator.git
   cd ecommerce-invoice-generator
   ```

2. **Run the Invoice Generator**:
   - Ensure you have all the required files, including `signature.png` (or update the path in the code).
   - Run the script using Python:
   ```bash
   python invoice_generator.py
   ```

3. **Check the Output**:
   - The generated invoice will be saved as `invoice.pdf` in the same directory.

## License

This project is open-source and available under the [MIT License](LICENSE).
