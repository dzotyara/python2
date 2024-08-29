calls = 0
a = str(input("Введите строку "))
list = ['хаха, хехе, хохо']
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    z = len(string)
    x = string.upper()
    c = string.lower()
    a = (z, x, c)
    return a

def is_contains(a,b):
    count_calls()
    a.upper()
    for n in b:
        n.upper()
        if a in n:
            return True
        else:
            return False

print(is_contains(a, list))
print(string_info(a))
print(calls)
