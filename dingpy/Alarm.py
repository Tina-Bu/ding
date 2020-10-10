import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import logging
from pydub import AudioSegment
from pydub.playback import play
import tempfile
from typing import List

logging.getLogger().setLevel(logging.INFO)

BUCKET='dingpy'


class Alarm:
    def __init__(self, sound: str='bells_tibetan'):
        '''
        Constructor.
        '''
        self._sound = sound
        # create a local temporary directory to save the downloaded audio file
        self._dir = tempfile.mkdtemp()
        self._audio_file = f'{self._dir}/dingpy_{self._sound}.mp3'
        self._pre_loaded_alarms = [
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
        self.s3_client = boto3.client('s3')

        try:
            self.s3_client.download_file(
                Bucket=BUCKET,
                Key=f'{self._sound}.mp3',
                Filename=self._audio_file)

            logging.info(f'Put me at the end of your code block and I will notify you with a {self._sound} sound 🛎.')

        except ClientError as e:
            logging.error(f'❌ Error downloading audio file {self._sound} from bucket s3://{BUCKET}/: {e}')


    def __str__(self):
        return f'DingPy Alarm(sound=\'{self._sound}\')'


    def __repr__(self):
        return {
            'sound': self._sound,
            'temp_local_dir': self._audio_file,
            's3_file_dir': f's3://{BUCKET}/{self._sound}.mp3'
        }


    def ding(self) -> None:
        '''
        Play the alarm and print the alarm time.
        '''
        alarm = AudioSegment.from_file(self._audio_file, format="mp3")
        play(alarm)
        logging.info(f'🛎 at {datetime.now()}')


    def list_alarms(self) -> None:
        '''
        Print a list of pre-loaded alarm sounds.
        '''
        alarm_files = self._get_s3_keys(bucket=BUCKET)
        alarms = sorted([alarm[:-4] if alarm.endswith('mp3') else alarm for alarm in alarm_files])

        print('All available alarm sounds include:')
        for _ in alarms:
            print(f'- \'{_}\'')


    def upload_alarm(self, file_path: str, sound_name : str) -> None:
        '''
        Allow user to upload a customized mp3 alarm to a public s3 bucket.

        Args:
            file_path: local path that contains the mp3 file.
            sound_name: name you want for your alarm, without the '.mp3' extension.
        '''
        key = f'{sound_name}.mp3'
        if self._check_exists_in_s3(bucket=BUCKET, key=key):
            logging.error(f'🚫 Sound \'{sound_name}\' already exists, please choose a different name.')
        else:
            try:
                response = self.s3_client.upload_file(file_path, Bucket=BUCKET, Key=key)
                logging.info(f'🎉 Upload succeeded! You can now create your own Alarm 🛎 with \n `alarm = Alarm(sound=\'{sound_name}\')`')
            except ClientError as e:
                logging.error(f'❌ Error uploading audio file \'{sound_name}\' to bucket s3://{BUCKET}/: {e}')


    def delete_alarm(self, sound_name : str):
        '''
        Allow user to delete custom uploaded alarm sounds.

        Args:
            sound_name: name of the alarm to delete, without the '.mp3' extension.
        '''
        key = f'{sound_name}.mp3'
        if sound_name in self._pre_loaded_alarms:
            logging.error(f'🚫 \'{sound_name}\' is a pre-loaded alarm sound that can\'t be deleted.')

        if self._check_exists_in_s3(bucket=BUCKET, key=key):
            self.s3_client.delete_object(Bucket=BUCKET, Key=key)
            logging.info(f'✅ Deleted alarm \'{sound_name}\' from bucket s3://{BUCKET}/.')
        else:
            logging.error(f'❌ Alarm file {sound_name}.mp3 doesn\'t exist in bucket s3://{BUCKET}/')


    def _check_exists_in_s3(self, bucket: str, key: str) -> bool:
        '''
        Check if a key exists in the given bucket.
        '''
        try:
            self.s3_client.head_object(Bucket=BUCKET, Key=key)
        except ClientError as e:
            return int(e.response['Error']['Code']) != 404
        return True


    def _get_s3_keys(self, bucket: str) -> List[str]:
        '''
        Get a list of keys in an S3 bucket.
        '''
        keys = []
        resp = self.s3_client.list_objects_v2(Bucket=bucket)
        for obj in resp['Contents']:
            keys.append(obj['Key'])
        return keys

