import os
import json
import psycopg2

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "muaythai.settings")

# Import the Django settings module
import django
django.setup()

# Now you can import the settings
from django.conf import settings

# Database settings from Django settings
database_settings = settings.DATABASES['default']
host = database_settings['HOST']
port = database_settings['PORT']
database = database_settings['NAME']
user = database_settings['USER']
password = database_settings['PASSWORD']

# Read the JSON file
with open('./techniques.json') as json_file:
    data = json.load(json_file)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

# Create a cursor
cur = conn.cursor()

# Insert records into the database
for category in data['categories']:
    for move in category['moves']:
        name = move['name']
        description = move['description']
        img = move['img']
        category_name = category['category']

        cur.execute(
            "INSERT INTO muaythaiapp_category (name, description, img, category) VALUES (%s, %s, %s, %s)",
            (name, description, img, category_name)
        )

# Commit the transaction and close the cursor
conn.commit()
cur.close()

# Close the database connection
conn.close()
