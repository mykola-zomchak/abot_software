from threading import  *

def func1():
  for i in range(100):
    print("1")

t = Thread(target=func1)
t.start()
print("2")