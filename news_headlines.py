import requests
from bs4 import BeautifulSoup

def abc_headlines():
    """
    Gets the current headlines of the ABC News website.
        Returns:
            list of strings representing the headlines
    """

    page = requests.get("https://abc.net.au/news")
    soup = BeautifulSoup(page.content, 'html.parser')  
    top_stories = soup.select_one('div[data-component="TopStories"]')
    headlines_tags = top_stories.find_all('span', attrs={"data-component": "KeyboardFocus"})
    headlines = list(map(lambda h: h.text, headlines_tags))
    return headlines