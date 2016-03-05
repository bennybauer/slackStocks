# Slack Stocks
A slack slash command that gives you pricing information on a stock ticker

![Showcase](https://github.com/savala/slackStocks/blob/master/screenshots/screenshot.png)


# Setup

In your team settings, add a Slash Command Configuration
![Add a custom slash command configuration](https://github.com/savala/slackStocks/blob/master/screenshots/setup2.png)


Make sure your settings are like so:
1. Add the command name "/stock"
2. Add in the URL like so "http://<yourappurl>/stock
⋅⋅1. This assumes that you've deployed your application to AWS, heroku, digitalocean, or wherever you feel like so
⋅⋅2. Essentially, in slack when you type in "  /stock xyz  ", it will automatically call the above url as http://yourappurl/stock?text=xyz
3. If you've configured it correctly then you should be good to go! I've added a setup screenshot below as well

![Add a custom slash command configuration](https://github.com/savala/slackStocks/blob/master/screenshots/setup3.png)


If you have any questions, concerns, or anything feel free to reach out to me @savala
