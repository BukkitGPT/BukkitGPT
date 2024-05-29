from cx_Freeze import setup, Executable

import config

files = [
    "logs",
    "projects",
    "i18n",
    "ui",
    "LICENSE",
    "README.md",
    "config.yaml"
]

setup(name='BukkitGPT',
      version=config.VERSION_NUMBER,
      maintainer="CubeGPT Team",
      maintainer_email="admin@cubegpt.org",
      url="https://github.com/CubeGPT/BukkitGPT",
      license="Apache License 2.0",
      description='An open source, free, AI-powered Minecraft Bukkit plugin generator developed by CubeGPT.',
      executables=[Executable('ui.py', base="gui")],
      options={
          "build_exe": {
              "include_files": files,
          }
      })