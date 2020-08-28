# MLBHeadlinesBot

A twitter bot that scrapes mlb.com news headlines and tweets the headlines and their links in a twitter thread. Follow the bot @mlbheadlinesbot or try it out for yourself with your own API keys!

## Set up

1. Create a twitter account if you don't already have one
2. Create an app on developer.twitter.com to access your own API keys
3. Clone this repository
4. Create a file in the root directory called config.py and format it in the following way:
   <pre>
   cKey = "xxxxxxxxxxxxxxxxxxxxxxxxx"
   cKeySecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   aToken = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   aTokenSecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   <pre>
Note: make sure that each key is surrounded by double quotes and the variables are named appropriately

```shell
git clone https://github.com/sambluestone/MLBHeadlinesBot.git
```

5. Install necessary packages

   Beautiful Soup

   ```shell
   pip install bs4
   ```

   Tweepy

   ```shell
   pip install tweepy
   ```

## Usage

Run mlb_webscraper.py in your IDE (if possible) or run in the command line:

```shell
python mlb_webscraper.py
```
