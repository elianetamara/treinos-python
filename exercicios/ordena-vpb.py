def ordena_vpb(l):
    for i in range(1, len(l)-1):
        if l[i] < l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
        if l[i] > l[i+1]:
            l[i], l[i-1] = l[i-1], l[i]

l = ['b', 'v', 'v', 'p', 'b', 'v', 'b']
assert ordena_vpb(l) == None
print(l)

l2 = ['p', 'b', 'v']
assert ordena_vpb(l2) == None
print(l2)
