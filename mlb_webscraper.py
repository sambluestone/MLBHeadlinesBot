from bs4 import BeautifulSoup
import requests
import tweepy
from tweepy import *
import datetime
import config


def tweet_thread(api, hyperlinks, headlines):
    x = datetime.datetime.now()
    date = x.strftime("%A") + ", " + x.strftime("%B") + " " + x.strftime("%d")

    tweets = ["Here are the mlb.com headlines for " + date + "\n"]

    for i in range(len(headlines)):
        tweets.append(headlines[i].get_text().strip() + ": " + hyperlinks[i] +  "\n")

    prevStatus = api.update_status(status = tweets[0])
    for i in range(1, len(tweets)):
        status = api.update_status(status = tweets[i], in_reply_to_status_id = prevStatus.id)
        prevStatus = status

def get_hyperlinks(links):
    
    hyperLinks =  []

    for link in links:
        string = str(link)
        if "Continue Reading" in string:
            index = string.find("href")
            index += 6
            restOfLink = ""
            while string[index] != "\"":
                restOfLink += string[index]
                index += 1

            hyperLinks.append("https://www.mlb.com" + restOfLink)
    
    return hyperLinks


def get_content():
    url = "http://mlb.com/news"
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")
 
def get_headlines(content):
    return content.find_all('span', class_ = "article-navigation__item__meta-headline")

def get_links(content):
    return content.find_all('a', class_ = "p-button__link")

def get_api():
    auth = OAuthHandler(config.cKey, config.cKeySecret)
    auth.set_access_token(config.aToken, config.aTokenSecret)
    return tweepy.API(auth)

def main():
    content = get_content()
    links = get_links(content)
    headlines = get_headlines(content)
    hyperlinks = get_hyperlinks(links)
    api = get_api()
    tweet_thread(api, hyperlinks, headlines)


if __name__ == "__main__":
    main()









