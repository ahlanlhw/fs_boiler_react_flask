import feedparser as fp
import re
# class requester():
def get_feed():
    dd = []
    d= fp.parse("https://www.reddit.com/r/CryptoCurrency/.rss")
    clean = re.compile(r'[^\x00-\x7F]+')
    for k in range(len(d['entries'])):
        dd.append(
        {
        "key": k,
        "title":re.sub(clean, ' ',d['entries'][k].title),
        "published":d['entries'][k].published,
        "url":d['entries'][k]['link']
        }
        )
    return dd