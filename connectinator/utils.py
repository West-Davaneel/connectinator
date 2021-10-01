import logging
import random

from slack_bolt.logger import messages 

def get_random_member_id(client, exclude_users: list = None):
    memberRequest = client.users_list()
    valid_members = []

    # Get only valid members
    if memberRequest['ok']:
        members = memberRequest['members']
        for member in members: 
            if is_valid_user(member, exclude_users):
                valid_members.append(member)

    # Now get the random member
    random_member = random.choice(valid_members)

    return random_member['id']


def is_valid_user(user, exclude_users: list = None): 

    return not user['is_bot'] and \
        user['id'] != 'USLACKBOT' and \
        user['id'] not in exclude_users

        
def is_valid_reaction(event):
    pass


def get_nathan_and_nick(client):
    members = client.users_list().get("members")
    nathan_and_nick = set()
    our_names = ["nathan", "nic"]

    for member in members:
        if not member['is_bot'] and member['id'] != 'USLACKBOT':
            nathan_and_nick.add(member["id"])


    logging.debug(f"n8 and nic {nathan_and_nick}")

    return nathan_and_nick




