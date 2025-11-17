subj = []
for n in range(1, 6):
    sub_score = int(input(f"Enter subject {n}:"))
    subj.append(sub_score)

min_score = min(subj)
max_score = max(subj)
print()
print("Lowest Score: " ,min_score,)
print("Highest Score" ,max_score )
