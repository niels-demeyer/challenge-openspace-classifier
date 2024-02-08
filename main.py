from utils.openspace import Openspace
from utils.file_utils import load_colleagues

# Load the colleagues from the excel file
colleagues = load_colleagues('new_colleagues.txt')

# Create an openspace and organize the colleagues
openspace = Openspace(number_of_tables=6, table_capacity=4)
openspace.organize(colleagues)

# Display the results
openspace.display()

# Store the results
openspace.store('results.xlsx')