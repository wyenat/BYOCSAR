class Register:
    def __init__(self, action, next):
        self.value = 0
        self.action = action
        self.next = next

    def consume(self):
        self.action(self.value)
        self.value = 0

    def get(self, val):
        if self.next != None:
            self.next.get(self.value)
        self.value = val