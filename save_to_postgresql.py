import os
import json
import psycopg2
from prettytable import PrettyTable

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "muaythai.settings")

# Import the Django settings module
import django
django.setup()

# Now you can import the models
from muaythaiapp.models import Technique

# Read the JSON file
with open('./techniques.json') as json_file:
    data = json.load(json_file)

# Insert records into the database
for technique_data in data['techniques']:
    name = technique_data['name']
    description = technique_data['description']
    img = technique_data['img']
    category = technique_data['category']

    technique = Technique(name=name, description=description, img=img, category=category)
    technique.save(using='default')

# Retrieve the inserted data
techniques = Technique.objects.all()

# Create a table to display the data
table = PrettyTable()
table.field_names = ["id", "name", "description", "img", "category"]

# Add rows to the table
for technique in techniques:
    table.add_row([technique.id, technique.name, technique.description, technique.img, technique.category])

# Print the table
print(table)
