from Queue import Queue
from threading import Thread


class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()

            try:
                func(*args, **kargs)
            except Exception, e:
                print e

            self.tasks.task_done()


class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)

        for i in range(num_threads):
            Worker(self.tasks)

    def __str__(self):
        return 'Thread Pool tasks: %s' % self.tasks

    def add_task(self, function, *args, **kwargs):
        self.tasks.put((function, args, kwargs))

    def wait_completion(self):
        self.tasks.join()