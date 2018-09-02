"""Cats

This app retrieves cat or dog images from an API and shows them.
"""

___name___         = "Cats"
___license___      = "MIT"
___dependencies___ = ["wifi", "http", "ugfx_helper", "sleep", "app"]
___categories___   = ["EMF"]

import ugfx_helper, os, wifi, ugfx, http, time, sleep, app
from tilda import Buttons

ugfx_helper.init()
ugfx.clear()

      
image_api = "http://94.45.235.239:8888"

ugfx.text(5, 5, "Loading Image Url", ugfx.BLACK)
ugfx.text(5, 10, "from %s ..." % image_api, ugfx.BLACK)
try:
    image_url = http.get(image_url).raise_for_status().text()
    ugfx.text(5, 15, "Result: %s" % image_url, ugfx.BLACK)
    #image = http.get("http://s3.amazonaws.com/tilda-badge/sponsors/screen.png").raise_for_status().content
    #r = http.get("http://94.45.235.239:8888") 
    #ugfx.display_image(0,0,bytearray(image))
except:
    ugfx.clear()
    ugfx.text(5, 5, "Couldn't download image", ugfx.BLACK)

while (not Buttons.is_pressed(Buttons.BTN_A)) and (not Buttons.is_pressed(Buttons.BTN_B)) and (not Buttons.is_pressed(Buttons.BTN_Menu)):
    sleep.wfi()

ugfx.clear()
app.restart_to_default()

