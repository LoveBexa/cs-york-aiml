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

# --------------------------- Next States --------------------------- #
# These are actions made on parent nodes to show available child nodes

def action(state):
    next_states = [state_list[state.actionLeft - 1], state_list[state.actionRight - 1], state_list[state.actionSuck - 1]]
    return next_states
    
def print_states(states):
    array_of_states = []
    for each in states:
        array_of_states.append(each.state)
    return array_of_states

# --------------------------- Main Method --------------------------- #
# Checks each state; explores the next states
# And if it's a new state then it expanded
# ----------------------------------------------------------------- #

current_state = state_one

while not clean_world:

    print("\nCurrent state:", current_state.state)

    # If current state is the goal state then world is clean!
    if current_state in goal_state:
        clean_world = True
        print("The world is finally clean!")
    print("\nThe world is not clean yet\n")

    # If frontier is empty -> fail
    if not frontier:
        sys.exit("Error: frontier is empty!")

    # Remove first state from oldest frontier then add it to explored item
    # Then we check which next child states are available

    frontier.popleft()
    explored.append(current_state)
    next_states = action(current_state)
    print("Child states of",current_state.state,"are", print_states(next_states))
    
    # If any of these states are not in the explored or frontier
    # Then we can add them to current state

    for states in next_states:
        if states not in frontier and states not in explored:
            if states in goal_state: 
                print( "\nWOOHOO!!! Goal state found after state", current_state.state,". World is clean!")
                clean_world = True
                break
            frontier.append(states)
            print("Adding state", states.state, "to frontier")

    print("States in frontier:", print_states(frontier))
    print("States explored:", print_states(explored))

    # New current state is the first item in frontier (oldest as FIFO)

    current_state = frontier[0]

        