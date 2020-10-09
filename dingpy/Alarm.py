from pydub import AudioSegment
from pydub.playback import play
import os

import boto3
import tempfile
from pync import Notifier

s3_client = boto3.client('s3')
BUCKET='dingpy'


class Alarm:
    def __init__(self, timer=False, alarm='beep'):
        '''
        Alarm constructor
        '''
        # logging.basicConfig()
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)

        # set directory of audio file
        self.alarm_audio_path = f'./alarm_audio/{alarm}.mp3'

        audio_file_key = f'{alarm}.mp3'
        f = tempfile.NamedTemporaryFile()

        try:
            s3_client.head_object(Bucket=BUCKET, Key=audio_file_key)
            s3_client.download_file(Bucket=BUCKET, Key=audio_file_key, Filename=f.name)
            self.alarm_audio_path = f.name
        except:
            print(f'Alarm audio file {alarm} doesn''t exist in bucket s3://{BUCKET}')
            raise


    def ding(self):
        '''
        play an alarm sound
        '''
        print(self.alarm_audio_path)
        alarm = AudioSegment.from_file(self.alarm_audio_path, format="mp3")
        play(alarm)


    def list_alarms(self):
        '''
        Print a list of pre-built alarm sound effects.
        '''
        # enumerate local files recursively
        for root, dirs, files in os.walk("./alarm_audio"):
            print([filename for filename in files if not filename.startswith('.')])

                # local_path = os.path.join(root, filename)
                # relative_path = os.path.relpath(local_path, local_src_dir)



Alarm = Alarm()


if __name__ == '__main__':
    Alarm.ding()

