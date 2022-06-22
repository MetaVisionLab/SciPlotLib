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

    def test_group_and_group_names_mismatch(self):
        with self.assertRaises(Exception) as context:
            plot.scatter([], group=[], group_names=["1"])
        self.assertEqual(str(context.exception),
                         "The length of group_names does not match group.")

    def test_series_and_series_names_mismatch(self):
        with self.assertRaises(Exception) as context:
            plot.scatter([], group=[], series=[], series_names=["1"])
        self.assertEqual(str(context.exception),
                         "The length of series_names does not match series.")

    def test_group_is_none(self):
        data = np.random.randn(2, 100)
        group_names = ['test group is none']
        plot.scatter(data,
                     group_names=group_names,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=f"{os.path.basename(__file__.split('.')[0])}."
                               f"{self.__class__.__name__}."
                               f"{inspect.currentframe().f_code.co_name}"
                     )

    def test_group(self):
        data = np.array([[], []], dtype=float)
        group = np.array([], dtype=int)
        group_names = []
        for i in range(7):
            group_names.append(f"group_{i}")
            temp = [[], []]
            temp[0] = i + 0.15 * np.random.randn(10)
            temp[1] = i + 0.15 * np.random.randn(10)
            data = np.concatenate((data, temp), axis=1)
            group = np.concatenate((group, np.repeat(i, 10)), axis=0)
        plot.scatter(data,
                     group=group,
                     group_names=group_names,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=f"{os.path.basename(__file__.split('.')[0])}."
                               f"{self.__class__.__name__}."
                               f"{inspect.currentframe().f_code.co_name}"
                     )

    def test_group_fix_marker(self):
        data = np.array([[], []], dtype=float)
        group = np.array([], dtype=int)
        group_names = []
        for i in range(7):
            group_names.append(f"group_{i}")
            temp = [[], []]
            temp[0] = i + 0.15 * np.random.randn(10)
            temp[1] = i + 0.15 * np.random.randn(10)
            data = np.concatenate((data, temp), axis=1)
            group = np.concatenate((group, np.repeat(i, 10)), axis=0)
        plot.scatter(data,
                     group=group,
                     group_names=group_names,
                     fix_marker=True,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=f"{os.path.basename(__file__.split('.')[0])}."
                               f"{self.__class__.__name__}."
                               f"{inspect.currentframe().f_code.co_name}"
                     )

    def test_group_and_series(self):
        data = np.array([[], []], dtype=float)
        group = np.array([], dtype=int)
        series = np.array([], dtype=int)
        for i in range(4):
            for j in range(7):
                temp = [[], []]
                temp[0] = j + 0.1 * np.random.randn(10)
                temp[1] = i + 0.1 * np.random.randn(10)
                data = np.concatenate((data, temp), axis=1)
                series = np.concatenate((series, np.repeat(i, 10)), axis=0)
                group = np.concatenate((group, np.repeat(j, 10)), axis=0)
        plot.scatter(data,
                     group=group,
                     series=series,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=f"{os.path.basename(__file__.split('.')[0])}."
                               f"{self.__class__.__name__}."
                               f"{inspect.currentframe().f_code.co_name}"
                     )

    def test_group_and_series_fix_marker(self):
        data = np.array([[], []], dtype=float)
        group = np.array([], dtype=int)
        series = np.array([], dtype=int)
        for i in range(4):
            for j in range(7):
                temp = [[], []]
                temp[0] = j + 0.1 * np.random.randn(10)
                temp[1] = i + 0.1 * np.random.randn(10)
                data = np.concatenate((data, temp), axis=1)
                series = np.concatenate((series, np.repeat(i, 10)), axis=0)
                group = np.concatenate((group, np.repeat(j, 10)), axis=0)
        plot.scatter(data,
                     group=group,
                     series=series,
                     fix_marker=True,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=f"{os.path.basename(__file__.split('.')[0])}."
                               f"{self.__class__.__name__}."
                               f"{inspect.currentframe().f_code.co_name}"
                     )

    def test_group_names(self):
        data = np.array([[], []], dtype=float)
        group = np.array([], dtype=int)
        group_names = []
        series = np.array([], dtype=int)
        for i in range(4):
            for j in range(7):
                if i == 0:
                    group_names.append(f"group_{j}")
                temp = [[], []]
                temp[0] = j + 0.1 * np.random.randn(10)
                temp[1] = i + 0.1 * np.random.randn(10)
                data = np.concatenate((data, temp), axis=1)
                series = np.concatenate((series, np.repeat(i, 10)), axis=0)
                group = np.concatenate((group, np.repeat(j, 10)), axis=0)
        plot.scatter(data,
                     group=group,
                     group_names=group_names,
                     series=series,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=f"{os.path.basename(__file__.split('.')[0])}."
                               f"{self.__class__.__name__}."
                               f"{inspect.currentframe().f_code.co_name}"
                     )

    def test_series_names(self):
        data = np.array([[], []], dtype=float)
        group = np.array([], dtype=int)
        series = np.array([], dtype=int)
        series_names = []
        for i in range(4):
            series_names.append(f"series_{i}")
            for j in range(7):
                temp = [[], []]
                temp[0] = j + 0.1 * np.random.randn(10)
                temp[1] = i + 0.1 * np.random.randn(10)
                data = np.concatenate((data, temp), axis=1)
                series = np.concatenate((series, np.repeat(i, 10)), axis=0)
                group = np.concatenate((group, np.repeat(j, 10)), axis=0)
        plot.scatter(data,
                     group=group,
                     series=series,
                     series_names=series_names,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=f"{os.path.basename(__file__.split('.')[0])}."
                               f"{self.__class__.__name__}."
                               f"{inspect.currentframe().f_code.co_name}"
                     )

    def test_series_names_fix_marker(self):
        data = np.array([[], []], dtype=float)
        group = np.array([], dtype=int)
        series = np.array([], dtype=int)
        series_names = []
        for i in range(4):
            series_names.append(f"series_{i}")
            for j in range(7):
                temp = [[], []]
                temp[0] = j + 0.1 * np.random.randn(10)
                temp[1] = i + 0.1 * np.random.randn(10)
                data = np.concatenate((data, temp), axis=1)
                series = np.concatenate((series, np.repeat(i, 10)), axis=0)
                group = np.concatenate((group, np.repeat(j, 10)), axis=0)
        plot.scatter(data,
                     group=group,
                     series=series,
                     series_names=series_names,
                     fix_marker=True,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=f"{os.path.basename(__file__.split('.')[0])}."
                               f"{self.__class__.__name__}."
                               f"{inspect.currentframe().f_code.co_name}"
                     )

    def test_group_names_and_series_names(self):
        data = np.array([[], []], dtype=float)
        group = np.array([], dtype=int)
        group_names = []
        series = np.array([], dtype=int)
        series_names = []
        for i in range(4):
            series_names.append(f"series_{i}")
            for j in range(7):
                if i == 0:
                    group_names.append(f"group_{j}")
                temp = [[], []]
                temp[0] = j + 0.1 * np.random.randn(10)
                temp[1] = i + 0.1 * np.random.randn(10)
                data = np.concatenate((data, temp), axis=1)
                series = np.concatenate((series, np.repeat(i, 10)), axis=0)
                group = np.concatenate((group, np.repeat(j, 10)), axis=0)
        plot.scatter(data,
                     group=group,
                     group_names=group_names,
                     series=series,
                     series_names=series_names,
                     save_path=os.path.join(sys.path[0], '../examples'),
                     save_name=f"{os.path.basename(__file__.split('.')[0])}."
                               f"{self.__class__.__name__}."
                               f"{inspect.currentframe().f_code.co_name}"
                     )


if __name__ == "__main__":
    unittest.main()
