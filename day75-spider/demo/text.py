import re
import csv

# html = "A B C D"

# p = re.compile(r"((\w+)\s+(\w+))")
# r3 = p.findall(html)

# print(r3)


with open("test.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["小姐姐", "20"])
print("save ok.")