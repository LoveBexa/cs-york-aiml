from collections import deque
import sys


# -------------------- Setting up the States  -------------------- #

class State:

    def __init__(self, state, dirtLeft, dirtRight, vacPosition, actionleft, actionRight, actionSuck):
        self.state = state
        self.dirtLeft = dirtLeft
        self.dirtRight = dirtRight
        self.vacPosition = vacPosition
        self.actionLeft = actionleft
        self.actionRight = actionRight
        self.actionSuck = actionSuck
    

state_one = State(1, True, True, "Left", 1, 2, 3)
state_two = State(2, True, True, "Right", 1, 2, 6)
state_three = State(3, False, True, "Left", 3, 4, 3)
state_four = State(4, False, True, "Right", 3, 4, 8)
state_five = State(5, True, False, "Left", 5, 6, 7)
state_six = State(6, True, False, "Right", 5, 6, 6)
state_seven = State(7, False, False, "Left", 7, 8, 7)
state_eight = State(8, False, True, "Right", 7, 8, 8)

state_list = [state_one, state_two, state_three, state_four, state_five, state_six, state_seven, state_eight]

# Initialise states 
goal_state = [state_seven, state_eight]
frontier = deque([state_one])
explored = deque()

clean_world = False

# --------------------------- Action on Nodes Show Next States --------------------------- #

def action(state):
    next_states = [state_list[state.actionLeft - 1], state_list[state.actionRight - 1], state_list[state.actionSuck - 1]]
    return next_states
    
def print_states(states):
    array_of_states = []
    if isinstance(states, list) == True:
        for each in states:
            array_of_states.append(each.state)
        print(array_of_states)
        return array_of_states
    else:
        print(states.state)
        return states.state


# --------------------------- Main Method --------------------------- #
# Checks each state; explores the next actions
# And if it's a new action then it expanded
# ----------------------------------------------------------------- #


current_state = state_one


while not clean_world:

    print("Current state:", print_states(current_state))

    # If current state is the goal state then world is clean!
    if current_state in goal_state:
        clean_world = True
        print("The world is finally clean!")
    
    print("\n  =( The world is not clean yet ########## \n")

    # If frontier is empty -> fail
    if not frontier:
        sys.exit("Error: frontier is empty!")

    # Remove first state from oldest frontier then add it to explored item
    # Then we check which next child states are available
    frontier.popleft()
    explored.append(current_state)

    print("States in frontier:", print_states(frontier))
    print("States in explored:", print_states(explored))
    

    next_states = action(current_state)

    print("Child states:")
    print_states(next_states)
    # If any of these states are not in the explored or frontier
    # Then we can add them to current state

    for states in next_states:
        if states not in frontier or states not in explored:
            if states in goal_state: 
                print( "Goal state found at state", states.state, ". World is clean!")
                clean_world = True
                break
            frontier.append(states)
            current_state = states
            print("Adding state", states.state, "to frontier")

        