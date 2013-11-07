def PanSort(a):
    n = len(a)
    for k in range(0, n-1):
        print "k =", k
        x = k
        for i in range(k, n):
            if a[i] < a[x]:
                x = i;
        if x == k:
            continue
        print "x =", x
        for i in range(0, x/2+1):
            a[i], a[x-i] = a[x-i], a[i]
        print a
        for i in range(0, (x-k)/2+1):
            a[i], a[x-k-i] = a[x-k-i], a[i]
        print a
        for i in range(0, x/2+1):
            a[i], a[x-i] = a[x-i], a[i]
        print a
        print "=========================="

a = [5, 1, 3, 4, 2, 6, 8, 7]
print a
PanSort(a)
