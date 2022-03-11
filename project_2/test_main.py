import statistics
from unittest import TestCase

from project_2.main import rand_num_generator, cdf, cdf_inv, OutOfDomainError, guess_time_till_pickup


class Test(TestCase):
    def test_first_three_numbers(self):
        self.assertListEqual([round(i, 4) for i in rand_num_generator(3)], [0.4195, 0.0425, 0.1274])

    def test_51_52_53(self):
        self.skipTest("not implemented")

    def test_cdf_inverse_is_inverse(self):
        self.assertAlmostEqual(cdf(50), 0.9844961464009907)
        self.assertAlmostEqual(cdf_inv(0.9844961464009907), 50)

    def test_cdf_less_than_zero(self):
        with self.assertRaises(OutOfDomainError) as cm:
            cdf(-1)
        with self.assertRaises(OutOfDomainError) as cm:
            cdf_inv(1.0000001)

    def test_average_of_guess_time_till_pickup(self):
        x = [guess_time_till_pickup(cdf(n))[0] for n in rand_num_generator(10000)]
        self.assertAlmostEqual(9, statistics.mean(x))

    def test_million_person_4_times(self):
        rand_numbers = [x for x in rand_num_generator(10000000)]
        z = []
        for j in range(1000000):
            x = 0
            for i in range(4):
                g = guess_time_till_pickup(rand_numbers[4 * j + i])

                x += g[0] if g[1] else 0
                # stop
                if g[1]:
                    break
            z.append(x)
        self.assertAlmostEqual(17.214436477758387, statistics.fmean(z), 1)

    def test_average_random_number_2_decimal_places(self):
        x = [x_i for x_i in rand_num_generator(100000)]
        self.assertAlmostEqual(.5, statistics.mean(x), 2)
        pass

    def test_sum_of_cdf(self):
        self.assertEqual(1, cdf(100000))

    def test_greater_than_25(self):
        self.assertAlmostEqual(0.12451447144412309, 1 - cdf(25))

    def test_less_than_6(self):
        self.assertAlmostEqual(0.3934693402873666, cdf(6))