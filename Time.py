n = 5
a = 0
for i in range(n):
    for j in reversed(range(i, n)):
        a = a + i + j
print(a)



for i in range(n):
    i *= 2
print(1)



def algo(*items):
    print(min(items) + 5)

algo(4, 5, 6, 8, -5, 10, 12)



def dummy_function(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

dummy_function(n)