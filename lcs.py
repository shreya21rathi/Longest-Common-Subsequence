def lcs(a, b):
    matrix=[]
    max=0
    for i in range(len(a)+1):
        d=[]
        for j in range(len(b)+1):
            if i==0 or j==0:
                d.append('0H')
            else:
                if a[i-1] != b[j-1]:
                    t=matrix[i-1][j]
                    v=d[j-1]
                    if int(t[:-1])>=int(v[:-1]):
                        d.append('{0}U'.format(t[:-1]))
                    else:
                        d.append('{0}S'.format(v[:-1]))
                else:
                    u=matrix[i - 1][j - 1]
                    d.append('{0}D'.format(str(int(u[:-1]) + 1)))
                    if max<int(u[:-1]) + 1:
                        max=int(u[:-1]) + 1
        matrix.append(d)
    return matrix,int(max)

list=[]
def print_lcs(a,c,i,j):
    x=c[i][j]
    global list
    if i==0 or j==0:
        print("".join(list[::-1]))
        return list
    if x[-1]=='D':
        list.append(a[i-1])
        print_lcs(a,c,i-1,j-1)
    elif x[-1]=='U':
        print_lcs(a,c,i-1,j)
    else:
        print_lcs(a,c,i,j-1)

a=input("Enter 1st string:")
b=input("Enter 2nd string:")
matrix,length=lcs(a,b)
#-----------Print matrix----------
for i in range(len(a)+1):
    for j in range(len(b)+1):
        print(matrix[i][j]+" ",end="")
    print()
#---------------------------------
print("Lenth of longest common subsequence is:",length)
print_lcs(a,matrix,len(a),len(b))
q=max(len(a),len(b))
percent=((q-length)/q)*100
print("Percent difference is: %.2f"%percent,"%")
if percent>7:
    print("Signature mismatch")
else:
    print("Signature matched")