class State:

    def __init__(self, state, dirtLeft, dirtRight, vacPosition, actionleft, actionRight, actionSuck):
        self.state = state
        self.dirtLeft = dirtLeft
        self.dirtRight = dirtRight
        self.vacPosition = vacPosition
        self.actionLeft = actionleft
        self.actionRight = actionRight
        self.actionSuck = actionSuck

    def initialise_state(self):
        print(self.state) 


state_one = State(1, True, True, "Left", 1, 2, 3)
state_two = State(2, True, True, "Right", 1, 2, 6)
state_three = State(3, False, True, "Left", 3, 4, 3)
state_four = State(4, False, True, "Right", 3, 4, 8)
state_five = State(5, True, False, "Left", 5, 6, 7)
state_six = State(6, True, False, "Right", 5, 6, 6)
state_seven = State(7, False, False, "Left", 7, 8, 7)
state_eight = State(8, False, True, "Right", 7, 8, 8)


State.initialise_state(state_one)