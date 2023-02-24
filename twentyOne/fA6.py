# here we can pass arguments as dictionary
def func(**key):
    print(type(key))
    print(key["name"], key["course"], key["section"])


func(name="rahul", course="B.Tech", section="H")
