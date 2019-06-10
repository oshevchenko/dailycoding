# This problem was asked by Snapchat.
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
intervals=[(30, 75), (0, 50), (60, 150)]
# intervals=[(30, 75), (0, 50), (60, 150), (49,60)]

START  = 0
FINISH = 1


def sortByTime(val):
    return val[0]

def rooms(intervals):
    n_room_free = 0

    events = []
    for x in intervals:
        event = (x[0]+0.1, START)
        events.append(event)
        event = (x[1]-0.1, FINISH)
        events.append(event)

    events.sort(key = sortByTime)
    # print(events)
    for x in events:
        if x[1] == START:
            if n_room_free > 0:
                n_room_free = n_room_free-1
        elif x[1] == FINISH:
            n_room_free = n_room_free+1
    # print("n_room_free=", n_room_free)
    return n_room_free

print("For",intervals)
print("we need:",rooms(intervals),"room(s)")