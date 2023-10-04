#!/usr/bin/env python3

if __name__ == '__main__':
    tempC = float(input('Enter temperature in celcius: '))
    tempF = (tempC * (9/5)) + 32
    print(tempC, '^oC =', tempF, '^oF')
