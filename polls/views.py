from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from kwikapi import API
from logging import Logger, log


class BaseCalc():
    def add(self, a: int, b: int) -> int:
        """
        This API is for perform addition of two numbers using BaseScript
        @param request:a value and b value
        @return:Addition of two values a+b

        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """
        This API is for perform subtract of two numbers using BaseScript
        @param request:a and b values:
        @return:Subtraction of two values a-b
        """
        return a - b


class StandardCalc():
    def multiply(self, a: int, b: int) -> int:
        """
        This API is for perform Mutlipy of two numbers using BaseScript
        @param request:a and b values:
        @return:Mutlipication of two values a*b

        """
        return a * b

    def divide(self, a: int, b: int) -> float:
        """
        This API is for perform devide  of two numbers using BaseScript
        @param request:a and b values:
        @return:Division  of two values a/b

        """
        return a / b


class LeapYear():
    def leapyear(self, year: int) -> str:
        """
         This API is for perform find given year is leap year are not

        :param request:year
        :return:year is leap year are not
        """
        if year % 4 == 0 and year % 100 != 0:
            return year, "is a Leap Year"
        elif year % 100 == 0:
            return year, "is not a Leap Year"
        elif year % 400 == 0:
            return  (year, "is a Leap Year")
        else:
            return  (year, "is not a Leap Year")

class BubbleSort():
        def bubbleSort(arr) -> int:
            """

            :return:
            """
            n = len(arr)

            # Traverse through all array elements
            for i in range(n):

                # Last i elements are already in place
                for j in range(0, n - i - 1):

                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is greater
                    # than the next element
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]



        arr = [64, 34, 25, 12, 22, 11, 90]

        bubbleSort(arr)

        print("Sorted array is:")
        for i in range(len(arr)):
            print("%d" % arr[i]),


api = API(log)
api.register(BaseCalc(), 'v1')
print("siva")
api.register(StandardCalc(), "v2")
api.register(LeapYear(), "v3")
print("v3 working")
api.register(BubbleSort(),"v4")
print("work")
