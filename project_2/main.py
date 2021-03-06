import math
import sys

X_I = 1000
a = 24693
c = 3517
K = pow(2, 17)

# CDF

L = 1 / 12

sys.setrecursionlimit(100000)


class OutOfDomainError(ArithmeticError):
    pass


def rand_num_generator(num_of_random_numbers):
    i = 0
    prev = X_I % K
    while i < num_of_random_numbers:
        prev = (prev * a + c) % K
        i += 1
        yield prev / K


def cdf(x_i):
    """
    The CDF as described in section 5

    :param x_i: The continuous variable
    :return: u_i, the probability that X ≤ x_i
    """
    if x_i < 0:
        raise OutOfDomainError(f"x_i must be ≥ 0. Instead, it was {x_i}")
    u_i = 1 - pow(math.e, -L * x_i)
    return u_i


def cdf_inv(u_i):
    """
    The inverse of the CDF function

    :param u_i: the probability that X ≤ x_i
    :return: x_i, the continuous variable
    """
    if u_i < 0 or u_i > 1:
        raise OutOfDomainError(f"u_i must be inclusively between 0 and 1. Instead, it was {u_i}")

    x_i = (math.log(1 - u_i, math.e)) / -L
    return x_i


class MonteCarloStats:
    def __init__(self):
        self.didnt_reach_phone = 0
        self.times_busy = 0
        self.times_unavailable = 0

        self.times_picked_up = 0
        self.total_times = 0

    def busy(self):
        self.total_times += 1
        self.times_busy += 1

    def unavailable(self):
        self.total_times += 1
        self.times_unavailable += 1

    def available_picked_up(self):
        self.total_times += 1
        self.times_picked_up += 1

    def didnt_get_to_phone_in_time(self):
        self.didnt_reach_phone += 1
        self.total_times += 1

    def times_available(self):
        return self.didnt_reach_phone + self.times_picked_up


def guess_time_till_pickup(p, u_i2, stats=MonteCarloStats()):
    """
    No matter what, it will take her 6 seconds at least.
    If x_i1 > .2, customer is not busy. otherwise, customer is busy and hang up immediately
    :param stats:
    :param p: The random number between 0 and 1 for checking if customer is busy or unavailable
    """
    # Initial time to start up phone
    time_till_pickup = 6

    if p < 0.2:
        stats.busy()
        return time_till_pickup + 3 + 1, False
    elif .2 <= p < .5:
        stats.unavailable()
        return time_till_pickup + 25 + 1, False
    else:
        # If neither of these variables are true, check what the expected time is for supplied probability

        # Note that we will only wait for 25 seconds. If it takes longer than that, we'll hang up
        if cdf_inv(u_i2) > 25:
            stats.didnt_get_to_phone_in_time()
            return time_till_pickup + 25 + 1, False
        else:
            stats.available_picked_up()
            return time_till_pickup + cdf_inv(u_i2), True
