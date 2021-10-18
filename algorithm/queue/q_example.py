#!/usr/bin/env python3

import queue

if __name__ == '__main__':
    Q=queue.Queue(maxsize=1)
    Q.put(1)
    Q.get()
    print(Q.task_done())

