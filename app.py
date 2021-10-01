import os
import logging

logging.basicConfig(level=logging.DEBUG)

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from connectinator.connect_command import ConnectCommand
from connectinator.utils import (
    get_nathan_and_nick,
    get_random_member_id,
)
from connectinator.create_dm import CreateDm


load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

app = App(token=SLACK_BOT_TOKEN)





@app.event("reaction_added")
def track_question_level(event, say):
    print(event)
    print("Reaction detected")
    say(event)


@app.message("hello")
def message_hello(message, say):
    
    say(f"Check your DMs -- I'm connecting you with a random workmate <@{message['user']}>!")

    sender_id = message['user']

    users = [
        get_random_member_id(app.client, [sender_id]),
        sender_id,
    ]

    createDm = CreateDm(app.client, users)

    logging.info(f"Created Channel, ID = {createDm.get_channel_id()}")

    say("READY TO CONNECT?!??!?!?!??!?!?!?!?!?!??!", channel = createDm.get_channel_id())




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