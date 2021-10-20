#!/usr/bin/env python3

import queue

if __name__ == '__main__':
    Q=queue.Queue(1)
    try:
        item=Q.get_nowait()
    except queue.Empty:
        print("Queue is empty")
    else:
        print(item)

