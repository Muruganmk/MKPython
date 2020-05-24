count=int(input("Enter the count"))
inp=input("enter the numbers now")

lt1=inp.split()

if count==len(lt1):
    lt2=[]
    for i in lt1:
        if int(i) not in lt2:
            lt2.append(int(i))
    #print(max(lt2))
    index=lt2.index(max(lt2))
    lt2.pop(index)
    print(max(lt2))
    
    
    
        
'''        
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

list1=[]
for item in arr:
    if item not in list1:
        list1.append(item)

list1.sort()
print(list1[-2])
'''
