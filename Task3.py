import time
def decorator_1(function):
    def wrapper(*args,**kwargs):
        starting_time=time.time()
        result=function(*args, **kwargs)
        ending_time=time.time()
        time_of_execution=ending_time-starting_time
        print(f"Calculated execution time for the function is {time_of_execution} seconds")
        return result
    return wrapper
    
@decorator_1
def function1234():
    for i in range(1,10):
        print (i)
        
function1234()