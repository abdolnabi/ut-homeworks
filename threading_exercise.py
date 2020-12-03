"""
This program has been return fr the exercise 1
of the Advanced Operating System course instructed
by Dr. Hedieh Sajedi
Student:Abdolnabi Zameni
Date: 13 Azar 1399
"""
#importing the threading module
import threading
import sys

def print_random_value(step):
    """
    function to print the given num step to output
    """
    ordinal_numbers = {1: "st",
                       2: "nd",
                       3: "rd",
                       4: "th"
                       }

    print( format(step) + (ordinal_numbers.get(step,False) or ordinal_numbers[4] ) + " thread output is: {}".format(step))




if __name__ == "__main__":

    LCL = int(sys.argv[1] or 1)
    UCL = int(sys.argv[2]  or 9) + 1
    print(UCL)
    #loop over the range of 1 to 10, to create totally 9 threads displaying from 1 to 9
    for i in range(LCL,UCL):
        # creating a working thread
        working_thread = threading.Thread(target=print_random_value, args=(i,))
        # starting the working thread
        working_thread.start()
        # wait until the working thread  is completely executed
        # working_thread.join()

    # All of the 9 threads completely executed
    print("Done!")