import time
"""
    时间装饰器
        获取函数执行时间
"""
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute.")
        return result
    return wrapper


@timer
def add_number(x, y):
    sum = x + y 
    return sum

if __name__ == "__main__":
    print(add_number(1, 1))