import sys

class State:

    def __init__(self, state, dirtLeft, dirtRight, vacPosition, actionleft, actionRight, actionSuck):
        self.state = state
        self.dirtLeft = dirtLeft
        self.dirtRight = dirtRight
        self.vacPosition = vacPosition
        self.actionLeft = actionleft
        self.actionRight = actionRight
        self.actionSuck = actionSuck


# state_one = State(1, True, True, "Left", 1, 2, 3)
# state_two = State(2, True, True, "Right", 1, 2, 6)
# state_three = State(3, False, True, "Left", 3, 4, 3)
# state_four = State(4, False, True, "Right", 3, 4, 8)
# state_five = State(5, True, False, "Left", 5, 6, 7)
# state_six = State(6, True, False, "Right", 5, 6, 6)
# state_seven = State(7, False, False, "Left", 7, 8, 7)
# state_eight = State(8, False, True, "Right", 7, 8, 8)


state_one = State(1, False, False, "Left", 1, 2, 3)
state_two = State(2, False, False, "Right", 1, 2, 6)
state_three = State(3, False, False, "Left", 3, 4, 3)
state_four = State(4, False, False, "Right", 3, 4, 8)
state_five = State(5, False, False, "Left", 5, 6, 7)
state_six = State(6, False, False, "Right", 5, 6, 6)
state_seven = State(7, False, False, "Left", 7, 8, 7)
state_eight = State(8, False, False, "Right", 7, 8, 8)



state_list = [state_one, state_two, state_three, state_four, state_five, state_six, state_seven, state_eight]

# The goal state is when the floor is clean and there is no dirt left
# This checks if all the dirt has been vacuumed 
def goalTest():
    counter = 1
    for state in state_list:
        # If either side of floor is dirty then entire floor needs cleaning
        if (state.dirtLeft == True) or (state.dirtRight == True):
            print("The vacuum has not finished cleaning!")
            return 0
        # Checks if floor is clean for each state
        elif (state.dirtLeft == False) and (state.dirtRight == False):
            counter += 1
            # When each state is completely clean then entire floor is clean!
            if (counter == 8):
                return counter


frontier = []
explored = []


# Main method 
# Initialise first state

first_state = state_two 

# Checks to see if goal state is met when all states are clean of dirt
if (goalTest() == 8):
    sys.exit("Goal achieved - floor is clean! Search ends")
else:
    print("The vacuum has not 0 finished cleaning!")


# frontier -> contains first state
# explored -> empty 

# while loop
# if frontier is empty -> fail
# state <-remove  node from frontier (pop)
# add state to explored

# for each state in the actions of current state 
# child state = child (problem, node , action)
# if the child states are not in explored or frontier 
# if goal_test = child state 
# add child state to the frontier 