| Machine          | Application       | Precision | Language | MFlops Avg | MFlops Min | MFlops Max | MFlops Std Dev | Iters | Seconds |
| ---------------- | ----------------- |-----------| -------- | ---------- | ---------- | ---------- |----------------| ----- |---------|
| Apple M1         | Native            | Single    | Fortran  | 12940.70   | 12260.00   | 13040.00   | 123.14         | 100   | 6.67    |
| Apple M1         | Native            | Double    | Fortran  |  6258.73   |  6025.00   |  6318.00   | 38.45          | 100   | 12.24   |
| Apple M1         | Native            | Double    | C        |  5016.30   |  4847.90   |  5040.42   | 21.68          | 100   | 14.94   |
| Apple M1         | Native            | Quad      | Fortran  |    52.27   |    53.20   |    54.46   | 0.14           | 100   | 1267.03 |
| Apple M4 Max     | Native            | Single    | Fortran  | 23440.30   | 15230.00   | 24380.00   | 964.80         | 100   | 4.04    |
| Apple M4 Max     | Native            | Double    | Fortran  | 12479.35   |  9185.00   | 12830.00   | 373.35         | 100   | 6.56    |
| Apple M4 Max     | Native            | Double    | C        |  9181.71   |  7166.92   |  9472.54   | 234.22         | 100   | 8.62    |
| Apple M4 Max     | Native            | Quad      | Fortran  |    88.51   |    86.79   |    90.72   | 0.96           | 100   | 775.42  |
| IBM POWER9       | Native            | Single    | Fortran  |  7077.27   |  6444.00   |  7153.00   | 92.80          | 100   | 13.00   |
| IBM POWER9       | Native            | Double    | Fortran  |  4089.31   |  3883.00   |  4131.00   | 43.70          | 100   | 20.16   |
| IBM POWER9       | Native            | Double    | C        |  4311.81   |  4070.81   |  4352.45   | 41.12          | 100   | 20.04   |
| IBM POWER9       | Native            | Quad      | Fortran  |   170.41   |   164.70   |   171.80   | 1.37           | 100   | 414.56  |
| Intel i7-6700K   | Native            | Single    | Fortran  |  8080.98   |  6646.00   | 11490.00   | 1331.55        | 100   | 10.92   |
| Intel i7-6700K   | Native            | Double    | Fortran  |  3738.88   |  2871.00   |  6082.00   | 970.84         | 100   | 21.38   |
| Intel i7-6700K   | Native            | Double    | C        |  3993.95   |  2861.99   |  6909.50   | 1236.74        | 100   | 21.08   |
| Intel i7-6700K   | Native            | Quad      | Fortran  |    32.82   |    31.51   |    33.52   | 0.33           | 100   | 2094.10 |
| Intel i7-9750H   | Native            | Single    | Fortran  | 11134.40   |  9705.00   | 11520.00   | 291.62         | 100   | 7.65    |
| Intel i7-9750H   | Native            | Double    | Fortran  |  6112.12   |  5588.00   |  6460.00   | 165.42         | 100   | 12.77   |
| Intel i7-9750H   | Native            | Double    | C        |  7026.79   |  6179.97   |  7311.27   | 203.05         | 100   | 11.75   |
| Intel i7-9750H   | Native            | Quad      | Fortran  |    44.08   |    45.65   |    40.88   | 0.88           | 100   | 1558.26 |
| Intel i5-1035G7  | Native            | Single    | Fortran  |  3882.29   |  3684.00   |  3984.00   | 58.32          | 100   | 27.07   |
| Intel i5-1035G7  | Native            | Double    | Fortran  |  1870.01   |  1818.00   |  1904.00   | 17.51          | 100   | 46.26   |
| Intel i5-1035G7  | Native            | Double    | C        |  1960.79   |  1904.63   |  1992.77   | 19.09          | 100   | 45.29   |
| Intel i5-1035G7  | Native            | Quad      | Fortran  |    20.80   |    20.61   |    21.41   | 0.16           | 100   | 3624.80 |
| Intel i5-1035G7  | Enarx[^1] SGX[^2] | Double    | C        |   388.06   |   317.73   |   794.73   | 47.65          | 100   | 1088.42 |
| Raspberry Pi 3   | Native            | Single    | Fortran  |    90.76   |    81.05   |   111.00   | 6.62           | 100   | 784.07  |
| Raspberry Pi 3   | Native            | Double    | Fortran  |    62.28   |    57.85   |    71.77   | 3.24           | 100   | 1132.48 |
| Raspberry Pi 3   | Native            | Double    | C        |    71.89   |    63.93   |    86.92   | 4.55           | 100   | 997.02  |
| Raspberry Pi 4   | Native            | Single    | Fortran  |   440.37   |   417.40   |   477.60   | 10.24          | 100   | 158.41  |
| Raspberry Pi 4   | Native            | Double    | Fortran  |   277.90   |   254.80   |   284.70   | 5.50           | 100   | 248.90  |
| Raspberry Pi 4   | Native            | Quad      | Fortran  |    13.18   |    12.03   |    13.24   | 0.12           | 100   | 5212.57 |
| Pine64 RockPro64 | Native            | Single    | Fortran  |   648.01   |   603.00   |   690.60   | 19.43          | 100   | 110.54  |
| Pine64 RockPro64 | Native            | Double    | Fortran  |   377.98   |   360.40   |   393.20   | 6.72           | 100   | 185.18  |
| Pine64 RockPro64 | Native            | Double    | C        |   377.18   |   356.08   |   395.74   | 9.16           | 100   | 187.56  |
| Pine64 RockPro64 | Native            | Quad      | Fortran  |    16.13   |    15.94   |    16.20   | 0.07           | 100   | 4262.29 |

All results are single-threaded.

[^1]: The version of Enarx used was 0.7.1, hash [7ee95ce4](https://github.com/enarx/enarx/tree/7ee95ce4512ad1856f7517231a99680cc50d5478).

[^2]: Enarx with SGX start-up delay across 15 starts had an average of 8.53 seconds, with a maximum of 27 seconds, minimum of 3 seconds, and a standard deviation of 6.42.

