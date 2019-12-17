from math import cos, sin, pi
import json

theta1 = pi / 2
theta2 = pi / 2
m1, m2 = 2, 2
l1, l2 = 1, 1
g = 9.99
a_v1 = 0
a_v2 = 0
step = 0.025
angles = []


def derivative(theta1, theta2):
    numerator = -g * (2 * m1 + m2) * sin(theta1) - m2 * g * sin(theta1 - 2 * theta2) - 2 * sin(theta1 - theta2) * m2 * (
            a_v2 ** 2 * l2 + a_v1 ** 2 * l1 * cos(theta1 - theta2))
    denominator = l1 * (2 * m1 + m2 - m2 * cos(2 * theta1 - 2 * theta2))
    acceleration1 = numerator / denominator

    numerator = 2 * (sin(theta1 - theta2)) * (
            a_v1 ** 2 * l1 * (m1 + m2) + g * (m1 + m2) * cos(theta1) + a_v2 ** 2 * l2 * m2 * cos(theta1 - theta2))
    denominator = l2 * (2 * m1 + m2 - m2 * cos(2 * theta1 - 2 * theta2))
    acceleration2 = numerator / denominator
    return acceleration1, acceleration2


def legge_orararia(a_a, a_v, t):
    return (1 / 2 * a_a * (t ** 2)) + t


def integrate():
    h = step
    a1, a2 = a_a1, a_a2

    b1, b2 = derivative(
        theta1 + legge_orararia(a1, a_v1 + a1 * h / 2, h / 2),
        theta2 + legge_orararia(a2, a_v2 + a2 * h / 2, h / 2)
    )

    c1, c2 = derivative(theta1 + legge_orararia(b1, a_v1 + b1 * h / 2, h / 2),
                        theta2 + legge_orararia(b2, a_v2 + b2 * h / 2, h / 2)
                        )

    d1, d2 = derivative(theta1 + legge_orararia(c1, a_v1 + c1 * h, h),
                        theta2 + legge_orararia(c2, a_v2 + c2 * h, h)
                        )

    omega1 = a_v1 + (h / 6) * (a1 + 2 * b1 + 2 * c1 + d1)
    omega2 = a_v2 + (h / 6) * (a2 + 2 * b2 + 2 * c2 + d2)

    return omega1, omega2


a_a1, a_a2 = derivative(theta1, theta2)

for i in range(0, 10000):
    # print(a_a1, a_a2)

    # a_v1, a_v2 = integrate() #non funziona, dovrebbe seguire l'algoritmo di runge-kutta

    a_v1 += a_a1 * step
    a_v2 += a_a2 * step
    theta1 += a_v1 * step
    theta2 += a_v2 * step
    #theta1 += legge_orararia(a_a1, a_v1, step)
    #theta2 += legge_orararia(a_a2, a_v2, step)

    angles.append((theta1, theta2))

    a_a1, a_a2 = derivative(theta1, theta2)

    """print((theta1, theta2))
    print(a_v1, a_v2)
    print(a_a1, a_a2)"""

f = open("./angles.js", 'w')

f.write("var angles = " + '"' + json.dumps(angles) + '"')
