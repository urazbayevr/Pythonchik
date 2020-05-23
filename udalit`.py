from functools import wraps
def glavniy(*types):
    def function(fn):
        @wraps(fn)
        def wrapper(*args,**argv):
            newargs = []
            for i,v in zip(args,types):
                newargs.append(v(i))
            return fn(*newargs,**argv)
        return wrapper
    return function

@glavniy(str,int)
def pechatai(name,value):
    for i in range(value): print(name)
hello = ['minanin','turu','bar','go']
pechatai(hello,5)

coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 'l']
print(list(zip(coordinate,value)))