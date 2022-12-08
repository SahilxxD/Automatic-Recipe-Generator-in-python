
from itertools import count
import copy
from tempfile import tempdir

a = {"apple","banana","cherry","milk"}
b = {"2 teaspoons olive oil","1 (16 ounce) package cold, prepared pizza dough","4 ounces provolone cheese"," diced,¾ cup cooked"," crumbled Italian sausage","½ cup cooked","diced sweet peppers","4 ounces mozzarella cheese","grated, cup prepared pizza sauce","¾ cup freshly grated Parmigiano-Reggiano cheese"}
c = {"apple","banana","salt","sugar","wheat"}

recipies = [a,b,c]
ingridients = input("Enter ingridients U have :").replace(',',"")
ingridients.split()
ingridients = ingridients.split()
print(ingridients)

'''
for x in ingridients:
    if x in a:
        count = count+1
    else: continue
'''

def check_ingredients(recipe,ingrident):
    count = int(0)
    missing = copy.copy(recipe)
    unused  = copy.copy(ingrident)
    for x in ingrident:
            for z in recipe:
                if x in z:
                    count = count+1
                    missing.remove(x)
                    unused.remove(x)
    return count,missing,unused


for x in recipies:
    sorted_list = []
    info = check_ingredients(x,ingridients)
    count= info[0]  
    if count>1:
        list = {count:[]}
        list[count].append(x) 
        

print(list[2])


#count  = check_ingredients(a,ingridients)
#print(count)

3