def deco(func):
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        x = [i.upper() for i in f if type(i) == str]
        return x
    return wrapper


@deco
def uppercase(*args, **kwargs):
    return [i for i in args] + [j for j in kwargs.values()]


print(uppercase(1, 'sampletext', 'SampleText2', t1='SAMPLETEXT3', t2='sampleText4'))
