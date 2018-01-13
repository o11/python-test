class Math:
    """Math class:
    Basic 4 math operation for 2 numbers
    1 multiply
    2 division
    3 addition
    4 subtraction"""
    __num_1 = 0  # initializing of __num_1: 0
    __num_2 = 0  # initializing of __num_2: 0

    def __init__(self, num_1, num_2):
        """Constructor of Math class
        Takes 2 arguments
        1 num_1
        2 num_2"""
        self.__num_1 = num_1
        self.__num_2 = num_2

    def multiply(self):
        """multiply __num_1 with __num_2"""
        return self.__num_1 * self.__num_2

    def division(self):
        """Divide __num_1 to __num_2"""
        return self.__num_1 / self.__num_2

    def addition(self):
        """Add __num_1 to __num_2"""
        return self.__num_1 + self.__num_2

    def subtraction(self):
        """Subtract __num_1 from __num_2"""
        return self.__num_1 - self.__num_2

    @property
    def num_1(self):
        """return value of __num_1"""
        return self.__num_1

    @num_1.setter
    def num_1(self, value):
        """set the value f __num_1 to value arguments"""
        self.__num_1 = value

    @property
    def num_2(self):
        """return value of __num_2"""
        return self.__num_2

    @num_2.setter
    def num_2(self, value):
        """set the value f __num_2 to value arguments"""
        self.__num_2 = value
