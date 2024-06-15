# race_strat_project Main File
# Read README before commiting

import tkinter as tk
from tkinter import ttk

def print_strategy():
    # Example strategy printing logic
    print(f"Car: {car_var.get()}, Race Type: {race_type_var.get()}, "
          f"Laps/Time: {laps_time_var.get()}, Other Cars: {other_cars_var.get()}")

root = tk.Tk()                         # Create the main window
root.title("Race Strategy Generator")  # Set the window title

car_var = tk.StringVar(root)               # Car selection dropdown variable
car_options = ["Car A", "Car B", "Car C"]  # Car options
car_dropdown = ttk.Combobox(root, textvariable=car_var, values=car_options, state="readonly")
car_dropdown.grid(column=0, row=0)

race_type_var = tk.StringVar(root)               # Race type selection
race_types = [("Lap", "lap"), ("Time", "time")]  # Race type options
race_type_dropdown = ttk.OptionMenu(root, race_type_var, *race_types)
race_type_dropdown.grid(column=1, row=0)

laps_time_var = tk.StringVar(root)  # Input for laps or time
laps_time_entry = ttk.Entry(root, textvariable=laps_time_var)
laps_time_entry.grid(column=0, row=1)

other_cars_var = tk.StringVar(root)  # Multiclass race selection
other_cars_options = ["Car D", "Car E", "Car F"]
other_cars_dropdown = ttk.Combobox(root, textvariable=other_cars_var, values=other_cars_options, state="readonly")
other_cars_dropdown.grid(column=1, row=1)

strategy_button = ttk.Button(root, text="Print Strategy", command=print_strategy)  # Print strategy button
strategy_button.grid(columnspan=2, row=2)

root.mainloop()  # Run the application
