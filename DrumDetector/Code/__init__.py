#glavni modul aplikacije
from midi_transform import midi_transform as mt
from mido import MidiFile
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from fourier_transform import stft

mid = MidiFile('C:\Users\mitep\Desktop\soft_dataset_reaper\pattern01\midi_pattern.mid')
sample_rate, data = read('C:\Users\mitep\Desktop\soft_dataset_reaper\pattern01\drums00.wav')
time_interval_of_col, result =  stft(data)
result_col_num = len(result[1])
'''
print time_interval_of_col #duzina u sekundama jedne kolone
print len(result[1]) # broj kolona matrice vracene
print len(result) # broj vrsta vracene matrice
print time_interval_of_col*len(result[1]) # duzina klipa
'''
#ovo cemo iz nekog fajla ucitati
cinela = 55
bas_bubanj = 36
dobos = 38
midi_notes = {bas_bubanj:0, dobos:1, cinela:2} #dictionary kao kljuc ime note a vrednost broj kolone kojoj pripada
midi_result = mt(mid, result_col_num, time_interval_of_col, midi_notes)


img = plt.imshow(midi_result, origin='lower', cmap='jet', interpolation='nearest', aspect='auto')
plt.show()