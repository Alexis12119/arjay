import customtkinter as ctk

# Initialize the main window
app = ctk.CTk()
app.title("Business Income Calculator")
app.geometry("400x300")

# Function to calculate business income
def calculate_income():
    try:
        revenue = float(entry_revenue.get())
        expenses = float(entry_expenses.get())
        income = revenue - expenses
        label_result.configure(text=f"Business Income: ${income:,.2f}")
    except ValueError:
        label_result.configure(text="Please enter valid numbers")

# Heading
label_heading = ctk.CTkLabel(app, text="Business Income Calculator", font=("Arial", 18))
label_heading.pack(pady=20)

# Revenue input
label_revenue = ctk.CTkLabel(app, text="Enter Revenue:")
label_revenue.pack(pady=5)
entry_revenue = ctk.CTkEntry(app, placeholder_text="e.g. 50000")
entry_revenue.pack(pady=5)

# Expenses input
label_expenses = ctk.CTkLabel(app, text="Enter Expenses:")
label_expenses.pack(pady=5)
entry_expenses = ctk.CTkEntry(app, placeholder_text="e.g. 20000")
entry_expenses.pack(pady=5)

# Calculate button
btn_calculate = ctk.CTkButton(app, text="Calculate Income", command=calculate_income)
btn_calculate.pack(pady=20)

# Result display
label_result = ctk.CTkLabel(app, text="Business Income: ₱0.00", font=("Arial", 16))
label_result.pack(pady=10)

# Run the application
app.mainloop()
