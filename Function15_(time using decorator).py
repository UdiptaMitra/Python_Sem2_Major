#time of computation
'''import time
def square():
    l1=[i for i in range(100)]
    return sum(l1)
start_time=time.perf_counter()#performance counter hold starting time instance
square()
end_time=time.perf_counter()
time_taken=end_time-start_time
print(time_taken)'''

import time
def timer(func):
    def wrapper(*args,**kwargs): #so that values are taken and assinged at correct positions
        start_time=time.perf_counter()
        result=func(*args,**kwargs)
        end_time=time.perf_counter()
        print(f"Executed function {func.__name__} in {end_time-start_time}s")
        return result
    return wrapper
@timer
def heavy_comp():
    time.sleep(1.5) #to specify quite a time difference
    return "done"
print(heavy_comp())

@timer
def heavy_comp_add(a,b):
    return a+b
print(heavy_comp_add(5,6))
