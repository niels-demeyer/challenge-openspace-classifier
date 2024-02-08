import json
from utils.openspace import Openspace
from utils.file_utils import load_colleagues
from utils.file_utils import load_json


def compare_json_with_new_colleagues(config):
    config = load_json('config.json')
    colleagues = load_colleagues('new_colleagues.txt')
    new_colleagues = [colleague for colleague in colleagues if colleague not in config['colleagues_to_remove']]
    new_colleagues += [colleague for colleague in config['colleagues'] if colleague not in new_colleagues]
    return new_colleagues
        

config = load_json('config.json')
# Load the colleagues from the excel file
colleagues = compare_json_with_new_colleagues(config=config)

# Create an openspace and organize the colleagues
openspace = Openspace(number_of_tables=config['number_of_tables'], table_capacity=config['table_capacity'])
# Check the capacity
openspace.check_capacity()
# Organize the colleagues
openspace.organize(colleagues)
# Display the results
openspace.display() 


# Print the total number of seats, the total number of people, and the number of remaining seats
print(f"Total seats: {openspace.total_seats()}")
print(f"Total people: {openspace.total_people()}")
print(f"Remaining seats: {openspace.remaining_seats()}")
print(f"config: {config}") 
print(f"colleagues: {colleagues}")