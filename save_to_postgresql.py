import json
import psycopg2
from django.conf import settings

# Connection details from Django settings
database_settings = settings.DATABASES['default']
host = database_settings['HOST']
port = database_settings['PORT']
database = database_settings['NAME']
user = database_settings['USER']
password = database_settings['PASSWORD']

# Read the JSON file
with open('techniques.json') as json_file:
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

# Iterate through the JSON data and insert into the table
for category in data['categories']:
    category_name = category['name']
    moves = category['moves']
    for move in moves:
        move_name = move['name']
        description = move['description']
        image_url = move['img']

        # Execute the SQL statement to insert data
        cur.execute(
            "INSERT INTO your_table (category_name, move_name, description, image_url) VALUES (%s, %s, %s, %s)",
            (category_name, move_name, description, image_url)
        )

# Commit the transaction and close the cursor
conn.commit()
cur.close()

# Close the database connection
conn.close()
