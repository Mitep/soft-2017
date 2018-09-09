'''
glavni modul aplikacije
'''
#import dataset_processing as dp
from keras.models import load_model
from rnn import run_rnn, train_rnn, build_model
from PIL import Image

WAV_IN_PATH = '/home/mitep/Workspace/soft_old/dataset_raw/input'
MIDI_IN_PATH = '/home/mitep/Workspace/soft_old/dataset_raw/output'
WAV_OUT_PATH = '/home/mitep/Workspace/soft_old/dataset/input'
MIDI_OUT_PATH = '/home/mitep/Workspace/soft_old/dataset/output'
RNN_TEST = '/home/mitep/Workspace/soft_old/dataset_test/input'

#transformacija wav i midi fajlova u matrice
#dp.wav_to_image(WAV_IN_PATH, WAV_OUT_PATH)
#dp.midi_to_image(MIDI_IN_PATH, MIDI_OUT_PATH)

#formatiranje dataseta i kreidanje modela)
model = build_model(1024, 3)
trained_model = train_rnn(model, WAV_OUT_PATH, MIDI_OUT_PATH)
trained_model.save('rnn_model.h5')

# pokretanje
'''
model = load_model('rnn_model.h5')
midi_mat = run_rnn(model, RNN_TEST)
img = Image.fromarray(midi_mat)
if img.mode != 'L':
    img = img.convert('L')
img.save("test.png", 'png')
'''
