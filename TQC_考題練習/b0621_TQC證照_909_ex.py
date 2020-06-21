f_name = "data.dat"
with open(f_name,'w+') as file:
    for i in range(5):
        user = str(input())
        file.write(user+'\n')
    file.seek(0)
    print('The content of "data.dat":')
    for i in file:
        print(i)