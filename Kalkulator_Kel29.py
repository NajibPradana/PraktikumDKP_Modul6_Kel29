from abc import ABC, abstractmethod 

import math 

 
 

class Calculator(ABC): 

    def __init__(self): 

        self._numbers = [] 

 
 

    def get_numbers(self): 

        return self._numbers 

 
 

    def set_numbers(self, numbers): 

        self._numbers = numbers 

 
 

    def num(self): 

        num_count = int(input("Enter the number of values: ")) 

        for i in range(num_count): 

            num = int(input("Enter a Number: ")) 

            self._numbers.append(num) 

 
 

    @abstractmethod 

    def calculate(self): 

        pass 

 
 
 

class Basic_Calculator(Calculator): 

    def value(self): 

        super().num() 

 
 

    def calculate(self): 

        if choice1 == '1': 

            self._add() 

        elif choice1 == '2': 

            self._subtract() 

        elif choice1 == '3': 

            self._multiply() 

        elif choice1 == '4': 

            self._divide() 

        else: 

            print("Invalid input") 

 
 

    def _add(self): 

        result = sum(self.get_numbers()) 

        print(f"The Answer is: {result}") 

 
 

    def _subtract(self): 

        result = self.get_numbers()[0] 

        for num in self.get_numbers()[1:]: 

            result -= num 

        print(f"The Answer is: {result}") 

 
 

    def _multiply(self): 

        result = 1 

        for num in self.get_numbers(): 

            result *= num 

        print(f"The Answer is: {result}") 

 
 

    def _divide(self): 

        result = self.get_numbers()[0] 

        for num in self.get_numbers()[1:]: 

            result /= num 

        print(f"The Answer is: {result}") 

 
 

    def clear(self): 

        self.set_numbers([]) 

 
 

class ScientificCalculator(Calculator): 

    def value(self): 

        super().num() 

 
 

    def calculate(self): 

        if choice2 == '1': 

            self._squareRoot() 

        elif choice2 == '2': 

            self._exponentiation() 

        elif choice2 == '3': 

            self._factorial() 

        else: 

            print("Invalid input") 

 
 

    def _squareRoot(self): 

        results = [math.sqrt(num) for num in self.get_numbers()] 

        print("The Answers are:") 

        for result in results: 

            print(result) 

 
 

    def _exponentiation(self): 

        base = self.get_numbers()[0] 

        exponent = 1 

        for num in self.get_numbers()[1:]: 

            exponent = exponent ** num 

        result = base ** exponent 

        print(f"The Answer is: {result}") 

 
 

    def _factorial(self): 

        results = [math.factorial(num) for num in self.get_numbers()] 

        print("The Answers are:") 

        for result in results: 

            print(result) 

 
 

    def clear(self): 

        self.set_numbers([]) 

 
 

print("***CALCULATOR***") 

 
 

while True : 

    print("1. Basic Calculator\n2. Scientific Calculator") 

    choice = input("Choose Calculator (x for exit): ") 

 
 

    if choice == 'x': 

        break 

 
 

    choice = int(choice) 

 
 

    if choice == 1: 

        BC = Basic_Calculator() 

        print("\nBasic Calculator\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division") 

        choice1 = input("Choose Arithmetic Operation (x to go): ") 

 
 

        if choice1 == 'x': 

            continue 

        else: 

            BC.value() 

            BC.calculate() 

            BC.clear() 

            break 

 
 

    elif choice == 2: 

        SC = ScientificCalculator() 

        print("\nScientific Calculator\n1. Square Root\n2. Exponentiation\n3. Factorial") 

        choice2 = input("Choose Arithmetic Operation (x to go back): ") 

 
 

        if choice2 == 'x': 

            continue 

        else: 

            SC.value() 

            SC.calculate() 

            SC.clear() 

            break   

    else: 

        print('Invalid input') 

 
 

 