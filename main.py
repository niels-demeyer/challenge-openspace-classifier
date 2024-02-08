import json
from utils.openspace import Openspace
from utils.file_utils import load_colleagues

# Load the configuration from the JSON file
with open('config.json', 'r') as file:
    config = json.load(file)

# Load the colleagues from the excel file
colleagues = load_colleagues('new_colleagues.xlsx')

# Create an openspace and organize the colleagues
openspace = Openspace(number_of_tables=config['number_of_tables'], table_capacity=config['table_capacity'])
openspace.organize(colleagues)

# Display the results
openspace.display()

# Store the results
openspace.store('results.xlsx')

# Add a new colleague
openspace.add_colleague('New Colleague')

# Add a new table
openspace.add_table(4)

# Display the updated results
openspace.display()

# Store the updated results
openspace.store('updated_results.xlsx')

# Print the total number of seats, the total number of people, and the number of remaining seats
print(f"Total seats: {openspace.total_seats()}")
print(f"Total people: {openspace.total_people()}")
print(f"Remaining seats: {openspace.remaining_seats()}")