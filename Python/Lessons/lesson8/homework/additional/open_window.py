# ex2
engineer1 = [[1, 6], [10, 17], [19, 24], [40, 67], [80, 91], [93, 97]]
engineer2 = [[5, 11], [19, 30], [47, 60], [80, 94]]

duration = int(input("Enter meeting duration: "))

windows = []

for time1 in engineer1:
    if time1[1] - time1[0] >= duration:
        for time2 in engineer2:
            if time2[1] - time2[0] >= duration:
                start = max(time1[0], time2[0])
                end = min(time1[1], time2[1])
                if start < end and (end - start) >= duration:
                    windows.append([start, end])

if not windows:
    print("There are no open windows for meeting")
else:
    print(f"Open windows for meeting: {windows}")

