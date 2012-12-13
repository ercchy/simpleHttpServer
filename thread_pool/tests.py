"""
My simple thread Pool creation and task execution.
"""
from Queue import Queue
from nose import tools
from time import sleep
from thread_pool import ThreadPool


def wait_delay(d):
    print 'sleeping for (%d)sec' % d
    sleep(d)

def test_if_pool_exists():
    # setup
    pool = ThreadPool(3)

    #pool.add_task(wait_delay(0.01))

    # assert
    tools.assert_false(pool.tasks.empty)