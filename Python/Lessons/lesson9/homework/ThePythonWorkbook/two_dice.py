# ex 137
import random

def dice_sum_probability()->dict:
    total_outcomes = 6 * 6
    probabilities = {}

    for total in range(2, 13):
        if 2 <= total <= 7:
            favorable = total - 1
        else:
            favorable = 13 - total
        percent = round((favorable / total_outcomes) * 100, 2)
        probabilities[total] = percent

    return probabilities

def throw_two_dice()->int:
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    return first_dice + second_dice

def dice_simulation(iterations)->dict:
    simulation = dict.fromkeys([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 0)
    if iterations == 0:
        return simulation
    count = dict.fromkeys([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 0)
    for _ in range(iterations):
        count[throw_two_dice()] += 1

    for summ in count:
        simulation[summ] = round((count[summ] / iterations) * 100, 2)

    return simulation

if __name__ == '__main__':
    test_iter = int(input("Enter iterations count: "))
    simulated_percent = dice_simulation(test_iter)
    expected_percent = dice_sum_probability()

    col1 = "Total"
    col2 = "Simulated %"
    col3 = "Expected %"

    w1 = len(col1) + 2
    w2 = len(col2) + 2
    w3 = len(col3) + 2

    print(f"{col1:>{w1}}{col2:>{w2}}{col3:>{w3}}")
    for summ in sorted(simulated_percent):
        sp = simulated_percent[summ]
        ep = expected_percent[summ]
        print(f"{summ:>{w1}}{sp:>{w2}.2f}{ep:>{w3}.2f}")

