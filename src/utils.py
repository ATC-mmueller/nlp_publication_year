class PrivateKeysHandler:
    def __init__(self, relative_path_to_file : str):
        from configparser import RawConfigParser
        import os
        self.configParser = RawConfigParser()   
        configFilePath = os.path.join(os.path.dirname(''), relative_path_to_file) 
        self.configParser.read(configFilePath)

    def load_keys(self, section : str) -> dict:
        return self.configParser[section]
    
    
def dict_to_csv(author, author_dict):
    import flatdict
    import pandas as pd
    auth_dict = flatdict.FlatterDict(authors_dict)
    auth_df = pd.DataFrame(data = zip(auth_dict.keys(), auth_dict.values()),
                         columns = ['keys', 'values'])
    auth_df.to_csv('data/' + author + '.csv', index=False)
    
def csv_to_dict(author):
    import flatdict
    import pandas as pd
    df = pd.read_csv('data/' + author + '.csv')
    d = {}
    for key, value in zip(df['keys'], df['values']):
        d[key] = value
    d = flatdict.FlatterDict(d).as_dict()
    for title in d['titles']:
        d['titles'][title]['chapters'] = list(d['titles'][title]['chapters'].values())
    return d



    
        
    
# def get_titles_links(url):
#     from bs4 import BeautifulSoup
#     import requests
#     r = requests.get(url)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     titles = []
#     titles_links = []
#     for a in soup.select('.archived ul li a'): 
#         titles.append(a.get_text()) #name of the title
#     # url is of the for ../../actual url, therefore we skip the first 5 chars
#         titles_links.append(a['href'][5:]) 
#     return titles, titles_links

# def get_titles(author):
#     author_url = 'https://www.projekt-gutenberg.org/autoren/namen' + author + '.html'
#     response = requests.get(author_url)
#     if response.status_code != 200:
#         return
#     soup = BeautifulSoup(response.content, 'html.parser')
#     for a in soup.select('.archived ul li a'):  #name of the title
#         # url is of the for ../../actual url, therefore we skip the first 5 chars
#         authors_dict[author]['titles'][a.get_text()] = {}
#         authors_dict[author]['titles'][a.get_text()]['link'] = a['href'][5:]
#         authors_dict[author]['titles'][a.get_text()]['chapters'] = []
    
# for author in authors_dict:
#     author_url = 'https://www.projekt-gutenberg.org/autoren/namen/' + author + '.html'
#     response = requests.get(author_url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     for a in soup.select('.archived ul li a'):  #name of the title
#         # url is of the for ../../actual url, therefore we skip the first 5 chars
#         authors_dict[author]['titles'][a.get_text()] = {}
#         authors_dict[author]['titles'][a.get_text()]['link'] = a['href'][5:]
#         authors_dict[author]['titles'][a.get_text()]['chapters'] = []
    
    
#     for title in authors_dict[author]['titles']:
#         url = gutenberg_url + authors_dict[author]['titles'][title]['link'] #get to title page
#         r = requests.get(url)
#         soup = BeautifulSoup(r.content, 'html.parser')
    
#         year = soup.select('meta[name = firstpub]')
#         if len(year) > 0:
#             authors_dict[author]['titles'][title]['year'] = int(year[0]['content'])
#         else:
#             authors_dict[author]['titles'][title]['year'] = 0
        
#     # collect each chapters url
#         chapters_links = soup.select('.dropdown-content li a[href]') 
#         paragraphs = soup.select('a[href] ~ p, .poem') 
#         text = ''
#         for par in paragraphs:
#             text += par.get_text()
#         authors_dict[author]['titles'][title]['chapters'].append(text)
#         for i in range(len(chapters_links)-1):
#             url = url.replace(url.rsplit('/', 1)[-1], chapters_links[i+1]['href'])
#             r = requests.get(url)
#             soup = BeautifulSoup(r.content, 'html.parser')
#             # text is split into several paragraphs, that can consist of poems
#             # we staert collecting after a certain header
#             paragraphs = soup.select('a[href] ~ p, .poem') 
#             text = ''
#             for par in paragraphs:
#                 text += par.get_text()
#             authors_dict[author]['titles'][title]['chapters'].append(text)