import time


def retry(*exceptions):
    """
    Retry Decorator
    Retries the wrapped function/method `times` times if the exceptions listed in exceptions raise
    """

    def decorator(func):
        def newfn(*args, **kwargs):
            attempt = 0
            while attempt < 5:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    time.sleep(attempt)
                    attempt += 1
            return func(*args, **kwargs)

        return newfn

    return decorator
