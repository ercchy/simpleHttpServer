"""
Thread pool.
Based on http://code.activestate.com/recipes/577187-python-thread-pool/
"""

from Queue import Queue
from worker import Worker


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
