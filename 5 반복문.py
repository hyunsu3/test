# whatnumber = int(input("구구단 몇 단 욀까요? "))

# for j in range(whatnumber, 15):
#     for i in range(1, 10):
#         print(f"{j} x {i} = {j * i}")
#     print()  # Add a blank line for better readability


import time

progress = 0
while progress < 100:
    progress += 1
    print(f"{progress}%", end="\r")  # Overwrites the same line
    time.sleep(0.1)

print("완료!")