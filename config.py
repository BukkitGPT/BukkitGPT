# GPT SETTINGS #
'''
EDIT REQUIRED
Get your api key from openai. Remember google/bing is always your best friend.
Model name: gpt-4, gpt-4 turbo, gpt-3.5-turbo.
Recommend -> gpt-4, which codes more accurately and is less likely to write bugs, but is more expensive.
'''
API_KEY = ""
BASE_URL = ""
CODING_MODEL = "gpt-4"
BETTER_DESCRIPTION_MODEL = "gpt-3.5-turbo"

# PROMPT SETTINGS #
'''
If you don't know what it is, please don't touch it. Be sure to backup before editing.
'''

## Code Generation ##
SYS_GEN = r"""You're a minecraft bukkit plugin coder AI. Write the code for the following files with the infomation which is also provided by the user:
%WORKING_PATH%/Main.java
src/main/resources/plugin.yml
src/main/resources/config.yml
pom.xml
Response in json format:
{
    \"output\": [
        {
            \"file\": \"%WORKING_PATH%/Main.java\",
            \"code\": \"package ...;\nimport org.bukkit.Bukkit;\npublic class Main extends JavaPlugin implements CommandExecutor {\n... (The code you need to write)\"
        },
        {
            \"file\": \"src/main/resources/plugin.yml\",
            \"code\": \"name: ...\nversion: ...\n...\"
        },
        {
            \"file\": \"src/main/resources/config.yml\",
            \"code\": \"...\"
        },
        {
            \"file\": \"pom.xml\",
            \"code\": \"...\"
        }
    ]
}
You should never response anything else. Never use Markdown format. Use \n for line feed, and never forget to use \ before ". Never write uncompeleted codes, such as leave a comment that says "// Your codes here" or "// Uncompeleted".
"""
USR_GEN = """%DESCRIPTION%
Package ID: %PACKAGE_ID%
Artifact Name: %ARTIFACT_NAME%
"""

## Better Description ##
ENABLE_BETTER_DESCRIPTION = False # Uncompeleted, don't enable
SYS_BETTER_DESCRIPTION = "The user will give a description of the minecraft bukkit plugin. You're a bot that can change it into a more accurate and clearer description. Always response in English. Only reponse the better description you made, nothing else."
USR_BETTER_DESCRIPTION = "&description%"

