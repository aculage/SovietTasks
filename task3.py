import array

def linear_sort(l):
    supportarray = [ 0 for i in range(0, 255)]
    for i in l :
        supportarray[int(i)] += 1
    retstr = []
    for i in range(0, 255) :
        for j in range (0, supportarray[i] ) :
            retstr.append(i)

    return retstr

inp = open('tsk1_input.txt')
l = inp.read().split()
inp.close()

print(l)

l =linear_sort(l)

print(l)