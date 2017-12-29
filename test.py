import newspaper

bangla_paper = newspaper.build('http://www.prothomalo.com/')

for article in bangla_paper.articles:

    try :
        article.download()
        article.parse()
        print(article.url)
        print ('Title :\n' + str(article.title) + '\n')
        print ('Content :\n' + str(article.text) + '\n')

        if (len(article.tags) > 0) :
            print ('Tags :\n' + str(article.tags) + '\n')

    except Exception :
        print(Exception)

'''
#print (newspaper.languages())
url = 'http://www.kalerkantho.com/online/Islamic-lifestylie/2017/12/29/583269';
#url = 'https://bdnews24.com/neighbours/2017/12/29/indian-state-of-assam-tense-ahead-of-citizens-list-targeting-illegal-bangladeshis'
article = Article(url, language='bn')
'''