i= int(input("rows:-"))
k=i
k=2*i-2
for i in range(1,i+1):
    for j in range(1,k):
        print(end=' ')
    k=k-2
    for j in range(0,2*i-1):
        print(i, end=' ')
    print('')
print("\n")


i= int(input("rows:-"))
k=i
k=2*i-2
lastEvenNumber = 2*i
evenNumber = lastEvenNumber
for i in range(1,i+1):
    evenNumber = lastEvenNumber
    k=k-2
    for j in range(i):
        print(evenNumber, end = '')
        evenNumber -=2
    print("\r")