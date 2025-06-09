"""
Setup script for Mac Photo Migrator app
"""
from setuptools import setup

APP = ['scripts/migrate_photos_gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['osxphotos', 'piexif', 'PIL', 'tkinter'],
    'iconfile': None,
    'plist': {
        'CFBundleName': 'Mac Photo Migrator',
        'CFBundleDisplayName': 'Mac写真移行ツール',
        'CFBundleGetInfoString': "Mac写真ライブラリをWindowsに移行",
        'CFBundleIdentifier': "com.yourname.macphotomigrator",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0.0",
        'NSHumanReadableCopyright': u"Copyright © 2025",
        'NSRequiresAquaSystemAppearance': False,
        'NSHighResolutionCapable': True,
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)