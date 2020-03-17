#!/usr/bin/env python3
#!/usr/local/lib/python3.7/site-packages requests
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import os
import requests


# In[2]:


# the test variables
journalurl = "https://link.springer.com/journal/10982/volumes-and-issues" # law and philosophy
issueurl = "https://link.springer.com/journal/10506/27/2"
articleurl = "https://link.springer.com/article/10.1007/s10506-019-09243-2"
baseurl = "https://link.springer.com"
scihuburl = "https://sci-hub.tw/" # node in Taiwan
# scihub = "https://scihub.bban.top" # node in Singapore

proxies = {
  "http": "http://127.0.0.1:1087",
  "https": "http://127.0.0.1:1087",
}


# In[3]:


def getpage(url):
    # return BeautifulSoup(requests.get(url=url,proxies=proxies).content,'lxml')
    return BeautifulSoup(requests.get(url=url,proxies=proxies).content,'html.parser')


# In[4]:


def downloader(filename,url):
    open(filename,'wb').write(requests.get(url, allow_redirects=True,proxies=proxies).content)    


# In[5]:


class Article:
    def __init__(self, soup):
        self.title = soup.get_text()
        self.citeurl = baseurl+soup.get('href')+".ris"
        onclick = getpage(scihuburl+baseurl+soup.get('href')).findAll('a',{'href' : '#'})[0].get('onclick')
        try:
            self.saveurl = onclick[onclick.index('https://'):-1]
        except:
            self.saveurl = "https:"+onclick[onclick.index('//'):-1]


# In[6]:


class Issue:
    def __init__(self, soup):
        soup = getpage(baseurl+soup.get('href'))
#         self.title = soup.findAll('h1',{'id':'title'})[-1].get_text()
        self.title = soup.h1.get_text()
        self.articles = [i.a for i in soup.find_all('h3')]


# In[7]:


class Journal:
    def __init__(self, soup):
        self.title = soup.findAll('div',{'id' : 'journalTitle'})[0].a.contents[0]
        self.issues = [i for i in soup.findAll('a',{'class':"u-interface-link u-text-sans-serif u-text-sm"})]


# In[8]:


def parser(url):
    soup = getpage(url)
    journal = Journal(soup)
    # title = journal.title
    try:
        os.mkdir(journal.title)
        print("The folder {title} has been created.\n".format(title=journal.title))
    except:
        print("The folder {title} exists already.\n".format(title=journal.title))
    
    os.chdir(journal.title)
    path = os.getcwd()
    
    for i in journal.issues:
#         print(i)
        try:
            issue = Issue(i)
            print(issue.title)
        except:
            print('cannot instantiate issue\n')
            continue
            
        try:
            os.mkdir(issue.title)
            print("The folder {title} has been created.\n".format(title=issue.title))
        except:
            print("The folder {title} exists already.\n".format(title=issue.title))
            
        os.chdir(issue.title)
        
        for k in issue.articles:
#             print(k)
            try:
                article = Article(k)
                print(article.title)
            except:
                print('cannot instantiate article\n')
                continue
                
            downloader(article.title+".pdf",article.saveurl)
            downloader(article.title+".ris",article.citeurl)
        
        os.chdir(path)


# In[9]:


# parser("https://link.springer.com/journal/10506/volumes-and-issues")


# In[ ]:




