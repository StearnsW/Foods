import random
import json
food_file=open('foods.txt')
list_of_foods=food_file.read().title().splitlines() # turn list file data into a list   
high_fiber_file=open('highfiber.txt')
list_of_fiber=high_fiber_file.read().title().splitlines() # turn list file data into a list
low_fat_file=open('lowfat.txt')
list_of_fat=low_fat_file.read().title().splitlines() # turn list file data into a list
low_glycemic_index_file=open('low-glycemic-index.txt')
list_of_GI=low_glycemic_index_file.read().title().splitlines() # turn list file data into a list
rows_to_keep=set()

for i in range(len(list_of_foods)):
    if list_of_fat[i]==("Yes " or " Yes"):
        list_of_fat[i]="Yes"
    elif list_of_fat[i]==("No "or" No"):
        list_of_fat[i]="No"
for i in range(len(list_of_foods)):
    if list_of_fiber[i]==("Yes " or " Yes"):
        list_of_fiber[i]="Yes"
    elif list_of_fiber[i]==("No "or" No"):
        list_of_fiber[i]="No"
for i in range(len(list_of_foods)):
    if list_of_GI[i]==("Yes " or " Yes"):
        list_of_GI[i]="Yes"
    elif list_of_GI[i]==("No "or" No"):
        list_of_GI[i]="No"

rows_to_remove={0}
rows_to_review=set()
for i in range(len(list_of_foods)):
    rows_to_keep.add(i)
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

for i in rows_to_review:
    print(f'The following food needs review: {list_of_foods[i]}')
    edit_data = False # boolean for conflict solving
    while not edit_data: # conflict resolution loop
        needs_edit=input('Should this food name be edited, stay the same, or removed? [e/s/r]\n')
        if needs_edit not in {'e','s','r'}: # invalid reply
            print("That wasn't one of the options, please resond only 'e', 's', or 'r'")
        elif needs_edit == 's': # not to edit existing, leave edit conflict loop
            print("This food name shall not be edited or removed.\n")
            edit_data = True
        elif needs_edit == 'e': # want to edit existing, leave edit conflict loop and same name loop, change edit boolean
            new_food_name=input("The new name should be: ")
            edit_data = True
            list_of_foods[i]=new_food_name
        else:
            edit_data = True
            rows_to_remove.add(i)

rows_to_keep=rows_to_keep-rows_to_remove
food_dictionary_list=[]
for i in rows_to_keep:
    food_dictionary={"Food":list_of_foods[i],list_of_fiber[0]:list_of_fiber[i],list_of_fat[0]:list_of_fat[i],list_of_GI[0]:list_of_GI[i]}
    food_dictionary_list.append(food_dictionary)
with open("json_test.json", "w") as outfile:
    json.dump(food_dictionary_list, outfile)    
#json.dump(food_dictionary_list)
    

file=open('other_test.json','w') # open the file to edit
json.dump(food_dictionary_list,file)
file.close()