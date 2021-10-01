import logging
import random 

def get_random_member_id(client):
    memberRequest = client.users_list()
    if memberRequest['ok']:
        randomMember = random.choice(list(memberRequest['members']))
        while randomMember['is_bot'] == True:
            randomMember = random.choice(list(memberRequest['members']))
            logging.debug(f"random member = {randomMember['name']}")
            return randomMember["id"]
        



def get_nathan_and_nick(client):
    members = client.users_list().get("members")
    nathan_and_nick = set()
    our_names = ["nathan", "nic"]

    for member in members:
        if not member['is_bot'] and member['id'] != 'USLACKBOT':
            nathan_and_nick.add(member["id"])


    logging.debug(f"n8 and nic {nathan_and_nick}")

    return nathan_and_nick
