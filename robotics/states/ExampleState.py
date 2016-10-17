from robotics.core.DefaultState import DefaultState
from robotics.behaviours.ExampleBehaviour import ExampleBehaviour

class ExampleState(DefaultState):
    def testBehaviour(self):
        return ExampleBehaviour()()
