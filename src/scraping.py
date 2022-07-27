import requests
from bs4 import BeautifulSoup

def scrape_titles_years(author_url : str) -> list:
    url = 'https://www.projekt-gutenberg.org/autoren/namen/' + author_url + '.html'
    response = requests.get(url)
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.content, 'html.parser')
    titles_years_list = []
    for a in soup.select('.archived ul li a'):
        if '../../' in a['href']:
            titles_years_list.append([author_url, a.get_text(), a['href'][5:]])
    
    for title in titles_years_list:
        url = 'https://www.projekt-gutenberg.org' + title[2]
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        
        year = soup.select('meta[name = firstpub]')
        if len(year) > 0:
            title.append(year[0]['content'])
        else:
            title.append(0)
    return titles_years_list

def scrape_chapters(title_url : str) -> list:
    titles_chapters_list = []
    url = 'https://www.projekt-gutenberg.org' + title_url
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    chapters_links = soup.select('.dropdown-content li a[href]') 

    paragraphs = soup.select('a[href] ~ p, .poem') 
    text = ''
    for par in paragraphs:
        text += par.get_text()
    titles_chapters_list.extend([title_url, 0, text])
        #collect text from following chapters
    for i in range(len(chapters_links)-1):
        url = url.replace(url.rsplit('/', 1)[-1], chapters_links[i+1]['href'])
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
            # text is split into several paragraphs, that can consist of poems
            # we staert collecting after a certain header
        paragraphs = soup.select('a[href] ~ p, .poem') 
        text = ''
        for par in paragraphs:
            text += par.get_text()
        titles_chapters_list.extend([title_url, i+1, text])
    return titles_chapters_list
    
    
    
def scrape_birth_year(author_url : str) -> int:
    wiki_url = 'https://en.wikipedia.org/wiki/'
    wiki_author_url = wiki_url + author_url
    r = requests.get(wiki_author_url)
    if r.status_code != 200:
        return 2
    soup = BeautifulSoup(r.content, 'html.parser')
    categories = soup.select('#mw-normal-catlinks > ul > li')
    for cat in categories:
        if 'births' in cat.get_text():
            return int(cat.get_text()[:4])
    return 0
      
    
    
def scrape_death_year(author_url : str) -> int:
    wiki_url = 'https://en.wikipedia.org/wiki/'
    wiki_author_url = wiki_url + author_url
    r = requests.get(wiki_author_url)
    if r.status_code != 200:
        return 2
    soup = BeautifulSoup(r.content, 'html.parser')
    categories = soup.select('#mw-normal-catlinks > ul > li')
    for cat in categories:     
        if 'deaths' in cat.get_text():
            return int(cat.get_text()[:4])
    return 0