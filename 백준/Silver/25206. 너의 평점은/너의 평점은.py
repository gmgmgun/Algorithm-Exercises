import sys

l = [sys.stdin.readline().strip().split() for _ in range(20)]

filtered = [subj for subj in l if subj[-1] != 'P']
grades = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
scores = [4.5 - 0.5 * i for i in range(len(grades) - 1)]
scores.append(0.0) 

sum_credit = sum(float(subj[1]) for subj in filtered)
sum_score = sum(scores[grades.index(subj[-1])] * float(subj[1]) for subj in filtered)

average_score = sum_score / sum_credit

print(average_score)
