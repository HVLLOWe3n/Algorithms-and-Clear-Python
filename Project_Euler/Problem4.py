l = list()
new_list = list()
two_new_list = list()

temp = 0
val_result_one = 0
val_result_two = 0

for i in range(1, 101):
    l.append(i)

for i in l:
    new_list.append(l[i-1]**2)
    val_result_one += new_list[i-1]

    two_new_list.append(l[i-1])
    temp += two_new_list[i-1]
    val_result_two = temp ** 2


print(val_result_two - val_result_one)

