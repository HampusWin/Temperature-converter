import tkinter as tk

#Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("720x360")
root.config(bg="green")

#Function to convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit():
    try:
        celsius = float(entry.get())
        fahrenheit = celsius * 9 / 5 + 32
        result_label.config(text=f"{celsius}° Celsius = {fahrenheit}° Fahrenheit")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

#Function to convert Fahrenheit to Celsius
def convert_fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5 / 9
        celsius = round(celsius, 2)#Make the decimals stop after 2
        result_label.config(text=f"{fahrenheit}° Fahrenheit = {celsius}° Celsius")
    except ValueError:#If not a numeric answer or a unvalid input
        result_label.config(text="Please enter a valid number.")

#Create a label
label = tk.Label(root, text="Welcome to Winborgs super duper simple temperature converter! Please enter a value and choose a conversion type.",
font=("Times new roman", 12))
label.pack(pady=20)

#Create an entry for the temperature input
entry = tk.Entry(root, font=("Times new roman", 12))
entry.pack(pady=10)

#Create buttons for both conversion types
celsius_to_fahrenheit_button = tk.Button(root, text="Convert Celsius to Fahrenheit", font=("Times new roman", 12),
command=convert_celsius_to_fahrenheit)
celsius_to_fahrenheit_button.pack(pady=5)

fahrenheit_to_celsius_button = tk.Button(root, text="Convert Fahrenheit to Celsius", font=("Times new roman", 12),
command=convert_fahrenheit_to_celsius)
fahrenheit_to_celsius_button.pack(pady=5)

#Label to display the result
result_label = tk.Label(root, text="", font=("Times new roman", 14))
result_label.pack(pady=20)

#Start the main loop
root.mainloop()
