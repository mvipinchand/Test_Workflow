import datetime
import os

# Get current time
current_time = datetime.datetime.now()

# Define the file path on your desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
file_path = os.path.join(desktop_path, 'current_time.txt')

# Write current time to the file
with open(file_path, 'w') as file:
    file.write(str(current_time))

print(f"Current time has been written to {file_path}")
