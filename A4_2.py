"""A4_2 contains a recursive function hopping_game(n) that takes the
number of squares lined up on the ground n and returns a list of all the
possible hopping paths if one or two squares can be hopped at a time.

Authour: Victor Tarnovski
Date 2020-12-2

"""


def hopping_game(n):
    """Takes the number of squares n and returns all possible hopping
    paths if one or two squares can be hopped at a time"""
    if n < 1:
        return"Error"
    elif n == 1:
        return ["0-1"]
    elif n == 2:
        return ["0-1-2", "0-2"]
    else:
        one_step_string = "-" + str(n)
        one_step_list = [x + one_step_string for x in hopping_game(n-1)]
        # Adds n to each item of the hopping_game(n-1) list  
        
        two_step_string = "-" + str(n)
        two_step_list = [x + one_step_string for x in hopping_game(n-2)]
        # Adds n to each item of the hopping_game(n-2) list 
        
        return one_step_list + two_step_list


if __name__ == "__main__":
    # Module Testing

    # Function hopping_game(n)

    # Case 1
    n = 2
    print("The number of squares is: ", n)
    print("The possible hopping paths are: ", hopping_game(n))
    print("\n")

    # Case 2
    n = 4
    print("The number of squares is: ", n)
    print("The possible hopping paths are: ", hopping_game(n))
    print("\n")

    
    # Case 3
    n = 6
    print("The number of squares is: ", n)
    print("The possible hopping paths are: ", hopping_game(n))
    print("\n")

        
        
