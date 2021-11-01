import time
import multiprocessing
import psutil


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)')
    time.sleep(seconds)
    print('Done sleeping ...')


if __name__ == "__main__":

    print('CPUs', psutil.cpu_count())
    print('CPUs per sec', psutil.cpu_times_percent(interval=1, percpu=False))

    start = time.perf_counter()

    processes = [multiprocessing.Process(target=do_something, args=[10]) for _ in range(1000)]
    for process in processes:
        process.start()

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
