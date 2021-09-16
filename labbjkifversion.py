print("Loading the amazing Area calculator app..\nArea calulator app successfully loaded!")
answer = input("press 1 for cube area or 2 for tetrahedron area:")
if answer == "1":
    cube = eval(input("enter cube side in cm:"))
    cubea = cube ** 3
    cubel = cubea / 1000
    print(f"cube area is: {round(cubea, 1)}cm^2 or {round(cubel, 4)}L")
elif answer == "2":
    tetra = eval(input("enter tetra side in cm:"))
    tetraa = tetra ** 3 / (6 * (2 ** 0.5))
    tetral = tetraa / 1000
    print(f"tetra area is: {round(tetraa, 1)}cm^2 or {round(tetral, 4)}L")
else:
    print("hey buddy you gotta give me the right number here!\nTry again when you find the right keys.")
