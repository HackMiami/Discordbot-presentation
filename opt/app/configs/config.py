
# Bot token from discord developer portal (https://discord.com/developers/applications)
TOKEN = 'YOUR_BOT_TOKEN'

# Bot prefix for commands
PREFIX = '!'

# Server ID for the bot to run on.
GUILD_ID = 000000000000000000

ROLE_ID = 000000000000000000
# List of cogs to load on startup (cogs are located in opt/app/cogs)
# Cogs are loaded in the order they are listed here
MODS = ['BotHelp',
        'CogsLoader',
        # 'TestCommand',
        'SlashTest',
        'OnJoin',
        'OnReaction',
        'OnReady',
        ]
