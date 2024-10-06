# Currency Converter

This ""Currency Converter"" is a Python GUI application built using ""Tkinter"". It allows users to convert between various currencies using a manual or predefined exchange rate. The app includes features like input validation, currency swapping, and dynamic exchange rate hints for a user-friendly experience.

## Features

  "Convert between multiple currencies": Supports conversion for currencies like USD, EUR, GBP, INR, AUD, CAD, and JPY.
  "Manual exchange rate input"": Enter the exchange rate manually or use the mock exchange rate hints for popular currency pairs.
  "Swap currencies": Instantly swap the "From" and "To" currencies with a single click.
  "Clear fields": Reset all input fields and the conversion result to start a new calculation.
  "Dynamic exchange rate hints"": Displays real-time hints for popular currency pairs to assist with conversions.

## How It Works

1. ""Enter the amount"": Input the amount to be converted.
2. ""Select currencies"": Choose the "From" and "To" currencies from the dropdown menus.
3. ""Input the exchange rate"": Enter the exchange rate between the selected currencies.
4. ""Click Convert"": See the converted result instantly.
5. ""Use Swap"": Reverse the "From" and "To" currencies with the **Swap** button.
6. ""Clear fields"": Reset all the fields using the **Clear** button.

# Getting Started

# Prerequisites

  "Python 3.x" needs to be installed.
  "Tkinter" comes pre-installed with Python, but if not, you can install it using:

    #bash:
  
    pip install tk
    

# Running the Application

1. Download or clone the repository.
2. Run the "currency_converter.py" file using Python:

    #bash:
   
    python currency_converter.py
    

4. The ""Currency Converter"" window will open, allowing you to perform currency conversions.

# Example 

+--------------------------------------------+
|              Currency Converter            |
+--------------------------------------------+
| Amount:         [ 100.00           ]       |
| From Currency:  [ USD  v]                  |
| To Currency:    [ EUR  v]                  |
| Exchange Rate:  [ 0.85             ]       |
| Exchange Rate Hint: USD -> EUR = 0.85      |
+--------------------------------------------+
| [ Convert ]   [ Clear ]   [ Swap ]         |
+--------------------------------------------+
| Result: 100.00 USD = 85.00 EUR             |
+--------------------------------------------+



# Mock Exchange Rates

The application uses mock exchange rates for the following currency pairs:

| From Currency | To Currency | Exchange Rate |
| ------------- | ----------- | ------------- |
| USD           | EUR         | 0.85          |
| EUR           | USD         | 1.18          |
| GBP           | USD         | 1.37          |
| USD           | INR         | 74.15         |
| INR           | USD         | 0.013         |

These rates are hardcoded into the app, but you can easily extend it to fetch live rates from an API like **Open Exchange Rates** or **CurrencyLayer**.

## License

This project is licensed under the MIT License.

