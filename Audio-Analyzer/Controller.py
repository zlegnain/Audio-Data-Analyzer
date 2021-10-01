from Frontend import Plot2D

"""
Class controller that will handle runnning our application
"""
class Controller:
    def __init__(self):
        self.fe = Plot2D()

    def run(self):
        self.fe.Clock()


if __name__ == '__main__':
    app = Controller()
    app.run()

