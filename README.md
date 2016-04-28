# Slack Stocks w/ Zappa
This repo uses [SlackStocks](https://github.com/savala/slackStocks) - a slack slash command that gives you pricing information on a stock ticker, 
together with [Zappa](https://github.com/Miserlou/Zappa) - a wrapper for running WSGI in AWS Lambda.   


## Usage

1. `pip install -r requirements.txt`

2. Create `zappa_settings.json` based on the attached template

3. [Configure](https://blogs.aws.amazon.com/security/post/Tx3D6U6WSFGOK2H/A-New-and-Standardized-Way-to-Manage-Credentials-in-the-AWS-SDKs) your AWS credentials 

4. Deploy with `zappa deploy dev`

5. In your slack team settings, add a Slash Command Configuration
![Add a custom slash command configuration](https://github.com/savala/slackStocks/blob/master/screenshots/setup2.png)


Make sure your settings are like so:

1. Add the command name "/stock"
2. Add in the URL like so "http://<yourappurl>/stock
    * Essentially, in slack when you type in "/stock xyz", it will automatically call the above url as http://yourappurl/stock?text=xyz
3. Set the Method type to GET
4. If you've configured it correctly then you should be good to go! I've added a setup screenshot below as well

![Add a custom slash command configuration](https://github.com/savala/slackStocks/blob/master/screenshots/setup3.png)
