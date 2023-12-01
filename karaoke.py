import demucs.api
import torchaudio
import whisper
from argparse import ArgumentParser
from pathvalidate.argparse import validate_filename_arg, validate_filepath_arg


##Gestion du chemin du fichier donné dans la commande
parser = ArgumentParser()
parser.add_argument("--filepath", type=validate_filepath_arg)
chemin= parser.parse_args().filepath

##Séparation des sources
non_vocals_track = 0
separator = demucs.api.Separator()
origin, separated = separator.separate_audio_file(chemin)
for name, audio_tracks in separated.items():
    torchaudio.save(f"{name}.wav",audio_tracks, separator.samplerate)
torchaudio.save('non_vocals.wav',separated['bass']+separated['drums']+separated['other'],separator.samplerate)

## Enregistrement des paroles en .txt
model = whisper.load_model("base")
result = model.transcribe("vocals.wav")
transcribed_vocals = result["text"]
with open("transcription.txt", "w") as file:
    file.write(transcribed_vocals)

    