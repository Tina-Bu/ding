# DingPy

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

To choose a different alarm (default is `'bells_tibetan'`): 

```
alarm = dingpy.Alarm(sound='music_box')
alarm.ding()
```

To upload your custom alarm audio (currently only support mp3 format):

```
alarm.upload_alarm(file_path='/local_path/sound.mp3', sound_name='custom-alarm-name') # sound_name needs to be globally unique

# listing all available alarms to confirm submission success
alarm.list_alarms()
```

To delete an uploaded alarm audio file (only user uploaded alarms can be deleted):

```
alarm.delete_alarm('custom-alarm-name')

# listing all available alarms to confirm deletion success
alarm.list_alarms()
```

## Alarm Options

`Dingpy` comes pre-loaded with 10 alarm sounds:

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

All the audios are royalty free. They were downloaded from http://soundbible.com/

## Installation 

`DingPy` can be installed with `pip` or `conda`.

```
$ pip install dingpy
$ conda install dingpy
```

You will have to install the ffmpeg dependency with brew install and add it to path `echo 'export PATH="/usr/local/opt/ffmpeg/bin:$PATH"' >> ~/.zshrc`.

- PyPI: https://pypi.org/project/dingpy/
- Conda: 

## Future Work

- Support other audio formats
- Support text to speech for speech alert 
- Integrate with `pync` to add notifications to the Mac notification center

## Inspirations <a name="inspirations"></a>

https://github.com/Shahor/dingdingdong

https://github.com/xxv/ding/

https://github.com/msbarry/woof

https://pypi.org/project/pync/


---

Author: [Tina Bu](http://medium.com/@tinabu/)


