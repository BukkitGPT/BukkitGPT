import yaml
import config

with open(f"i18n/{config.UI_LANGUAGE}.yaml", "r") as lang:
    lang_content = yaml.safe_load(lang)
    for key, value in lang_content.items():
        globals()[key] = value

def get_localization(key):
    return globals()[key]

# Usage: get_localization("sidebar.title")