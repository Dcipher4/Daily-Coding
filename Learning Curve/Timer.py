import time

userinput4 = int(input("NO. of days: "))
userinput1 = int(input("NO. of hours: "))
userinput2 = int(input("NO. of mins: "))
userinput3 = int(input("NO. of secs: "))

x = 60 * 60
y = 60
w = 24 * 60 * 60

z = (userinput4 * w) + (userinput1 * x) + (userinput2 * y) + userinput3

def countdown(seconds):
    while seconds:
        days, remainder = divmod(seconds, w)
        hours, remainder = divmod(remainder, x)
        mins, secs = divmod(remainder, y)
        timer = f'{days:02d}:{hours:02d}:{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("time's up")

countdown(z)
