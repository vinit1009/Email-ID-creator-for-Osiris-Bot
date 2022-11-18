read = open("break.txt", 'r')
address = read.readlines()

em = open("em.txt", 'w')

pa = open('pw.txt', 'w')


n = int(input("enter the number of gmails: "))
m = 0

for x in range(n):
    m = m+1
    addy = address[m-1]
    add = addy.split(',')
    email = str(add[1]).lower()
    pw = add[2]
    print(email+":::"+pw, file = pa)
    print(email, file = em)
    


read.close()
em.close()
pa.close()