import psutil

def memory_usage():
    # gives a single float value
    x=psutil.cpu_percent()
    # gives an object with many fields
    y=psutil.virtual_memory()
    # you can convert that object to a dictionary
    z=dict(psutil.virtual_memory()._asdict())
    # you can have the percentage of used RAM
    m=psutil.virtual_memory().percent
    # 79.2
    # # you can calculate percentage of available memory
    n=psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    # 20.8

    return (x,m,n)

#memory_usage()