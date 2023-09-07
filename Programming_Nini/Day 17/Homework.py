#Day 17
#Homework

#1

import random
crew_leaders = ['Kruashvili', 'amiranashvili', 'tyeshelashvili', 'janezashvili', 'molodini', 'kereselidze', 'kurtanidze']

random1 = random.choice(crew_leaders)
random2 = random.choice(crew_leaders)
random3 = random.choice(crew_leaders)

while random1 == random2 or random1 == random3 or random2 == random3:
    print(random1)
    print(random2)
    print(random3)


#2

crew_members = ['Nozadze', 'janashia','Motiahvili','Tsamalaidze','Katsarava','Mgeladze','Jatchvadze','Gogadze','Gelashvili','Wiklauri','Egvipte','Bochorishvili','Oqropiridze','Gochitashvili','Chochia']

for i in range (3):
    Random = random.choice(crew_members)
    print(Random + " studies hard")


#3

crew_members = ['Nozadze', 'janashia','Motiahvili','Tsamalaidze','Katsarava','Mgeladze','Jatchvadze','Gogadze','Gelashvili','Wiklauri','Egvipte','Bochorishvili','Oqropiridze','Gochitashvili','Chochia']

random1 = random.choice(crew_members)
random2 = random.choice(crew_members)
random3 = random.choice(crew_members)


if random1[-1] == "i":
    print(random1 + " is cool<3")
    print(random2)
    print(random3)

elif random2[-1] == "i":
    print(random1)
    print(random2 + " is cool<3")
    print(random3)

elif random3[-1] == "i":
    print(random1)
    print(random2)
    print(random3 + " is cool<3")

else:
    print(random1)
    print(random2)
    print(random3)
