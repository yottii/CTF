flag = "picoCTF{w1{1wq8a8_g/fb6}"
flag_list = list(flag)
print(flag_list)
list = []
for i in range(8,22):
    if(i&1):
        print("ok",+i-2)
        list.append(i-2)
    else:
        print("no",+i+5)
        list.append(i+5)

for j in list:
    print(flag[j])
