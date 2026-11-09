import station, defaulte_bicikle, electro_bicikle, user, admin

station1 = station.Station(1)
print("station1 was created" )
station2 = station.Station(2)
print("station2 was created")

bike1 = electro_bicikle.Electro_bicikle(1)
print("electro_bike was created with number 1")
bike2 = defaulte_bicikle.Default_bicikle(2)
print("defaulte_bicikle was created with number 2")
bike3 = defaulte_bicikle.Default_bicikle(3)
print("defaulte_bicikle was created with number 3")
bike4 = electro_bicikle.Electro_bicikle(4)
print("electro_bicikle was created with number 4")
bike5 = defaulte_bicikle.Default_bicikle(5)
print("defaulte_bicikle was created with number 5")

station1.add_bicikle(bike1)
station1.add_bicikle(bike2)
station2.add_bicikle(bike3)
station2.add_bicikle(bike4)
station2.add_bicikle(bike5)

for i in station1.get_bicikles():
    print(f"{i.get_number()} in station 1")

for i in station2.get_bicikles():
    print(f"{i.get_number()} in station 2")

user1 = user.Client("A", 100)
print(f"user {user1.get_name()} was created, balance: {user1.get_balance()}")
user2 = user.Client("B", 50)
print(f"user {user2.get_name()} was created, balance: {user2.get_balance()}")

print("trip 1")
station1.rent_bicikle(bike1, user1)
print(f"user {user1.get_name()} rented bicikle {bike1.get_number()} at station 1")
station2.receive_bicikle(bike1, user1, 5)
print(f"user {user1.get_name()} returned bicikle {bike1.get_number()} at station 2 after 5 minutes, balance: {user1.get_balance()}")

print("trip 2")
station2.rent_bicikle(bike4, user2)
print(f"user {user2.get_name()} rented bicikle {bike4.get_number()} at station 2")
station1.receive_bicikle(bike4, user2, 4)
print(f"user {user2.get_name()} returned bicikle {bike4.get_number()} at station 1 after 4 minutes, balance: {user2.get_balance()}")

print("trip 3")
station1.rent_bicikle(bike2, user1)
print(f"user {user1.get_name()} rented bicikle {bike2.get_number()} at station 1")
station2.receive_bicikle(bike2, user1, 10)
print(f"user {user1.get_name()} returned bicikle {bike2.get_number()} at station 2 after 10 minutes, balance: {user1.get_balance()}")

print("bicikles in stations after trips:")
print(f"station 1 has {len(station1.get_bicikles())} bicikles")
print(f"station 2 has {len(station2.get_bicikles())} bicikles")

for i in station2.get_bicikles():
    print(f"{i.get_number()} in station 2")

print("try to rent bicikle at station 1, where no bicikles left")
try:
    station1.rent_bicikle(bike1, user1)
except ValueError:
    pass

print("balances after trips:")
print(f"user {user1.get_name()}, balance: {user1.get_balance()}")
print(f"user {user2.get_name()}, balance: {user2.get_balance()}")

admin1 = admin.Admin("Admin", 0)
print(f"admin {admin1.get_name()} was created")
print(f"station 1 has {len(station1.get_bicikles())} bicikles")
print(f"station 2 has {len(station2.get_bicikles())} bicikles")
print(f"network earned: {station1.get_total_profit(admin1)}")