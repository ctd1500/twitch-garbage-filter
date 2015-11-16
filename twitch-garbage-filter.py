__module_name__ = 'Twitch Garbage Filter'
__module_version__ = '0.2'
__module_description__ = 'Filters some garbage messages'

import hexchat

filter = ["USERSTATE", "ROOMSTATE", "CLEARCHAT", "HOSTTARGET"]

def rawgarbage_cb(word, word_eol, userdata):
    if word[1] in filter:
        # print("RAW: {}".format(word))
        if word[1] == "CLEARCHAT":
            print("\00304Chat was cleared by a moderator\003")
        return hexchat.EAT_HEXCHAT

hexchat.hook_server("RAW LINE", rawgarbage_cb)

print("\00304{} v{} successfully loaded.\003".format(__module_name__, __module_version__))
