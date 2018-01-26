import numpy as np

# data = a numpy array containing the signal to be processed
# fs = a scalar which is the sampling frequency of the data

'''
Kod preuzet sa https://kevinsprojects.wordpress.com/2014/12/13/short-time-fourier-transform-using-python-and-numpy/.
Dio koda prepravljen tako da odgovara nasem algoritmu.
'''

def stft(data, fft_size=1024, overlap_fac=0.5, sample_rate=44100):
    hop_size = np.int32(np.floor(fft_size * (1-overlap_fac)))
    pad_end_size = fft_size          # the last segment can overlap the end of the data array by no more than one window size
    total_segments = np.int32(np.ceil(len(data) / np.float32(hop_size)))
    #t_max = len(data) / np.float32(sample_rate)
     
    window = np.hanning(fft_size)  # our half cosine window
    inner_pad = np.zeros(fft_size) # the zeros which will be used to double each segment size
     
    proc = np.concatenate((data, np.zeros(pad_end_size)))              # the data to process
    result = np.empty((fft_size, total_segments), dtype=np.float32)    # space to hold the result
     
    for i in xrange(total_segments):                      # for each segment
        current_hop = hop_size * i                        # figure out the current segment offset
        segment = proc[current_hop:current_hop+fft_size]  # get the current segment
        windowed = segment * window                       # multiply by the half cosine function
        padded = np.append(windowed, inner_pad)           # add 0s to double the length of the data
        spectrum = np.fft.fft(padded) / fft_size          # take the Fourier Transform and scale by the number of samples
        autopower = np.abs(spectrum * np.conj(spectrum))  # find the autopower spectrum
        result[:, i] = autopower[:fft_size]               # append to the results array
     
    result = 20*np.log10(result)         # scale to db
    result = np.clip(result, -40, 200)    # clip values
    
    time_interval_of_col = (float(fft_size)/sample_rate)*(1 - overlap_fac)
    
    return time_interval_of_col, result