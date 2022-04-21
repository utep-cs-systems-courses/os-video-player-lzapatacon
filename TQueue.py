import threading

class TQueue:
    def _init_(self):
        self.queue = []
        self.q_lock = threading.Lock()
        self.full = threading.Semaphore(0)
        self.empty = threading.Semaphore(10)
                                                          #sus
    def dequeue(self):
        self.full.aquire()
        self.q_lock.aquire()
        val = self.queue.pop(0)
        self.q_lock.release()
        self.empty.release()
        return val

    def enqueue (self, val):
        self.empty.acquire()
        self.q_lock.acquire()
        self.queue.append(val)
        self.q_lock.release()
        self.full.release()

    
