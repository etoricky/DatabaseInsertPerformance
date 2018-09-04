import time

class Timer:    
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        elapsed = time.time()-self.start
        print('Imported {} records in {:.2f} seconds or {:.0f} per second'.format(self.size, elapsed, self.size/elapsed))
    def setSize(self, size):
        self.size = size