"""
Setup script for Mac Photo Migrator app (Simple version)
"""
from setuptools import setup

APP = ['app_launcher.py']
DATA_FILES = [
    ('scripts', [
        'scripts/migrate_photos_gui.py',
        'scripts/migrate_photos_no_heic.py',
        'scripts/migrate_photos.py',
        'scripts/migrate_photos_auto.py'
    ]),
    ('heic_converters', [
        'heic_converters/convert_heic_simple.py',
        'heic_converters/convert_heic_to_jpeg.py'
    ]),
    ('', ['README.md', 'requirements.txt'])
]

OPTIONS = {
    'argv_emulation': False,
    'packages': ['tkinter'],
    'iconfile': None,
    'plist': {
        'CFBundleName': 'Mac Photo Migrator',
        'CFBundleDisplayName': 'Mac写真移行ツール',
        'CFBundleGetInfoString': "Mac写真ライブラリをWindowsに移行",
        'CFBundleIdentifier': "com.mintiasaikoh.macphotomigrator",
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
    name='Mac Photo Migrator',
)