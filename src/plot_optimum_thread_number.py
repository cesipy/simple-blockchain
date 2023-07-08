import matplotlib.pyplot as plt
import testing
import time


def main():
    times = []
    threads = list(range(1, 50, 3))

    for num in threads:
        print("num:", num)
        times_in_loop = []
        counter = 0
        while counter < 10:
            start = time.time()
            testing.test_main(num)
            end = time.time()
            times_in_loop.append(end - start)
            counter += 1
        avg = sum(times_in_loop) / 10
        times.append(avg)

    for i in range(len(times)):
        print(f"number of threads: {i + 1}, avg: {times[i]}")

    # Plotting the results
    plt.plot(threads, times)
    plt.xlabel('Number of threads')
    plt.ylabel('Average time')
    plt.title('Average time per number of threads')
    plt.grid(True)
    plt.show()


main()
