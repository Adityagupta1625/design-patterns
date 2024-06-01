class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class Mediator:
    def __init__(self):
        self.events=Event()
    
    def broadcast(self,sender,value):
        self.events(sender,value)

class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        mediator.events.append(self.alert)
    
    def alert(self,source,value):
        if self!=source:
            self.value+=value

    def say(self, value):
        self.mediator.broadcast(self,value)