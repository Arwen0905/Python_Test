data = []
with open("read.txt","r") as file:
    r = file.readlines()
    for i in r:
        print(i)
        i = i.strip('\n').split()
        data.append(i)
name = [data[x][0] for x in range(3)]
height = [int(data[x][1]) for x in range(3)]
width = [int(data[x][2]) for x in range(3)]
print('Average height: %.2f'%(sum(height)/3))
print('Average weight: %.2f'%(sum(width)/3))
print('The tallest is %s with %.2fcm'%(name[height.index(max(height))],max(height)))
print('The heaviest is %s with %.2fkg'%(name[width.index(max(width))],max(width)))

