from colorama import Fore, Style

print(f"{Fore.BLUE}[All] [Wrong] [Empty]{Style.RESET_ALL}")
v1, v2, v3 = input().split()
v4 = int(v1) - int(v2) - int(v3)
s1 = int(v1) * 3
s2 = int(v2) * 4
s3 = int(v3) * 3
s4 = s1 - s2 - s3
s5 = s4 * 10000 // s1
s6 = s5 // 100
s7 = s5 % 100

print(f"\n[All]: \t\t {Style.BRIGHT}{v1}{Style.RESET_ALL}")
print(f"[Correct]: \t {Style.BRIGHT}{v4}{Style.RESET_ALL}")
print(f"[Wrong]: \t {Style.BRIGHT}{v2}{Style.RESET_ALL}")
print(f"[Empty]: \t {Style.BRIGHT}{v3}{Style.RESET_ALL}\n")
print(f"{Fore.YELLOW}[Score(-)]: \t {Style.BRIGHT}{s6}.{s7:02}{Style.RESET_ALL}")
s8 = s5 // 1000
s9 = 10 - s8
print("[", end='')
while s8 > 0:
    print('#', end='')
    s8 -= 1
while s9 > 0:
    print('-', end='')
    s9 -= 1
print("]\n")

q2 = v4 * 10000 // int(v1)
q3 = q2 // 100
q4 = q2 % 100
print(f"{Fore.YELLOW}[Score]: \t {Style.BRIGHT}{q3}.{q4:02}{Style.RESET_ALL}")
q5 = q2 // 1000
q6 = 10 - q5
print("[", end='')
while q5 > 0:
    print('#', end='')
    q5 -= 1
while q6 > 0:
    print('-', end='')
    q6 -= 1
print("]\n")
input("Press Enter to exit.")
