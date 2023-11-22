#this easy
def write():
    a = int(input("Next item:"))
    if a == 0:
        return
    elif a % 2 == 1:
        print(a)
        write()
    else:
        write()
write()
#ТЕРМИНАЛ
#Next item:1
#1
#Next item:3
#3
#Next item:5
#5
#Next item:7
#7
#Next item:9
#9
#Next item:0