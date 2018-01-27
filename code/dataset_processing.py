'''
Konvertovanje wav i midi fajla u sliku.
'''
import os
from scipy.io.wavfile import read
from PIL import Image
from mido import MidiFile
import matplotlib.pyplot as plt
import fourier_transform as ft
from midi_transform import midi_transform as mt

wav_col_len = {}
time_interval = (float(1024)/44100)*(0.5)

def wav_to_image(input_dir, output_dir):
    '''
    Konvertovanje wav fajla u sliku.
    '''
    for filename in os.listdir(input_dir):
        path = os.path.join(input_dir, filename)
        sample_rate, data = read(path)
        time_interval_of_col, result = ft.stft(data)
        wav_col_len[filename[7:9]] = len(result[1])
        img = Image.fromarray(result)
        output_path = os.path.join(output_dir, filename[0:-4]) + '.png'
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(output_path, 'png')

def midi_to_image(input_dir, output_dir):
    '''
    Konvertovanje midi fajla u sliku.
    '''
    cinela = 55
    bas_bubanj = 36
    dobos = 38
    midi_notes = {bas_bubanj:0, dobos:1, cinela:2}
    for filename in os.listdir(input_dir):
        path = os.path.join(input_dir, filename)
        mid = MidiFile(path)
        midi_result = mt(mid, wav_col_len[filename[-6:-4]], time_interval, midi_notes)
        img = Image.fromarray(midi_result)
        output_path = os.path.join(output_dir, filename[0:-4]) + '.png'
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(output_path, 'png')
        