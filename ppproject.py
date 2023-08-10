import tkinter as tk

def show_balance():
    balance_label.config(text=f"Your current balance is {balance}")

def withdraw_balance():
    global balance
    withdraw_amount = int(withdraw_entry.get())
    balance -= withdraw_amount
    balance_label.config(text=f"{withdraw_amount} is debited from your account")
    show_balance()

def deposit_balance():
    global balance
    deposit_amount = int(deposit_entry.get())
    balance += deposit_amount
    balance_label.config(text=f"Your updated balance is {balance}")

def exit_program():
    root.destroy()

# Replace password with your desired PIN
password = 1234
balance = 5000

def check_pin():
    pin = int(pin_entry.get())
    if pin == password:
        pin_frame.pack_forget()
        main_frame.pack()
    else:
        pin_entry.delete(0, tk.END)
        status_label.config(text="Wrong PIN. Please try again.")

# Create the main application window
root = tk.Tk()
root.title("ATM Simulation")

# Create frames
pin_frame = tk.Frame(root)
pin_frame.pack(pady=20)

main_frame = tk.Frame(root)

# PIN entry and verification
pin_label = tk.Label(pin_frame, text="Enter your ATM PIN:")
pin_label.pack()
pin_entry = tk.Entry(pin_frame, show="*")
pin_entry.pack()
pin_btn = tk.Button(pin_frame, text="Submit", command=check_pin)
pin_btn.pack()
status_label = tk.Label(pin_frame, text="")
status_label.pack()

# Main ATM interface
main_label = tk.Label(main_frame, text="Please select an option:")
main_label.pack()

balance_btn = tk.Button(main_frame, text="1. Balance", command=show_balance)
balance_btn.pack()

withdraw_btn = tk.Button(main_frame, text="2. Withdraw", command=withdraw_balance)
withdraw_btn.pack()
withdraw_entry = tk.Entry(main_frame)
withdraw_entry.pack()

deposit_btn = tk.Button(main_frame, text="3. Deposit", command=deposit_balance)
deposit_btn.pack()
deposit_entry = tk.Entry(main_frame)
deposit_entry.pack()

exit_btn = tk.Button(main_frame, text="4. Exit", command=exit_program)
exit_btn.pack()

balance_label = tk.Label(main_frame, text="")
balance_label.pack()

main_frame.pack_forget()

root.mainloop()
