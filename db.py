import psycopg2
import datetime
from datetime import datetime
import pytz
import os

class db():
	
	def __init__(self):
		self.inserted = 0

	def get_inserted(self):
		return self.inserted

	def set_inserted(self, amount):
		self.inserted = amount

	def insert(self, title, link, image, tag, source):
		try:
		    # Connect to an existing database
		    connection = psycopg2.connect(user=os.environ.get('DB_USER'),
		    	password=os.environ.get('DB_PASSWORD'),
		    	host=os.environ.get('DB_HOST'),
		    	port="5432",
		    	database=os.environ.get('DB_NAME'))

		    cursor = connection.cursor()
		    # Check
		    insert_query =  f"SELECT EXISTS(SELECT 1 FROM news WHERE link = '{link}');"
		    cursor.execute(insert_query)
		    res = cursor.fetchone()

		    timezone = pytz.timezone('Asia/Jakarta')
		    now = timezone.localize(datetime.now())

		    if res[0] == False:
		    	cursor.execute("""INSERT INTO news (title, link, image, tag, source, created_at, updated_at) 
		    		VALUES (%s, %s, %s, %s, %s, %s, %s)""",
		    		(title, link, image, tag.title(), source, now, now))
		    	self.inserted += 1
		    	connection.commit()

		except (Exception, psycopg2.Error) as error:
			pass
		finally:
			if (connection):
				cursor.close()
				connection.close()

