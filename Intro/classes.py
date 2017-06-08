class LogicGate:

    def __init__(self, label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input('Enter Pin A input for gate ' + self.getLabel() + '--> '))
        else:
            self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input('Enter Pin B input for gate ' + self.getLabel() + '--> '))
        else:
            self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.getPinB == None
                self.getPinB = source
            else
                raise RuntimeError('Error: No empty pins on this gate.')

class UnaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input('Enter Pin input for gate ' + self.getLabel() + '--> '))
        else:
            self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError('Error: No empty pins on this gate.')

class AndGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return int(a and b)

class OrGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return int(a or b)

class NotGate(UnaryGate):

    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def performGateLogic(self):
        pin = self.getPin()
        return int(not pin)

class Connector:

    def __init(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        to_gate.setNextPin(self)

    def getFrom(self):
        return from_gate

    def getTo(self):
        return to_gate

n1 = OrGate('G1')
print(n1.getOutput())
