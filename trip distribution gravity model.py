r=int(input("enter no. of zones"))

#initialize fij matrix

#l matrix to save values for each row of matric before moving onto next row

print("**Values for Fi-j matrix")
fij=[]
kij=[]
for i in range(r):
    l=[]
    for j in range(r):
        print("enter fij matrix value for trip from %d to %d." % (i+1,j+1))
        v=int(input())
        l.append(v)
    fij.append(l)
print("the fij matrix is %s" %fij)

print("\n Are K values 1? press y if yes and any other character if no")
t=input()
if(t=="y"):
    for i in range(r):
        l=[]
        for j in range(r):
            l.append(1)
        kij.append(l)
else:
    for i in range(r):
        l=[]
        for j in range(r):
            print("enter kij matrix value for trip from %d to %d." % (i+1,j+1))
            v=int(input())
            l.append(v)
        kij.append(l)
print("the kij matrix is %s" %kij)
#dist matrix is distribution matrix at end of each iteration
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
#balancing attraction [if needed upto line 65]
print("Check for production attraction balance\n")
sa=0
sp=0
for i in range(len(prod)):
    sp+=prod[i]
for i in range(len(attr)):
    sa+=attr[i]
if(sp==sa):
    print("production and attraction are balanced")
else:
    f=sp/sa
    for i in range(len(attr)):
        attr[i]=round(attr[i]*f,4)
print ("updated attraction matrix is %s\n"%attr)


attr1=attr.copy()
attrii=attr.copy()
#attr1 values are kept constant
#attrii matrix will be used as updated attraction matrix 



#define distribution matrix
#sum is constant part for elements in same row denominatior term

def distributionmatrix():
    for i in range(r):
        l=[]
        #note: we used matrix l earlier. redefining it again here will erase ita value and hence new l is blank matrix
        for j in range(r):
            sum=0
            for k in range (r):
                sum+=attrii[k]*fij[i][k]*kij[i][k]
            p=round(fij[i][j]*kij[i][j]*prod[i]*attrii[j]/sum ,2)
            l.append(p)
        dist.append(l)
    print(dist)


#distribution matrix for iteration 1:
print("**Iteration 1**")
print("\n The values of distribution matrix are\n")
distributionmatrix()


#new attraction matrix for next iteration
def cmatrix():
    c=[]
    for i in range(r):
        s1=0
        for j in range(r):
            s1=s1+dist[j][i]
        c.append(s1)
    #in c matrix we have attraction for each zone i.e. C in actual formula
    attr=attrii.copy()
    attrii.clear()
    for j in range(r):
        s1=attr1[j]*attr[j]/c[j]
        attrii.append(round(s1,3))
    print(attrii)
    #updated attrii matric values by using attr as temp variable.

print("Updated attraction matrix for next iteration for computation purpose")
cmatrix()
q=2
y='y'

#q and y are declared on to print iteration number
#selection matrix is where iterations 2 to n are run by calling required functions
def selection():
    global y
    while(y=="y"):
        global q
        print("\n*** Iteration %d ***\n"%q)
        q+=1
       #upto here is inly about printing iteration number
        print("distrbution matrix elements")
        dist.clear()   
        distributionmatrix()
        y=input("Do you want another iteration?press y to continue and n to break ")
        if(y=="y"):
            print("\nupdated attraction matrix for next iteration for computation purpose")
            cmatrix()
        else:
            print("\nFinal distribution matrix is\n%s\n END"%dist)
        
selection()

