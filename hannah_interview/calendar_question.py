## EXAMPLE INPUT
#
# calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
# d_bounds1 = ['9:00', '20:00']
#
# calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
# d_bounds2 = ['9:30', '18:30']
#
# meeting_length = 30
#
# expected_output = [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]







# def main(
#     calendar1,
#     daily_bounds1,
#     calendar2,
#     daily_bounds2,
#     meeting_length
# ):
#     return


def main(
    calendar1,
    daily_bounds1,
    calendar2,
    daily_bounds2,
    meeting_length
):
    full_calendar1 = combine_calendar_and_bounds(calendar1, daily_bounds1)
    full_calendar2 = combine_calendar_and_bounds(calendar2, daily_bounds2)

    cal1 = [[convert_time_to_int(start), convert_time_to_int(end)] for (start, end) in full_calendar1]
    cal2 = [[convert_time_to_int(start), convert_time_to_int(end)] for (start, end) in full_calendar2]

    master_cal = []
    pointer1 = 0
    pointer2 = 0
    while pointer1<len(cal1) and pointer2<len(cal2):
        if cal1[pointer1][0] < cal2[pointer2][0]:
            master_cal.append(cal1[pointer1])
            pointer1 += 1
        else:
            master_cal.append(cal2[pointer2])
            pointer2 += 1

    if pointer1 == len(cal1):
        master_cal += cal2[pointer2:]
    if pointer2 == len(cal2):
        master_cal += cal1[pointer1:]

    meeting_index = 0
    while meeting_index < len(master_cal)-1:
        if master_cal[meeting_index][1] >= master_cal[meeting_index+1][0]:
            master_cal[meeting_index][1] = max(master_cal[meeting_index][1], master_cal[meeting_index+1][1])
            del master_cal[meeting_index+1]
        else:
            meeting_index += 1

    free_periods = []
    for meeting_index in range(len(master_cal)-1):
        if master_cal[meeting_index+1][0] - master_cal[meeting_index][1] >= meeting_length:
            free_periods.append([
                convert_int_to_time(master_cal[meeting_index][1]),
                convert_int_to_time(master_cal[meeting_index+1][0])
            ])

    return free_periods



def combine_calendar_and_bounds(calendar, daily_bounds):
    start_period = ['00:00', daily_bounds[0]]
    end_period = [daily_bounds[1], '24:00']
    return [start_period] + calendar + [end_period]

def convert_time_to_int(time_string):
    hour = int(time_string.split(":")[0])
    minute = int(time_string.split(":")[1])
    return 60*hour + minute

def convert_int_to_time(time_int):
    hour = time_int // 60
    minutes = time_int % 60
    return f"{hour}:{minutes:02}"








def test_main():
    calendar_ben = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
    daily_bounds_ben = ['9:00', '20:00']

    calendar_hannah = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
    daily_bounds_hannah = ['9:30', '18:30']

    meeting_length = 30

    expected_output = [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]

    assert main(
        calendar_ben,
        daily_bounds_ben,
        calendar_hannah,
        daily_bounds_hannah,
        meeting_length
    ) == expected_output

test_main()
