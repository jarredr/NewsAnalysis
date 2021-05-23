import requests
from bs4 import BeautifulSoup


def get_page(url):
    """
    Helper function which gets the HTML content of a website.
        Returns:
            BeautifulSoup object representing the web page
    """
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')


def abc_headlines():
    """
    Gets the current headlines of the ABC News website.
        Returns:
            list of strings representing the headlines
    """

    soup = get_page("https://abc.net.au/news")
    top_stories = soup.select_one('div[data-component="TopStories"]')
    headlines_tags = top_stories.find_all('span', attrs={"data-component": "KeyboardFocus"})
    headlines = list(map(lambda h: h.text, headlines_tags))
    return headlines


def news_dotcomau_headlines():
    """
    Gets the current headlines of the news.com.au website.
        Returns:
            list of strings representing the headlines
    """
    soup = get_page("https://www.news.com.au/national/national-news")
    headlines_tags = soup.select('h4[class="heading"] a')[:30]
    headlines = list(map(lambda h: h.text[4:-3], headlines_tags))
    return headlines


def smh_headlines():
    """
    Gets the current headlines of the smh.com.au website.
        Returns:
            list of strings representing the headlines
    """
    soup = get_page("https://www.smh.com.au/national")
    headlines_tags = soup.select('h3[data-testid="article-headline"] a')
    headlines = list(map(lambda h: h.text, headlines_tags))
    return headlines


def nine_headlines():
    """
    Gets the current headlines of the 9news.com.au website.
        Returns:
            list of strings representing the headlines
    """
    soup = get_page("https://www.9news.com.au/national")
    headlines_tags = soup.select('span[class="story__headline__text"]')[:30]
    headlines = list(map(lambda h: h.text, headlines_tags))
    return headlines


def australian_headlines():
    """
    Gets the current headlines of the theaustralian.com.au website.
        Returns:
            list of strings representing the headlines
    """
    soup = get_page("https://www.theaustralian.com.au/nation")
    headlines_tags = soup.select('h3[class="story-block__heading"] a')[:30]
    headlines = list(map(lambda h: h.text, headlines_tags))
    return headlines


def guardian_headlines():
    """
    Gets the current headlines of the theguardian.com website.
        Returns:
            list of strings representing the headlines
    """
    soup = get_page("https://www.theguardian.com/australia-news/all")
    headlines_tags = soup.select('span[class="js-headline-text"]')[:30]
    headlines = list(map(lambda h: h.text, headlines_tags))
    return headlines


def sbs_headlines():
    """
    Gets the current headlines of the sbs.com.au website.
        Returns:
            list of strings representing the headlines
    """
    soup = get_page("https://www.sbs.com.au/news/topic/australia")
    headlines_tags = soup.select('p[class="headline preview__headline"] a')[:30]
    headlines = list(map(lambda h: h.text, headlines_tags))
    return headlines
    

def skynews_headlines():
    """
    Gets the current headlines of the skynews.com.au website.
        Returns:
            list of strings representing the headlines
    """
    soup = get_page("https://www.skynews.com.au/page/national-news")
    headlines_tags = soup.select('a[class="card-img-overlay"]')[:30]
    headlines = list(map(lambda h: h.attrs['aria-label'], headlines_tags))
    return headlines