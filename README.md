# ***IMPORTANT: THIS PROJECT WILL BE COMPLETELY REWRITTEN AND THE REPOSITORY WILL BE ARCHIVED. CHECK OUT THE REWRITTEN VERSION AT THE REPOSITORY URL: [https://github.com/CubeGPT/BukkitGPT-v3](https://github.com/CubeGPT/BukkitGPT-v3)***
# Please do not use the version in this repository and switch to the new, rewritten version. Why I made this decision: https://gist.github.com/Zhou-Shilin/e3503bb3d86de72e5f8875325c0f07d4
# Chinese: 重要：本项目将被完全重写，存储库将被存档。请查看重写版本的存储库网址：[https://github.com/CubeGPT/BukkitGPT-v3](https://github.com/CubeGPT/BukkitGPT-v3)；请不要使用本存储库中的版本，切换到新的、重写的版本；关于为何我做了这个决定：https://gist.github.com/Zhou-Shilin/e3503bb3d86de72e5f8875325c0f07d4


<div align="center">
<img src="https://cdn.jsdelivr.net/gh/Zhou-Shilin/picx-images-hosting@master/20240202/bukkitgpt-logo.webp"/> 
<h1>BukkitGPT</h1>
<img src="https://img.shields.io/badge/Bukkit-GPT-blue">
<a href="https://github.com/Zhou-Shilin/BukkitGPT/pulls"><img src="https://img.shields.io/badge/PRs-welcome-20BF20"></a>
<img src="https://img.shields.io/badge/License-Apache-red">
<a href="https://crowdin.com/project/bukkitgpt"><img src="https://img.shields.io/badge/i18n-Crowdin-darkblue"></a>
<a href="https://discord.gg/kTZtXw8s7r"><img src="https://img.shields.io/discord/1212765516532289587
"></a>
<p>English | <a href="https://github.com/BukkitGPT/BukkitGPT/blob/master/README-zh_cn.md">简体中文</a></p>
<br>
<a href="https://discord.gg/kTZtXw8s7r">Join our discord</a>
<br/>
</div>

> [!NOTE]
> Developers and translators are welcome to join the CubeGPT Team!

> [!NOTE]
> Generate a house or other structure using our other open source project, [BuilderGPT](https://github.com/CubeGPT/BuilderGPT)!

## Table of Contents
- [Introduction](https://github.com/BukkitGPT/BukkitGPT#introduction)
- [Advertisement](https://github.com/BukkitGPT/BukkitGPT#advertisement)
- [Features](https://github.com/BukkitGPT/BukkitGPT#features)
  - [Core](https://github.com/BukkitGPT/BukkitGPT#core)
  - [GUI](https://github.com/BukkitGPT/BukkitGPT#gui)
- [Plans](https://github.com/BukkitGPT/BukkitGPT#plans)
  - [Other projects of CubeGPT Team](https://github.com/BukkitGPT/BukkitGPT#other-projects-of-CubeGPT-team)
- [How it works](https://github.com/BukkitGPT/BukkitGPT#how-it-works)
- [Requirements](https://github.com/BukkitGPT/BukkitGPT#requirements)
- [Quick Start](https://github.com/BukkitGPT/BukkitGPT#quick-start)
  - [Windows/Linux](https://github.com/BukkitGPT/BukkitGPT#windows-linux)
  - [Python/Console](https://github.com/BukkitGPT/BukkitGPT#python-console)
  - [Python/UI](https://github.com/BukkitGPT/BukkitGPT#python-ui)
- [Troubleshooting](https://github.com/BukkitGPT/BukkitGPT#troubleshooting)
  - [The POM for org.spigotmc:spigot:jar:1.13.2-R0.1-SNAPSHOT is missing](https://github.com/BukkitGPT/BukkitGPT#the-pom-for-orgspigotmcspigotjar1132-r01-snapshot-is-missing)
- [Contributing](https://github.com/BukkitGPT/BukkitGPT#contributing)
- [Lisence](https://github.com/BukkitGPT/BukkitGPT#lisence)

## Introduction
> Give GPT your idea, AI generates customized Minecraft server plugins with one click, which is suitable for Bukkit, Spigot, Paper, Purpur, Arclight, CatServer, Magma, Mohist and other Bukkit-based servers.

BukkitGPT is an open source, free, AI-powered Minecraft Bukkit plugin generator. It was developed for minecraft server owners who are not technically savvy but need to implement all kinds of customized small plugins. From code to build, debug, all done by gpt.

## GET YOUR FREE API KEY WITH GPT-4 ACCESS
We are pleased to announce that SEC-API is offering a free apikey for users of programs developed by CubeGPT!
This key has access to gpt-4-1106-preview and gpt-3.5-turbo-1106.

**Note that this key does not have access to models such as gpt-4-vision and expires at any time.**

Get the key from [here](https://github.com/orgs/CubeGPT/discussions/1). You can use it in BuilderGPT.

## Partner
[![](https://www.bisecthosting.com/partners/custom-banners/c37f58c7-c49b-414d-b53c-1a6e1b1cff71.webp)](https://bisecthosting.com/cubegpt)

## Features

### Core
- Automatically generate code
- Automatically fix bugs
- AI `Better Description`

### GUI
- Creating projects
- Projects management

## Plans and TODOs

Moved to [Projects Tab](https://github.com/orgs/CubeGPT/projects/4).

### Other projects of CubeGPT Team
- [x] Bukkit plugin generator. {*.jar} ([BukkitGPT](https://github.com/CubeGPT/BukkitGPT))
- [ ] Structure generator. {*.schem} (BuilderGPT, or something?)
- [ ] Serverpack generator. {*.zip} (ServerpackGPT or ServerGPT, or..?)
- [ ] Have ideas or want to join our team? Send [us](mailto:admin@baimoqilin.top) an email!

## How it works
When the user types the plugin description, the program lets `gpt-3.5-turbo` optimize the prompt, and then gives the optimized prompt to `gpt-4-turbo-preview`. `gpt-4-turbo-preview` will return it in json format, for example:
```
{
    "output": [
        {
            "file": "%WORKING_PATH%/Main.java",
            "code": "package ...;\nimport org.bukkit.Bukkit;\npublic class Main extends JavaPlugin implements CommandExecutor {\n..."
        },
        {
            "file": "src/main/resources/plugin.yml",
            "code": "name: ...\nversion: ...\n..."
        },
        {
            "file\": "src/main/resources/config.yml",
            "code\": "..."
        },
        {
            "file": "pom.xml",
            "code": "..."
        }
    ]
}
```
The program parses this prompt, copies the entire `projects/template` folder and names it `artifact_name`, and puts the code from the prompt into the each file. Finally the program builds the jar using maven.

## Requirements
You can use BukkitGPT on any computer with [Java](https://www.azul.com/downloads/), [Maven](https://maven.apache.org/), [Python 3+](https://www.python.org/).  

And you need to install this package:
```
pip install openai
```

## Quick Start

*(Make sure you have the [Python](https://www.python.org) environment installed on your computer)*

### Windows/Linux
1. Download `Source Code.zip` from [the release page](https://github.com/CubeGPT/BukkitGPT/releases) and unzip it.
2. Edit `config.py`, fill in your OpenAI Apikey. If you don't know how, remember that [Google](https://www.google.com/) and [Bing](https://www.bing.com/) are always your best friends.
3. Run `ui.exe` (bash `python console.py`), enter the artifact name & description & package id as instructed to generate your plugin.
4. Copy your plugin from `projects/<artifact_name>/target/<artifact_name>-<version>.jar` to your server `plugins/` folder.
5. Restart your server and enjoy your AI-powered-plugin.

### Python/Console
1. Download `Source Code.zip` from [the release page](https://github.com/CubeGPT/BukkitGPT/releases) and unzip it.
2. Edit `config.yaml`, fill in your OpenAI Apikey. If you don't know how, remember that [Google](https://www.google.com/) and [Bing](https://www.bing.com/) are always your best friends.
3. Run `console.py` (bash `python console.py`), enter the artifact name & description & package id as instructed to generate your plugin.
4. Copy your plugin from `projects/<artifact_name>/target/<artifact_name>-<version>.jar` to your server `plugins/` folder.
5. Restart your server and enjoy your AI-powered-plugin.

### Python/UI

1. Download `Source Code.zip` from [the release page](https://github.com/CubeGPT/BukkitGPT/releases) and unzip it.
2. Edit `config.yaml`, fill in your OpenAI Apikey. If you don't know how, remember that [Google](https://www.google.com/) and [Bing](https://www.bing.com/) are always your best friends.
3. Run `ui.py` (bash `python console.py`).
4. Enter the artifact name & description & package id as instructed to generate your plugin.
5. Copy your plugin from `projects/<artifact_name>/target/<artifact_name>-<version>.jar` to your server `plugins/` folder.
6. Restart your server and enjoy your AI-powered-plugin.

## Troubleshooting

### The POM for org.spigotmc:spigot:jar:1.13.2-R0.1-SNAPSHOT is missing
Solution: [Download BuildTools](https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar), place it in an empty folder, double-click it, choose "1.13.2" in `Settings/Select Version`, click `Compile` in the bottom right corner and let it finish. And then go to your BukkitGPT folder, in `projects/<artifact_name_of_your_plugin>`, double-click `build.bat`. You'll find your plugin in `projects/<artifact_name_of_your_plugin>/target` folder.

## Contributing
If you like the project, you can give the project a star, or [submit an issue](https://github.com/CubeGPT/BukkitGPT/issues) or [pull request](https://github.com/CubeGPT/BukkitGPT/pulls) to help make it better.

## License
```
Copyright [2024] [CubeGPT Team]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
