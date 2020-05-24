import os


print(os.getcwd())
os.chdir(r'c:\temp')
print(os.getcwd())


for x in os.listdir():
    print(x)

#os.mkdir(r'c:\temp\MKTest3')
os.makedirs(r'c:\temp\MKTest5\Test')
