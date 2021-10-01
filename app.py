import os
import logging
import random 

logging.basicConfig(level=logging.DEBUG)

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from connectinator.connect_command import ConnectCommand



load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

app = App(token=SLACK_BOT_TOKEN)


memberRequest = app.client.users_list()
if memberRequest['ok']:
    randomMember = random.choice(list(memberRequest['members']))
    while randomMember['is_bot'] == True:
        randomMember = random.choice(list(memberRequest['members']))
    logging.debug(f"random member = {randomMember['name']}")


@app.event("reaction_added")
def track_question_level(event, say):
    print(event)
    print("Reaction detected")
    say(event)


@app.message("hello")
def message_hello(message, say):
    logging.debug("someone said hello")
    say(f"Hey there <@{message['user']}>!")


@app.command("/lil-connect")
def connect(ack, client, say, command):
    ack()
    connectCommand = ConnectCommand(client, say)
    connectCommand = connectCommand.do_command()

@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()