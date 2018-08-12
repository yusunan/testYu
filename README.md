Current result

2018-08-12 21:59:20,967 - root - INFO - -------------- Execute TestCases ---------------
2018-08-12 21:59:22,120 - root - INFO - --------Number: 1 Check status passed--------
2018-08-12 21:59:22,126 - root - INFO - --------Number: 1 Check body passed--------
2018-08-12 21:59:22,578 - root - INFO - --------Number: 2 Check status passed--------
2018-08-12 21:59:22,578 - root - INFO - --------Number: 2 Check body passed--------
2018-08-12 21:59:23,506 - root - ERROR - --------Number: 3 Check status code failed------Expect: 403, But found: 200
2018-08-12 21:59:24,457 - root - INFO - --------Number: 4 Check status passed--------
2018-08-12 21:59:24,463 - root - ERROR - --------Check body failed------Expect: 100, But found: 500
2018-08-12 21:59:24,463 - root - ERROR - --------Number: 4 Check body failed------
+--------+----------------+-----------------------------------------------------------------+--------------------------------------+--------+
| Number |  Description   | URL                                                             |                 Data                 | Result |
+--------+----------------+-----------------------------------------------------------------+--------------------------------------+--------+
|   1    | 正常取得比赛ID | http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/ | key=B0B7CEE0FFBD6AD9A807EC1E471D1D2E |  Pass  |
|   2    |    key为空     | http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/ |                                      |  Pass  |
|   3    |  failed case1  | http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/ | key=B0B7CEE0FFBD6AD9A807EC1E471D1D2E | Failed |
|   4    |  failed case2  | http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/ | key=B0B7CEE0FFBD6AD9A807EC1E471D1D2E | Failed |
+--------+----------------+-----------------------------------------------------------------+--------------------------------------+--------+

Process finished with exit code 0