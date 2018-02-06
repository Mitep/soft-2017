'''
glavni modul aplikacije
'''

#from keras.models import load_model
import dataset_processing as dp
#import rnn

WAV_IN_PATH = '..\..\dataset\in'
MIDI_IN_PATH = '..\..\dataset\out'
WAV_OUT_PATH = '..\dataset\in'
MIDI_OUT_PATH = '..\dataset\out'

#transformacija wav i midi fajlova u matrice
dp.wav_to_image(WAV_IN_PATH, WAV_OUT_PATH)
dp.midi_to_image(MIDI_IN_PATH, MIDI_OUT_PATH)

#model = rnn.build_model()
#data = dp.format_dataset(WAV_OUT_PATH, MIDI_OUT_PATH)
#model, train_start_time, train_end_time = rnn.train_rnn(model, data, 2)

#model.save('rnn_model.h5')
#model = load_model('rnn_model.h5')
