# Telegram Youtube Livestream Notifier
A Python bot that notifies you via Telegram whenever the specified YouTube channel starts or stops livestreaming. It doesn't use YouTube's API and it can be running 24/7 for free using Replit and UptimeRobot.

## Setup
In order for the bot to work, you have to follow these steps which are explained in greater detail below.
- Setup a new Repl
- Create a Telegram Bot
- Run your Repl and use UptimeRobot to keep it active 24/7

### Setting Up Your Repl
First you'll have to setup a Repl:
1. Go to [replit.com](https://replit.com/) and create an account.
2. Make a new Repl by pressing the blue `+ Create` button.
3. Select Python as a Template, give it a title and click `+ Create Repl`
4. Wait for the IDE to load
5. On the left-hand side, delete the `main.py` file, click the 3 vertical dots next to the folder icon with the "+" symbol inside it and select `Uplaod File`
6. Select the `main.py` and `keep_alive.py` files you downloaded from this repository and upload them

Next, you're going to have to install the dependencies.  You can accomplish this either by using the `pip` command in the shell command line to your right or by selecting the 4th element from the menu on the left named "Packages" and using the search bar to find the following packages:

```
requests    (2.28.1)
Flask       (2.1.3)
urllib3     (1.26.10)
bs4         (0.0.1)
lxml        (4.9.1)
```
**Note:** The bot has been tested in `Python 3.8.12`. In the unlike scenario of the bot not working properly in newer versions of Python, try using that one instead. Additionally, in parentheses you can find the package versions used while testing the bot.

7. Select the lock from the menu on the left (5th element) named "Secrets (Environment Variables)"
8. Add the following 4 key-value pairs

| Key | Value |
| ------ | ------ |
| TOKEN | YOUR_BOT_TOKEN |
| CHAT_ID | YOUR_TELEGRAM_ACCOUNT_ID |
| CHANNEL_ID | YOUTUBE_CHANNEL_ID |
| CHANNEL_NAME | YOUTUBE_CHANNEL_NAME |

Make sure that the keys are written exactly like in the table. Below you'll find instructions on how to obtain each value mentioned above.

### Creating a Telegram Bot

1. Create a Telegram account using your phone number
2. Go to settings and set a username. It is required to obtain an ID that your bot will use to message you
3. Search for RawDataBot and send any message to that bot. It will reply with `YOUR_TELEGRAM_ACCOUNT_ID`
4. Search for BotFather and send the message `/start`. Then send the message `/newbot` and follow the instructions. After a few messages the bot will give you an HTTP API token. That is `YOUR_BOT_TOKEN`
5. You'll also get a `t.me/your_bot_name` link. Click on it to open a new chat with your bot and send any message. After that, your bot will be able to message you

Now for the `YOUTUBE_CHANNEL_ID`:

1. Go to the desired YouTube channel
2. Press `Ctrl + U` to view the page's source code
3. Press `Ctrl + F` and search for `externalId`
4. You'll find something like `"externalId":"UCjBCvQBVTh4XjPwtSMQNcFg"`. `UCjBCvQBVTh4XjPwtSMQNcFg` is the `YOUTUBE_CHANNEL_ID`

The `YOUTUBE_CHANNEL_NAME` can be whatever you want. It's the name the bot is going to use when referring to the channel that's being monitored.

**Note:** It's important you pass these values as Environment Variables and not have them hardcoded inside the `main.py` file as all free Repls are **PUBLIC**! Using Environment Variables you can make sure that your tokens, passwords, etc. are not publicly visible.

### Keeping Your Bot Running 24/7
The free tier on Replit won't allow you to run Repls non-stop. Fortunately, there is a free workaround that works perfectly in our case.

1. Go to [uptimerobot.com](https://uptimerobot.com/) and create an account
2. Once you're redirected to the Dashboard click the green `+ Add New Monitor` button
3. Go back to Replit and run `main.py`. If everything worked as expected you should see a simple white page saying "Hello. I am alive!" on the top right of the IDE
4. Exactly above the greeting message you can find a URL that looks like this `https://YourAppName.YourUsername.repl.co`. Copy it and go back to UptimeRobot
5. In the `Monitor Type` choose `HTTP(s)`
6. `Friendly Name` can be whatever name you want. In the `URL` field paste the URL you copied from Replit earlier. Set the `Monitoring Interval` to 5 minutes (the minimum interval in the free plan). Leave `Monitor Timeout` as is. Deselect both checkboxes about `SSL` and click `Create Monitor`. Ignore any prompts about upgrading to the PRO Version and continue with the creation of the Monitor

After successfully creating the Monitor make sure that your Repl is still running. If you did everything right the Monitor will keep pinging your Repl every 5 minutes and thus not allowing it to fall asleep due to inactivity.

That's it!

## Future Improvements
- Read the checking time interval and other settings from a config file
- Allow the user to change settings using commands without the need to restart the Repl
- Make it possible to monitor multiple channels at once
- Read and write the `notificationSent` status from a file instead of a variable. Even though the method described above can keep your Repl alive 27/4, Replit occasionally resets Repls to move them to different servers. The downtime is only a few minutes max but can lead to the bot sending multiple notifications for the same Livestream. Reading from a file would solve that problem.

## Limitations
- The bot does not use the YouTube API so it doesn't have any theoretical limit to the requests it can send to YouTube. However, since checking whether a channel is Live or not is done by looking for specific HTML tags with the help of BeautifulSoup, this method could break in case YouTube changes its Channel Pages' HTML structure.

P.S. Use this bot at your own risk. Please **DO NOT SPAM** YouTube with countless requests per second. Checking every minute or so worked just fine for me and I never had any issues.