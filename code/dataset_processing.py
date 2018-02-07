'''
Konvertovanje wav i midi fajla u sliku.
'''

import numpy as np
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
    mat = np.zeros((1024,1))
    for filename in os.listdir(input_dir):
        path = os.path.join(input_dir, filename)
        sample_rate, data = read(path)
        time_interval_of_col, result = ft.stft(data)
        wav_col_len[filename[7:9]] = len(result[1])
        #transormacije nad matricom
        result = wav_process_type(result, 'multiply_by_3')
        
        mat = np.concatenate((mat,result), axis=1)
        img = Image.fromarray(result)
        output_path = os.path.join(output_dir, filename[0:-4]) + '.png'
        if img.mode != 'L':
            img = img.convert('L')
        img.save(output_path, 'png')
        print(filename + ' converted to img')
    mat = np.delete(mat, 0, 1)
    img = Image.fromarray(mat)
    output_path = os.path.join(output_dir, 'input.png')
    if img.mode != 'L':
        img = img.convert('L')
    img.save(output_path, 'png')

def wav_process_type(wav_img, type):
    '''
    transformacije nad ulaznom matricom
    '''
    if type == 'multiply_by_3':
        wav_img = wav_img*3
        return wav_img
    elif type == 'inverse':
        wav_img = 255-wav_img
        return wav_img
    elif type == 'cut':
        wav_img[wav_img > 30] =255
        wav_img[wav_img <= 30] = 0
        return wav_img
    else:
        '''
        nije navedeno nista pa cemo samo preskociti
        '''
    return wav_img

def midi_to_image(input_dir, output_dir):
    '''
    Konvertovanje midi fajla u sliku.
    '''
    drum_col = {'kick':0, 'snare':1, 'hihat':2}
    midi_notes = {36:drum_col['kick'], 38:drum_col['snare'], 48:drum_col['hihat'], 49:drum_col['hihat'], 50:drum_col['hihat'], 51:drum_col['hihat'], 52:drum_col['hihat'], 53:drum_col['hihat'], 54:drum_col['hihat'], 55:drum_col['hihat'], 56:drum_col['hihat'], 57:drum_col['hihat'], 58:drum_col['hihat'], 59:drum_col['hihat']}
    mat = np.zeros((3,1))
    for filename in os.listdir(input_dir):
        path = os.path.join(input_dir, filename)
        mid = MidiFile(path)
        midi_result = mt(mid, wav_col_len[filename[-6:-4]], time_interval, midi_notes, drum_col)
        mat = np.concatenate((mat, midi_result, midi_result, midi_result), axis=1)
        img = Image.fromarray(midi_result)
        output_path = os.path.join(output_dir, filename[0:-4]) + '.png'
        if img.mode != '1':
            img = img.convert('1')
        img.save(output_path, 'png')
        print(filename + ' converted to img')
    mat = np.delete(mat, 0, 1)
    img = Image.fromarray(mat)
    output_path = os.path.join(output_dir, 'output.png')
    if img.mode != '1':
        img = img.convert('1')
    img.save(output_path, 'png')
