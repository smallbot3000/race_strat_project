# race_strat_project Main File
# Read README before committing

# Char Vars
lap_or_time = ""
multiclass_y_n = ""

# Int Vars
race_pace = 0.0
fuel_per_lap = 0.0
num_of_laps = 0
race_time = 0.0

while True:
    lap_or_time = input("Is the race determined by laps or by time? (Enter 'laps' or 'time'): ")
    if lap_or_time == "laps" or lap_or_time == "time":
        break

if lap_or_time == "laps":
    num_of_laps = int(input("Enter the number of laps: "))
elif lap_or_time == "time":
    race_time = (float(input("Enter the race time in MIN: ")))  # entering minutes shuld allows ease of input

race_pace = float(input("Enter your race pace in seconds: "))
fuel_per_lap = float(input("Enter your fuel per lap: "))

if lap_or_time == "laps":
    print("The race will be " + str((race_pace * num_of_laps) / 60) + " minutes long, and need " + str(fuel_per_lap * num_of_laps) + " gallons of fuel.")
elif lap_or_time == "time":
    print("The race will be " + str((race_time / race_pace) * 60) + " laps long, and need " + str(fuel_per_lap * (race_time / race_pace)) + " gallons of fuel.")