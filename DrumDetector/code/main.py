#glavni modul aplikacije
from mido import MidiFile
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from fourier_transform import stft
import dataset_processing as dp
from midi_transform import midi_transform as mt

#dp.wav_to_image('...', '...')
#dp.midi_to_image('...','...')
