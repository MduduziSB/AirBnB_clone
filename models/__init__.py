#!/usr/bin/python3
"""Magic init method for the models directory"""

from models.engine.file_storage import FileStorage


"""An init file for the models directory"""

storage = FileStorage()
storage.reload()
