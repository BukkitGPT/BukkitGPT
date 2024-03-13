import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sv_ttk

import os
import json
import shutil
import re
import sys
import subprocess
import threading

from log_writer import logger
import core
import config

# Define global variables
CurrentProject = None
artifact_name = None
description = None
package_id = None

def run_maven(text_area, maven):
    process = subprocess.Popen(f"projects/{artifact_name}/build.bat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    for line in process.stdout:
        text_area.insert(tk.END, line)
        text_area.see(tk.END)
    process.stdout.close()
    return_code = process.wait()
    if return_code == 0:
        maven.destroy()

def BuildProject():
    working_path = core.package_to_path(package_id)
    package_list = core.package_id_to_list(package_id)
    core.generate_plugin(working_path, description, package_id, artifact_name, package_list, dont_build=True)

    maven = tk.Tk()
    maven.title("Building logs")

    text_area = scrolledtext.ScrolledText(maven, wrap=tk.WORD)
    text_area.pack(expand=True, fill='both')

    thread = threading.Thread(target=run_maven(text_area, maven))
    thread.start()

    maven.mainloop()

    logger(f"BuildProject: {result}")
    if "BUILD SUCCESS" in result:
        return f"Congratulations! Your plugin is ready. Now add the plugin to the projects/{artifact_name}/target directory and just find the jar file and put it in your server's plugins folder. BukkitGPT is an open source and free project. Feel free to make pull requests. If you can, please donate this project: https://www.buymeacoffee.com/baimoqilin"
    else:
        return "Build failed. This may be due to a bug in the ChatGPT writeup. Typically, GPT4 writes more accurate code. So you should probably toggle CODING_MODEL to gpt-4 in config.py. In later releases, we'll add the ability to have ChatGPT fix bugs automatically, but not yet in the version you're using. You can start the program again and enter the same description to have ChatGPT regenerate the code."


class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.logo = tk.PhotoImage(file="ui/logo.png")
        self.logo_label = ttk.Label(self, image=self.logo)  # Change tk.Label to ttk.Label
        self.logo_label.pack(pady=(10))
        self.create_button = ttk.Button(self, text="Create", command=lambda: self.create_project(), width=15)
        self.create_button.pack(pady=(10, 5))
        # self.settings_button = ttk.Button(self, text="Settings", command=lambda: controller.show_frame(SettingsPage), width=15)
        self.settings_button = ttk.Button(self, text="Settings", command=self.open_settings, width=15)
        self.settings_button.pack(pady=(5, 5))
        self.theme_button = ttk.Button(self, text="Switch Theme", command=lambda: sv_ttk.toggle_theme(), width=15)
        self.theme_button.pack(pady=(5))

    def create_project(self):
        global CurrentProject
        if config.API_KEY == "" and config.DEBUG_MODE == False:
            messagebox.showwarning("Warning", "Please enter an API_KEY!")
        else:
            CurrentProject = "New"
            logger("HomePage: New project")
            self.controller.show_frame(ProjectPage)
    
    def open_settings(self):
        os.system("notepad config.yaml")

class ProjectPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Load information from the file when CurrentProject is not "New"
        if CurrentProject != "New":
            self.load_info_from_file()
        
        self.title_label = ttk.Label(self, text="")
        self.title_label.pack(pady=10)
        self.text1 = ttk.Label(self, text="artifact_name")
        self.text1.pack(anchor="w")
        self.text2 = ttk.Label(self, text="Let's start by nameing your plugin! The name should be in English and without spaces.")
        self.text2.pack(anchor="w")
        self.input1 = ttk.Entry(self)
        self.input1.pack(anchor="w")
        self.text3 = ttk.Label(self, text="description")
        self.text3.pack(anchor="w")
        self.text4 = ttk.Label(self, text="What features do you want your plugin to have? Please describe as clearly and thoroughly as possible. For example, does it require any commands to be registered? If you think you're inexperienced in this aspect of prompt engineering, we recommend you turn on the better description option in Settings.")
        self.text4.pack(anchor="w")
        self.input2 = ttk.Entry(self)
        self.input2.pack(anchor="w")
        self.text5 = ttk.Label(self, text="package_id")
        self.text5.pack(anchor="w")
        self.text6 = ttk.Label(self, text="What is the package id of your plugin? If you have a domain name like baimoqilin.top, you should write the domain name backwards and add the name of your plugin at the end (no spaces), for example if my plugin is called demo, then you should fill in top.baimoqilin.demo.")
        self.text6.pack(anchor="w")
        self.input3 = ttk.Entry(self)
        self.input3.pack(anchor="w")
        self.generate_button = ttk.Button(self, text="Generate", command=lambda: self.generate_project())
        self.generate_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.delete_button = ttk.Button(self, text="Delete", command=lambda: self.delete_project(), style="Red.TButton")
        self.delete_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def load_info_from_file(self):
        global artifact_name, description, package_id

        # Load information from the "info.bukkitgpt" file
        try:
            with open(f"projects/{CurrentProject}/info.bukkitgpt", "r") as file:
                info_data = json.load(file)

            # Update the variables with the loaded information
            artifact_name = info_data.get("artifact_name", "")
            description = info_data.get("description", "")
            package_id = info_data.get("package_id", "")

            # Set the values in the input boxes
            self.input1.insert(0, artifact_name)
            self.input2.insert(0, description)
            self.input3.insert(0, package_id)

        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            # messagebox.showwarning("Warning", f"Info file not found for {CurrentProject}. Creating a new file.")
            pass

    def generate_project(self):
        global artifact_name, description, package_id
        artifact_name = self.input1.get()
        description = self.input2.get()
        package_id = self.input3.get()
        self.generate_button.config(text="Generating", state=tk.DISABLED)
        info = BuildProject()

        # Save information to the "info.bukkitgpt" file
        info_data = {
            "artifact_name": artifact_name,
            "description": description,
            "package_id": package_id
        }

        with open(f"projects/{artifact_name}/info.bukkitgpt", "w") as file:
            json.dump(info_data, file)

        messagebox.showinfo("Result", info)
        self.generate_button.config(text="Generate", state=tk.NORMAL)

    def delete_project(self):
        global CurrentProject
        try:
            shutil.rmtree(f"projects/{artifact_name}")
        except:
            pass
        self.controller.show_frame(HomePage)

    def update_title(self):
        self.title_label.config(text=CurrentProject)

# The orignal settings page.
# class SettingsPage(ttk.Frame):
#     def __init__(self, parent, controller):
#         ttk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.title_label = ttk.Label(self, text="Settings")
#         self.title_label.pack(pady=10)

#         # Add API_KEY input box and label
#         self.text1 = ttk.Label(self, text="API_KEY")
#         self.text1.pack(anchor="w")
#         self.input1 = ttk.Entry(self)
#         self.input1.insert(0, config.API_KEY)  # Load API_KEY from config.py
#         self.input1.pack(anchor="w")

#         # Add BASE_URL input box and label
#         self.text2 = ttk.Label(self, text="BASE_URL")
#         self.text2.pack(anchor="w")
#         self.input2 = ttk.Entry(self)
#         self.input2.insert(0, config.BASE_URL)  # Load BASE_URL from config.py
#         self.input2.pack(anchor="w")

#         # Add CODING_MODEL dropdown and label
#         self.text3 = ttk.Label(self, text="CODING_MODEL")
#         self.text3.pack(anchor="w")
#         self.options_coding_model = ["gpt-4", "gpt-3.5-turbo"]
#         self.selected_coding_model = tk.StringVar(value=config.CODING_MODEL)
#         self.dropdown_coding_model = ttk.Combobox(self, values=self.options_coding_model, textvariable=self.selected_coding_model)
#         self.dropdown_coding_model.pack(anchor="w")

#         # Add BETTER_DESCRIPTION_MODEL dropdown and label
#         self.text4 = ttk.Label(self, text="BETTER_DESCRIPTION_MODEL")
#         self.text4.pack(anchor="w")
#         self.options_description_model = ["gpt-4", "gpt-3.5-turbo"]
#         self.selected_description_model = tk.StringVar(value=config.BETTER_DESCRIPTION_MODEL)
#         self.dropdown_description_model = ttk.Combobox(self, values=self.options_description_model, textvariable=self.selected_description_model)
#         self.dropdown_description_model.pack(anchor="w")

#         # Add Save button
#         self.save_button = ttk.Button(self, text="Save", command=self.save_options)
#         self.save_button.pack(side=tk.BOTTOM, pady=10)

#     def save_options(self):
#         # Save the options to config.py (replace with your actual saving logic)
#         api_key = self.input1.get()
#         base_url = self.input2.get()
#         coding_model = self.selected_coding_model.get()
#         description_model = self.selected_description_model.get()

#         # Read the content of config.py
#         config.edit_config("API_KEY", api_key)
#         config.edit_config("BASE_URL", base_url)
#         config.edit_config("CODING_MODEL", coding_model)
#         config.edit_config("DESCRIPTION_MODEL", description_model)
        
#         logger(f"SettingsPage: save options")

#         messagebox.showwarning("Save Options", "Please exit the program and reopen it to reload the config.")

#         sys.exit()

# Define App class
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Set the window title
        self.title("BukkitGPT")
        # Set the window size
        self.geometry("800x600")
        # Create a container frame
        self.container = tk.Frame(self)
        self.container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        # Create a sidebar frame
        self.sidebar = tk.Frame(self)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        # Create a title label for the sidebar
        self.sidebar_title = tk.Label(self.sidebar, text="Projects")
        self.sidebar_title.pack(pady=10)
        # Create a listbox for the sidebar
        self.sidebar_list = tk.Listbox(self.sidebar)
        self.sidebar_list.pack(fill=tk.Y, expand=True)
        # Bind the listbox selection to a callback function
        self.sidebar_list.bind("<<ListboxSelect>>", self.on_select)
        # Create Home and Settings buttons under the sidebar
        self.home_button = ttk.Button(self.sidebar, text="Home", command=lambda: self.show_frame(HomePage), width=15)
        self.home_button.pack(pady=(30, 5))
        # self.settings_button_sidebar = ttk.Button(self.sidebar, text="Settings", command=lambda: self.show_frame(SettingsPage), width=15)
        self.settings_button_sidebar = ttk.Button(self.sidebar, text="Settings", command=self.open_settings, width=15)
        self.settings_button_sidebar.pack(pady=(5, 30))
        # Populate the listbox with the names of the folders in projects/
        self.populate_list()
        # Create a dictionary of frames
        self.frames = {}
        # Loop through the HomePage, ProjectPage, and SettingsPage classes
        for F in (HomePage, ProjectPage):
            # Create a frame for each class
            frame = F(self.container, self)
            # Store the frame in the dictionary
            self.frames[F] = frame
            # Place the frame in the container
            frame.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.show_frame(HomePage)

        # Configure the style for the red button
        self.style = ttk.Style()
        self.style.configure("Red.TButton", fg="white", background="red")

    def show_frame(self, frame_class):
        # Show the frame corresponding to the frame_class
        frame = self.frames[frame_class]
        frame.tkraise()
        # If the frame is ProjectPage, update the title
        if frame_class == ProjectPage:
            frame.update_title()
    
    def open_settings(self):
        os.system("notepad config.yaml")

    def populate_list(self):
        # Populate the listbox with the names of the folders in projects/
        # Clear the listbox first
        self.sidebar_list.delete(0, tk.END)
        # Get the list of folders in projects/
        folders = [folder for folder in os.listdir("projects/") if folder != "template"]  # Ignore the "template" folder
        # Loop through the folders
        for folder in folders:
            # Insert the folder name to the listbox
            self.sidebar_list.insert(tk.END, folder)

    def on_select(self, event):
        # This function is called when the user selects an item in the listbox
        # Get the index of the selected item
        index = self.sidebar_list.curselection()[0]
        # Get the name of the selected item
        name = self.sidebar_list.get(index)
        # Set the CurrentProject variable to the name
        global CurrentProject
        CurrentProject = name
        # Show the ProjectPage frame
        self.show_frame(ProjectPage)

# Create an app object
app = App()
# Start the main loop
# app.after(1, sv_ttk.use_light_theme)
sv_ttk.set_theme("light")
app.mainloop()
