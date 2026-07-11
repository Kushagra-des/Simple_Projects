# 💱 Real-Time Currency Converter

A command-line Python application that retrieves live exchange rates from the **Fixer.io API** and performs real-time currency conversion between supported currencies.

This project demonstrates how to work with REST APIs, parse JSON data, handle user input, and perform currency conversion using Python.

---

## Features

* Fetches live exchange rates using the Fixer.io API
* Converts between more than 150 supported currencies
* Displays the complete list of available currency codes
* Simple and interactive command-line interface
* Handles invalid currency code input
* Lightweight and easy to understand

---

## Technologies Used

* Python 3
* Requests
* JSON
* Fixer.io API

---

## Concepts Practiced

* Python Functions
* Lists and Dictionaries
* User Input Handling
* Exception Handling
* HTTP Requests
* REST API Integration
* JSON Parsing
* Data Manipulation
* Module Imports

---

## Project Structure

```text
currency-converter-python/
│
├── currency_converter.py
├── README.md
└── requirements.txt
```

---

## Installation

1. Clone the repository.

```bash
git clone https://github.com/yourusername/currency-converter-python.git
```

2. Navigate to the project folder.

```bash
cd currency-converter-python
```

3. Install the required package.

```bash
pip install requests
```

---

## Configuration

This project uses the **Fixer.io API** to retrieve exchange rates.

1. Create an account on Fixer.io.
2. Generate your API key.
3. Replace the existing API key in the source code with your own.

For better security, store your API key in a `.env` file instead of hardcoding it into the application.

---

## How to Run

```bash
python currency_converter.py
```

---

## Usage

Enter the amount, source currency, and destination currency separated by spaces.

Example:

```text
100 USD INR
```

To display all supported currencies:

```text
SHOW
```

To exit the program:

```text
Q
```

---

## Example Output

```text
Please specify the amount of currency to convert, from currency, to currency.

100 USD INR

100.0 of currency USD amounts to 8565.34 of currency INR today
```

---

## Future Improvements

* Secure API key using environment variables
* Replace recursive calls with a loop
* Add better input validation
* Improve exception handling for network errors
* Display exchange rate information separately
* Add support for historical exchange rates
* Create a graphical user interface using Tkinter
* Build a web version using Streamlit
* Export conversion history to CSV
* Add automated unit tests

---

## Learning Outcomes

This project helped practice:

* Consuming REST APIs
* Working with JSON responses
* Making HTTP requests
* Using dictionaries for data lookup
* Creating command-line applications
* Handling user input
* Basic exception handling
* Working with third-party Python libraries

---

## Requirements

* Python 3.8 or later
* requests

Install dependencies:

```bash
pip install requests
```
---

## Author

**Kushagra-des**
