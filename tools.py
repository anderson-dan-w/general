## all about decorators for function counting, memoizing, tracing, etc
import time
from functools import update_wrapper

def nice_decorator(d):
    def wrap(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(wrap, d)
    return wrap

def makeImmutable(*args, **kwargs):
    argKey = []
    for arg in args:
        if arg.__hash__ is not None:
            argKey.append(arg)
        elif isinstance(arg, dict):
            for k, v in arg.items():
                argKey.append((k, makeImmutable(v)))
        else:
            argKey.append(tuple([makeImmutable(a) for a in arg]))
    for k, v in kwargs.items():
        argKey.append((k, makeImmutable(v)))
    return tuple(argKey)

@nice_decorator
def memo(f):
    cache = {}
    def wrapper(*args, **kwargs):
        argKey = makeImmutable(*args, **kwargs)
        try:
            return cache[argKey]
        except KeyError:
            cache[argKey] = result = f(*args, **kwargs)
            return result
    return wrapper

@nice_decorator
def timeme(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        isTiming = False
        try:
            isTiming = kwargs.pop('timeme')
        except KeyError:
            pass
        result = f(*args, **kwargs)
        if isTiming:
            print("Took {}s".format(time.time() - start))
        return result
    return wrapper

calls = {}
@nice_decorator
def countcalls(f):
    def wrapper(*args, **kwargs):
        calls[wrapper] += 1
        return f(*args, **kwargs)
    calls[wrapper] = 0
    return wrapper
