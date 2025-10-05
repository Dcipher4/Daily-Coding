def func(a, b):
    b.append(a)
    return b

print(func(1))
#output 1
print(func(2))
# output 1, 2
# but pycharm- shows error

'''similarly'''
def mystery(x=[]):
    x.append("python"
    return x

print(mystery())        # 1st call
print(mystery())        # 2nd call
print(mystery(["laptop"])



def sorcery(spells=["✨"]):
    copied = spells
    copied.append("🧙‍♂️")
    print("Spells:", spells)
    return copied