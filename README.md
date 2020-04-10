
# gsearch-bot-discord
A discord bot which can be used to fetch search results from Google's search engine. Also supports search history feature


### Demo
Add the bot to your [Discord](https://discordapp.com/) server from [here](https://discordapp.com/api/oauth2/authorize?client_id=697626974503436358&permissions=141312&scope=bot)

### Requires
- [Discord](https://discordapp.com/) account
- Python 3.6+
- MongoDB

### Setup locally
To setup the bot run locally, you need to follow the steps below:

1. [Create a bot account](https://discordpy.readthedocs.io/en/latest/discord.html) on [Discord](https://discordapp.com/) developer portal

2. Clone the repository in your local system

```bash
git clone https://github.com/ashwani99/gsearch-bot-discord
```

3. Create a virtual environment (recommended) and install all the dependencies

```bash
cd gsearch-bot-discord && \
python -m venv .venv && \
source .venv/bin/activate && \
pip install -r requirements.txt
```

4. Set the environment variables. 

    You need to obtain your discord app token from [Discord's developer portal](https://discordapp.com/developers/)

    Note that, currently only [MongoDB](https://www.mongodb.com/) is supported as database.

```bash
export DISCORD_TOKEN=<your-bot-token-here> && \
export GSEARCH_BOT_DB_URL=<your-database-connection-url>
```

5. Start the bot

```bash
python bot/bot.py
```

6. You can now generate an invite link for your __gsearch bot__. [Invite your bot](https://discordpy.readthedocs.io/en/latest/discord.html#inviting-your-bot) to your Discord server and start chatting with it!
