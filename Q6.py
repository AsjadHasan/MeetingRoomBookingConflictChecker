
def time_to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


n = int(input("Number of bookings: "))

bookings = []

for i in range(n):
    print(f"\nBooking {i + 1}:")
    start = input("Start time (HH:MM): ")
    end = input("End time (HH:MM): ")

    bookings.append((start, end))


for i in range(len(bookings)):
    for j in range(i + 1, len(bookings)):
        start1, end1 = bookings[i]
        start2, end2 = bookings[j]

        start1_min = time_to_minutes(start1)
        end1_min = time_to_minutes(end1)
        start2_min = time_to_minutes(start2)
        end2_min = time_to_minutes(end2)

        if start1_min < end2_min and start2_min < end1_min:
            print(
                f"Conflict: ('{start1}-{end1}') overlaps "
                f"with ('{start2}-{end2}')"
            )