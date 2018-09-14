def compute_code(name, surname, bday):
    return name[:2] + surname[:2] + str(bday)

student_types = {1: 'committee',
                 2: 'EPFL student',
                 3: 'UNIL student',
                 4: 'EPFL PHD',
                 5: 'UNIL PHD'}