f_name,string = input(),input()
with open(f_name,'r') as f:
    r = f.read()
    print("=== Before the deletion")
    print(r)
    r = r.replace(string,"")
    print("=== After the deletion")
    print(r)
with open(f_name,'w') as f:
    f.write(r)
