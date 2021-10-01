from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
from numpy import arange, sin, cos, pi
import pyqtgraph as pg
import struct
import sys
from Backend import AudioData


"""
class Plot2d that will iniatilize our window, graph, and plot data

"""
class Plot2D():

    """"
    __init__ constructor that will init our window and graph,
    """
    def __init__(self):
        self.a = AudioData()
        self.traces = dict()
        self.app = QtGui.QApplication([])
        self.win = pg.GraphicsWindow(title="Plotting Audio Input")
        self.win.resize(1000,600)
        self.canvas = self.win.addPlot(title="Waveform")




    """
    start method that will begin our application
    """
    def start(self):
        QtGui.QApplication.instance().exec_()




    """
    plot_data method that will determine our Range of values for X and Y variables,
    also plots our x and y values to the graph
    """
    def plot_data(self, x,y):
        if 'waveform' in self.traces:
            self.traces['waveform'].setData(x,y)
        else:
            self.traces['waveform'] = self.canvas.plot(p='y', width=0.5)
            self.canvas.setYRange(0, 255, padding=0)
            self.canvas.setXRange(0, 2*self.a.CHUNK, padding=0.005)



    """
    the update method will keep unpacking new audio data,
    and then convert that data from binary to integers so that it is
    possible to graph the audio data
    """
    def update(self):
        data = self.a.stream.read(self.a.CHUNK)
        data = struct.unpack(str(2*self.a.CHUNK)+ 'B', data)
        data = np.array(data, dtype='b')[::2] + 128
        self.plot_data(self.a.x, data)



    """
    the Clock method will keep refreshing our graph so that
    there is a continous stream of audio data constantly being plotted
    on the graph
    """
    def Clock(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(20)
        self.start()