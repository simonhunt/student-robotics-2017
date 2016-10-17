""" Tests will be run from any class contained within a file that is prefixed
    with test_ that is within the tests folder.

    You may name your class however you like but test methods must
    also be prefixed with test_."""

import logging
import unittest
from robotics.core.StateMachine import StateMachine
from robotics.states.ExampleState import ExampleState

class example(unittest.TestCase):
    """ An example test class. """

    def test_example(self):
        """ An example test method. """

        # You may log information to the terminal from within your tests by
        # using the logging library and running nose2 with the --log-capture
        # flag.
        logging.info("This is an example log message.")

        # Given: The following objects and variables.
        example_state = ExampleState()

        # When: The testBehaviour method is called on the StateMachine.
        state_machine = StateMachine(example_state)
        result = state_machine.testBehaviour()

        # Then: The correct output is returned.
        self.assertEqual(result, "Example Behaviour")

if __name__ == "__main__":
    unittest.main()
