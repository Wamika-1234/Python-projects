a=str(input("Enter a phrase"))
text=a.split()
#print(text)
acronym=""
for i in text:
    #print(i[0].upper())
    acronym=acronym+(i[0].upper())
print(acronym)