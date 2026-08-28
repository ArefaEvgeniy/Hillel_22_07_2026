my_dict = {"YYY": 34, 56: 0, 99: "RRR", (1, 2, 3): ["Hello", "World"]}

print(len(my_dict))

print(my_dict[99])
print(my_dict["YYY"])

new_dict = {"name": "Имя", "age": "Возраст", "city": "Город"}

text = "phone"

print(new_dict.get(text, "перевод не найден"))

person = [
    {"age": 25, "city": "New York", "name": "Nick"},
    {"name": "Bob", "age": 30},
    {"name": "Yevhen", "age": 35, "city": "Kyiv"}
]

person_2 = [
    [25, "Nick", "New York"],
    ["Bob", 30],
    ["Yevhen", 35, "Kyiv"]
]

print(person[-1]["name"])
print(person[-1]["city"])
print(person[0]["city"])
print(person[1].get("city", "Данные отсутствуют"))

print(person_2[0][0])
print(person[0].get("name"))
