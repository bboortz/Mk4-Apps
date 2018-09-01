"""Cats

This app retrieves cat or dog images from an API and shows them.
"""

___name___         = "Cats"
___license___      = "MIT"
___dependencies___ = ["sleep", "app", "http"]
___categories___   = ["EMF"]

import ugfx, http, app, sleep


# Padding for name
logo_height = 240
logo_width = 320

# Maximum length of name before downscaling
max_name = 8

# Background stuff
init()
ugfx.clear(ugfx.html_color(0xFFFFFF))

# Retrieve Logo
r = http.get("http://94.45.235.239:8888") 
url = r.text()
r = http.get(url) 
http.download_to("cat.jpg")

# Logo stuff
ugfx.display_image(
    int((ugfx.width() - logo_width) / 2),
    int((ugfx.height() - logo_height) / 2),
    "cat.jpg" 
)
