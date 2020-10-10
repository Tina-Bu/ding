# DingPy 🛎 

A Python package that plays an audio alert when your program finishes, particularly useful for long running batch jobs and impatient developers 🙋‍♀️🙋.

## Examples 

```
# first instantiate a dingpy Alarm object
import dingpy

alarm = dingpy.Alarm()
```

To play an alarm at the end of a code block:

```
# a long running block 
for i in range(100):
    sleep(1)

alarm.ding()
```

To list all available alarm sounds:

```
alarm.list_alarms()
```

To use a different alarm sound (default is `'bells_tibetan'`): 

```
alarm = dingpy.Alarm(sound='music_box')
alarm.ding()
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
alarm.upload_alarm(file_path='/local_path/sound.mp3', sound_name='custom-alarm-name') # sound_name needs to be globally unique

# listing all available alarms to confirm upload success
alarm.list_alarms()
```

To delete an uploaded alarm audio file (only user uploaded alarms can be deleted):

```
alarm.delete_alarm('custom-alarm-name')

# listing all available alarms to confirm deletion success
alarm.list_alarms()
```

## Installation 

`DingPy` can be installed via `pip` or `conda`.

```
$ pip install dingpy
$ 
$ conda install dingpy
```

## Future Work

- Support other audio formats
- Support text to speech for speech alert 
- Integrate with `pync` to add notifications to the Mac notification center
- Make this work for jobs running on remote machines

## Inspirations <a name="inspirations"></a>

- [`dingdingdong`](https://github.com/Shahor/dingdingdong) a Node.js notification package 
- [`ding`](https://github.com/xxv/ding/) a CLI alarm for local and remote jobs
- [`woof`](https://github.com/msbarry/woof) a set of CLI tools to send notifications (options: music, growl notification, text message, tweet, twitter DM, email, and text-to-speech) (Mac only)
- [`pync`](https://pypi.org/project/pync/) a Python wrapper to send growl notifications (Mac only)

