import re
allinform=re.findall("hi","hi Dharanees, Hi Tamizheesh, hi Magizhini")
for eachhi in allinform:
    print(eachhi)




'''
list1=['india','china','England']
res=list1.append('France')
print(list1)
res1=list1.pop(1)
print(list1)
res2=list1.insert(2,'Japan')
print(list1)



set1={'india','china','England'}
print(set1)
res3=set1.add('USA')
print(set1)
res4=set1.pop()
print(set1)
'''




'''
email=input("Enter your Email address:")
if(email.endswith('@live.com')):
    emailsplit=email.split('@')
    print("Your email account is:", emailsplit[1])



var="hi python hello python bye python"
# no of python
res=var.count('python')
pos=0
while(res>0):
    op=var.find('python',pos,len(var))
    print(op)
    print(var[3:9])
    pos=op+1
    res-=1
'''


'''
# no of python
res1=var.count('<start>')
res2=var.count('<end>')
pos=0

while(res1>0):
    #op=var.find('<start>',pos,len(var))
    op=var.find('<start>',pos,len(var))
    op1=var.find('<end>',pos,len(var))
    #print(var[op+8:op1])
    print(var[op+8:op1])
    #print(var[49:op1])
    #print(var[96:op1])
    pos=op+1
    res1-=1
    res2-=1

count=1
res2=var.count('<end>')
my_split=var.split('<start>')
while(count<=res2):
    print(my_split[3])
    count+=1



"""
'''
