import os
import logging
import random 
import json
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)

from connectinator.constants import (
    QUESTIONS_TYPE_EMOJIS_DICT, 
    QUESTIONS_TYPE_NAMES_DICT,
)

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
    # logging.debug(f"random member = {randomMember['name']}")


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
    # logging.debug("someone said hello")
    say(f"Hey there <@{message['user']}>!")


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