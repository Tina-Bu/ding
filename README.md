# DingPy

`DingPy` is a Python package that plays an audio alert when your program finishes. It is particularly useful for long running batch jobs and impatient developers.

- PyPI: https://pypi.org/project/dingpy/
- Medium post: 


## Examples 

```
import dingpy

# a long running block 
for i in range(100):
    sleep(1)

dingpy.main()
```


## Installation 

`DingPy` can be installed with `pip` or `conda`.

```
$ pip install dingpy
$ conda install dingpy
```

You will have to install the ffmpeg dependency with brew install and add it to path `echo 'export PATH="/usr/local/opt/ffmpeg/bin:$PATH"' >> ~/.zshrc`.

## TODO 
- package alarm_audio file into package build

## I want to add a different alarm sound!

If you have an alarm audio you would like to use, 

Please consider submitting a pull request so we can enrich the audio library of this project. 


## Copyright

Audios downloaded from: http://soundbible.com/

## Inspirations <a name="inspirations"></a>

https://github.com/Shahor/dingdingdong

https://github.com/xxv/ding/

https://github.com/msbarry/woof

https://pypi.org/project/pync/

https://pypi.org/project/notify2/

---

Author: [Tina Bu](http://medium.com/@tinabu/)


