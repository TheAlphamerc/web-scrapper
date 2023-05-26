from bs4 import BeautifulSoup
import requests
import datetime
from util import tagList


def readMeta(url):
    print('\nURL :', url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser",
                         from_encoding="utf-8", )

    # Get title string from soup if is is not None
    title = soup.title.string if soup.title is not None else ''
    print('TITLE IS :', title)

    meta = soup.find_all('meta')
    print('TOTAL META TAGS :', len(meta))
    results = {
        'url': url,
        'title': title,
        'date': datetime.datetime.now().utcnow().isoformat()
    }
    tags = tagList()
    for tag in meta:
        try:
            if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in tags:
                print(tag.attrs['name'], tag.attrs['content'].lower())
                results.update(
                    {tag.attrs['name'].lower(): str(tag.attrs['content'])})
            elif 'property' in tag.attrs.keys() and tag.attrs['property'].strip().lower() in tags:
                print(tag.attrs['property'], '          :',
                      tag.attrs['content'].lower())
                results.update(
                    {tag.attrs['property'].lower(): str(tag.attrs['content'])})
        except Exception as e:
            print('\n\nERROR:', e)

    return results
