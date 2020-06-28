import time


def wait_until(predicate, timeout=15, interval=0.2):
    starting_time = time.time()
    number_or_calls = 0
    while 1:
        number_or_calls += 1
        try:
            return predicate()
        except Exception as exception:
            time_spent_waiting = time.time() - starting_time
            if time_spent_waiting < timeout:
                time.sleep(interval)
                continue
            else:
                raise TimeoutError(
                    f"Waited {time_spent_waiting:.2f}s. Timeout is {timeout}s.\n"
                    f"Called the functions {number_or_calls} times but there was still "
                    f"an exception. \n"
                    f"Look above for the stacktrace of the function."
                ) from exception
