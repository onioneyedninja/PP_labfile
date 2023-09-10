import math


def calculate_mean(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean


numbers = [10, 15, 20, 25, 30]
mean = calculate_mean(numbers)
print("Mean:", mean)


def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[(n // 2) - 1] + sorted_numbers[n // 2]) / 2

    return median


numbers = [10, 15, 20, 25, 30]
median = calculate_median(numbers)
print("Median:", median)
from collections import Counter


def calculate_mode(numbers):
    counter = Counter(numbers)
    mode = counter.most_common(1)[0][0]
    return mode


numbers = [10, 15, 20, 15, 30, 15, 20]
mode = calculate_mode(numbers)
print("Mode:", mode)


def calculate_standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
    variance = squared_diff_sum / len(numbers)
    standard_deviation = math.sqrt(variance)
    return standard_deviation


numbers = [10, 15, 20, 25, 30]
std_dev = calculate_standard_deviation(numbers)
print("Standard Deviation:", std_dev)

total_possible_outcomes = 6  # For a standard six-sided die
desired_outcomes = 2  # We want to roll a 1 or a 2

probability = desired_outcomes / total_possible_outcomes
print("Probability:", probability)
