def func():
    a=2
    return  "你是猪"


func()
print(func())

a=1
b=2

try:
    assert a==b
except AssertionError as s:
    print("666")