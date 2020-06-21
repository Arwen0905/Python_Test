f = open("data.txt","a+")
for i in range(5):
    s = str(input())
    f.write('\n'+s)
    f.seek(0)
r = f.read()
f.close()
# TODO

print("Append completed!")
print('Content of "data.txt":')
print(r)
# TODO
