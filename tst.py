from datetime import datetime, timedelta

# Start date and time
start_date = datetime(2025, 3, 8, 8, 0, 0)

# Given time
hours, minutes, seconds = 155, 51, 50

# Convert hours to days and remaining hours
days = hours // 24
remaining_hours = hours % 24

# Create a timedelta object
time_delta = timedelta(days=days, hours=remaining_hours, minutes=minutes, seconds=seconds)

# Calculate the final date and time
final_date = start_date + time_delta

# Print the result in 12-hour format with AM/PM
print("Start Date and Time:", start_date.strftime('%Y-%m-%d %I:%M:%S %p'))
print("Final Date and Time:", final_date.strftime('%Y-%m-%d %I:%M:%S %p'))