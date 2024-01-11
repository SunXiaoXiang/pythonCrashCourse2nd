motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles[0]='ducati'
print(motocycles)

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles.append('ducati')
print(motocycles)

motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')
print(motocycles)

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles.insert(0, 'ducati')
print(motocycles)

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
del motocycles[0]
print(motocycles)
del motocycles[1]
print(motocycles)

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

popped_motocycle = motocycles.pop()
print(motocycles)

print(popped_motocycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
