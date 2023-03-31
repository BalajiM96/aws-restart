import re

file = open("preproinsulin-seq.txt").read()
newStr = re.sub("[^a-z]","", file)
open("preproinsulin-seq-clean.txt", "w").write(newStr)

file1 = open("preproinsulin-seq-clean.txt").read()
newStr1 = file1[0:24]
open("lsinsulin-seq-clean.txt", "w").write(newStr1)

newStr2= file1[24:54]
open("binsulin-seq-clean.txt", "w").write(newStr2)

newStr3= file1[54:89]
open("cinsulin-seq-clean.txt", "w").write(newStr3)

newStr4= file1[89:110]
open("ainsulin-seq-clean.txt", "w").write(newStr4)