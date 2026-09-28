import threading
import multiprocessing
import queue
import time


# =========================================================
# THREADING IMPLEMENTATION
# =========================================================

def threaded_producer(
    q: queue.Queue[int],
    producer_id: int,
    count: int
) -> None:
    for i in range(count):
        item = producer_id * 100 + i
        q.put(item)  # Blocks if queue is full
        print(f"Thread Producer {producer_id}: Produced {item}")
        time.sleep(0.1)


def threaded_consumer(
    q: queue.Queue[int],
    consumer_id: int,
    count: int
) -> None:
    for _ in range(count):
        item = q.get()  # Blocks if queue is empty
        print(f"Thread Consumer {consumer_id}: Consumed {item}")
        q.task_done()
        time.sleep(0.15)


def run_threading() -> None:
    print("\n===== THREADING =====")

    buffer: queue.Queue[int] = queue.Queue(maxsize=5)

    producer = threading.Thread(
        target=threaded_producer,
        args=(buffer, 1, 10)
    )

    consumer = threading.Thread(
        target=threaded_consumer,
        args=(buffer, 1, 10)
    )

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("Threading completed.")


# =========================================================
# MULTIPROCESSING IMPLEMENTATION
# =========================================================

def multiprocessing_producer(
    q: multiprocessing.Queue,
    count: int
) -> None:
    for i in range(count):
        item = i + 1
        q.put(item)
        print(f"Process Producer: Produced {item}")
        time.sleep(0.1)


def multiprocessing_consumer(
    q: multiprocessing.Queue,
    count: int
) -> None:
    for _ in range(count):
        item = q.get()
        print(f"Process Consumer: Consumed {item}")
        time.sleep(0.15)


def run_multiprocessing() -> None:
    print("\n===== MULTIPROCESSING =====")

    buffer: multiprocessing.Queue = multiprocessing.Queue(maxsize=5)

    producer = multiprocessing.Process(
        target=multiprocessing_producer,
        args=(buffer, 10)
    )

    consumer = multiprocessing.Process(
        target=multiprocessing_consumer,
        args=(buffer, 10)
    )

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("Multiprocessing completed.")


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    # Run threading version
    run_threading()

    # Run multiprocessing version
    run_multiprocessing()

    print("\nProducer-Consumer program completed successfully.")