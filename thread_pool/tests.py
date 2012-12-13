"""
My simple thread Pool creation and task execution.
"""

from Queue import Queue
from nose import tools
from pool import ThreadPool


def simple_handler(output_q, value):
    output_q.put(value)
    output_q.task_done()


def test_if_pool_exists():
    # setup
    output_q = Queue()
    pool = ThreadPool(5)
    input_values = set(range(50))

    # run
    for i in input_values:
        pool.add_task(simple_handler, output_q, i)

    # assert
    output_q.join()
    all_values = set()

    while not output_q.empty():
        all_values.add(output_q.get())

    tools.assert_equals(input_values, all_values)
