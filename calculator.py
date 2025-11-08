class Calculator:
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self) -> float:
        return self.op1 + self.op2

    def substract(self) -> float:
        return self.op1 - self.op2

    def multiply(self) -> float:
        return self.op1 * self.op2

    def divide(self) -> float:
        if self.op2 == 0:
            if self.op1 == 0:
                return float('nan')
            elif self.op1 > 0:
                return float('inf')
            else:
                return float('-inf')
        return self.op1 / self.op2


# Test działania klasy
if __name__ == "__main__":
    calculator1 = Calculator(op1=4, op2=7)
    calculator2 = Calculator(op1=3, op2=5)
    calculator3 = Calculator(op1=0, op2=0)

    print("Suma:", calculator1.sum())
    print("Różnica:", calculator2.substract())
    print("Iloczyn:", calculator1.multiply())
    print("Iloraz:", calculator2.divide())
    print("Iloraz:", calculator3.divide())

