class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name 
        self.payment = payment
        self.amount = amount

    # function to show payment's status
    def  pay(self):
        self.payment = "yes"

    # function to update the status
    def status(self):
         if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
         else:
             return self.name + " is not paid yet"

nathan = Payslips("Nathan", "no", 1000)
roger = Payslips("Roger", "no", 3000)

print(nathan.status(), "\n", roger.status())
# output:
# Nathan is not paid yet 
#  Roger is not paid yet

nathan.pay()
print("After payment")
print(nathan.status(), "\n", roger.status())

# After payment
# Nathan is paid 1000 
#  Roger is not paid yet