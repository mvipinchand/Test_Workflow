import datetime
import os

# Get current time
current_time = datetime.datetime.now()

# Define the file path on your desktop
file_path = "C:\Users\mvipi\Desktop\new 2.txt"

# Write current time to the file
with open(file_path, 'w') as file:
    file.write(str(current_time))

print(f"Current time has been written to {file_path}")
