# # TODO
def compute(a,b,c):
    # delta = ''
    ans = b**2 - 4 * a * c
    if ans < 0:
        return 'Your equation has no root.'
    elif ans == 0:
        return -b / (2*a)
    elif ans > 0:
        res1 = (-b + ans**0.5) / (2*a)
        res2 = (-b - ans**0.5) / (2*a)
        return str(res1)+', '+str(res2)

a = eval(input())
b = eval(input())
c = eval(input())
print(compute(a,b,c))

"""
Your equation has no root.
"""
