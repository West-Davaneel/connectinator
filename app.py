import os
import logging
import random 
import json
from collections import defaultdict

logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from connectinator.constants import (
    QUESTIONS_TYPE_EMOJIS_DICT, 
    QUESTIONS_TYPE_NAMES_DICT,
    EMOJIS_QUESTION_TYPE_DICT,
)
from connectinator.connect_command import ConnectCommand
from connectinator.reply import Reply
from connectinator.bot_message_manager import BotMessageManager
from connectinator.utils import (
    get_nathan_and_nick,
    get_random_member_id,

)
from connectinator.create_dm import CreateDm


load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

app = App(token=SLACK_BOT_TOKEN)


bot_message_mananger = BotMessageManager()


def create_dm_with_user_and_random_user(client, event, say, text):

    say(f"Check your DMs -- I'm connecting you with a random workmate, <@{event['user']}>!")
    
    sender_id = event['user']
    users = [
        get_random_member_id(client, [sender_id]),
        sender_id,
    ]
    createDm = CreateDm(client, users)

    logging.debug(f"Created Channel, ID = {createDm.get_channel_id()}")

    say(text, channel = createDm.get_channel_id())


@app.event("reaction_added")
def track_question_level(client, event, say):

    channel = event.get('item').get('channel')
    ts = event.get('item').get('ts')

    if bot_message_mananger.is_connect_command_message(ts, channel):
        questionBank = open('QUESTION_BANK.json', mode='r', encoding='utf-8-sig')
        question_bank = json.load(questionBank)
        questionBank.close()

        questions_by_level_dict = defaultdict(list)
        for question in question_bank:
            questions_by_level_dict[question['QUESTION_TYPE']].append(question)

        logging.debug(f"event = {event}")

        try:
            question_type = EMOJIS_QUESTION_TYPE_DICT[event['reaction']]
            question = random.choice(questions_by_level_dict[question_type])['QUESTION_BODY']
            
            create_dm_with_user_and_random_user(client, event, say, question)

        except KeyError:
            pass



@app.command("/connect")
def connect(ack, client, say, command):
    ack()
    connectCommand = ConnectCommand(client, say)
    response = connectCommand = connectCommand.do_command()

    bot_message_mananger.add_message(response.get('ts'), response.get('channel'))


@app.event("app_mention")
def on_mention(event, client, say):
    mentioner_user_id = event['user']
    reply = Reply(mentioner_user_id, say)
    reply.reply()

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()