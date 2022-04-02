#it is a collection of value in key pair.

users = {
    "first_name": "chima",
    "last_name":  "offia",
    "profession": "software developer",
    "age":  26,
    "hobbies":  ["coding", "playing game", "football",]
}

print(users)
print(users["first_name"])
print(users["profession"])
print(users["hobbies"][1])


#  creating a list of dictionaries

employers = [
    {
        "first_name": "chima",
        "last_name": "offia",
        "profession": "software engineer"
    },

    {
        "first_name": "mike",
        "last_name": "mat",
        "profession": "software engineer"
    }
]

print(employers)
print(employers[0]["first_name"])


#adding items to a dictionary

workers = {
    "first_name": "chima",
    "last_name": "offia"
}

workers["email"] = "offiahchima@gmail.com"
workers["last_name"] = "johnson"
workers["hobbies"] = ["gaming", "playing chess"]

print(workers["hobbies"][1])

#dictionary method update

workers.update({"last_name":"mike"}) #.update is used to update or add item in the dictionary. 
workers2 = workers.copy()  #copy is another method.
print(workers2)

workers.pop("last_name") #pop means remove
workers.clear() #it clears everything
print(workers.get("nickname", "sorry not found"))  #it same as assessing items in dictionary

