# Simple Sample Pad for Android

## Description
Simple Sample pad application for Android by kivy.

## Demo
[Drum Pad APK](https://drive.google.com/file/d/1o6HX-zIUIE8tbY5ULUTTzIVyRfvEkYv3/view?usp=sharing)
## Installation
    $ python -m venv kivy_venv
    $ source kivy_venv/bin/activate
    $ pip install https://github.com/kivy/buildozer/archive/master.zip
    $ pip install kivy==2.3.0

## Deploy
    $ buildozer init
    $ buildozer android debug deploy

## Discussion
This app could not be used in practice due to time lags between pressing buttons and playing sounds. Instead of using SoundLoader from Kivy, I tried Pygame to shorten the delay. However, it could not be deployed because of an error related to longintrepr.h. Additionally, I tested using Pydub and Simpleaudio. These seemed to work better but could not be deployed because those libraries are not supported on Linux.

## References
- [Installation of buildozer](https://github.com/kivy/python-for-android/issues/2977#issuecomment-2079334315)
- [Building an android apk from Kivy Crush Course](https://youtu.be/t8N_8WkALdE?si=WHo-AN0GA-sBBSSo)
- [Set efficient key maps](https://youtu.be/krdN-VCngtI?si=SwMGi2Yc12nlaVkc)
