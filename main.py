import json
from utils.openspace import Openspace
from utils.file_utils import load_colleagues

# Load the configuration from the JSON file
with open('config.json', 'r') as file:
    config = json.load(file)

# Load the colleagues from the excel file
colleagues = load_colleagues('new_colleagues.txt')

# Create an openspace and organize the colleagues
openspace = Openspace(number_of_tables=config['number_of_tables'], table_capacity=config['table_capacity'])
# Check the capacity
openspace.check_capacity()
# Add or remove the colleagues from the json file
openspace.add_colleagues_from_json('config.json')
openspace.remove_colleagues_from_json('config.json')
# Organize the colleagues
openspace.organize(colleagues)

# Display the results
openspace.display()


# Print the total number of seats, the total number of people, and the number of remaining seats
print(f"Total seats: {openspace.total_seats()}")
print(f"Total people: {openspace.total_people()}")
print(f"Remaining seats: {openspace.remaining_seats()}")