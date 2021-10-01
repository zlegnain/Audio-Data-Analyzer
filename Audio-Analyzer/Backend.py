import numpy as np
import pyaudio
from scipy.fftpack import fft

"""
class AudioData that will handle the packaging of data from our input
device (Microphone)
"""
class AudioData():

    """
    init constructor that will init a pyaudio object so that we
    can open a stream such that we can begin capturing audio data from our device (microphone)
    """
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 2

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.FORMAT,
            channels = self.CHANNELS,
            rate = self.RATE,
            input = True,
            output = True,
            frames_per_buffer = self.CHUNK
        )

        # this is our x variable
        self.x = np.arange(0, 2*self.CHUNK, 2)





