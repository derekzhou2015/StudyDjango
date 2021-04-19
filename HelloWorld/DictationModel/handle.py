from pydub import AudioSegment, silence
from django.conf import settings
import time
import random


def get_sound_list(f):
    sound = AudioSegment.from_file(f, format=f.content_type[-3:])
    #loudness = sound.dBFS
    s_l = []
    chunks = silence.split_on_silence(
        sound, min_silence_len=1200, silence_thresh=-45, keep_silence=500)
    chunks2 = list(filter(lambda x: len(x) >= 1000, chunks))
    for i, v in enumerate(chunks2):
        file_name = '{0}{1:03d}.mp3'.format(
            int(time.time()), random.randint(1, 1000))
        v.export('{0}\sounds\{1}'.format(
            settings.MEDIA_ROOT, file_name), format="mp3")
        s_l.append({'id': i+1, 'file_name': file_name,
                    'file_path': 'sounds/%s' % file_name})
    return s_l
