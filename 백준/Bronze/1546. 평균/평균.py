cnt = input()
nums = [int(num) for num in input().split()]


def calculate_manipulated_average(scores):
    max_score = max(scores)
    manipulated_scores = [score / max_score * 100 for score in scores]
    manipulated_average = sum(manipulated_scores) / len(scores)
    return manipulated_average


print(calculate_manipulated_average(nums))