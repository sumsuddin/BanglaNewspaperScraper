import newspaper
from newspaper import SingleCategorySource
from newspaper import Source
import requests

'''
url = 'http://www.kalerkantho.com/print-edition/2018/01/11'

catSource = SingleCategorySource(url, memoize_articles=False, number_threads=20)
catSource.build_as_category()
print (catSource.size())

for article in catSource.articles:
    print(article.url)


'''
url = 'http://www.kalerkantho.com'
bangla_paper = Source(url, memoize_articles=False, number_threads=20)
bangla_paper.build()
print (bangla_paper.size())

for article in bangla_paper.articles:

    try :
        article.download()
        article.parse()
        print(article.url)
        '''
        print ('Title :\n' + str(article.title) + '\n')
        print ('Content :\n' + str(article.text) + '\n')

        if (len(article.tags) > 0) :
            print ('Tags :\n' + str(article.tags) + '\n')
        else :
            print('Tags :\n{}\n')
        '''
        r = requests.post('http://127.0.0.1:8000/news/', auth=('admin', 'styls327'), json={"title": article.title, "link": article.url, "article": article.text})
        if (r.ok):
            print ("Sucess with status code: " + str(r.status_code))
        else:
            print ("Failed with status code: " + str(r.status_code))

    except Exception :
        print(Exception)


'''
#print (newspaper.languages())
url = 'http://www.kalerkantho.com/online/Islamic-lifestylie/2017/12/29/583269';
#url = 'https://bdnews24.com/neighbours/2017/12/29/indian-state-of-assam-tense-ahead-of-citizens-list-targeting-illegal-bangladeshis'
article = Article(url, language='bn')
'''