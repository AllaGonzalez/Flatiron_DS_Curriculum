import unittest2 as unittest
from ipynb.fs.full.index import (budgets, revenues, scaled_m_values, rss_values, b_value, slope_at, updated_m, gradient_descent)

class TestDistance(unittest.TestCase):
    def test_rss_values(self):
        rss_dict = {'m_values': [0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8],
         'rss_values': [64693.76669999998,
          45559.96669999998,
          30626.166699999987,
          19892.36669999999,
          13358.5667,
          11024.766700000004,
          12890.96670000001,
          18957.166700000016,
          29223.36670000002,
          43689.566700000025,
          62355.76670000004]}
        return_value = rss_values(budgets, revenues, scaled_m_values, b_value)
        self.assertEqual(return_value, rss_dict)

    def test_updated_m(self):
        current_slope = slope_at(budgets, revenues, 1.7, 133.33333333333326)['slope']
        self.assertEqual(updated_m(1.7, .000001, current_slope), 1.5343123333335096)
        current_slope = slope_at(budgets, revenues, 1.534, 133.33333333333326)['slope']
        self.assertEqual(updated_m(1.534, .000001, current_slope), 1.43803233333338)


    def test_gradient_descent(self):
        descent_values = gradient_descent(budgets, revenues, 12, 133.33, learning_rate = .000001, current_m = 0)
        self.assertEqual(len(descent_values), 12)
        self.assertEqual(descent_values[-1], {'m': 1.302254618648021, 'rss': 11020.562895703, 'slope': -1370.0601677373925})
        self.assertEqual(descent_values[1], {'m': 0.5483169999998062, 'rss': 131437.9413767516, 'slope': -318023.86000024853})

        higher_descent_values = gradient_descent(budgets, revenues, 10, 133.33, learning_rate = .000001, current_m = 1)
        self.assertEqual(len(higher_descent_values), 10)
        self.assertEqual(higher_descent_values[1], {'m': 1.128316999999879, 'rss': 17615.922576699, 'slope': -74423.85999995167})
