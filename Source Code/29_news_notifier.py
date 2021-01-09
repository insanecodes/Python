import feedparser
from win10toast import ToastNotifier


def parsefeed():
    feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")

    for news in feed['items']:
        ToastNotifier().show_toast(news['title'], news['summary'], duration=15)


if __name__ == "__main__":
    parsefeed()
