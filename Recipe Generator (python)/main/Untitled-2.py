from dataclasses import dataclass
from os import remove
import  psycopg2
import  psycopg2.extras

mydb = psycopg2.connect("dbname=RecipeGen user=postgres password=1234")

cursor = mydb.cursor(cursor_factory=psycopg2.extras.DictCursor)
i = 1
names = []
for i in range(10):
    cursor.execute('select * from  public.recipe where "Recipe_id" = %s;',(i,))

    for record in cursor.fetchall():
                print(record)


#print(names)
mydb.close()