import requests
from bs4 import BeautifulSoup

def kompas():
	page = requests.get('https://www.kompas.com/')
	soup = BeautifulSoup(page.content, 'html.parser')

	latest_news = soup.select('.latest .article__list')

	results = []
	for news in latest_news:
		try:
			title = news.select('.article__list__title h3 a')[0]
			link = title.get('href')
			tag = news.select('.article__list__info .article__subtitle')[0].get_text()
			image = news.select('.article__list__asset .article__asset a img')[0].get('data-src')

			results.append((title.get_text(), link, tag, image, 'kompas'))
		except:
			pass

	return results

def cnn():
	page = requests.get('https://www.cnnindonesia.com/')
	soup = BeautifulSoup(page.content, 'html.parser')

	latest_news = soup.select('.berita_terbaru_lst article a')

	results = []
	for news in latest_news:
		try:
			title = news.select('.box_text h2')[0].get_text()
			link = news.get('href')
			image = news.select('.box_img img')[0].get('src')
			tag = news.select('.box_text .kanal')[0].get_text()

			results.append((title, link, tag, image, 'cnn'))
		except:
			pass

	return results

def liputan6():
	page = requests.get('https://www.liputan6.com/')
	soup = BeautifulSoup(page.content, 'html.parser')

	latest_news = soup.select('.articles--iridescent-list')[2].select('article')

	results = []
	for news in latest_news:
		try:
			title = news.select('figure a')[0].get('title')
			link = news.select('figure a')[0].get('href')
			image = news.select('figure a picture img')[0].get('data-src')
			tag = news.select('aside header a')[0].get_text()

			results.append((title, link, tag, image, 'liputan6'))
		except:
			pass

	return results



	

	