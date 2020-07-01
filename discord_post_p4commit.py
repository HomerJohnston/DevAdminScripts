import sys, os, getopt, subprocess

# Webhook library - I am using an old .py version from https://github.com/kyb3r/dhooks
from discord_hooks import Webhook

# Import Webhook URLs for my Discord bot(s). If I run this script with -t argument it will use the TEST webhook instead.
from discord_config import TEST_WEBHOOK_URL
from discord_config import P4_COMMITS_WEBHOOK_URL

# Import perforce login info
from discord_config import P4LOGIN
from discord_config import P4PASS
from discord_config import P4PORT

# Import URL to an icon for perforce commits
from discord_config import changelist_icon

# Import dictionaries mapping perforce username to discord userid# and discord username
from discord_config import discord_userids
from discord_config import discord_usernames

# Import helper functions
from perforce_helpers import get_change_data

#-------------------------------------------------
def main(argv):
        global changelist_icon
        webhook_url = P4_COMMITS_WEBHOOK_URL
        change = -1
        discord_userid = '-1'

        # Retrieve input arguments
        try:
                opts, args = getopt.getopt(argv, "tc:")

        except getopt.GetoptError:
                print("Invalid arguments! -c ChangeNumber -t (to use TEST_WEBHOOK_URL)")
                sys.exit(2)

        for opt, arg in opts:
                if opt == '-c':
                        change = arg
                if opt == '-t':
                        webhook_url = TEST_WEBHOOK_URL

        # If no change was given, simply exit
        if change == -1:
                print("No change number supplied!")
                sys.exit(3)

        # Function will get description and user info about this change and store in a dictionary
        change_data = get_change_data(change, P4PORT, P4LOGIN, P4PASS)

        # Match Perforce user from perforce change info to actual Discord user using pre-set dictionaries
        discord_userid = discord_userids[change_data["user"]]
        discord_username = discord_usernames[change_data['user']]

        # Set up and send the embed
        embed_title = u'Change %s  \u2022  %s (%s)  \u2022  %s' % (change, change_data['user'], discord_username, change_data['client'])
        embed_description = '%s' % (change_data['desc'])

        message = Webhook(webhook_url, color=0x10b1df)
        message.set_author(name=embed_title, icon=changelist_icon) # Author field is used for smaller/more compact font and inline icon
        message.set_desc(embed_description)
        message.post()

#-------------------------------------------------
if __name__ == "__main__":
        main(sys.argv[1:])
