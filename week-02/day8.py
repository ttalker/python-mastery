import time

registry = []   
def register(func):   
    print(f'running register({func})')   
    registry.append(func)   
    return func
   
@register   
def f1(): 
    print('running f1()')
    
@register 
def f2(): 
    print('running f2()') 
    
def f3():  
    print('running f3()')

def main():   
    print('running main()') 
    print('registry ->', registry) 
    f1() 
    f2() 
    f3()


# @timer (execution time), 

def timer(func):
    def wrapper(*args, **kwargs):
        
        start = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        end = time.perf_counter()

       
        elapsed = (end - start) * 1000

        print(
            f"{func.__name__} took "
            f"{elapsed:.2f} ms"
        )
        
        return result
    return wrapper


# example of this
@timer
def example1(n):
    list = []
    for i in range(n):
        list.append(i)

example1(10000000)
# @retry(n) (retries on exception, parametrized),

def retry(n):
    
    def decorator(func):
        def wrapper(*args, **kwargs):
        
            for attempt in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt+=1
                    print(f"This func has failed {attempt} times")
                    
            raise RuntimeError(
                f"Failed after {n} retries"
            )
        return wrapper
    return decorator

count = 0

@retry(15)
def example2():
    global count
    count += 1
    if count < 8:
        raise ValueError("temporary failure")
    
    return "success"
            
print(example2())


# @cache (memoize without functools.lru_cache).


if __name__ == '__main__': 
    main()