

row1 = ["⬜","⬜", "⬜"]
row2 = ["⬜","⬜", "⬜"]
row3 = ["⬜","⬜", "⬜"]

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

positon = input("Where you want to hide your tressure?")

horizontal = int(positon[0])
vertical = int(positon[1])
# you will input column or row 31 or 13, but there is 0,1,2 in column and row that is why we need to give this
# File "C:\Users\StarInfinity\PycharmProjects\Coding_Exercises\Treassure_Map.py", line 16, in <module>
#     map[vertical][horizontal] = "X"
# IndexError: list assignment index out of range
map[vertical-1][horizontal-1] = "X"

print(f"{row1}\n{row2}\n{row3}")