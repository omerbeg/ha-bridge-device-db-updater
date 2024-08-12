import json
import re

# Load the content of the file
with open('device.db', 'r') as file:
    data = file.read()

# Parse the JSON data
devices = json.loads(data)

# Initialize the counter for uniqueid
counter = 1

# Update uniqueid for each device
for device in devices:
    # Format the counter to be two digits
    counter_str = f'{counter:02d}'
    # Replace the uniqueid
    device['uniqueid'] = f'00:11:22:33:44:55:66:{counter_str}-00'
    counter += 1
    # Reset the counter after 99
    if counter > 99:
        counter = 1

# Convert the modified devices back to JSON string
modified_data = json.dumps(devices, ensure_ascii=False, indent=2)

# Save the modified content back to the file
with open('device.db', 'w') as file:
    file.write(modified_data)

print("uniqueid values updated successfully in the file!")
