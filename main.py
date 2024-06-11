# race_strat_project Main File
# Read README before commiting

import tkinter as tk
from tkinter import ttk

def print_strategy():
    # Example strategy printing logic
    print(f"Car: {car_var.get()}, Race Type: {race_type_var.get()}, "
          f"Laps/Time: {laps_time_var.get()}, Other Cars: {other_cars_var.get()}")

# Create the main window
root = tk.Tk()
root.title("Race Strategy Generator")

# Car selection dropdown
car_var = tk.StringVar(root)
car_options = ["Car A", "Car B", "Car C"]
car_dropdown = ttk.Combobox(root, textvariable=car_var, values=car_options, state="readonly")
car_dropdown.grid(column=0, row=0)

# Race type selection
race_type_var = tk.StringVar(root)
race_types = [("Lap", "lap"), ("Time", "time")]
race_type_dropdown = ttk.OptionMenu(root, race_type_var, *race_types)
race_type_dropdown.grid(column=1, row=0)

# Input for laps or time
laps_time_var = tk.StringVar(root)
laps_time_entry = ttk.Entry(root, textvariable=laps_time_var)
laps_time_entry.grid(column=0, row=1)

# Multiclass race selection
other_cars_var = tk.StringVar(root)
other_cars_options = ["Car D", "Car E", "Car F"]
other_cars_dropdown = ttk.Combobox(root, textvariable=other_cars_var, values=other_cars_options, state="readonly")
other_cars_dropdown.grid(column=1, row=1)

# Print strategy button
strategy_button = ttk.Button(root, text="Print Strategy", command=print_strategy)
strategy_button.grid(columnspan=2, row=2)

# Run the application
root.mainloop()
