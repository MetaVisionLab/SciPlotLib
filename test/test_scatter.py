import inspect
import os.path
import sys
import unittest

import numpy as np

from sciplotlib import plot


class TestScatter(unittest.TestCase):

    def test_group_is_none_but_series_is_not_none(self):
        with self.assertRaises(Exception) as context:
            plot.scatter([], series=[])
        self.assertEqual(str(context.exception),
                         "group must not None when series is not None.")

    def test_group_is_none(self):
        data = np.random.randn(2, 100)
        legend_names = ['test group is none']
        plot.scatter(data,
                     legend_names=legend_names,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=inspect.currentframe().f_code.co_name)

    def test_group(self):
        data = np.array([[], []], dtype=float)
        group = np.array([], dtype=int)
        legend_names = []
        for i in range(7):
            legend_names.append(f"group_{i}")
            temp = [[], []]
            temp[0] = i + 0.15 * np.random.randn(10)
            temp[1] = i + 0.15 * np.random.randn(10)
            data = np.concatenate((data, temp), axis=1)
            group = np.concatenate((group, np.repeat(i, 10)), axis=0)
        plot.scatter(data,
                     group=group,
                     legend_names=legend_names,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=inspect.currentframe().f_code.co_name)

    def test_group_and_series(self):
        data = np.array([[], []], dtype=float)
        group = np.array([], dtype=int)
        legend_names = []
        series = np.array([], dtype=int)
        for i in range(4):
            legend_names.append(f"series_{i}")
            for j in range(7):
                temp = [[], []]
                temp[0] = j + 0.1 * np.random.randn(10)
                temp[1] = i + 0.1 * np.random.randn(10)
                data = np.concatenate((data, temp), axis=1)
                series = np.concatenate((series, np.repeat(i, 10)), axis=0)
                group = np.concatenate((group, np.repeat(j, 10)), axis=0)
        plot.scatter(data,
                     group=group,
                     legend_names=legend_names,
                     series=series,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    unittest.main()
