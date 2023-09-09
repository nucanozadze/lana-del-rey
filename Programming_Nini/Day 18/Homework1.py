#!

#1

crew_members = ['alexandre Katsarava','dato Jachvadze','dato Mgeladze','davit Janashia','gabriel Gogadze','gabrieli Molodini','giorgi Gelashvili','ilia Wiklauri','muhammedali Mamedov','nini Nozadze','sandro Bochorishvili','sandro Oqropiridze','vano Motiashvili','erekle gochitashvili','lasha wamalaidze','nika chochia']

i_count = 0
superlist = []


for element in crew_members:
    i_count = 0
    for char in element:
        if char == "i":
            i_count += 1

    if i_count > 2:
        superlist.append(element.capitalize())

print(superlist)
