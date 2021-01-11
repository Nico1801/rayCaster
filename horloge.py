import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    n = 0
    while n < 20:
        n += 1
        time.sleep(1)
        print(f"chrono thread {n}")
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    formatT = "%(asctime)s: %(message)s"
    logging.basicConfig(format=formatT, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    p = 0
    while p < 20:
        p += 1
        time.sleep(0.5)
        print(f"chrono prog {p}")
    x.join()
    logging.info("Main    : all done")
