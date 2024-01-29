#Файл содержит числа и буквы. Каждый записан в отдельной строке.
#Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию, а потом слова по возрастанию их длины.
lst1=[]
lst2=[]
with open('file.txt','r') as file:
     for line in file:
         #line=line[:-1]
         line=line.strip('\n')
         print(line)
         if line.isalpha():
             lst1.append(line)
         else:
             lst2.append(int(line))
print(sorted(lst2)+sorted(lst1,key=len))