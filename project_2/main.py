import decimal
import math

X_I = 1000
a = 24693
c = 3517
K = pow(2, 17)

# CDF

L = 1 / 12


class OutOfDomainError(ArithmeticError):
    pass


def generate_random_number(i) -> decimal:
    if i == 0:
        ret = X_I
    else:
        ret = (generate_random_number(i - 1) * a + c)
    return ret % K


def rand_num(i):
    return generate_random_number(i) / K


def cdf(x_i):
    """
    The CDF as described in section 5

    :param x_i: The continuous variable
    :return: u_i, the probability that X ≤ x_i
    """
    if (x_i < 0):
        raise OutOfDomainError(f"x_i must be ≥ 0. Instead, it was {x_i}")
    u_i = L * pow(math.e, -L * x_i)
    return u_i


def cdf_inv(u_i):
    """
    The inverse of the CDF function

    :param u_i: the probability that X ≤ x_i
    :return: x_i, the continuous variable
    """
    if u_i < 0 or u_i > 1:
        raise OutOfDomainError(f"u_i must be inclusively between 0 and 1. Instead, it was {u_i}")
    x_i = (math.log(u_i / L, math.e)) / -L
    return x_i