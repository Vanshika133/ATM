# atm_gui.py

import tkinter as tk
from tkinter import messagebox
from atm_backend import authenticate

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")
        self.user = None
        self.login_screen()

    def login_screen(self):
        self.clear()
        tk.Label(self.root, text="Enter PIN", font=('Arial', 16)).pack(pady=10)
        self.pin_entry = tk.Entry(self.root, show="*", font=('Arial', 16))
        self.pin_entry.pack()
        tk.Button(self.root, text="Login", command=self.verify_pin).pack(pady=10)

    def verify_pin(self):
        pin = self.pin_entry.get()
        user = authenticate(pin)
        if user:
            self.user = user
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def main_menu(self):
        self.clear()
        tk.Label(self.root, text=f"Welcome, {self.user.name}", font=('Arial', 16)).pack(pady=10)
        tk.Button(self.root, text="Check Balance", command=self.show_balance).pack(fill='x')
        tk.Button(self.root, text="Deposit Money", command=self.deposit_screen).pack(fill='x')
        tk.Button(self.root, text="Withdraw Money", command=self.withdraw_screen).pack(fill='x')
        tk.Button(self.root, text="Transaction History", command=self.show_history).pack(fill='x')
        tk.Button(self.root, text="Logout", command=self.login_screen).pack(fill='x')

    def show_balance(self):
        messagebox.showinfo("Balance", f"₹{self.user.balance}")

    def deposit_screen(self):
        self.clear()
        tk.Label(self.root, text="Enter Amount to Deposit", font=('Arial', 14)).pack()
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()

        def deposit():
            try:
                amount = float(amount_entry.get())
                self.user.deposit(amount)
                messagebox.showinfo("Success", f"Deposited ₹{amount}")
                self.main_menu()
            except ValueError:
                messagebox.showerror("Error", "Enter a valid amount")

        tk.Button(self.root, text="Deposit", command=deposit).pack()
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def withdraw_screen(self):
        self.clear()
        tk.Label(self.root, text="Enter Amount to Withdraw", font=('Arial', 14)).pack()
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()

        def withdraw():
            try:
                amount = float(amount_entry.get())
                if self.user.withdraw(amount):
                    messagebox.showinfo("Success", f"Withdrawn ₹{amount}")
                else:
                    messagebox.showerror("Failed", "Insufficient balance")
                self.main_menu()
            except ValueError:
                messagebox.showerror("Error", "Enter a valid amount")

        tk.Button(self.root, text="Withdraw", command=withdraw).pack()
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def show_history(self):
        history = "\n".join(self.user.get_history()) or "No transactions yet"
        messagebox.showinfo("Transaction History", history)

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.geometry("300x350")
    root.mainloop()