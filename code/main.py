'''
glavni modul aplikacije
'''

from keras.models import load_model
import dataset_processing as dp
import rnn

WAV_IN_PATH = 'dataset_raw\input'
MIDI_IN_PATH = 'dataset_raw\output'
WAV_OUT_PATH = 'dataset\input'
MIDI_OUT_PATH = 'dataset\output'

#transformacija wav i midi fajlova u matrice
#dp.wav_to_image(WAV_IN_PATH, WAV_OUT_PATH)
#dp.midi_to_image(MIDI_IN_PATH, MIDI_OUT_PATH)

#formatiranje dataseta i kreidanje modela)
#model = rnn.build_model(1024, 3)
#trained_model = rnn.train_rnn(model, WAV_OUT_PATH, MIDI_OUT_PATH)

#trained_model.save('rnn_model.h5')
model = load_model('rnn_model.h5')
trained_model = rnn.train_rnn(model, WAV_OUT_PATH, MIDI_OUT_PATH)
trained_model.save('rnn_model2.h5')