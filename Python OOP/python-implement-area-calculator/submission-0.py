import math

class AreaCalc:
    def calculate(self, length, width = None) -> float:
        if width == None:
            area_circle = math.pi * (length * length)
            area_circle = round(area_circle, 2)
            return area_circle
        else:
            area_rectangle = length * width
            return area_rectangle
        
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
