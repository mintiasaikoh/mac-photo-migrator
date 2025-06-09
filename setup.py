"""
Setup script for Mac Photo Migrator app
"""
from setuptools import setup

APP = ['scripts/migrate_photos_gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['osxphotos', 'piexif', 'PIL', 'tkinter'],
    'includes': ['tkinter', 'tkinter.ttk', 'tkinter.filedialog', 'tkinter.messagebox'],
    'excludes': ['matplotlib', 'numpy', 'scipy', 'pandas'],
    'resources': [],
    'iconfile': None,
    'plist': {
        'CFBundleName': 'Mac Photos to Windows',
        'CFBundleDisplayName': 'Mac Photos to Windows',
        'CFBundleGetInfoString': "Transfer photos from Mac Photos app to Windows with metadata",
        'CFBundleIdentifier': "com.macphotostowindows.app",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0.0",
        'NSHumanReadableCopyright': u"Copyright © 2025",
        'NSRequiresAquaSystemAppearance': False,
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '10.15.0',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
