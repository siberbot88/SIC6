import requests
import tkinter as tk
from tkinter import ttk, messagebox

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x300")
        
        # API configuration
        self.API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
        self.rates = self.fetch_rates()
        
        self.create_widgets()
        
    def fetch_rates(self):
        try:
            response = requests.get(self.API_URL)
            data = response.json()
            return data['rates']
        except Exception as e:
            messagebox.showerror("Error", "Failed to fetch exchange rates")
            return None
    
    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            if self.rates is None:
                self.rates = self.fetch_rates()
            
            if from_curr != "USD":
                amount = amount / self.rates[from_curr]
            
            converted = amount * self.rates[to_curr]
            self.result_label.config(text=f"{self.amount_entry.get()} {from_curr} = {converted:.2f} {to_curr}")
            
        except ValueError:
            messagebox.showerror("Error", "Invalid input amount")
        except KeyError:
            messagebox.showerror("Error", "Currency not supported")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text="Amount:").grid(row=0, column=0, sticky='w')
        self.amount_entry = ttk.Entry(main_frame, width=20)
        self.amount_entry.grid(row=0, column=1, pady=5)
        self.amount_entry.insert(0, "100")
        
        ttk.Label(main_frame, text="From:").grid(row=1, column=0, sticky='w')
        self.from_currency = ttk.Combobox(main_frame, values=list(self.rates.keys()), width=17)
        self.from_currency.grid(row=1, column=1, pady=5)
        self.from_currency.set("USD")
        
        ttk.Label(main_frame, text="To:").grid(row=2, column=0, sticky='w')
        self.to_currency = ttk.Combobox(main_frame, values=list(self.rates.keys()), width=17)
        self.to_currency.grid(row=2, column=1, pady=5)
        self.to_currency.set("EUR")
        
        convert_btn = ttk.Button(main_frame, text="Convert", command=self.convert_currency)
        convert_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.result_label = ttk.Label(main_frame, text="", font=('Arial', 12, 'bold'))
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()