from .upload_privacy import *
from .password import *

# For loading all custom js
WEB_DIRECTORY = "js"

NODE_CLASS_MAPPINGS = {
    "LoadImageWithPrivacy": LoadImageWithPrivacy,
    "RemoveImageForPrivacy": RemoveImageForPrivacy,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImageWithPrivacy": "Load Image with Privacy",
    "RemoveImageForPrivacy": "Remove Image for Privacy",
}
