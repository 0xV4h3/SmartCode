# 86 from The Python Workbook
base_fare = 4.0
variable_fare = 0.25
variable_distance = 0.14

def taxifare(distance : float) -> float:
    return (distance * base_fare) + ((distance // variable_distance) * variable_fare)

if __name__ == "__main__":
    print(taxifare(0.01))
    print(taxifare(0.13))
    print(taxifare(0.14))
    print(taxifare(14))
    print(taxifare(14.13))
