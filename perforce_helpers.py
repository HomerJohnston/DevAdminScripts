# This file simply contains perforce-related functions for use in other scripts.

import subprocess

# Given a particular P4 change number, retrieve and return a dictionary containing the user, workspace name and change description
def get_change_data(change, P4PORT, P4LOGIN, P4PASS):

        change_data = {
                'user' : '',
                'client' : '',
                'desc' : ''
        }

        user = subprocess.Popen('p4 -p %s -u "%s" -P "%s" -Ztag -F "%%user%%" describe %s' % (P4PORT, P4LOGIN, P4PASS, change), stdout=subprocess.PIPE, shell=True)
        user = user.stdout.read().decode('ISO-8859-1')
        user = user.rstrip('\r\n')

        client = subprocess.Popen('p4 -p %s -u "%s" -P "%s" -Ztag -F "%%client%%" describe %s' % (P4PORT, P4LOGIN, P4PASS, change), stdout=subprocess.PIPE, shell=True)
        client = client.stdout.read().decode('ISO-8859-1')
        client = client.rstrip('\r\n')

        desc = subprocess.Popen('p4 -p %s -u "%s" -P "%s" -Ztag -F "%%desc%%" describe %s' % (P4PORT, P4LOGIN, P4PASS, change), stdout=subprocess.PIPE, shell=True)
        desc = desc.stdout.read().decode('ISO-8859-1')
        desc = desc.rstrip('\r\n')

        change_data['user'] = user
        change_data['client'] = client
        change_data['desc'] = desc

        return change_data
