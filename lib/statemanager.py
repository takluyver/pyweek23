class StateManager(object):
    def __init__(self, tick_callback):
        self.states = []
        self.tick_callback = tick_callback

    def update(self):
        dt = self.tick_callback()
        """ if current state is not done, update it.  othewise, move to the next state.
         return True if state machine is still running, false otherwise."""
        if self.current().isdone() or self.current().super_isdone():
            self.movenext()
            if (not self.isdone()):
                self.current().super_active()
        else:
            self.current().update_super(dt)
        return not (self.isdone())

    def add(self, state):
        self.states.append(state)

    def addnextstate(self, state):
        self.states.insert(1, state)

    def movenext(self):
        self.states = self.states[1:]

    def current(self):
        if len(self.states) > 0:
            return self.states[0]
        return None

    def isdone(self):
        return len(self.states) == 0
