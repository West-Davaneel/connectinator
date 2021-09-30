import os

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

app = App(token=SLACK_BOT_TOKEN)


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