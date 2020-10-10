import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import logging
from pydub import AudioSegment
from pydub.playback import play
import tempfile
from typing import List

s3_client = boto3.client('s3')

BUCKET='dingpy'
PRE_LOADED_ALARMS = [
    'beep',
    'bells_tibetan',
    'clock_chimes',
    'computer_magic',
    'house_finch',
    'japanese_temple_bell_small',
    'music_box',
    'old_fashioned_school_bell',
    'service_bell',
    'tinkle'
]


class MyAlarm(object):
    def __init__(self):

        # create a local temporary directory to save the downloaded audio file
        self._dir = tempfile.mkdtemp()
        self._sound = None
        self._local_tmp_path = None


    def __str__(self):
        return f'DingPy MyAlarm Object (sound=\'{self._sound}\')'


    def __repr__(self):
        return {
            'sound': self._sound,
            'temp_local_dir': self._local_tmp_path,
            's3_file_dir': f's3://{BUCKET}/{self._sound}.mp3'
        }


    def ding(self, sound: str='japanese_temple_bell_small') -> None:
        '''
        Play the alarm and print the alarm time.
        '''
        self._play_alarm(sound=sound)
        logging.info(f'🛎  at {datetime.now()}')


    def _play_alarm(self, sound: str) -> None:
        '''
        Downloads the sound audio file to a temporary local directory and play it.
        '''
        # create a local temporary directory to save the downloaded audio file
        self._dir = tempfile.mkdtemp()
        self._sound = sound
        self._local_tmp_path = f'{self._dir}/dingpy_{self._sound}.mp3'

        try:
            s3_client.download_file(
                Bucket=BUCKET,
                Key=f'{self._sound}.mp3',
                Filename=self._local_tmp_path)
            alarm = AudioSegment.from_file(self._local_tmp_path, format="mp3")
            play(alarm)
        except ClientError as e:
            logging.error(f'❌ Error downloading audio file {self._sound} from s3 bucket: {e}')


    @staticmethod
    def list_alarms() -> None:
        '''
        Print a list of pre-loaded alarm sounds.
        '''
        alarm_files = _get_s3_keys(bucket=BUCKET)
        alarms = sorted([alarm[:-4] if alarm.endswith('mp3') else alarm for alarm in alarm_files])

        print('All available alarm sounds include: 🛎')
        for _ in alarms:
            print(f'- \'{_}\'')


    @staticmethod
    def upload_alarm(file_path: str, sound_name : str) -> None:
        '''
        Allow user to upload a customized mp3 alarm to a public s3 bucket.

        Args:
            file_path: local path that contains the mp3 file.
            sound_name: name you want for your alarm, without the '.mp3' extension.
        '''
        # check if file is of mp3 type
        if not file_path.endswith('.mp3'):
            logging.error(f'😢 Sorry we only support mp3 format currently.')

        key = f'{sound_name}.mp3'
        if _check_exists_in_s3(bucket=BUCKET, key=key):
            logging.error(f'🚫 Sound \'{sound_name}\' already exists, please choose a different name.')
        else:
            try:
                response = s3_client.upload_file(file_path, Bucket=BUCKET, Key=key)
                logging.info(f'🎉 Upload succeeded! You can now create your own Alarm 🛎 with \n `dingpy.ding(\'{sound_name}\')`')
            except ClientError as e:
                logging.error(f'❌ Error uploading audio file \'{sound_name}\' to s3 bucket: {e}')


    @staticmethod
    def delete_alarm(sound_name : str):
        '''
        Allow user to delete custom uploaded alarm sounds.

        Args:
            sound_name: name of the alarm to delete, without the '.mp3' extension.
        '''
        key = f'{sound_name}.mp3'
        if sound_name in PRE_LOADED_ALARMS:
            logging.error(f'🚫 \'{sound_name}\' is a pre-loaded alarm sound that can\'t be deleted.')

        if _check_exists_in_s3(bucket=BUCKET, key=key):
            s3_client.delete_object(Bucket=BUCKET, Key=key)
            logging.info(f'✅ Successfully deleted alarm \'{sound_name}\' from s3 bucket.')
        else:
            logging.error(f'❌ Alarm file {sound_name}.mp3 doesn\'t exist in s3 bucket')


def _check_exists_in_s3(bucket: str, key: str) -> bool:
    '''
    Check if a key exists in the given bucket.
    '''
    try:
        s3_client.head_object(Bucket=BUCKET, Key=key)
    except ClientError as e:
        return int(e.response['Error']['Code']) != 404
    return True


def _get_s3_keys(bucket: str) -> List[str]:
    '''
    Get a list of keys in an S3 bucket.
    '''
    keys = []
    resp = s3_client.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
        keys.append(obj['Key'])
    return keys


Alarm = MyAlarm()


def ding(sound: str='japanese_temple_bell_small') -> None:
    '''
    Play the alarm and print the alarm time.

    There is an option `sound` to set the alarm sound.

    Example:
        import dingpy
        dingpy.ding()
        dingpy.ding(sound='computer_magic')
    '''
    Alarm.ding(sound=sound)


def list_alarms() -> None:
    Alarm.list_alarms()


def upload_alarm(file_path: str, sound_name : str) -> None:
    Alarm.upload_alarm(file_path, sound_name)


def delete_alarm(sound_name: str) -> None:
    Alarm.delete_alarm(sound_name)



