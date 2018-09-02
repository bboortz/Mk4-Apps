"""Your custom homescreen

This is a customable homescreen for the Tilda Mk4.

 How to use:
 1. store an 150x150px image at shared/me.png"
 2. install this app
"""

___name___         = "Homescreen (Custom)"
___license___      = "MIT"
___categories___   = ["Homescreens"]
___dependencies___ = ["homescreen", "ospath"]
___launchable___   = False        # should be False for a homescreen
___bootstrapped___ = False

import ugfx
from homescreen import *
import time, ospath, os
from tilda import Buttons


# some variables
intro_height = 30                                # introduction height
intro_text = "Hi! I'm"                           # introduction text
name_height = 60                                 # height of name
status_height = 20                               # height of status text
info_height = 30                                 # height of info text
info_text = "EMF 2018"                           # info text
logo_path = "home_custom/me.png"                 # logo path
logo_height = 150                                # logo height
logo_width = 150                                 # logo width
max_name = 8                                     # Maximum length of name before downscaling
bg_color_setting = background_color(0xFFFFFF)    # background color
text_color_setting = text_color(ugfx.BLUE)       # text color
title_text = "TiLDA Mk4"                         # title text


# initialize the homescreen
init()


# Set Background 
ugfx.clear(ugfx.html_color(bg_color_setting))

# Set Colours
style = ugfx.Style()
style.set_enabled([text_color_setting, ugfx.html_color(bg_color_setting), ugfx.html_color(bg_color_setting), ugfx.html_color(bg_color_setting)])
style.set_background(ugfx.html_color(bg_color_setting))
ugfx.set_default_style(style)

# Draw Logo
if ospath.exists(logo_path):
    # Draw logo
    ugfx.display_image(
        int((ugfx.width() - logo_width) / 2),
        int((ugfx.height() - logo_height) / 2),
        logo_path
    )
else:
    ugfx.Label(0, int(round( ugfx.height() / 2 )), ugfx.width(), info_height, "Logo not found!", justification=ugfx.Label.CENTER)

# Draw introduction
ugfx.orientation(90)
ugfx.set_default_font(ugfx.FONT_TITLE)
ugfx.Label(0, ugfx.height() - name_height - intro_height + 4, ugfx.width(), intro_height, intro_text, justification=ugfx.Label.CENTER)

# Process name
name_setting = name("Set your name in the settings app")
if len(name_setting) <= max_name:
    ugfx.set_default_font(ugfx.FONT_NAME)
else:
    ugfx.set_default_font(ugfx.FONT_MEDIUM_BOLD)
# Draw name
ugfx.Label(0, ugfx.height() - name_height, ugfx.width(), name_height, name_setting, justification=ugfx.Label.CENTER)


# Draw Title
ugfx.set_default_font(ugfx.FONT_TITLE)
ugfx.Label(0, 0, ugfx.width(), info_height, title_text, justification=ugfx.Label.CENTER)
# Draw info
ugfx.Label(0, info_height, ugfx.width(), info_height, info_text, justification=ugfx.Label.CENTER)

ugfx.set_default_font(ugfx.FONT_SMALL)
status = ugfx.Label(0, info_height + status_height + 6, ugfx.width(), status_height, "", justification=ugfx.Label.CENTER)

# update loop
while True:
    text = "";
    value_wifi_strength = wifi_strength()
    value_battery = battery()
    if value_wifi_strength:
        text += "Wi-Fi: %s%%, " % int(value_wifi_strength)
    if value_battery:
        text += "Battery: %s%%" % int(value_battery)
    status.text(text)
    sleep_or_exit(0.5)
