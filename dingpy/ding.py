from Alarm import Alarm
import os

if __name__ == "__main__":
    alarm = Alarm(sound='japanese_temple_bell_small')
    alarm.ding()
    alarm.list_alarms()
    alarm.upload_alarm(file_path='./alarm_audio/beep.mp3', sound_name='beep-test-upload3')
    alarm.list_alarms()

    alarm = Alarm(sound='beep-test-upload3')
    alarm.ding()
    alarm.delete_alarm('beep-test-upload3')
    alarm.list_alarms()
    alarm.delete_alarm('beep-test-upload')
