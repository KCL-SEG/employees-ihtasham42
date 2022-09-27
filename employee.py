"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from tkinter import E


class Employee:
    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        total_pay = 0

        if self.contract["is_monthly"]:
            total_pay += self.contract["pay"]
        else:
            total_pay += self.contract["pay"] * self.contract["hours"]

        if self.commission:
            if self.commission["is_bonus"]:
                total_pay += self.commission["pay"]
            else:
                total_pay += self.commission["pay"] * self.commission["contracts"]

        return total_pay

    def __str__(self):
        description_string = self.name + " works on a "

        if self.contract["is_monthly"]:
            description_string += "monthly salary of " + str(self.contract["pay"])
        else:
            description_string += "contract of " + str(self.contract["hours"]) + " hours at " + str(self.contract["pay"]) + "/hour"

        if self.commission:
            description_string += " and receives a "
            if self.commission["is_bonus"]:
                description_string += "bonus commission of " + str(self.commission["pay"])
            else:
                description_string += "commission for " + str(self.commission["contracts"]) + " contract(s) at " + str(self.commission["pay"]) + "/contract"

        description_string += "."

        total_pay_string = "  Their total pay is " + str(self.get_pay()) + "."

        final_string = description_string + total_pay_string

        return final_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee(
    'Billie',
    {
        "is_monthly": True,
        "pay": 4000
    },
)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee(
    'Charlie',
    {
        "is_monthly": False,
        "pay": 25,
        "hours": 100
    }
)

print(charlie)



# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee(
    'Renee',
    {
        "is_monthly": True,
        "pay": 3000
    },
    {
        "is_bonus": False,
        "pay": 200,
        "contracts": 4
    }
)



# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee(
    'Jan',
    {
        "is_monthly": False,
        "pay": 25,
        "hours": 150
    },
    {
        "is_bonus": False,
        "pay": 220,
        "contracts": 3
    }
)

print(jan)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee(
    'Robbie',
    {
        "is_monthly": True,
        "pay": 2000
    },
    {
        "is_bonus": True,
        "pay": 1500
    }
)

print(robbie)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee(
    'Ariel',
    {
        "is_monthly": False,
        "pay": 30,
        "hours": 120
    },
    {
        "is_bonus": True,
        "pay": 600
    }
)

print(ariel)
