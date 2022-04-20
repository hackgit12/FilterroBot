class Script(object):

    START_MSG = """<b>Hy {}, I'm a filter bot used for adding unlimited custom filter messages in groups. Type /help for view my commands
"""


    HELP_MSG = """
How to use this bot:

- /viewfilters  -  List all filters in chat

Can be used by Group admins only:

- /add <name> <reply message>: add a filter to this chat. If you want your keyword to be a sentence, use quotes. eg: /add "hi bro" Hey buddy!
- /del <filter name>: stop that filter.
- /delall -  Delete all the filters (Group Owner Only!)
"""


    ABOUT_MSG = """
Here is the help for the Connections module:

- /connect <groupid> -  Connect your group to my PM. You can also simply use,
- /connect - in groups.

/connections  - list all the connections in your Group.
"""
