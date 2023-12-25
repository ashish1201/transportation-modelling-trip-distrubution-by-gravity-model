r=int(input("enter no. of zones"))

#initialize fij matrix

print("**Values for Fi-j matrix")
fij=[]
for i in range(1,r+1):
    l=[]
    for j in range(1,r+1):
        print("enter fij matrix value for trip from %d to %d." % (i,j))
        v=int(input())
        l.append(v)
    fij.append(l)
print("the fij matrix is %s" %fij)
#declare variables
dist=[]

#initialize production matrix

prod=[]
for j in range(1,r+1):
    print("enter production for zone %d ." %j)
    prod.append(int(input()))

#intialize attraction matrix

attr=[]
for j in range(1,r+1):
    print("enter attraction for zone %d ." %j)
    attr.append(int(input()))
attr1=attr.copy()
attrii=attr.copy()
#define distribution matrix*****************************
def distributionmatrix():
    for i in range(0,r):
        l=[]
        for j in range(0,r):
            sum=0
            for k in range (0,r):
                sum=sum+attrii[k]*fij[i][k]
            p=fij[i][j]*prod[i]*attrii[j]/sum
            #print(fij[i][j])
            l.append(p)
        dist.append(l)
    print("\n")
    print(dist)


#distribution matrix for iteration 1:
print("**Iteration 1**")
print("\n The values of distribution matrix are")
distributionmatrix()


#new attraction matrix for next iteration
def cmatrix():
    c=[]
    for i in range(r):
        s1=0
        for j in range(r):
            s1=s1+dist[j][i]
        c.append(s1)
    attr=attrii.copy()
    attrii.clear()
    for j in range(r):
        s1=attr1[j]*attr[j]/c[j]
        attrii.append(s1)
    print("\n")
    print(attrii)
    return attrii
print("\n updated attraction matrix for next iteration for computation purpose\n")
cmatrix()

def sumc():
    sum2=0
    for i in attrii:
        sum2=sum2+i
    print("the sum of attraction is:")
    print(sum2)
q=2
y='y'
def selection():
    global y
    while(y=="y"):
        global q
        j=q
        print("\n*** iteration %d ***\n"%j)
        j=j+1
        q=j
        print("distrbution matrix elements")
        dist.clear()
        distributionmatrix()
        y=input("Do you want another iteration?press y to continue and n to break")
        print("\nupdated attraction matrix for next iteration for computation purpose\n")
        cmatrix()
selection()
print("end")

