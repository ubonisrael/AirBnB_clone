#!/usr/bin/python3
"""Doc
"""
from models.engine.file_storage import *
from models.engine.file_storage import FileStorage


class FileStorage(FileStorage):
    """Doc
    """

    def reload(self):
        """DOC
        """
        pass

if __name__ == '__main__':
    fs = FileStorage()
    print(type(fs.reload))