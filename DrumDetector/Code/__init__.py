#glavni modul aplikacije
import wave
import path
import ntpath
import os


file_dir = os.path.dirname(os.path.realpath('__init__'))

drum_dir = os.path.join(file_dir, '../Dataset/')


filename = os.path.abspath(os.path.realpath(drum_dir))
                           
print file_dir
print filename
#drum_pattern = wave.open('', 'r')



