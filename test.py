from newspaper import Source
import requests

urls = ['http://www.kalerkantho.com', 'http://www.prothomalo.com'] # add new newspaper here...

for url in urls:
    bangla_paper = Source(url, memoize_articles=False, number_threads=20)
    bangla_paper.build()
    print (bangla_paper.size())

    for article in bangla_paper.articles:

        try :
            article.download()
            article.parse()
            print(article.url)

            publish_date = "1952-01-01T00:00:00Z"

            if (article.publish_date is not None) :
                publish_date = article.publish_date.strftime('%Y-%m-%dT00:00:00Z')


            r = requests.post('http://127.0.0.1:8000/news/', auth=('admin', 'styls327'),
                              json={
                                  "title": article.title,
                                  "link": article.url,
                                  "publish_date": publish_date,
                                  "article": article.text})
            if (r.ok):
                print ("Sucess with status code: " + str(r.status_code))
            else:
                print ("Failed with status code: " + str(r.status_code) + " " + r.text)

        except Exception :
            print(repr(Exception))
