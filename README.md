# Quick Scan

A fast and secure payment solution that enables merchants to scan QR codes to receive payments.

## Overview

Sonic Scan simplifies the payment process for merchants by providing a streamlined QR code scanning solution. This Python-based application allows merchants to quickly process payments, track transactions, and manage their business finances all in one place.

## Features

- **QR Code Scanning**: Quickly scan customer payment QR codes
- **Instant Verification**: Real-time payment confirmation
- **Transaction History**: Track all transactions in one place
- **Secure Processing**: End-to-end encryption for all payments
- **Multi-platform Support**: Works on various devices and operating systems

## Installation

```python
# Clone the repository
git clone https://github.com/BhekumuziTshabalala/sonic-scan.git

# Navigate to project directory
cd sonic-scan

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Requirements

- Python 3.7+
- OpenCV
- PyQt5 (for GUI)
- pyzbar
- requests

## Usage

```python
from sonic_scan import PaymentScanner

# Initialize scanner
scanner = PaymentScanner()

# Start scanning for payments
scanner.start()

# Process a payment
payment_info = scanner.scan_qr_code()
result = scanner.process_payment(payment_info)

# Check payment status
if result.status == "success":
    print(f"Payment of {result.amount} received successfully!")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
