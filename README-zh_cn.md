<div align="center">
<img src="https://cdn.jsdelivr.net/gh/Zhou-Shilin/picx-images-hosting@master/20240202/bukkitgpt-logo.webp"/> 
<h1>BukkitGPT</h1>
<img src="https://img.shields.io/badge/Bukkit-GPT-blue">
<a href="https://github.com/Zhou-Shilin/BukkitGPT/pulls"><img src="https://img.shields.io/badge/PRs-welcome-20BF20"></a>
<img src="https://img.shields.io/badge/License-Apache-red">
<a href="https://crowdin.com/project/bukkitgpt"><img src="https://img.shields.io/badge/i18n-Crowdin-darkblue"></a>
<br/>
</div>

> [!WARNING]
> 中文README并不经常更新，请以英文README为准。欢迎提交PR贡献翻译！
> 本中文版本使用ChatGPT 3.5翻译，未经校对。
  
> [!NOTE]
> CubeGPT Team正在招贤纳士! 欢迎开发者和README翻译人员加入我们！

## 目录
- [介绍](https://github.com/BukkitGPT/BukkitGPT#introduction)
- [广告](https://github.com/BukkitGPT/BukkitGPT#advertisement)
- [功能](https://github.com/BukkitGPT/BukkitGPT#features)
  - [核心](https://github.com/BukkitGPT/BukkitGPT#core)
  - [图形用户界面](https://github.com/BukkitGPT/BukkitGPT#gui)
- [计划](https://github.com/BukkitGPT/BukkitGPT#plans)
  - [CubeGPT 团队的其他项目](https://github.com/BukkitGPT/BukkitGPT#other-projects-of-CubeGPT-team)
- [工作原理](https://github.com/BukkitGPT/BukkitGPT#how-it-works)
- [要求](https://github.com/BukkitGPT/BukkitGPT#requirements)
- [快速开始](https://github.com/BukkitGPT/BukkitGPT#quick-start)
  - [控制台](https://github.com/BukkitGPT/BukkitGPT#console)
  - [UI](https://github.com/BukkitGPT/BukkitGPT#ui)
- [故障排除](https://github.com/BukkitGPT/BukkitGPT#troubleshooting)
  - [org.spigotmc:spigot:jar:1.13.2-R0.1-SNAPSHOT 的 POM 丢失](https://github.com/BukkitGPT/BukkitGPT#the-pom-for-orgspigotmcspigotjar1132-r01-snapshot-is-missing)
- [贡献](https://github.com/BukkitGPT/BukkitGPT#contributing)
- [许可证](https://github.com/BukkitGPT/BukkitGPT#lisence)

## 介绍
> 将您的想法交给 GPT，AI 将为 Bukkit、Spigot、Paper、Purpur、Arclight、CatServer、Magma、Mohist 等基于 Bukkit 的服务器生成定制的 Minecraft 服务器插件，一键即可完成。

BukkitGPT 是一个开源、免费、由人工智能驱动的 Minecraft Bukkit 插件生成器。它是为那些不精通技术但需要实现各种定制小插件的 Minecraft 服务器所有者开发的。从代码到构建、调试，一切由 GPT 完成。

## 推广

![木桶面板Logo](https://cdn.jsdelivr.net/gh/Zhou-Shilin/picx-images-hosting@master/20240208/woodenbarrelsvr.jpeg)
**木桶高频面板服**  
- 支持130+大型整合包整合包联机体验
- 一键开启 网页管理
- ***独家优惠码`BGPT`***
- i9 10900K 8C10G ***年付低至43.2r每月*** (月付86.4r每月)
- i9 13900K 8C10G ***年付低至62.1r每月*** (月付124r每月)

[官网购买地址 优惠码BGPT](https://vat.yunqiaold.com/index.php?rp=/store/mc)  
***购买时使用优惠码:`BGPT`***  
获得10%off优惠  
支持无条件按剩余时间比例退款  

## 功能

### 核心
- 自动生成代码
- 自动修复错误
- AI“更好的描述”

### 图形用户界面
- 创建项目
- 项目管理

## 计划和待办事项

已迁移到 [项目选项卡](https://github.com/orgs/CubeGPT/projects/4)。

### CubeGPT 团队的其他项目
- [x] Bukkit 插件生成器。{*.jar} ([BukkitGPT](https://github.com/CubeGPT/BukkitGPT))
- [ ] 结构生成器。{*.schem}（BuilderGPT，或其他名称？）
- [ ] 服务器包生成器。{*.zip}（ServerpackGPT 或 ServerGPT，或其他名称...？）
- [ ] 有想法或想加入我们的团队吗？发送电子邮件至 [我们](mailto:admin@baimoqilin.top)！

## 工作原理
当用户键入插件描述时，程序让 `gpt-3.5-turbo` 优化提示，然后将优化后的提示传递给 `gpt-4-turbo-preview`。`gpt-4-turbo-preview` 将以 json 格式返回，例如：
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
"file": "src/main/resources/config.yml",
"code": "..."
},
{
"file": "pom.xml",
"code": "..."
}
]
}
```
程序解析此提示，复制整个 `projects/template` 文件夹并将其命名为 `artifact_name`，然后将提示中的代码放入每个文件中。最后，程序使用 Maven 构建 jar 文件。

## 要求
您可以在任何安装了 [Java](https://www.azul.com/downloads/)、[Maven](https://maven.apache.org/) 和 [Python 3+](https://www.python.org/) 的计算机上使用 BukkitGPT。  

您需要安装以下软件包：
```
pip install openai
```

## 快速开始

*（确保您的计算机上已安装了 [Python](https://www.python.org) 环境）*

### 控制台
1. 从[发布页面](https://github.com/Zhou-Shilin/BukkitGPT/releases)下载 `Source Code.zip` 并解压缩。
2. 编辑 `config.py`，填写您的 OpenAI Apikey。如果您不知道如何填写，请记住 [Google](https://www.google.com/) 和 [Bing](https://www.bing.com/) 总是您最好的朋友。
3. 运行 `console.py`（bash 中执行 `python console.py`），按照提示输入 artifact 名称、描述和包 ID，以生成您的插件。
4. 将插件从 `projects/<artifact_name>/target/<artifact_name>-<version>.jar` 复制到服务器的 `plugins/` 文件夹中。
5. 重新启动服务器，享受您的 AI 动力插件。

### UI

1. 从[发布页面](https://github.com/Zhou-Shilin/BukkitGPT/releases)下载 `Source Code.zip` 并解压缩。
2. 运行 `ui.py`（bash 中执行 `python console.py`），转到设置页面并填写您的 apikey。
3. 按照提示输入 artifact 名称、描述和包 ID，以生成您的插件。
4. 将插件从 `projects/<artifact_name>/target/<artifact_name>-<version>.jar` 复制到服务器的 `plugins/` 文件夹中。
5. 重新启动服务器，享受您的 AI 动力插件。

## 故障排除

### org.spigotmc:spigot:jar:1.13.2-R0.1-SNAPSHOT 的 POM 丢失
解决方案：[下载 BuildTools](https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar)，将其放置在空文件夹中，双击它，在 `Settings/Select Version` 中选择 "1.13.2"，然后点击右下角的 `Compile`，等待完成。然后转到您的 BukkitGPT 文件夹，在 `projects/<artifact_name_of_your_plugin>` 中，双击 `build.bat`。您将在 `projects/<artifact_name_of_your_plugin>/target` 文件夹中找到您的插件。

## 贡献
如果您喜欢这个项目，您可以给它一个星星，或者[提交问题](https://github.com/Zhou-Shilin/BukkitGPT/issues)或[拉取请求](https://github.com/Zhou-Shilin/BukkitGPT/pulls)来帮助改进它。

## 许可证
```
Copyright [2024] [BukkitGPT Team]

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