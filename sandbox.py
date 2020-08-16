import time


def get_time(func):
    a=time.time()
    func()
    print( time.time()-a)

@get_time
def run_time():
    time.sleep(3)
    string = f'i have slept for {3} seconds'
    return string


x=run_time()
print(x)
