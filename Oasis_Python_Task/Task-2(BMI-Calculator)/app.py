import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI and category
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be positive numbers.")
            return

        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        label_result.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

# GUI setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")

label_weight = tk.Label(root, text="Enter your weight (kg):")
label_weight.pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

label_height = tk.Label(root, text="Enter your height (m):")
label_height.pack()
entry_height = tk.Entry(root)
entry_height.pack()

button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()