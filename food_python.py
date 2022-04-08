import random
food_file=open('foods.txt')
list_of_foods=food_file.read().title().splitlines() # turn list file data into a list   
high_fiber_file=open('highfiber.txt')
list_of_fiber=list(high_fiber_file.read().title().splitlines()) # turn list file data into a list
low_fat_file=open('lowfat.txt')
list_of_fat=list(low_fat_file.read().title().splitlines()) # turn list file data into a list
low_glycemic_index_file=open('low-glycemic-index.txt')
list_of_GI=list(low_glycemic_index_file.read().title().splitlines()) # turn list file data into a list
print(list_of_foods)
rows_to_remove=set()
rows_to_review=set()
for i in range(len(list_of_foods)):
    if list_of_foods[i]=="":
        rows_to_remove.add(i)
    if not list_of_foods[i].isalpha():
        no_space=list_of_foods[i].split()
        for word in no_space:
            if not word.isalpha():
                rows_to_review.add(i)
    for j in range(i+1,len(list_of_foods)):
        if list_of_foods[i]==list_of_foods[j]:
            rows_to_remove.add(j)
print(rows_to_remove)
print(rows_to_review)
