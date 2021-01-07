import db
import scraper
import schedule
import time


db = db.db()
def start():

	# print('Get news from kompas.com')
	# from_kompas = scraper.kompas()
	# print('Get news from cnnindonesia.com')
	# from_cnn = scraper.cnn()
	# print('Get news from liputan6.com')
	# from_liputan6 = scraper.liputan6()
	# print('Get news from bbc.com')
	# from_bbc = scraper.bbc()
	print('Get news from globalnews.ca')
	from_globalnews = scraper.globalnews()

	# insert data from kompas
	# for n in from_kompas:
	#     db.insert(title=n[0], link=n[1], image=n[3], tag=n[2], source=n[4])

	# # insert data from CNN
	# for n in from_cnn:
	#     db.insert(title=n[0], link=n[1], image=n[3], tag=n[2], source=n[4])

	# # insert data from liputan6
	# for n in from_liputan6:
	# 	db.insert(title=n[0], link=n[1], image=n[3], tag=n[2], source=n[4])

	# # insert data from bbc
	# for n in from_bbc:
	# 	db.insert(title=n[0], link=n[1], image=n[3], tag=n[2], source=n[4])

	# insert data from bbc
	for n in from_globalnews:
		db.insert(title=n[0], link=n[1], image=n[3], tag=n[2], source=n[4])
	
	print(db.get_inserted(), 'news inserted.')
	db.set_inserted(0)

schedule.every(0).minutes.do(start)

while True:
	schedule.run_pending()
	time.sleep(1)