var="""
line1
line2
<start>
MK
KT
MG
<end>
line3
<start>
Sandy
Sai
Chandra
<end>
line4
line5
<start>
Vk
Sabarish
<end>
"""



c=var.count('<start>')
pos=0
while(c>0):
    startpos=var.find('<start>',pos, len(var))
    endpos=var.find('<end>',startpos, len(var))
    mystr=var[startpos+7:endpos]
    print(mystr)
    pos=endpos+5
    c=c-1
