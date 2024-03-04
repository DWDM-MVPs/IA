def x_dividing_by_y(x/y):
    try:
        return x/y;
    except TypeError:
        print("You need to add a valid number")
    except ZeroDivisionError:
        print("You cannot divide {} by {}.".format(x,y))
