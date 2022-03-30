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