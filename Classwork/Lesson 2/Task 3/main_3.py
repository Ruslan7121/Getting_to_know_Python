s1 = "qwertyuiababaopasdfghj"
s2 = "aba"
def f(a, b):
    count = 0
    for i in range(len(a) - len(b)):
        print('->>', a[i:i + len(b)])
        if b == a[i:i + len(b)]:
            count += 1
    return count
print(f(s1, s2))