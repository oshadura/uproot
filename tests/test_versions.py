#!/usr/bin/env python

# Copyright 2017 DIANA-HEP
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import numpy

import uproot

class TestVersions(unittest.TestCase):
    def runTest(self):
        pass

    sample = {
        b"n": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4],

        b"b": [True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False],
        b"ab": [[False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True], [False, True, False], [True, False, True]],
        b"Ab": [[], [True], [True, True], [True, True, True], [True, True, True, True], [], [False], [False, False], [False, False, False], [False, False, False, False], [], [True], [True, True], [True, True, True], [True, True, True, True], [], [False], [False, False], [False, False, False], [False, False, False, False], [], [True], [True, True], [True, True, True], [True, True, True, True], [], [False], [False, False], [False, False, False], [False, False, False, False]],

        b"i1": [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        b"ai1": [[-14, -13, -12], [-13, -12, -11], [-12, -11, -10], [-11, -10, -9], [-10, -9, -8], [-9, -8, -7], [-8, -7, -6], [-7, -6, -5], [-6, -5, -4], [-5, -4, -3], [-4, -3, -2], [-3, -2, -1], [-2, -1, 0], [-1, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17]],
        b"Ai1": [[], [-15], [-15, -13], [-15, -13, -11], [-15, -13, -11, -9], [], [-10], [-10, -8], [-10, -8, -6], [-10, -8, -6, -4], [], [-5], [-5, -3], [-5, -3, -1], [-5, -3, -1, 1], [], [0], [0, 2], [0, 2, 4], [0, 2, 4, 6], [], [5], [5, 7], [5, 7, 9], [5, 7, 9, 11], [], [10], [10, 12], [10, 12, 14], [10, 12, 14, 16]],

        b"u1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        b"au1": [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17], [16, 17, 18], [17, 18, 19], [18, 19, 20], [19, 20, 21], [20, 21, 22], [21, 22, 23], [22, 23, 24], [23, 24, 25], [24, 25, 26], [25, 26, 27], [26, 27, 28], [27, 28, 29], [28, 29, 30], [29, 30, 31], [30, 31, 32]],
        b"Au1": [[], [0], [0, 2], [0, 2, 4], [0, 2, 4, 6], [], [5], [5, 7], [5, 7, 9], [5, 7, 9, 11], [], [10], [10, 12], [10, 12, 14], [10, 12, 14, 16], [], [15], [15, 17], [15, 17, 19], [15, 17, 19, 21], [], [20], [20, 22], [20, 22, 24], [20, 22, 24, 26], [], [25], [25, 27], [25, 27, 29], [25, 27, 29, 31]],

        b"i2": [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        b"ai2": [[-14, -13, -12], [-13, -12, -11], [-12, -11, -10], [-11, -10, -9], [-10, -9, -8], [-9, -8, -7], [-8, -7, -6], [-7, -6, -5], [-6, -5, -4], [-5, -4, -3], [-4, -3, -2], [-3, -2, -1], [-2, -1, 0], [-1, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17]],
        b"Ai2": [[], [-15], [-15, -13], [-15, -13, -11], [-15, -13, -11, -9], [], [-10], [-10, -8], [-10, -8, -6], [-10, -8, -6, -4], [], [-5], [-5, -3], [-5, -3, -1], [-5, -3, -1, 1], [], [0], [0, 2], [0, 2, 4], [0, 2, 4, 6], [], [5], [5, 7], [5, 7, 9], [5, 7, 9, 11], [], [10], [10, 12], [10, 12, 14], [10, 12, 14, 16]],

        b"u2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        b"au2": [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17], [16, 17, 18], [17, 18, 19], [18, 19, 20], [19, 20, 21], [20, 21, 22], [21, 22, 23], [22, 23, 24], [23, 24, 25], [24, 25, 26], [25, 26, 27], [26, 27, 28], [27, 28, 29], [28, 29, 30], [29, 30, 31], [30, 31, 32]],
        b"Au2": [[], [0], [0, 2], [0, 2, 4], [0, 2, 4, 6], [], [5], [5, 7], [5, 7, 9], [5, 7, 9, 11], [], [10], [10, 12], [10, 12, 14], [10, 12, 14, 16], [], [15], [15, 17], [15, 17, 19], [15, 17, 19, 21], [], [20], [20, 22], [20, 22, 24], [20, 22, 24, 26], [], [25], [25, 27], [25, 27, 29], [25, 27, 29, 31]],

        b"i4": [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        b"ai4": [[-14, -13, -12], [-13, -12, -11], [-12, -11, -10], [-11, -10, -9], [-10, -9, -8], [-9, -8, -7], [-8, -7, -6], [-7, -6, -5], [-6, -5, -4], [-5, -4, -3], [-4, -3, -2], [-3, -2, -1], [-2, -1, 0], [-1, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17]],
        b"Ai4": [[], [-15], [-15, -13], [-15, -13, -11], [-15, -13, -11, -9], [], [-10], [-10, -8], [-10, -8, -6], [-10, -8, -6, -4], [], [-5], [-5, -3], [-5, -3, -1], [-5, -3, -1, 1], [], [0], [0, 2], [0, 2, 4], [0, 2, 4, 6], [], [5], [5, 7], [5, 7, 9], [5, 7, 9, 11], [], [10], [10, 12], [10, 12, 14], [10, 12, 14, 16]],

        b"u4": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        b"au4": [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17], [16, 17, 18], [17, 18, 19], [18, 19, 20], [19, 20, 21], [20, 21, 22], [21, 22, 23], [22, 23, 24], [23, 24, 25], [24, 25, 26], [25, 26, 27], [26, 27, 28], [27, 28, 29], [28, 29, 30], [29, 30, 31], [30, 31, 32]],
        b"Au4": [[], [0], [0, 2], [0, 2, 4], [0, 2, 4, 6], [], [5], [5, 7], [5, 7, 9], [5, 7, 9, 11], [], [10], [10, 12], [10, 12, 14], [10, 12, 14, 16], [], [15], [15, 17], [15, 17, 19], [15, 17, 19, 21], [], [20], [20, 22], [20, 22, 24], [20, 22, 24, 26], [], [25], [25, 27], [25, 27, 29], [25, 27, 29, 31]],

        b"i8": [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        b"ai8": [[-14, -13, -12], [-13, -12, -11], [-12, -11, -10], [-11, -10, -9], [-10, -9, -8], [-9, -8, -7], [-8, -7, -6], [-7, -6, -5], [-6, -5, -4], [-5, -4, -3], [-4, -3, -2], [-3, -2, -1], [-2, -1, 0], [-1, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17]],
        b"Ai8": [[], [-15], [-15, -13], [-15, -13, -11], [-15, -13, -11, -9], [], [-10], [-10, -8], [-10, -8, -6], [-10, -8, -6, -4], [], [-5], [-5, -3], [-5, -3, -1], [-5, -3, -1, 1], [], [0], [0, 2], [0, 2, 4], [0, 2, 4, 6], [], [5], [5, 7], [5, 7, 9], [5, 7, 9, 11], [], [10], [10, 12], [10, 12, 14], [10, 12, 14, 16]],

        b"u8": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        b"au8": [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17], [16, 17, 18], [17, 18, 19], [18, 19, 20], [19, 20, 21], [20, 21, 22], [21, 22, 23], [22, 23, 24], [23, 24, 25], [24, 25, 26], [25, 26, 27], [26, 27, 28], [27, 28, 29], [28, 29, 30], [29, 30, 31], [30, 31, 32]],
        b"Au8": [[], [0], [0, 2], [0, 2, 4], [0, 2, 4, 6], [], [5], [5, 7], [5, 7, 9], [5, 7, 9, 11], [], [10], [10, 12], [10, 12, 14], [10, 12, 14, 16], [], [15], [15, 17], [15, 17, 19], [15, 17, 19, 21], [], [20], [20, 22], [20, 22, 24], [20, 22, 24, 26], [], [25], [25, 27], [25, 27, 29], [25, 27, 29, 31]],

        b"f4": [-14.899999618530273, -13.899999618530273, -12.899999618530273, -11.899999618530273, -10.899999618530273, -9.899999618530273, -8.899999618530273, -7.900000095367432, -6.900000095367432, -5.900000095367432, -4.900000095367432, -3.9000000953674316, -2.9000000953674316, -1.899999976158142, -0.8999999761581421, 0.10000000149011612, 1.100000023841858, 2.0999999046325684, 3.0999999046325684, 4.099999904632568, 5.099999904632568, 6.099999904632568, 7.099999904632568, 8.100000381469727, 9.100000381469727, 10.100000381469727, 11.100000381469727, 12.100000381469727, 13.100000381469727, 14.100000381469727],
        b"af4": [[-13.899999618530273, -12.899999618530273, -11.899999618530273], [-12.899999618530273, -11.899999618530273, -10.899999618530273], [-11.899999618530273, -10.899999618530273, -9.899999618530273], [-10.899999618530273, -9.899999618530273, -8.899999618530273], [-9.899999618530273, -8.899999618530273, -7.900000095367432], [-8.899999618530273, -7.900000095367432, -6.900000095367432], [-7.900000095367432, -6.900000095367432, -5.900000095367432], [-6.900000095367432, -5.900000095367432, -4.900000095367432], [-5.900000095367432, -4.900000095367432, -3.9000000953674316], [-4.900000095367432, -3.9000000953674316, -2.9000000953674316], [-3.9000000953674316, -2.9000000953674316, -1.899999976158142], [-2.9000000953674316, -1.899999976158142, -0.8999999761581421], [-1.899999976158142, -0.8999999761581421, 0.10000000149011612], [-0.8999999761581421, 0.10000000149011612, 1.100000023841858], [0.10000000149011612, 1.100000023841858, 2.0999999046325684], [1.100000023841858, 2.0999999046325684, 3.0999999046325684], [2.0999999046325684, 3.0999999046325684, 4.099999904632568], [3.0999999046325684, 4.099999904632568, 5.099999904632568], [4.099999904632568, 5.099999904632568, 6.099999904632568], [5.099999904632568, 6.099999904632568, 7.099999904632568], [6.099999904632568, 7.099999904632568, 8.100000381469727], [7.099999904632568, 8.100000381469727, 9.100000381469727], [8.100000381469727, 9.100000381469727, 10.100000381469727], [9.100000381469727, 10.100000381469727, 11.100000381469727], [10.100000381469727, 11.100000381469727, 12.100000381469727], [11.100000381469727, 12.100000381469727, 13.100000381469727], [12.100000381469727, 13.100000381469727, 14.100000381469727], [13.100000381469727, 14.100000381469727, 15.100000381469727], [14.100000381469727, 15.100000381469727, 16.100000381469727], [15.100000381469727, 16.100000381469727, 17.100000381469727]],
        b"Af4": [[], [-15.0], [-15.0, -13.899999618530273], [-15.0, -13.899999618530273, -12.800000190734863], [-15.0, -13.899999618530273, -12.800000190734863, -11.699999809265137], [], [-10.0], [-10.0, -8.899999618530273], [-10.0, -8.899999618530273, -7.800000190734863], [-10.0, -8.899999618530273, -7.800000190734863, -6.699999809265137], [], [-5.0], [-5.0, -3.9000000953674316], [-5.0, -3.9000000953674316, -2.799999952316284], [-5.0, -3.9000000953674316, -2.799999952316284, -1.7000000476837158], [], [0.0], [0.0, 1.100000023841858], [0.0, 1.100000023841858, 2.200000047683716], [0.0, 1.100000023841858, 2.200000047683716, 3.299999952316284], [], [5.0], [5.0, 6.099999904632568], [5.0, 6.099999904632568, 7.199999809265137], [5.0, 6.099999904632568, 7.199999809265137, 8.300000190734863], [], [10.0], [10.0, 11.100000381469727], [10.0, 11.100000381469727, 12.199999809265137], [10.0, 11.100000381469727, 12.199999809265137, 13.300000190734863]],

        b"f8": [-14.9, -13.9, -12.9, -11.9, -10.9, -9.9, -8.9, -7.9, -6.9, -5.9, -4.9, -3.9000000000000004, -2.9000000000000004, -1.9000000000000004, -0.9000000000000004, 0.09999999999999964, 1.0999999999999996, 2.0999999999999996, 3.0999999999999996, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1, 10.1, 11.1, 12.1, 13.1, 14.1],
        b"af8": [[-13.9, -12.9, -11.9], [-12.9, -11.9, -10.9], [-11.9, -10.9, -9.9], [-10.9, -9.9, -8.9], [-9.9, -8.9, -7.9], [-8.9, -7.9, -6.9], [-7.9, -6.9, -5.9], [-6.9, -5.9, -4.9], [-5.9, -4.9, -3.9000000000000004], [-4.9, -3.9000000000000004, -2.9000000000000004], [-3.9000000000000004, -2.9000000000000004, -1.9000000000000004], [-2.9000000000000004, -1.9000000000000004, -0.9000000000000004], [-1.9000000000000004, -0.9000000000000004, 0.09999999999999964], [-0.9000000000000004, 0.09999999999999964, 1.0999999999999996], [0.09999999999999964, 1.0999999999999996, 2.0999999999999996], [1.0999999999999996, 2.0999999999999996, 3.0999999999999996], [2.0999999999999996, 3.0999999999999996, 4.1], [3.0999999999999996, 4.1, 5.1], [4.1, 5.1, 6.1], [5.1, 6.1, 7.1], [6.1, 7.1, 8.1], [7.1, 8.1, 9.1], [8.1, 9.1, 10.1], [9.1, 10.1, 11.1], [10.1, 11.1, 12.1], [11.1, 12.1, 13.1], [12.1, 13.1, 14.1], [13.1, 14.1, 15.1], [14.1, 15.1, 16.1], [15.1, 16.1, 17.1]],
        b"Af8": [[], [-15.0], [-15.0, -13.9], [-15.0, -13.9, -12.8], [-15.0, -13.9, -12.8, -11.7], [], [-10.0], [-10.0, -8.9], [-10.0, -8.9, -7.8], [-10.0, -8.9, -7.8, -6.7], [], [-5.0], [-5.0, -3.9], [-5.0, -3.9, -2.8], [-5.0, -3.9, -2.8, -1.7], [], [0.0], [0.0, 1.1], [0.0, 1.1, 2.2], [0.0, 1.1, 2.2, 3.3], [], [5.0], [5.0, 6.1], [5.0, 6.1, 7.2], [5.0, 6.1, 7.2, 8.3], [], [10.0], [10.0, 11.1], [10.0, 11.1, 12.2], [10.0, 11.1, 12.2, 13.3]],

        b"str": [b"hey-0", b"hey-1", b"hey-2", b"hey-3", b"hey-4", b"hey-5", b"hey-6", b"hey-7", b"hey-8", b"hey-9", b"hey-10", b"hey-11", b"hey-12", b"hey-13", b"hey-14", b"hey-15", b"hey-16", b"hey-17", b"hey-18", b"hey-19", b"hey-20", b"hey-21", b"hey-22", b"hey-23", b"hey-24", b"hey-25", b"hey-26", b"hey-27", b"hey-28", b"hey-29"]
        }

    def compare(self, arrays):
        self.assertEqual(set(arrays.keys()), set(self.sample.keys()))
        for name in arrays.keys():
            expect = [y for x in self.sample[name] for y in x] if name.startswith(b"A") else self.sample[name]
            self.assertEqual(arrays[name].tolist(), expect)

    def test_5_23_02(self):
        # 2009-02-26, TTree version 16
        for compression in "uncompressed", "zlib":
            self.compare(uproot.open("tests/sample-5.23.02-{0}.root".format(compression))["sample"].arrays())
    
    def test_5_24_00(self):
        # 2009-06-30, TTree version 16
        for compression in "uncompressed", "zlib":
            self.compare(uproot.open("tests/sample-5.24.00-{0}.root".format(compression))["sample"].arrays())
    
    def test_5_25_02(self):
        # 2009-10-01, TTree version 17
        for compression in "uncompressed", "zlib":
            self.compare(uproot.open("tests/sample-5.25.02-{0}.root".format(compression))["sample"].arrays())
    
    def test_5_26_00(self):
        # 2009-12-14, TTree version 18
        for compression in "uncompressed", "zlib":
            self.compare(uproot.open("tests/sample-5.26.00-{0}.root".format(compression))["sample"].arrays())

    def test_5_27_02(self):
        # 2010-04-27, TTree version 18
        for compression in "uncompressed", "zlib":
            self.compare(uproot.open("tests/sample-5.27.02-{0}.root".format(compression))["sample"].arrays())

    def test_5_28_00(self):
        # 2010-12-15, TTree version 18
        for compression in "uncompressed", "zlib":
            self.compare(uproot.open("tests/sample-5.28.00-{0}.root".format(compression))["sample"].arrays())

    def test_5_29_02(self):
        # 2011-04-21, TTree version 18
        for compression in "uncompressed", "zlib":
            self.compare(uproot.open("tests/sample-5.29.02-{0}.root".format(compression))["sample"].arrays())

    def test_5_30_00(self):
        # 2011-06-28, TTree version 19
        for compression in "uncompressed", "zlib", "lzma":
            self.compare(uproot.open("tests/sample-5.30.00-{0}.root".format(compression))["sample"].arrays())

    def test_6_08_04(self):
        # 2017-01-13, TTree version 19
        for compression in "uncompressed", "zlib", "lzma":
            self.compare(uproot.open("tests/sample-6.08.04-{0}.root".format(compression))["sample"].arrays())

    def test_6_10_05(self):
        # 2017-07-28, TTree version 19
        for compression in "uncompressed", "zlib", "lzma", "lz4":
            self.compare(uproot.open("tests/sample-6.10.05-{0}.root".format(compression))["sample"].arrays())
