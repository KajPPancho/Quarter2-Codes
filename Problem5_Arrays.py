subj = []
for n in range(1, 4):
    sub_score = input(f"Enter subject {n}:")
    subj.append(sub_score)
    if n == 3:
       add = input("Enter subject to add:" )
       subj.append(add)
       insert1 = input("Enter subject to insert at position 1: ")
       subj.insert(0, insert1)
    else:
        pass
print("Final list: " ,subj)
