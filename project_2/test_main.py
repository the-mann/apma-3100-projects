import statistics
from unittest import TestCase

from project_2.main import rand_num_generator, cdf, cdf_inv, OutOfDomainError, guess_time_till_pickup, MonteCarloStats


class Test(TestCase):
    def test_first_three_numbers(self):
        self.assertListEqual([round(i, 4) for i in rand_num_generator(4)], [0.4195, 0.0425, 0.1274, 0.9955])
        self.assertListEqual([cdf_inv(i) for i in rand_num_generator(4)],
                             [6.525801577240943, 0.5214836201646981, 1.6353810411952014, 64.88130145944533])


    def test_51_52_53(self):
        list_of_rand_numbers = [x for x in rand_num_generator(100)]
        self.assertAlmostEqual(0.5157089233398438, list_of_rand_numbers[50])
        self.assertAlmostEqual(0.427276611328125, list_of_rand_numbers[51])
        self.assertAlmostEqual(0.7681961059570312, list_of_rand_numbers[52])

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
        self.assertAlmostEqual(10, statistics.mean(x))

    def test_million_person_4_times(self):
        stats = MonteCarloStats()
        rand_numbers = [x for x in rand_num_generator(4000000)]
        rand_numbers.reverse()
        # rand_numbers_2 = rand_numbers_2[4:]
        z = []
        for j in range(100000):
            x = 0
            for i in range(4):
                g = guess_time_till_pickup(rand_numbers.pop(), stats)
                x += g[0]
                # stop
                if g[1]:
                    break
            z.append(x)

        self.assertAlmostEqual(.2, stats.times_busy / stats.total_times, 1)
        self.assertAlmostEqual(.3, stats.times_unavailable / stats.total_times, 1)
        # Case 3 - .5 = .124 + (.5 0 .124)
        self.assertAlmostEqual(.5, stats.times_available() / stats.total_times, 1)

        # Case 3.a - pick up
        self.assertAlmostEqual(.5 - .124, stats.times_picked_up / stats.total_times, 2)
        # Case 3.b - don't reach the phone in time
        self.assertAlmostEqual(0.124, stats.didnt_reach_phone / stats.total_times, 2)

        self.assertEqual(52.89081954200399, statistics.mean(z))

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
