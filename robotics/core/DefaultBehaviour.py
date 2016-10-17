class DefaultBehaviour(object):
    def __call__(self):
        return self.behaviour()

    def behaviour(self):
        return True
