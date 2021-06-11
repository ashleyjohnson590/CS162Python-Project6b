#Author: Ashley Johnson
#Date: 5/3/2021
#Description: program takes a parameter a list of numbers and returns true if the numbers in the list
#are decreasing. Otherwise, it returns false.


def is_decreasing(num_list):
    """ compares 1st number with next number in num_list and returns true if list is decreasing."""
    if len(num_list) == 2:
        if num_list[1] > num_list[0]:
            return True
        else:
            return False
    else:
        if num_list[0] > is_decreasing(num_list[1:]):
            return True
        else:
            return False

def main():
    num_list = [5,6,7,1]
    is_decreasing(num_list)

if __name__ == "__main__":

    main()