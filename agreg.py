class personne:
    def __init__(self, nom, tel):
        self.nom = nom
        self.tel = tel

    def __str__(self):
        return f"nom : {self.nom}"


class student:
    def __init__(self, num_student, personne):
        self.num_student = num_student
        self.personne = personne

    def __str__(self):
        return f"num_student : {self.num_student}, personne : {self.personne.nom}, tel : {self.personne.tel}"


alex = personne("Alex", "12345")

print(alex)


alexandrekientz = student("23123123", alex)

print(alexandrekientz)