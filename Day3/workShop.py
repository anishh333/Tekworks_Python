def input_details(day: int) -> set:
    n = int(input(f"Enter the no of ppl attended on day {day}: "))
    A = set()
    for i in range(n):
        a = input("Enter the email id: ")
        A.add(a)
    return A

# Unique attendees of all days
def attendees(day1: set, day2: set, day3: set):
    print(f"{len(day1 | day2 | day3)} are the unique attendees")

# Present all days
def allDays(day1: set, day2: set, day3: set):
    print(f"Attendees present on all days: {day1 & day2 & day3}")

# Exactly one day 
def oneDay(day1: set, day2: set, day3: set):
    exact_one = (day1 ^ day2 ^ day3) - (day1 & day2 & day3)
    print(f"{exact_one} are attended in exactly one day")

# Pairwise overlaps
def overlaps(day1: set, day2: set, day3: set):
    print(f"{day1 & day2} are overlaps of Day1 and Day2, count = {len(day1 & day2)}")
    print(f"{day2 & day3} are overlaps of Day2 and Day3, count = {len(day2 & day3)}")
    print(f"{day1 & day3} are overlaps of Day1 and Day3, count = {len(day1 & day3)}")

# Counts and sorted lists
def report(day1: set, day2: set, day3: set):
    print(f"Day1 attendees ({len(day1)}): {sorted(day1)}")
    print(f"Day2 attendees ({len(day2)}): {sorted(day2)}")
    print(f"Day3 attendees ({len(day3)}): {sorted(day3)}")

day1=input_details(1)
day2=input_details(2)
day3=input_details(3)

attendees(day1,day2,day3)
allDays(day1,day2,day3)
oneDay(day1,day2,day3)
overlaps(day1,day2,day3)
report(day1,day2,day3)