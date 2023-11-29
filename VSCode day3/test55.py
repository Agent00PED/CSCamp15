# list3=[]
# start=1
# while True:
#     string=input(f"Input {start} : ")
#     if string=="done"or string=="":
#         print("list3 :",list3)
#         break

#     list3.append(string)
#     start+=1

# for i in range(0,len(list3)):
#         print(list3[i],i+1)

#--------------------------------------------

list4=[]
start=1
dic={}
while True:
    string=input(f"Input {start} : ")
    if string=="done"or string=="":
        # print("list4 :",list4)
        list5=list4
        break

    list4.append(string)
    start+=1

while len(list4)!=0:
    count=0
    A=list4[0]
    for i in range(len(list4)):
        if list4[i]==A:
            count+=1

    # print(A,count)
    dic[A]=count
    while A in list4:
        list4.remove(A)

dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
# print(dic)

for i in dic:
    print(i)