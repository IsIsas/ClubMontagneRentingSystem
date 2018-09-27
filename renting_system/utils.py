from enum import Enum
from renting_system.model import get_person_code_by_email
from wtforms import ValidationError


def compute_code(name, surname, bday):
    return name[:2] + surname[:2] + str(bday)


class PeopleTypes(Enum):
    COMMITTEE = 1
    EPFL_STUDENT = 2
    UNIL_STUDENT = 3
    EPFL_PHD = 4
    UNIL_PHD = 5






