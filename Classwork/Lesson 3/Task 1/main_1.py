list_of_words = ["qwe", "asd", "zxc", "qwe", "ertqwe"]

value = "qwe"
j = 0

for i in range(len(list_of_words)):
    if list_of_words[i] == value:
        j += 1
    if j == 2:
        print(i)
        break
else:
    print(-1)