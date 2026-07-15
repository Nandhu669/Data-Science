# #Dynamic Shopping list
# shop = [input("Enter three items: ")]
# print(shop)
# print(shop.pop(1))
# print(shop)

# #Geo-Coordinate Lock
# geo = [10,20]
# print("lat:",geo[0])
# print("long:",geo[1])

# #High/Low Temp Analyzer
# temp = [20,30,45,65,53,23,15]
# e = len(temp)
# print(min(temp))
# print(max(temp))
# average  = sum(temp) / e 
# print(average)

# #Student Grade Matrix
# grades = [("Bob", 85), ("Alice", 92), ("David", 78), ("Charlie", 90)]
# grades.sort()
# print(grades)

# #Parallel List Zipping
# ids = ["P101", "P102", "P103"]
# prices = [49.99, 19.99, 89.50]
# product_pairs = tuple(zip(ids, prices))
# print(product_pairs)

# #Matrix Flattening
# grid = [[255, 255], [0, 0], [128, 128]]
# flat_grid = [pixel for sublist in grid for pixel in sublist]
# print(flat_grid)

# #Immutable Database Mocking with only tuple
# db_mock = (
#     (1, "Alice", ("Kannur", "Kerala")),
#     (2, "Bob", ("Kochi","Kerala"))
# )
# target_id = 1
# old_addr = "Kannur"
# new_addr = "Trivandrum"
# updated_db = tuple(
#     (u_id, name, tuple(new_addr if a == old_addr else a for a in addrs))
#     if u_id == target_id else (u_id, name, addrs)
#     for u_id, name, addrs in db_mock
# )
# print(updated_db)
# #Immutable Database Mocking With tuple in list 
# db_mock = (
#     (1, "Alice", ["Kannur", "Kerala"]),
#     (2, "Bob", ["Kochi","Kerala"])
# )
# db_mock[0][2][0] = "Trivandrum"
# print(db_mock)

