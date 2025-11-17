colors = []
for f in range(1, 6):
    color = input(f"Enter color {f}: ")
    colors.append(color)
cc = input("Enter a color that appears MULTIPLE times: ")
if cc in colors:
    index = colors.index(cc)
    count = colors.count(cc)
    print("'",cc,"'" f"found at index {index} ")
    print("'",cc,"'" f"appears {count} time(s)")
