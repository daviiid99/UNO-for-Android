from distutils.core import setup
from setuptools import find_packages


setup(
    name="UNO",
    version='2.0',
    author="David Molina Morales(daviiid99)",
    author_email='daviiideveloper@gmail.com',
    description='UNO based game powered by pygame framework and Python',
    url='https://github.com/daviiid99/UNO-for-android',
    packages=find_packages(),
    package_data={
        '.': ['main.py', 'board.py', 'cards.py', 'player.py', 'player_name.py', 'save_game.py', 'game_values.json', 'version.txt'],
        '*/*': ['*.py', '*.mp3', '*.ttf', '*.png', '*.ico'],
        '*/*/*': ['*.py', '*.mp3', '*.ttf', '*.png', '*.ico'],
        
    },
    options={
            'apk': {
                'ignore-setup-py': None,
                # 'release': None,
                'arch': 'arm64-v8a',
                'package': 'com.daviiid99.uno',
                'requirements': 'pygame==2.1.2,multidict==5.1.0,\
                    attrs==21.2.0,async-timeout==3.0.1,chardet==4.0.0,idna==3.2,\
                        typing-extensions==3.10.0.0,yarl==1.6.3,Plyer',
                'sdk-dir': '../android-sdk',
                'ndk-dir': '../android-ndk-r19c',
                'presplash': 'Assets/images/presplash.png',
                'presplash-color': '#ee2229',
                'icon': 'Assets/logo/logo.png',
                'dist-name': 'Assets',
                'android-api': 27,
                'ndk-dir' : '../ndk',
                'sdk-dir' : '../sdk',
                'bootstrap': 'sdl2',
                'orientation': 'landscape',
                'wakelock': None,
                'permissions':
                    [
                        'VIBRATE',
                        'INTERNET'
                    ]
            }
        }
)