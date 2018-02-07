'''
Modul za transformisanje midi fajla u matricu
'''
import mido
from mido.midifiles.tracks import merge_tracks
import numpy as np


def midi_transform(midi_file, midi_matrix_col_num, time_interval, midi_notes, drum_col):
    '''
    midi_matric_col_num mora se poklapati sa brojem kolona spektrograma
    time_interval predstavlja vremenski interval jedne kolone spektrograma.
    koristimo ga da bismo sihronizovali udarce bubnjeva u spektrogramu sa udardima u midi matrici
    '''
    ret_mat = np.zeros((len(drum_col), midi_matrix_col_num))
    for msg in merge_tracks(midi_file.tracks):
        if msg.type == 'set_tempo':
            tempo = msg.tempo
    time_of_tick = mido.tick2second(1, midi_file.ticks_per_beat, tempo)
    ticks_per_col = time_interval/time_of_tick
    num_of_ticks = 0 #broj tickova
    for msg in merge_tracks(midi_file.tracks):
        num_of_ticks += msg.time
        if msg.type == 'note_on':
            if msg.note in midi_notes:
                col = int(round(num_of_ticks/ticks_per_col, 0))
                ret_mat[midi_notes[msg.note], col:col+2] = 255
    return ret_mat
