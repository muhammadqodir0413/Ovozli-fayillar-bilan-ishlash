# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NutgVV4BUS3xww055k5Sh-i-TRXyx3PB
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    # Read the WAV file
    sample_rate, data = wavfile.read(wav_file)

    # Check if data is stereo or mono
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo

    # Create a spectrogram
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)  # Set x-axis limit
    plt.ylim(0, sample_rate / 2)           # Frequency range from 0 to Nyquist frequency
    plt.grid(True)
    plt.show()

# Example usage
wav_file_path = 'brownian-noise_16-bit-441khz_brownsches-rauschen-103991.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path)

!pip install gtts

from gtts import gTTS
import os

# Matnni belgilash
text = " Recently, the number of translations from the original, including English, has increased. However, their quality and level of editing vary. The article deals with the peculiarities of editing text translated from English, the features of the language hierarchy in translation, and the issues of ensuring equivalence, which enabletranslators, editors, publishers and journalists to evaluate the consistency of the source text with the target Uzbek text."


# Ovoz yaratish (gTTS - Google Text-to-Speech)
language = 'en'  # Changed to English ('en')
tts = gTTS(text=text, lang=language, slow=False)

# Ovoz faylini saqlash
audio_file = "output.mp3"
tts.save(audio_file)

# Ovoz faylini tinglash (Google Colab-da)
from IPython.display import Audio
Audio(audio_file)