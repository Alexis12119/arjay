import tkinter as tk
from tkinter import messagebox

# Initialize the main window
app = tk.Tk()
app.title("Business Income Calculator")
app.geometry("400x300")

# Function to calculate business income
def calculate_income():
    try:
        revenue = float(entry_revenue.get())
        expenses = float(entry_expenses.get())
        income = revenue - expenses
        label_result.config(text=f"Business Income: ₱{income:,.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Heading
label_heading = tk.Label(app, text="Business Income Calculator", font=("Arial", 18))
label_heading.pack(pady=20)

# Revenue input
label_revenue = tk.Label(app, text="Enter Revenue:")
label_revenue.pack(pady=5)
entry_revenue = tk.Entry(app)
entry_revenue.pack(pady=5)

# Expenses input
label_expenses = tk.Label(app, text="Enter Expenses:")
label_expenses.pack(pady=5)
entry_expenses = tk.Entry(app)
entry_expenses.pack(pady=5)

# Calculate button
btn_calculate = tk.Button(app, text="Calculate Income", command=calculate_income)
btn_calculate.pack(pady=20)

# Result display
label_result = tk.Label(app, text="Business Income: ₱0.00", font=("Arial", 16))
label_result.pack(pady=10)

# Run the application
app.mainloop()
