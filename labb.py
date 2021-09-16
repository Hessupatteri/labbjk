#Labb JK
#calculator that takes input from user in order to calculate area(V) and amount(L) for a cube and a tetrahedron

#eval() automagically converts user string input to int or float.
cube_length = eval(input("I will calculate the area of a cube and a tetrahedron for you, please insert the length of a side: "))

#calculates area for cube and tetrahedron based on user input previously,
result_cube = cube_length ** 3
result_tetrahedron = ((cube_length ** 3) / (6 * (2 ** 0.5)))

#converts the resulting area into Litres.
result_cube_inlitres = result_cube / 1000
result_tetrahedron_inlitres = result_tetrahedron / 1000


print(f"area for cube: {result_cube} cm^2 or {result_cube_inlitres} L\narea for tetrahedron: {result_tetrahedron} cm^2 or {result_tetrahedron_inlitres} L.")