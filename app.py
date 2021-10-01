import os
import logging
import random 
import json
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from connectinator.constants import (
    QUESTIONS_TYPE_EMOJIS_DICT, 
    QUESTIONS_TYPE_NAMES_DICT,
)
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
    questionBank = open('QUESTION_BANK.json', mode='r', encoding='utf-8-sig')
    question_bank = json.load(questionBank)
    questionBank.close()

    questions_by_level_dict = defaultdict(list)
    for question in question_bank:
        questions_by_level_dict[question['QUESTION_TYPE']].append(question)

    logging.info(f"event = {event}")

    question = "Invalid reaction. Try again!"

    if event['reaction'] == QUESTIONS_TYPE_EMOJIS_DICT[1]:
        question = random.choice(questions_by_level_dict[1])['QUESTION_BODY']
    elif event['reaction'] == QUESTIONS_TYPE_EMOJIS_DICT[2]:
        question = random.choice(questions_by_level_dict[2])['QUESTION_BODY']
    elif event['reaction'] == QUESTIONS_TYPE_EMOJIS_DICT[0]:
        question = random.choice(questions_by_level_dict[0])['QUESTION_BODY']
    
    say(text=question, channel = event['item']['channel'])


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


@app.command("/connect")
def connect(ack, client, say, command):
    ack()
    connectCommand = ConnectCommand(client, say)
    connectCommand = connectCommand.do_command()

@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()