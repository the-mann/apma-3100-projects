from unittest import TestCase

from project_2.main import rand_num, cdf, cdf_inv, OutOfDomainError


class Test(TestCase):
    def test_first_three_numbers(self):
        self.assertAlmostEqual(rand_num(1), 0.4195, 4)
        self.assertAlmostEqual(rand_num(2), 0.0425, 4)
        self.assertAlmostEqual(rand_num(3), 0.1274, 4)

    def test_51_52_53(self):
        self.skipTest("not implemented")

    def test_cdf_inverse_is_inverse(self):
        self.assertAlmostEqual(cdf(50), 0.0012919877999174442)
        self.assertAlmostEqual(cdf_inv(0.0012919877999174442), 50)

    def test_cdf_less_than_zero(self):
        with self.assertRaises(OutOfDomainError) as cm:
            cdf(-1)
        with self.assertRaises(OutOfDomainError) as cm:
            cdf_inv(1.0000001)
