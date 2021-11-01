import time
import threading

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)')
    time.sleep(seconds)
    print('Done sleeping ...')


threads = [threading.Thread(target=do_something, args=[1]) for _ in range(1000)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
