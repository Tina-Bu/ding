# DingPy 🛎 

A Python package that plays an audio alert when your program finishes, especially helpful for long running jobs and impatient developers.

## Examples 

```
import dingpy
import time 

# some code
time.sleep(5)

dingpy.ding()

# to use a different alarm sound
# default is 'bells_tibetan'
dingpy.ding('music_box')

# to list all available alarm sounds
dingpy.list_alarms()
```

## Alarm Options

`Dingpy` comes pre-loaded with 10 royalty free alarm sounds (downloaded from http://soundbible.com/):

- `'beep'`
- `'bells_tibetan'`
- `'clock_chimes'`
- `'computer_magic'`
- `'house_finch'`
- `'japanese_temple_bell_small'`
- `'music_box'`
- `'old_fashioned_school_bell'`
- `'service_bell'`
- `'tinkle'`

To upload your custom alarm audio (currently only support mp3 format):

```
dingpy.upload_alarm(file_path='/local_path/sound.mp3', sound_name='custom-alarm-name') # sound_name needs to be globally unique
```

To delete an uploaded alarm audio file (only user uploaded alarms can be deleted):

```
dingpy.delete_alarm('custom-alarm-name')
```

If you did `from dingpy import Alarm` instead of `import dingpy`, just substitute all the `dingpy` in the above commands with `Alarm` and you should be good to go.

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

## Future Work

- Support other audio formats besides mp3
- Support text to speech alerts
- Integrate with `pync` to send MacOS notifications 
- Local ding for jobs running on remote machines

## Inspirations <a name="inspirations"></a>

I always wanted a Python package that notifies me with a ding when my code completes so I can go about doing other work in the meantime. I was surprised that I couldn't find one after quite some research. There are a few similar tools out there that somewhat do what I want them to do but not quite. So I decided to create `dingpy` for myself. And hopefully it will be helpful for you as well. That being said, if most of your work happens in the terminal or if you prefer to have a pop-up MacOS notification than an alarm, do checkout the projects below:

- [`pync`](https://pypi.org/project/pync/) a Python wrapper to send MacOS notifications (Mac only) (it claims to offer sound notification as well but I couldn't make it work)
- [`ding`](https://github.com/xxv/ding/) a CLI alarm tool for local and remote jobs (it seems to me that you will have to provide your own alarm audio file, you will also need to keep a terminal open running this code at all times, it's not a python package that you can import)
- [`woof`](https://github.com/msbarry/woof) a set of CLI tools to send notifications (options: music, growl notification, text message, tweet, twitter DM, email, and text-to-speech) (Mac only) (have to save alarm audio locally and modify bash profile, only works in the terminal)
- [`notify2`](https://bitbucket.org/takluyver/pynotify2/src) a Python package that sends a MacOS notification (seems not maintained, after installation I got import error for `dbus` and wasn't able to install `dbus` properlly to test it out)

