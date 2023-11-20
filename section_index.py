def relative_space(x1, x2, number):
    def stride_decimal(x1, x2, number):
        return abs(x1-x2)/number
    stride_float = stride_decimal(x1, x2, number)
    nums = []
    for i in range(number):
        nums.append( int(x1+stride_float*i) )
    return nums
