#!/usr/bin/env python3
"""
Poisson distribution module
"""


class Poisson:
    """
    Class Poisson that represents a poisson distribution
    """
    def __init__(self, data=None, lambtha=1.0):
        """
        Initializes the Poisson distribution
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of successes
        """
        if not isinstance(k, int):
            k = int(k)

        if k < 0:
            return 0

        e = 2.7182818285
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        return (pow(e, -self.lambtha) * pow(self.lambtha, k)) / factorial

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of “successes”.
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        summation = 0
        for i in range(k + 1):
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            summation += (self.lambtha ** i) / factorial
        return (e ** (-self.lambtha)) * summation
