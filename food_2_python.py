# importing the module
import json
 
# Opening JSON file
with open('other_test.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))

recommended_foods=set()
count_of_good_foods=0
for i in range(len(data)):
    if data[i]['High Fiber']=='Yes' and data[i]['Low Fat']=='Yes' and data[i]["Low Glycemic Index"]=="Yes":
        count_of_good_foods+=1
        recommended_foods.add(data[i]["Food"])
print(len(data))
print(f"There are {count_of_good_foods} foods with High Fiber, Low Fat, and a Low Glycemic Index.")
print(f"This represents {(count_of_good_foods*100)/len(data)} % of the overall list.")
print(f"The good foods are: {recommended_foods}")
