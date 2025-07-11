#65 from The Python Workbook
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == '__main__':
    print(f"| {'Celsius':>7} | {'Fahrenheit':>11} |")
    for celsius_temp in range(0, 101, 10):
        fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
        print(f"| {celsius_temp:>7} | {fahrenheit_temp:>11} |")
