# DingPy 🛎 

[![GitHub license](https://img.shields.io/github/license/tinahbu/dingpy)](https://github.com/tinahbu/dingpy/blob/master/LICENSE)
[![pypi](https://img.shields.io/badge/pypi-1.0.0-blue)](https://pypi.org/project/dingpy/)

A Python package that plays an audio alert when your program finishes, especially helpful for long running jobs and impatient developers.

## Examples 

```
import dingpy

dingpy.ding()  # plays the default alarm 'japanese_temple_bell'

# to use a different alarm sound:
dingpy.ding(sound='music_box')

# to list all available alarms
dingpy.list_alarms()
```

## Alarm Options

`Dingpy` comes pre-loaded with 10 royalty free alarm sounds (downloaded from http://soundbible.com/):

- `'beep'`
- `'bell_tibetan'`
- `'birds'`
- `'clock_chimes'`
- `'computer_magic'`
- `'japanese_temple_bell'`
- `'music_box'`
- `'school_bell'`
- `'service_bell'`
- `'tinkle'`

The 10 audio files are packaged and downloaded when you install `dingpy`. You can further customize `dingpy` by asking it to use a mp3 file from your local directory via the `path` parameter:

```
dingpy.ding(path='/local_path/sound.mp3')
```

If you'd like to contribute your mp3 file for other `dingpy` users to access, you can upload it to the public `dingpy` s3 bucket:

```
# sound_name needs to be globally unique
dingpy.upload_alarm(file_path='/local_path/sound.mp3', sound_name='alarm-name') 
```

Your uploaded mp3 file will be downloaded each time when `dingpy.ding()` is called. To use an alarm uploaded by other people (because it's not packaged with the `dingpy` installation), you will need to set the `s3` parameter:

```
dingpy.ding(sound='sound-name', s3=True)
```

To delete an uploaded alarm (the 10 pre-loaded alarms can't be deleted):

```
dingpy.delete_alarm('sound-name')
```

## Installation 

`DingPy` can be installed via `pip` like this

```
$ pip install dingpy
```

or from the source code like this

```
$ pip install git+https://github.com/tinahbu/dingpy.git
```

or this

```
$ git clone git@github.com:tinahbu/dingpy.git
$ cd dingpy
$ python setup.py install
```

## Prerequisite

As stated above, the 10 default alarms are packaged with `dingpy` but user uploaded alarms are hosted in a public s3 bucket. So if you'd like to use the customization feature you will have to have aws cli configured. To do that, follow the doc [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

## Future Work

- Support other audio formats besides mp3
- Support text to speech alerts
- Integrate with `pync` to send MacOS notifications 
- Local ding for jobs running on remote machines
- Make available on conda

## Inspirations <a name="inspirations"></a>

I always wanted a Python package that notifies me with a ding when my code completes so I can go about doing other work in the meantime. I was surprised that I couldn't find one after quite some research. There are a few similar tools out there that somewhat do what I want them to do but not quite. So I decided to create `dingpy` for myself. And hopefully it will be helpful for you as well. That being said, if most of your work happens in the terminal or if you prefer to have a pop-up MacOS notification than an alarm, do checkout the projects below:

- [`pync`](https://pypi.org/project/pync/) a Python wrapper to send MacOS notifications (Mac only) (it claims to offer sound notification as well but I couldn't make it work)
- [`ding`](https://github.com/xxv/ding/) a CLI alarm tool for local and remote jobs (it seems to me that you will have to provide your own alarm audio file, you will also need to keep a terminal open running this code at all times, it's not a python package that you can import)
- [`woof`](https://github.com/msbarry/woof) a set of CLI tools to send notifications (options: music, growl notification, text message, tweet, twitter DM, email, and text-to-speech) (Mac only) (have to save alarm audio locally and modify bash profile, only works in the terminal)
- [`notify2`](https://bitbucket.org/takluyver/pynotify2/src) a Python package that sends a MacOS notification (seems not maintained, after installation I got import error for `dbus` and wasn't able to install `dbus` properlly to test it out)

