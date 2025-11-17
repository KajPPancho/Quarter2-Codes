subj = []
for n in range(1, 6):
    sub_score = int(input(f"Enter subject {n}:"))
    subj.append(sub_score)

sum_score = sum(subj)
print()
print("Total = " ,sum_score,)
print("Average = " ,sum_score / len(subj ))
