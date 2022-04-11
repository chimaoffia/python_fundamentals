
staffs = [
    {
       "first_name": "chima",
        "last_name": "offia",
        "profession": "software engineer"
    },
    {
        "first_name" : "christian",
        "last_name" : "nnamani",
        "hobbies"  : ["hating chelsea","football", "accounting"]
    },
    {
        "first_name": "tochi",
        "last_name" : "ani",
        "hobbies" : ["music","football","crypto"]
    },

    {
        "first_name": "vincent",
        "last_name": "offia",
        "profession": "business"
    }
]

staffs[0]["email"] = "offiahchima@gmail"
print(staffs[0])

print(staffs)
print(staffs[0]["first_name"])


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

workers.update({"last_name":"mike"})
workers2 = workers.copy()
print(workers2)

workers.pop("last_name")
workers.clear()
print(workers.get("nickname", "sorry not found"))


