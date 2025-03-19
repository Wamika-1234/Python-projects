import random
when=["A few years ago","Last night", "This morning", "Once upon a time", "There was once a", "Many a year ago", "One day", "At night", "In the afternoon"]
who=[" a girl","a boy","a rabbit","a dog","two girls","two boys"]
name=["Sophie","Wamika","Hermione"]
place=["Abu Dhabi","London","Paris"]
went=["the movies","school","the park"]
happened=["made lot of friends","solved a mystery","wrote a book","got abducted by aliens during a zombie apocalypse"]
print(random.choice(when)+', '+random.choice(who)+' named '+random.choice(name)+' that lived in '+random.choice(place)+', went to '+random.choice(went)+' and '+random.choice(happened))
