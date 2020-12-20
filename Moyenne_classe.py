classroom = []
finclassroom = 0
compteur = 0
note = []
while finclassroom != -1:
    classs = input("ajoute les nom d'un eleve")
    classroom.append(classs)
    compteur += 1
    print(classroom)
    finclassroom = int(input("Tape -1 pour passer a la suite ou Any Key pour ajouter un eleve"))

for i in range(len(classroom)):
    print(classroom)
    print("Veuillez entrer la note de ", classroom[i])
    note.append(float(input()))




def moyenne():
    return sum(note) / len(note)


def note_max():
    notetrie = sorted(note)
    return notetrie[-1]


def note_min():
    notetrie = sorted(note)
    return notetrie[0]


print("La moyenne des notes est", moyenne())
print("La note minimale est:", note_min())
print("La note maximale est:", note_max())
print("Les eleves sont",classroom)