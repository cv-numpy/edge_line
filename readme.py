
# image => slided into three or four parts of "image row"

# the "image row" => "image col"s in the image row
# function get-col-index()
# {

        # stride_float = image_width / num
        # stride_int = int(stride_float)

        # col_image_width => stride * k, k=(1~2)

        # col_index_1 = int(i*stride_float)
        # col_index_2 = int(i*stride_float + col_image_width)

# }

# "image col" => "single row line"s in the image col
# {
    # nomalization missed

    # "single row line" pixals => avg of three color channels => square difference

    # sum of square differences of "single row line"s for the "image col"
# }

# list of [square difference of a "image col"]s

# indices = np.argsort(diffs_on_cols)[::-1]