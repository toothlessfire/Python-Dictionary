"""Dictionaries are data stuctures
you can define your own indices
index/key (e.g. "year") and value (e.g. "person of the year") pairs are stored in dictionaries
"""

filedict = {"2015":"Obama", "2016":"Clinton", "2017":"Trump"}
#print(filedict["2019"]) #key doesn't exist: KeyError: '2019'
print(filedict["2016"])

keyList = list(filedict.keys())

print(keyList)

for i in keyList:
    print(filedict[i])
#additional properties of dictionary

empty = {}
print(empty)

dull = {"1":"", "2":""}
print(dull["1"])

food = {"ham" : ["bad", "good"], "egg" : "good", "spam" : "bad", "banana":"good" }
#create a program to ask user for food and print preference

#uentry = input("enter your food, and I will tell you if it is good or not")
#print(food[uentry])

#enter the value, and find all matching keys 

#add value-key valie

print(food["egg"])
food["egg"] = "bad"
print(food["egg"])

food["bread"] = ["high sugar", "low fat"]
print(food)

del food["banana"]
print(food)

print(len(food))

#d2 = {[1,2,3]:"abc", 3.14:"abc"}
#cannot have mutable keys

d2 = {(1,2,3) : "abc", 3.14:"abc"}
print(d2[(1,2,3)])
print(d2[3.14])
if 3.1415 in d2:
    print("key exists")
else:
    print("key doesn't exist")
    
words = {}
words["animal"] = "sound"
words["cat"] = "meow"
words["dog"] = "woof"
words["tiger"] = "grrr"
words["snake"] = "hiss"
animals = words.keys()
csv = open("C:\\Users\\AJDandFamily\\python class 2\\DictionaryFunctions\\thing.csv","w")
for key in animals:
    csv.write(str(key)+", "+str(words[key]+"\n"))
csv.close()
csv = open("C:\\Users\\AJDandFamily\\python class 2\\DictionaryFunctions\\thing.csv","r")
csvcontent = csv.read()
print(csvcontent)

w1 = {"house":"Haus","cat":"Katze","red":"rot"}
w2 = {"red":"rouge","blue":"bleu"}
#print(w2)
#w2 = w1.copy()
#print(w2)

w2.update(w1)
#print(w2)

#for k in w2:
 #   print(k + " " + )
    
randomdict = {"a":"12","b":"13","c":"14"}
randomdictk = randomdict.keys()
randomdictv = []
for key in randomdictk:
    randomdictv.append(randomdict[key])
print(randomdictk)
print(randomdictv)
# write in own functions