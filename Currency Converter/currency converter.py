import tkinter as tk
from tkinter import ttk, messagebox

# Function to perform the currency conversion
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()
        exchange_rate = float(exchange_rate_entry.get())
        
        # Calculate the conversion
        converted_amount = amount * exchange_rate
        
        # Display the result
        result_label.config(text=f'{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}')
    
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Function to clear all input fields and the result
def clear_fields():
    amount_entry.delete(0, tk.END)
    exchange_rate_entry.delete(0, tk.END)
    result_label.config(text="")

# Function to swap the "From" and "To" currencies
def swap_currencies():
    from_currency = from_currency_combo.get()
    to_currency = to_currency_combo.get()
    
    # Swap the values in the dropdowns
    from_currency_combo.set(to_currency)
    to_currency_combo.set(from_currency)
    
    # Display updated exchange rate hint
    update_exchange_rate_hint()

# Function to dynamically display the exchange rate hint
def update_exchange_rate_hint():
    from_currency = from_currency_combo.get()
    to_currency = to_currency_combo.get()
    
    # Mock exchange rates (in real app, you could fetch live rates from an API)
    mock_rates = {
        ("USD", "EUR"): 0.85,
        ("EUR", "USD"): 1.18,
        ("GBP", "USD"): 1.37,
        ("USD", "INR"): 74.15,
        ("INR", "USD"): 0.013,
    }
    
    # Find the mock exchange rate
    exchange_rate = mock_rates.get((from_currency, to_currency), "N/A")
    
    # Update the exchange rate hint label
    exchange_rate_hint_label.config(text=f"Exchange Rate Hint: {from_currency} -> {to_currency} = {exchange_rate}")

# Set up the main window
root = tk.Tk()
root.title(" Currency Converter")
root.configure(bg="#f0f8ff")  # Light sky blue background

# Create and place widgets with some styles
title_label = tk.Label(root, text="Currency Converter", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#2e2e2e")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

tk.Label(root, text="Amount:", bg="#f0f8ff", fg="#333").grid(row=1, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="From Currency:", bg="#f0f8ff", fg="#333").grid(row=2, column=0, padx=10, pady=10)
from_currency_combo = ttk.Combobox(root, values=["USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY"])
from_currency_combo.grid(row=2, column=1, padx=10, pady=10)
from_currency_combo.current(0)

tk.Label(root, text="To Currency:", bg="#f0f8ff", fg="#333").grid(row=3, column=0, padx=10, pady=10)
to_currency_combo = ttk.Combobox(root, values=["USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY"])
to_currency_combo.grid(row=3, column=1, padx=10, pady=10)
to_currency_combo.current(1)

tk.Label(root, text="Exchange Rate:", bg="#f0f8ff", fg="#333").grid(row=4, column=0, padx=10, pady=10)
exchange_rate_entry = tk.Entry(root)
exchange_rate_entry.grid(row=4, column=1, padx=10, pady=10)

# Exchange Rate Hint Label (for dynamic exchange rate display)
exchange_rate_hint_label = tk.Label(root, text="", bg="#f0f8ff", fg="#555")
exchange_rate_hint_label.grid(row=5, column=0, columnspan=3, pady=5)

# Button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert_currency, bg="#4CAF50", fg="white", width=15)
convert_button.grid(row=6, column=0, padx=10, pady=10)

# Clear button to reset fields
clear_button = tk.Button(root, text="Clear", command=clear_fields, bg="#f44336", fg="white", width=15)
clear_button.grid(row=6, column=1, padx=10, pady=10)

# Swap button to swap the "From" and "To" currencies
swap_button = tk.Button(root, text="Swap", command=swap_currencies, bg="#2196F3", fg="white", width=15)
swap_button.grid(row=6, column=2, padx=10, pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff", fg="#2e2e2e")
result_label.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Automatically update the exchange rate hint when currencies are changed
from_currency_combo.bind("<<ComboboxSelected>>", lambda event: update_exchange_rate_hint())
to_currency_combo.bind("<<ComboboxSelected>>", lambda event: update_exchange_rate_hint())

# Start the main loop
root.mainloop()
