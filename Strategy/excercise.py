from abc import ABC
import cmath

class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b*b-4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        result=b*b-4*a*c
        return result if result>=0 else float('nan')

class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        disc=complex(self.strategy.calculate_discriminant(a,b,c),0)
        root_disc=cmath.sqrt(disc)

        return (
            (-b+root_disc)/(2*a),
            (-b-root_disc)/(2*a)
        )
        

strategy = RealDiscriminantStrategy()
solver = QuadraticEquationSolver(strategy)
results = solver.solve(1, 4, 5)

print(results[0].real,results[0].imag)

# self.assertTrue(math.isnan(results[0].real))
# self.assertTrue(math.isnan(results[1].real))
# self.assertTrue(math.isnan(results[0].imag))
# self.assertTrue(math.isnan(results[1].imag))