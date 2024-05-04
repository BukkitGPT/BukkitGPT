import requests
import zipfile
import os
import config

def download_and_extract_release(tag_name, zipball_url):
    response = requests.get(zipball_url)
    
    with open(f'temp_update/{tag_name}.zip', 'wb') as zip_file:
        zip_file.write(response.content)

    with zipfile.ZipFile(f'temp_update/{tag_name}.zip', 'r') as zip_ref:
        zip_ref.extractall(f'temp_update/{tag_name}')

def generate_update_scripts(tag_name):
    with open('temp_update/windows.bat', 'w') as bat_file:
        bat_file.write(f'cd ..\nxcopy /E /Y temp_update/{tag_name} .\\')

    with open('temp_update/linux.sh', 'w') as sh_file:
        sh_file.write(f'cd ..\ncp -R temp_update/{tag_name} ./')

def main():
    print("Checking updates...")

    # Fetch release information from GitHub
    response = requests.get('https://api.github.com/repos/CubeGPT/BukkitGPT/releases', verify=False)
    releases = response.json()

    if not releases:
        print("No releases found on GitHub.")
        return

    latest_release = releases[0]
    tag_name = latest_release['tag_name']

    # Compare with config.VERSION_NUMBER
    if tag_name == config.VERSION_NUMBER:
        print("No update available.")
        return

    # Create temp_update folder
    if not os.path.exists('temp_update'):
        os.makedirs('temp_update')

    # Download and extract the release
    download_and_extract_release(tag_name, latest_release['zipball_url'])

    # Generate update scripts
    generate_update_scripts(tag_name)

    print("Update available. Please execute 'windows.bat' or 'linux.sh' in the temp_update folder manually.")
    print("Make sure to backup your existing files before updating.")
    print("If you don't want to update or you are using a dev version, enable DEBUG_MODE in config.py.")

    return True

if __name__ == "__main__":
    main()
