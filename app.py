import os
import logging
import random 

logging.basicConfig(level=logging.DEBUG)

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from connectinator.connect_command import ConnectCommand

from slackclient import SlackClient

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

app = App(token=SLACK_BOT_TOKEN)

client = SlackClient(SLACK_BOT_TOKEN)
memberRequest = client.api_call("users.list")
if memberRequest['ok']:
    randomMember = random.choice(list(memberRequest['members']))
    while randomMember['is_bot'] == True:
        randomMember = random.choice(list(memberRequest['members']))
    print(randomMember['name'])
    # for member in memberRequest['members']:
    #     print(member)
        
 
        

@app.message("hello")
def message_hello(message, say):
    logging.debug("someone said hello")
    say(f"Hey there <@{message['user']}>!")


@app.command("/connect")
def connect(ack, say, command):
    ack()
    connectCommand = ConnectCommand()
    logging.debug("connect command triggered")
    say(connectCommand.get_command_response())


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()