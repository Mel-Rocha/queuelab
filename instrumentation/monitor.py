import time

class PerformanceMonitor:
    @staticmethod
    def measure(func, *args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        return {
            "result": result,
            "time": end - start,
        }
