def square_diff_of_rowLine(row):
    def square(num1, num2):
        return (num1-num2)* (num1-num2)
    length = len(row)

    channel_1_avg = 0
    channel_2_avg = 0
    channel_3_avg = 0

    for pixal in row:
        channel_1, channel_2, channel_3 = pixal

        channel_1_avg = channel_1_avg + channel_1
        channel_2_avg = channel_2_avg + channel_2
        channel_3_avg = channel_3_avg + channel_3

    channel_1_avg = channel_1_avg / length
    channel_2_avg = channel_2_avg / length
    channel_3_avg = channel_3_avg / length


    channel_1_diff = 0
    channel_2_diff = 0
    channel_3_diff = 0

    for pixal in row:
        channel_1_diff = channel_1_diff + square(channel_1_avg, pixal[0])
        channel_2_diff = channel_2_diff + square(channel_2_avg, pixal[1])
        channel_3_diff = channel_3_diff + square(channel_3_avg, pixal[2])

    channels_diff = (channel_1_diff + channel_2_diff + channel_3_diff) / 3
    return channels_diff, channel_1_diff, channel_2_diff, channel_3_diff
