class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def show(self):
        print(f"Result is: {self.numerator}/{self.denominator}")
    
    def SUM(self, franc_2):
        result = fraction(None, None)
        if self.denominator == franc_2.denominator:
            result.numerator = self.numerator + franc_2.numerator
            result.denominator = self.denominator
            return result
        
        else:
            result.numerator = (self.numerator * franc_2.denominator) + (franc_2.numerator * self.denominator)
            result.denominator = self.denominator * franc_2.denominator
            return result

    def Submission(self, franc_2):
        result = fraction(None, None)
        if self.denominator == franc_2.denominator:
            result.numerator = self.numerator - franc_2.numerator
            result.denominator = self.denominator
            return result

        else:
            result.numerator = (self.numerator * franc_2.denominator) - (franc_2.numerator * self.denominator)
            result.denominator = self.denominator * franc_2.denominator
            return result

    def Multiplication(self, franc_2):
        result = fraction(None, None)
        result.numerator = self.numerator * franc_2.numerator
        result.denominator = self.denominator * franc_2.denominator
        return result

    def Division(self, franc_2):
        result = fraction(None, None)
        result.numerator = self.numerator * franc_2.denominator
        result.denominator = self.denominator * franc_2.numerator
        return result
    
def get_input():
    numerator = int(input('Please enter The numerator: '))
    denominator = int(input('Please enter denominator: '))
    return fraction(numerator, denominator)

def show_menu():
    print("1- Sum\n2- Submission\n3- Multiplication\n4- Division\n5- Exit")

while True:
    show_menu()
    user_choice = int(input('Please choose an option: '))
    if user_choice == 1:
        fraction_1 = get_input()
        fraction_2 = get_input()
        fraction_1.SUM(fraction_2).show()

    elif user_choice == 2:
        fraction_1 = get_input()
        fraction_2 = get_input()
        fraction_1.Submission(fraction_2).show()

    elif user_choice == 3:
        fraction_1 = get_input()
        fraction_2 = get_input()
        fraction_1.Multiplication(fraction_2).show()

    elif user_choice == 4:
        fraction_1 = get_input()
        fraction_2 = get_input()
        fraction_1.Division(fraction_2).show()

    elif user_choice == 5:
        break