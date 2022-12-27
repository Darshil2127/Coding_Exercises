def paint_calc(height, width, cover):
    number_of_cans = (height*width)/cover
    print(round(number_of_cans))

test_h = int(input("Please enter height ="))
test_w = int(input("Please enter width ="))
coverage = 5

paint_calc(height = test_h, width = test_w, cover = coverage)

