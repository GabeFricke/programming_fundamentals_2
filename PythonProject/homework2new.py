grid = [
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
]
rows= 20
cols= 20
greatest_product= 0
numbers= []
#print(grid[0][0])
for r in range(rows):
    for c in range(cols):
        #hor
        if c + 3 < cols:
            curr_seq = grid[r][c], grid[r][c+1], grid[r][c+2], grid[r][c+3]
            product= grid[r][c]*grid[r][c+1]*grid[r][c+2]*grid[r][c+3]
            if product > greatest_product:
                greatest_product= product
                numbers = curr_seq




        #vert
        if r + 3 < rows:
            cur_seq= grid[r][c],grid[r+1][c],grid[r+2][c],grid[r+3][c]
            product= grid[r][c]*grid[r+1][c]*grid[r+2][c]*grid[r+3][c]
            if product > greatest_product:
                greatest_product= product
                numbers = curr_seq

        if r + 3 < rows and c + 3 < cols:
            curr_seq= grid[r][c],grid[r+1][c+1],grid[r+2][c+2],grid[r+3][c+3]
            product= grid[r][c]*grid[r+1][c+1]*grid[r+2][c+2]*grid[r+3][c+3]
            if product > greatest_product:
                greatest_product= product
                numbers = curr_seq

        if r +3 < rows and c - 3 >= 0:
            cur_seq= grid[r][c],grid[r+1][c-1],grid[r+2][c-2],grid[r+3][c-3]
            product= grid[r][c]*grid[r+1][c-1]*grid[r+2][c-2]*grid[r+3][c-3]
            if product > greatest_product:
                greatest_product= product
                numbers = cur_seq

print(greatest_product)
print(numbers)

print("this is my first commit")

my_string = "I am going to the store"
n = 2
new_string = [w for w in my_string.split() if len(w) == n]
print(new_string)

import random
class character:
    def __init__(self, name, villian = False):
        if villian:
            self.type= random.choice(["Fire Lord Sozin", "Combustion Man", "Princess Azula", "Fire Lord Ozai"])
        else:
            self.type= random.choice(["Air Bender", "Earth Bender", "Fire Bender", "Water Bender", "Avatar", "Non Bender"])

        self.name = name
        if self.type == "Fire Lord Ozai":
            self.attack = random.randint(15,18)
            self.defense = random.randint(5,9)
            self.speed =  random.randint(70,89)
            self.health = random.randint(1,100)
        if self.type == "Combustion Man":
            self.health = random.randint(1,100)
            self.defense = random.randint(4,7)
            self.speed = random.randint(50,80)
            self.attack = random.randint(14,17)
        if self.type == "Princess Azula":
            self.health = random.randint(1,100)
            self.defense = random.randint(3,7)
            self.speed = random.randint(70,90)
            self.attack = random.randint(13,18)
        if self.type == "Fire Lord Sozin":
            self.health = random.randint(1,100)
            self.defense = random.randint(4,8)
            self.speed = random.randint(60,80)
            self.attack = random.randint(13,16)
        if self.type == "Air Bender":
            self.attack = random.randint(8,12)
            self.defense = random.randint(3,6)
            self.health = random.randint(1,100)
            self.speed = random.randint(80,99)
        if self.type == "Earth Bender":
            self.attack = random.randint( 12,15)
            self.defense = random.randint(5,8)
            self.health = random.randint(1,100)
            self.speed = random.randint(50, 75)
        if self. type == "Fire Bender":
            self.attack = random.randint(11,14)
            self.defense = random.randint(4,6)
            self.health = random.randint(1,100)
            self.speed =  random.randint(60,85)
        if self.type == "Water Bender":
            self.attack = random.randint(10,15)
            self.defense = random.randint(5,7)
            self.health = random.randint(1,100)
            self.speed = random.randint(70,89)
        if self.type == "Avatar":
            self.attack = random.randint(15,20)
            self.defense = random.randint(7,10)
            self.health = random.randint(1,100)
            self.speed = random.randint(90,99)
        if self.type == "Non Bender":
            self.attack = random.randint(1, 5)
            self.defense = random.randint(1, 3)
            self.health = random.randint(1,100)
            self.speed = random.randint(30, 50)
        self.level = 1
        self.experience = 0
    def level_up(self):
        self.level += 1
        self.attack += 2
        self.defence += 1.5
        self.health += 3
        self.experience += 10
    def __str__(self):
        return "Name: " + self.name + " " + "Character: " + self.type + " " + "level: " + str(self.level) + " " + "Experience: " + str(self.experience) + " " + "Attack: " + str(self.attack) + " " + "Defense: " + str(self.defense) + " " + "Health: " + str(self.health) +" " + "Speed: " + str(self.speed)

def battle(c1, c2):
    h1 = c1.health
    h2 = c2.health
    print(f"{c1.name} health: {max(h1, 0)}")
    print(f"{c2.name} health: {max(h2, 0)}")
    print("   ")
    while h1 > 0 and h2 > 0:

        damage_to_c2 = max(c1.attack - c2.defense, 0)
        damage_to_c1 = max(c2.attack - c1.defense, 0)

        h2 -= damage_to_c2
        h1 -= damage_to_c1

        print(f"{c1.name} health: {max(h1, 0)}")
        print(f"{c2.name} health: {max(h2, 0)}")
        print("   ")

    if h1 <= 0 and h2 <= 0:
        print("It's a draw!")
    elif h1 > 0:
        print(f"{c1.name} wins!")
    else:
        print(f"{c2.name} wins!")

c1= character("j", True)
c2 = character("k", False)

print(c1)
print(c2)

battle(c1, c2)

