from ecdsa import ellipticcurve, SECP256k1
import secrets

class ECPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def BasePointGGet():
    generator = SECP256k1.generator
    return ECPoint(generator.x(), generator.y())

def ECPointGen(x, y):
    return ECPoint(x, y)

def IsOnCurveCheck(point):
    curve = SECP256k1.curve
    x, y = point.x, point.y
    return (y * y - x * x * x - curve.a() * x - curve.b()) % curve.p() == 0

def AddECPoints(a, b):
    curve = SECP256k1.curve
    p = ellipticcurve.Point(curve, a.x, a.y, SECP256k1.order)
    q = ellipticcurve.Point(curve, b.x, b.y, SECP256k1.order)
    r = p + q
    
    # Перевірка, чи точка лежить на еліптичній кривій
    assert IsOnCurveCheck(ECPoint(r.x(), r.y())), "Point is not on the curve"
    
    return ECPoint(r.x(), r.y())

def DoubleECPoints(a):
    curve = SECP256k1.curve
    p = ellipticcurve.Point(curve, a.x, a.y, SECP256k1.order)
    r = 2 * p
    
    # Перевірка, чи точка лежить на еліптичній кривій
    assert IsOnCurveCheck(ECPoint(r.x(), r.y())), "Point is not on the curve"
    
    return ECPoint(r.x(), r.y())

def ScalarMult(k, a):
    curve = SECP256k1.curve
    p = ellipticcurve.Point(curve, a.x, a.y, SECP256k1.order)
    r = k * p
    
    # Перевірка, чи точка лежить на еліптичній кривій
    assert IsOnCurveCheck(ECPoint(r.x(), r.y())), "Point is not on the curve"
    
    return ECPoint(r.x(), r.y())

def ECPointToString(point):
    return f"{point.x};{point.y}"

def StringToECPoint(s):
    x_str, y_str = map(int, s.split(";"))
    return ECPoint(x_str, y_str)

def PrintECPoint(point):
    print(f"X: {point.x}, Y: {point.y}")

def IsEqual(point1, point2):
    return point1.x == point2.x and point1.y == point2.y

if __name__ == "__main__":
    # при обчислені рівняння паралельно перевіряється генерація базової точки, скалярного добутку,
    # перевірка чи належить точка кривій, функцій серіалізації та десеріалізації, функція виводу точки у консоль
    # функція перевірки рівності двох точок. У другому рівнянні перевіряється сума точок та подвоєння(2P)
    print("k*(d*G) = d*(k*G)")
    G = BasePointGGet()
    k = secrets.randbits(256)
    d = secrets.randbits(256)
    H1 = ScalarMult(d, G)
    H2 = ScalarMult(k, H1)

    H3 = ScalarMult(k, G)
    H4 = ScalarMult(d, H3)

    print(ECPointToString(H2))
    PrintECPoint(StringToECPoint(ECPointToString(H4)))
    print("k*(d*G) = d*(k*G) result :", IsEqual(H2, H4))

    print("----------------------------------")

    print("P + P = 2P")
    P = BasePointGGet()
    PrintECPoint(P)
    Sum_res = AddECPoints(P, P)
    PrintECPoint(Sum_res)
    Double_res = DoubleECPoints(P)
    PrintECPoint(Double_res)

    print("P + P = 2P result:", IsEqual(Sum_res, Double_res))


