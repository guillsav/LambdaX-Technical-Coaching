def meeting_planner(slots_a: list, slots_b: list, dur: int) -> list:
    a_index = b_index = 0

    while a_index < len(slots_a) and b_index < len(slots_b):
        start = max(slots_a[a_index][0], slots_b[b_index][0])
        end = min(slots_a[a_index][1], slots_b[b_index][1])

        if end - start >= dur:
            return [start, start + dur]

        if slots_a[a_index][1] < slots_b[b_index][1]:
            a_index += 1
        else:
            b_index += 1

    return []


slots_a = [[10, 50], [60, 120], [140, 210]]
slots_b = [[0, 15], [60, 70]]
print(meeting_planner(slots_a, slots_b, 8))
