def average_numbers():
    total = 0
    count = 0
    while True:
        number = yield
        total += number
        count += 1
        print("Average :", total / count)

g= average_numbers()
next(g)

g.send(10)
g.send(20)
g.send(30)
