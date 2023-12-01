# Karaoke

## Overview

This project allows you to create automatic karaoke using open source AI models for source separation and speech-to-text.

## Installation

To install the project, follow these steps:

1. First, make sure you have all the necessary dependencies. You can do this by downloading the `requirements.txt` file.

2. Install the dependencies using the following command:

   ```bash
   $ pip install -r requirements.txt

## Utilization

Using the script is straightforward:

1. Ensure you know the file path to your music file, which should be in either `.wav` or `.mp3` format.

2. Execute the following command in your terminal:

   ```bash
   $ python karaoke.py --filepath your_file_path_to_the_music_file.wav

## Results

1. One `non_vocals.wav` file containing everything except the singer voice.
2. Three files `drums.wav`, `bass.wav`,`other.wav` containing the separated sound tracks.
3. The `vocals.wav` file containing the voice of the singer.
4. The `transcription.txt` file containing the singer vocals.
