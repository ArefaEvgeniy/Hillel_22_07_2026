from collections import namedtuple


plane_1 = ("Boeing", 747, 2010, 343, "U-RTYFS")
plane_2 = ("Airbus", 380, 2015, 253, "A556-T")
plane_3 = ("Embraer", 490, 2018, 100, "E-RTYF")

plane_1_1 = {"name": "Boeing", "number": 747, "year": 2010, "sits": 343, "sign": "U-RTYFS"}
plane_1_2 = {"name": "Airbus", "number": 380, "year": 2015, "sits": 253, "sign": "A556-T"}
plane_1_3 = {"name": "Embraer", "number": 490, "year": 2018, "sits": 100, "sign": "E-RTYF"}
print(plane_1_3["sits"])

planes = [plane_1, plane_2, plane_3]

print("-" * 20)
for plane in planes:
    if plane[2] > 250:
        print(plane[4])


Plain = namedtuple('Plain', 'name number year sits sign')

plane_2_1 = Plain("Boeing", 747, 2010, 343, "U-RTYFS")
plane_2_2 = Plain("Airbus", 380, 2015, 253, "A556-T")
plane_2_3 = Plain("Embraer", 490, 2018, 100, "E-RTYF")

planes_2 = [plane_2_1, plane_2_2, plane_2_3]

print("-" * 20)
for plane in planes_2:
    if plane.sits > 250:
        print(plane.sign)
