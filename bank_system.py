# import random

# print("--------menu----------")
# print("1.Open Account\n2.Check Blance\n3.Deposite Balance\n4.Withdraw Balance\n5.Change ATM PIN\n6.Exit")
# def creat_acc():
#     name=input("Enter Your Name Here: ")
#     father_name=input("Enter Your  Father's Name Here: ")
#     age=int(input("Enter Your Age Here: "))
#     dob=int(input("Enter Your D.O.B Here: "))
#     mob=int(input("Enter Your Mobile number Here: "))
#     aadhar_no=int(input("Enter Your Aadhar number Here: "))
#     pan_no=int(input("Enter Your PAN number Here: "))
#     more = input("Can you want ATM card? (y/n): ").lower()
#     if more == "y":
#         set_atm_pin=int(input("Enter your ATM pin here: "))
#         print("You can't share your ATM pin with any persone")
"""
Bank of Jayanta - ATM Dashboard Tkinter App
Features:
 - Create account (Name, Age, DOB, Aadhar, PAN)
 - Auto-generate 11-digit account number
 - Option to create ATM card + set 4-digit PIN
 - Save accounts to accounts.json (persistent)
 - Card insert animation
 - Numeric keypad for PIN & amount entry
 - Deposit / Withdraw / Check Balance
 - Generate receipt as .txt and attempt .pdf (requires reportlab)
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import json
import random
import os
import time
from datetime import datetime

DATA_FILE = "accounts.json"


# ------------------ Data handling ------------------
def load_accounts():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                raw = json.load(f)
                # rebuild BankAccount objects
                accounts = {}
                for k, v in raw.items():
                    accounts[k] = BankAccount.from_dict(v)
                return accounts
        except Exception:
            return {}
    return {}


def save_accounts(accounts):
    raw = {k: v.to_dict() for k, v in accounts.items()}
    with open(DATA_FILE, "w") as f:
        json.dump(raw, f, indent=2)


# ------------------ BankAccount class ------------------
class BankAccount:
    def __init__(self, name, age, dob, aadhar, pan, account_no, atm_card, pin, balance=0.0):
        self.name = name
        self.age = age
        self.dob = dob
        self.aadhar = aadhar
        self.pan = pan
        self.account_no = account_no
        self.atm_card = atm_card  # "yes" / "no"
        self.pin = pin  # string or None
        self.balance = float(balance)
        self.txn_history = []  # list of dicts {time, type, amount, balance}

    def deposit(self, amount):
        amount = float(amount)
        self.balance += amount
        self.txn_history.append({"time": now_str(), "type": "DEPOSIT", "amount": amount, "balance": self.balance})
        return self.balance

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self.balance:
            return False
        self.balance -= amount
        self.txn_history.append({"time": now_str(), "type": "WITHDRAW", "amount": amount, "balance": self.balance})
        return True

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "dob": self.dob,
            "aadhar": self.aadhar,
            "pan": self.pan,
            "account_no": self.account_no,
            "atm_card": self.atm_card,
            "pin": self.pin,
            "balance": self.balance,
            "txn_history": self.txn_history,
        }

    @classmethod
    def from_dict(cls, d):
        acc = cls(d["name"], d["age"], d["dob"], d["aadhar"], d["pan"],
                  d["account_no"], d["atm_card"], d.get("pin"), d.get("balance", 0.0))
        acc.txn_history = d.get("txn_history", [])
        return acc


def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ------------------ App ------------------
class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM - Bank of Jayanta")
        self.root.geometry("480x520")
        self.accounts = load_accounts()

        self.current_account = None  # BankAccount object after login
        self.build_main_menu()

    # ---------- UI helpers ----------
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def center(self, widget):
        widget.pack(pady=8)

    # ---------- Main Menu ----------
    def build_main_menu(self):
        self.clear()
        tk.Label(self.root, text="BANK OF JAYANTA", font=("Helvetica", 18, "bold")).pack(pady=16)

        tk.Button(self.root, text="Insert ATM Card / Login", width=28, height=2, command=self.card_insert_anim).pack(pady=8)
        tk.Button(self.root, text="Create New Account", width=28, height=2, command=self.create_account_ui).pack(pady=8)
        tk.Button(self.root, text="Exit", width=28, height=2, command=self.root.quit).pack(pady=12)

        tk.Label(self.root, text="(Accounts saved to accounts.json)", font=("Arial", 9)).pack(side="bottom", pady=8)

    # ---------- Card animation & Login ----------
    def card_insert_anim(self):
        # simple animation: show 'Card Inserted...' label with a sliding effect
        self.clear()
        canvas = tk.Canvas(self.root, width=460, height=420)
        canvas.pack(pady=10)
        label = tk.Label(self.root, text="Insert Card (Simulated)...", font=("Arial", 14))
        label.pack()
        x = -200
        text = canvas.create_text(x, 200, text="<< CARD >>", font=("Courier", 20), anchor="w")
        self.root.update()
        # slide
        for i in range(40):
            canvas.move(text, 14, 0)
            self.root.update()
            time.sleep(0.02)
        time.sleep(0.25)
        # proceed to login screen
        self.login_screen()

    def login_screen(self):
        self.clear()
        tk.Label(self.root, text="ENTER ACCOUNT & PIN", font=("Arial", 14, "bold")).pack(pady=12)

        tk.Label(self.root, text="Account Number:").pack()
        self.acc_entry = tk.Entry(self.root)
        self.acc_entry.pack()

        tk.Label(self.root, text="PIN:").pack()
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack()

        # numeric keypad
        self.active_entry = None  # will be set to either self.pin_entry or self.amount_entry on dashboard
        keypad_frame = tk.Frame(self.root)
        keypad_frame.pack(pady=8)
        self.build_keypad(keypad_frame, target=self.pin_entry)

        tk.Button(self.root, text="Login", width=15, command=self.try_login).pack(pady=6)
        tk.Button(self.root, text="Back", width=15, command=self.build_main_menu).pack(pady=6)

    def try_login(self):
        acc_no = self.acc_entry.get().strip()
        pin = self.pin_entry.get().strip()
        if acc_no in self.accounts:
            acc = self.accounts[acc_no]
            if acc.atm_card == "yes" and acc.pin == pin:
                self.current_account = acc
                messagebox.showinfo("Login", f"Welcome, {acc.name}!")
                self.atm_dashboard()
            else:
                messagebox.showerror("Error", "Invalid PIN or ATM card not present.")
        else:
            messagebox.showerror("Error", "Account not found.")

    # ---------- Create Account UI ----------
    def create_account_ui(self):
        self.clear()
        tk.Label(self.root, text="CREATE NEW ACCOUNT", font=("Arial", 14, "bold")).pack(pady=12)

        form = tk.Frame(self.root)
        form.pack(pady=4)

        labels = ["Name", "Age", "DOB (DD/MM/YYYY)", "Aadhar No", "PAN No"]
        self.form_entries = {}
        for lbl in labels:
            tk.Label(form, text=lbl).pack(anchor="w", padx=8)
            e = tk.Entry(form)
            e.pack(fill="x", padx=8, pady=2)
            self.form_entries[lbl] = e

        def create_action():
            name = self.form_entries["Name"].get().strip()
            age = self.form_entries["Age"].get().strip()
            dob = self.form_entries["DOB (DD/MM/YYYY)"].get().strip()
            aadhar = self.form_entries["Aadhar No"].get().strip()
            pan = self.form_entries["PAN No"].get().strip()

            if not name or not age:
                messagebox.showerror("Error", "Please provide at least Name and Age.")
                return

            account_no = str(random.randint(10**10, 10**11 - 1))  # 11-digit
            atm_choice = messagebox.askyesno("ATM Card", "Do you want an ATM card?")
            if atm_choice:
                # set 4-digit PIN via keypad dialog
                pin = simpledialog.askstring("Set PIN", "Enter 4-digit PIN (numbers only):", show="*")
                if not pin or not pin.isdigit() or len(pin) != 4:
                    messagebox.showerror("Error", "PIN must be 4 digits. Account creation cancelled.")
                    return
                pin_str = pin
            else:
                pin_str = None

            acc = BankAccount(name, age, dob, aadhar, pan, account_no, "yes" if atm_choice else "no", pin_str, balance=0.0)
            self.accounts[account_no] = acc
            save_accounts(self.accounts)
            messagebox.showinfo("Account Created", f"Account created!\nAccount No: {account_no}")
            self.build_main_menu()

        tk.Button(self.root, text="Create Account", command=create_action, width=18).pack(pady=8)
        tk.Button(self.root, text="Back", command=self.build_main_menu, width=18).pack()

    # ---------- Keypad builder ----------
    def build_keypad(self, parent, target):
        # target is the Entry widget to receive keypad digits
        def on_press(d):
            target.insert("end", str(d))

        btns = [
            ("1", 0, 0), ("2", 0, 1), ("3", 0, 2),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
            ("C", 3, 0), ("0", 3, 1), ("⌫", 3, 2),
        ]
        for (txt, r, c) in btns:
            b = tk.Button(parent, text=txt, width=6, height=2,
                          command=(lambda t=txt: (target.delete(0, "end") if t == "C" else
                                                  (target.delete(len(target.get()) - 1, "end") if t == "⌫" else
                                                   target.insert("end", t)))))
            b.grid(row=r, column=c, padx=3, pady=3)

    # ---------- ATM Dashboard ----------
    def atm_dashboard(self):
        self.clear()
        acc = self.current_account
        tk.Label(self.root, text=f"Welcome: {acc.name}", font=("Arial", 14)).pack(pady=8)

        info_frame = tk.Frame(self.root)
        info_frame.pack(pady=4)
        tk.Label(info_frame, text=f"Account No: {acc.account_no}").pack()
        tk.Label(info_frame, text=f"ATM Card: {acc.atm_card}").pack()
        tk.Label(info_frame, text=f"Current Balance: ₹{acc.balance:.2f}").pack()

        # Amount entry and keypad
        tk.Label(self.root, text="Amount (use keypad):").pack(pady=6)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()
        key_frame = tk.Frame(self.root)
        key_frame.pack(pady=4)
        self.build_keypad(key_frame, target=self.amount_entry)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=6)
        tk.Button(btn_frame, text="Check Balance", width=15, command=self.check_balance_ui).grid(row=0, column=0, padx=6, pady=6)
        tk.Button(btn_frame, text="Deposit", width=15, command=self.deposit_ui).grid(row=0, column=1, padx=6, pady=6)
        tk.Button(btn_frame, text="Withdraw", width=15, command=self.withdraw_ui).grid(row=1, column=0, padx=6, pady=6)
        tk.Button(btn_frame, text="Print Receipt", width=15, command=self.print_receipt_ui).grid(row=1, column=1, padx=6, pady=6)

        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=10)
        tk.Button(self.root, text="Exit App", command=self.root.quit).pack()

    def refresh_dashboard(self):
        # just re-open dashboard to update displayed balance
        self.atm_dashboard()

    def check_balance_ui(self):
        acc = self.current_account
        messagebox.showinfo("Balance", f"Current Balance: ₹{acc.balance:.2f}")

    def deposit_ui(self):
        acc = self.current_account
        amt_str = self.amount_entry.get().strip()
        try:
            amt = float(amt_str)
            if amt <= 0:
                raise ValueError
        except Exception:
            messagebox.showerror("Error", "Enter a valid amount > 0 using keypad.")
            return
        acc.deposit(amt)
        save_accounts(self.accounts)
        messagebox.showinfo("Success", f"Deposited ₹{amt:.2f}\nNew Balance: ₹{acc.balance:.2f}")
        self.amount_entry.delete(0, "end")
        self.refresh_dashboard()

    def withdraw_ui(self):
        acc = self.current_account
        if acc.atm_card != "yes":
            messagebox.showerror("Error", "This account has no ATM card. Cannot withdraw via ATM.")
            return
        # confirm PIN
        pin = simpledialog.askstring("PIN", "Enter your 4-digit PIN:", show="*")
        if not pin or pin != acc.pin:
            messagebox.showerror("Error", "Invalid PIN.")
            return
        amt_str = self.amount_entry.get().strip()
        try:
            amt = float(amt_str)
            if amt <= 0:
                raise ValueError
        except Exception:
            messagebox.showerror("Error", "Enter a valid amount > 0 using keypad.")
            return
        if acc.withdraw(amt):
            save_accounts(self.accounts)
            messagebox.showinfo("Success", f"Withdrawn ₹{amt:.2f}\nNew Balance: ₹{acc.balance:.2f}")
            self.amount_entry.delete(0, "end")
            self.refresh_dashboard()
        else:
            messagebox.showerror("Error", "Insufficient balance.")

    def print_receipt_ui(self):
        acc = self.current_account
        # ask for which txn to print? We'll print last 5 txns + balance
        txns = acc.txn_history[-5:]
        content_lines = [
            "BANK OF JAYANTA - RECEIPT",
            f"Name: {acc.name}",
            f"Account No: {acc.account_no}",
            f"Time: {now_str()}",
            "-" * 32,
            "Recent Transactions:"
        ]
        if txns:
            for t in txns:
                content_lines.append(f"{t['time']} | {t['type']} | ₹{t['amount']:.2f} | Bal: ₹{t['balance']:.2f}")
        else:
            content_lines.append("No recent transactions.")
        content_lines.append("-" * 32)
        content_lines.append(f"Current Balance: ₹{acc.balance:.2f}")
        content = "\n".join(content_lines)

        # Save text receipt
        default_name = f"receipt_{acc.account_no}_{int(time.time())}.txt"
        path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_name,
                                            filetypes=[("Text file", "*.txt"), ("PDF file", "*.pdf")])
        if not path:
            return
        try:
            if path.lower().endswith(".pdf"):
                # try to produce a PDF (reportlab optional)
                try:
                    from reportlab.lib.pagesizes import letter
                    from reportlab.pdfgen import canvas as pdfcanvas
                    c = pdfcanvas.Canvas(path, pagesize=letter)
                    y = 740
                    for line in content_lines:
                        c.drawString(40, y, line)
                        y -= 14
                        if y < 40:
                            c.showPage()
                            y = 740
                    c.save()
                    messagebox.showinfo("Receipt", f"PDF receipt saved to:\n{path}")
                except Exception as e:
                    # fallback: save as text
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(content)
                    messagebox.showwarning("PDF Unavailable", f"reportlab not installed or error making PDF.\nSaved plain text to {path}")
            else:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                messagebox.showinfo("Receipt", f"Receipt saved to:\n{path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save receipt: {e}")

    def logout(self):
        self.current_account = None
        save_accounts(self.accounts)
        messagebox.showinfo("Logout", "You have been logged out.")
        self.build_main_menu()


# ------------------ Run app ------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()

        
            
