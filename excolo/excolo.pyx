import time

def main() -> None:
    cdef float start = time.time()
    cdef int j = 1
    for i in range(1, 100):
        for k in range(1, 1000):
            for x in range(1, 1000):
                j += 1
    cdef float end = time.time()
    print(f"number: {j}, took {end-start} seconds")
