n = int(input())
l = {'Icosahedron': 20, 'Cube': 6, 'Tetrahedron': 4, 'Dodecahedron': 12, 'Octahedron': 8}
c=0
for _ in range(n):
    e = input()
    c = c+ l[e]

print(c)
    
