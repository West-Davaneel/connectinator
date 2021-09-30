import os
import logging

logging.basicConfig(level=logging.DEBUG)

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slackclient import SlackClient

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

app = App(token=SLACK_BOT_TOKEN)

client = SlackClient(SLACK_BOT_TOKEN)
request = client.api_call("users.list")
if request['ok']:
    for item in request['members']:
        print(item['name'])


@app.event("reaction_added")
def track_reactions(event, say):
    print(event)
    print("this got called")


@app.message("hello")
def message_hello(message, say):
    print("COOL")
    say(f"Hey there <@{message['user']}>!")


@app.command("/connect")
def connect(ack, say, command):
    ack()
    say("connecting...")


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()