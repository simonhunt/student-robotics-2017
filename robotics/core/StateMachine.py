class StateMachine(object):
    def __init__(self, initial_state):
        self.state = initial_state

    def testBehaviour(self):
        return self.state.testBehaviour()
