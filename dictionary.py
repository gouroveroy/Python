person = {"name": "John", "age": 30, "city": "New York", "email": "john@example.com"}

# print(person)
# print(person.keys())
# print(person.values())
# print(person.items())
# print(person.get("gender", "Male"))

person.update({"age": 22, "gender": "Male"})
print(person)
# print(person.pop("country", "India"))
# print(person.popitem())
person.update(dict.fromkeys(["isMarried"], False))
person.update(dict.fromkeys(["isStudent"], True))
print(person)