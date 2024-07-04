# Databricks notebook source
my_Dic = {"name":"Nagarjuna","Phone_number":"78888233","city":"hyd"}
print(my_Dic)
print(my_Dic['name'])
print(my_Dic.get('Phone_number'))
print(my_Dic.get('village'))
#print(my_Dic['village'])
#print(my_Dic)
#my_Dic.clear()
print(my_Dic)

my_Dic['three']= 3

my_Dic.update()

print(my_Dic)
print(my_Dic.keys())



# COMMAND ----------

# DBTITLE 1,DICTIONARY FUNCTIONS
print(my_Dic.keys())
print(my_Dic.values())
print(my_Dic.items())
# print(my_Dic.pop('three'))
print(my_Dic)


y = my_Dic.copy()
print(y)

print(id(y), id(my_Dic))

my_new_dic = my_Dic.update({"four": 4})

print(my_Dic.keys())

new_dic = {"village": "lrp"}
my_Dic.update(new_dic)
print(my_Dic)

# COMMAND ----------

print(my_Dic)
#Remove_item = my_Dic.popitem()
#print(Remove_item)


# COMMAND ----------

setA = {"a", "b", "c", "d", "e", "f"}
setB = {"a", "b", "c", "1", "2", "3"}
print(setA.union(setB))
print(setA.intersection(setB))
print(setA.difference(setB))
print(setB.difference(setA))
print(setA.symmetric_difference(setB))
print(setA.issubset(setB))
print(setA.issuperset(setB))
print(setA.isdisjoint(setB))
#print(setA.pop())


# COMMAND ----------

x=[10,20,30]
y='something'
print(type(x))
print(type(y))
print(type(x) is type(y))
print(type(x) is not type(y))
print(10 in x)


# COMMAND ----------

even_no = [0,2,4,6,8]
usr_input = input("enter the even number : ")

if usr_input in even_no:
    print("invalid list")
else:
    print("valid list")


# COMMAND ----------

usr_string = input("enter title name: ")
usr_conf = input("enter the user confirmation(yes/no): ")
print(usr_string.title())
if usr_conf is 'yes':
    print(usr_string.title())
else:
    print("usr_string")
