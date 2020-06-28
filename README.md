# wait-until
Allows one to wait until a function returns. Useful for testing web apps.


Signature:
```
wait_until.wait_until(
    predicate: Callable,
    timeout: Union[float, int] = 15, 
    interval: Union[float, int] = 0.2
)
```

Example:

```python
import psycopg2
from wait_until import wait_until


def get_db_connection():
    return psycopg2.connect("dbname=test user=postgres")


db_connection = wait_until(get_db_connection)

# even if the DB is not up when the python script started, it's going to 
# retry calling the function again and again until success for 15s with an interval
# of 0.2s. Will throw a TimeoutError with a proper stacktrace if the timeout is reached.
```
