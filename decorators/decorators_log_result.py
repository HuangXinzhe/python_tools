def log_results(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("results.log", "a") as log_file:
            log_file.write(f"{func.__name__} - Result: {result}\n")
        return result
    return wrapper

@log_results
def calculate_metrics(data):
    # Your metric calculation code here
    pass