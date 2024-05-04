import os
import sys
import platform

from log_writer import logger
import core
import config
import updater

def make_response(build_result):
    if "BUILD SUCCESS" in build_result:
        logger(f"Plugin is ready. {build_result}")
        print(f"Congratulations! Your plugin is ready. Now add the plugin to the projects/{artifact_name}/target directory and just find the jar file and put it in your server's plugins folder.")
        print("BukkitGPT is an open source and free project. Feel free to make pull requests. If you can, please donate this project: https://www.buymeacoffee.com/baimoqilin")
    else:
        print("Build failed. This may be due to a bug in the ChatGPT writeup. Typically, GPT4 writes more accurate code. So you should probably toggle CODING_MODEL to gpt-4 in config.py. In later releases, we'll add the ability to have ChatGPT fix bugs automatically, but not yet in the version you're using. You can start the program again and enter the same description to have ChatGPT regenerate the code.")
        logger(f"Build failed. {build_result}")
        print(build_result)
        regenerate = input("Regenerate codes? (Y/n) ")
        if regenerate == "n":
            pass
        else:
            build_result = core.generate_plugin(working_path, description, package_id, artifact_name)
            core.make_response(build_result)

core.initialize()

# will move to core.initialize in the future
if config.DEBUG_MODE == False:
    if updater.main() == True:
        sys.exit()

if sys.platform.startswith('linux') or sys.platform.startswith('daiwin'):
        clear_command = "clear"
elif sys.platform.startswith('win'):
        clear_command = "cls"

print("Welcome to BukkitGPT, an open source, free, AI-powered Minecraft Bukkit plugin generator developed by BaimoQilin (@Zhou-Shilin). Don't forget to check out the config.py configuration file, you need to fill in the OpenAI API key.")

print("\n")
print("[1/3] Let's start by nameing your plugin! The name should be in English and without spaces.")
artifact_name = input("(artifact_name) ")
logger(f"artifact_name = {artifact_name}")
os.system(clear_command)
print("[2/3] What features do you want your plugin to have? Please describe as clearly and thoroughly as possible. For example, does it require any commands to be registered? If you think you're inexperienced in this aspect of prompt engineering, we recommend you turn on the better description option in config.py.")
description = input("(description) ")
logger(f"description = {description}")
os.system(clear_command)
print("[3/3] What is the package id of your plugin? If you have a domain name like baimoqilin.top, you should write the domain name backwards and add the name of your plugin at the end (no spaces), for example if my plugin is called demo, then you should fill in top.baimoqilin.demo.")
package_id = input("(package_id) ")
logger(f"package_id = {package_id}")
os.system(clear_command)

working_path = core.package_to_path(package_id)
package_list = core.package_id_to_list(package_id)

if config.ENABLE_BETTER_DESCRIPTION == True:
    print("[0/3] Generating better description")
    description = core.askgpt(config.SYS_BETTER_DESCRIPTION, config.USR_BETTER_DESCRIPTION, config.BETTER_DESCRIPTION_MODEL, disable_json_mode=True)
    logger(f"better description: {description}")
    os.system(clear_command)

build_result = core.generate_plugin(working_path, description, package_id, artifact_name, package_list)
make_response(build_result)