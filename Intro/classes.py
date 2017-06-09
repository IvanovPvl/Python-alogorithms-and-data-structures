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
        if self.pinA is None:
            return int(input('Enter Pin A input for gate ' + self.getLabel() + '--> '))
        else:
            self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            return int(input('Enter Pin B input for gate ' + self.getLabel() + '--> '))
        else:
            self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError('Error: No empty pins on this gate.')


class UnaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input('Enter Pin input for gate ' + self.getLabel() + '--> '))
        else:
            self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError('Error: No empty pins on this gate.')


class AndGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        print(a, b)

        if a == 1 and b == 1:
            return 1
        else:
            return 0
        # return int(a and b)


class NandGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        # return int(not(a and b))
        if a == 1 and b == 1:
            return 0
        else:
            return 1


class OrGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return int(a or b)


class NorGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        # return int(not(a or b))

        print(a, b)

        if a == 1 or b == 1:
            return 0
        else:
            return 1


class NotGate(UnaryGate):

    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def performGateLogic(self):
        pin = self.getPin()
        return int(not pin)


class Connector:

    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        to_gate.setNextPin(self)

    def getFrom(self):
        return self.from_gate

    def getTo(self):
        return self.to_gate

# g1_1 = AndGate('G1_1')
# g2_1 = AndGate('G2_1')
# g3_1 = NorGate('G3_1')
# c1_1 = Connector(g1_1, g3_1)
# c1_2 = Connector(g2_1, g3_1)

# g1_2 = NandGate('G1_2')
# g2_2 = NandGate('G2_2')
g1_2 = AndGate('G1_2')
g2_2 = AndGate('G2_2')
g3_2 = AndGate('G3_2')
c2_1 = Connector(g1_2, g3_2)
c2_2 = Connector(g2_2, g3_2)

# print(g3_1.getOutput() == g3_2.getOutput())
print(g3_2.getOutput())
# print(g1_2.getOutput())
