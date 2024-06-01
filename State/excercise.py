
class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        self.combination=combination
        self.input=[]
        self.index=0

    def reset(self):
        self.input=[]
        self.status='LOCKED'

    def enter_digit(self, digit):
        self.input.append(digit)

        if self.input==self.combination:
            self.status='OPEN'
        
        elif self.input[self.index]!=self.combination[self.index]:
            self.status='ERROR'
        
        s=''
        for i in self.input:
            s+=str(i)

        self.status=s
        self.index+=1


def test_success():
    cl = CombinationLock([1, 2, 3, 4, 5])
    self.assertEqual('LOCKED', cl.status)
    cl.enter_digit(1)
    self.assertEqual('1', cl.status)
    cl.enter_digit(2)
    self.assertEqual('12', cl.status)
    cl.enter_digit(3)
    self.assertEqual('123', cl.status)
    cl.enter_digit(4)
    self.assertEqual('1234', cl.status)
    cl.enter_digit(5)
    self.assertEqual('OPEN', cl.status)

test_success()

# class FirstTestSuite(unittest.TestCase):
#     def test_success(self):
#         cl = CombinationLock([1, 2, 3, 4, 5])
#         self.assertEqual('LOCKED', cl.status)
#         cl.enter_digit(1)
#         self.assertEqual('1', cl.status)
#         cl.enter_digit(2)
#         self.assertEqual('12', cl.status)
#         cl.enter_digit(3)
#         self.assertEqual('123', cl.status)
#         cl.enter_digit(4)
#         self.assertEqual('1234', cl.status)
#         cl.enter_digit(5)
#         self.assertEqual('OPEN', cl.status)