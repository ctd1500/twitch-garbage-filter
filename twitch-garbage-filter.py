__module_name__ = 'Twitch Garbage Filter'
__module_version__ = '0.1'
__module_description__ = 'Filters some garbage messages'

import hexchat

def rawgarbage_cb(word, word_eol, userdata):
    if word[1] == "USERSTATE" or word[1] == "ROOMSTATE":
        # print("RAW: {}".format(word))
        return hexchat.EAT_ALL

hexchat.hook_server("RAW LINE", rawgarbage_cb)

print("\00304{} successfully loaded.\003".format(__module_name__))
