#!/bin/python
date1=input=open('file.txt','r')
for i in date1:
    file=i.strip('\n')
    file1=str(str("./result/")+i)
    file1=file1.strip('\n')
    input=open(file,'r')
    output=open(file1,'w+')
    for line in input:
        a=':'.join([line[i:i+2] for i in range(0, 12, 2)])
        print a
        output.write(a)
        output.write('\n')
