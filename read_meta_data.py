from bs4 import BeautifulSoup
import requests


def readMeta(url):
    # r = requests.get('http://www.aurionpro.com/')
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser",
                         from_encoding="utf-8", )

    title = soup.title.string
    print('TITLE IS :', title)

    meta = soup.find_all('meta')
    results = {
        'title': title
    }
    tagsList = [
        'description',
        'keywords',
        'language',
        'author',
        'url',
        'content-language',
        'content-type',
        'content-encoding',
        # FACEBOOK
        'og:title',
        'og:description',
        'og:image',
        'og:url',
        'og:site_name',
        'og:type',
        # TWITTER
        'twitter:card',
        'twitter:site',
        'twitter:title',
        'twitter:description',
        'twitter:image',
        'twitter:url',
        'twitter:creator',
        'twitter:site',
        'twitter:domain',
        # BASIC
        'generator',
        'application-name',
    ]
    for tag in meta:
        try:
            if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in tagsList:
                print('NAME    :', tag.attrs['name'].lower())
                print('CONTENT :', tag.attrs['content'])
                results.update(
                    {tag.attrs['name'].lower(): str(tag.attrs['content'])})
            elif 'property' in tag.attrs.keys() and tag.attrs['property'].strip().lower() in tagsList:
                print('PROPERTY:', tag.attrs['property'].lower())
                print('CONTENT :', tag.attrs['content'])
                results.update(
                    {tag.attrs['property'].lower(): str(tag.attrs['content'])})
        except Exception as e:
            print(e)

    return results
