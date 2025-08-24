Thappu_list=[]
while True:

    task=input("Enter a task?")
    if task=='stop':
        break
    else:
        Thappu_list.append(task)
print(Thappu_list)
for x in Thappu_list:
  print(x)