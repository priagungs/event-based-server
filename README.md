# IF4031 - Pengembangan Aplikasi Terdistribusi
# Tugas 1 - Event Based Server
## Metode Benchmark
Tool Benchmarking yang digunakan adalah _ApacheBench_.
Pengujian dilakukan dengan cara melakukan request sebanyak 10.000 kali, dengan banyaknya konkurensi 10.000 (sesuai c10k). Caranya, cukup memasukkan command :

`ab -n 10000 -c 10000 http://example.com`

* n = banyaknya request
* c = banyaknya konkurensi

### Hasil Pengujian pada Apache Web Server dan NGINX
1. Hasil Pengujian Apache Web Server
   * HTML ukuran 500 bytes
   ```
   Server Software:        Apache/2.4.29
   Server Hostname:        localhost
   Server Port:            80

   Document Path:          /small.html
   Document Length:        0 bytes

   Concurrency Level:      10000
   Time taken for tests:   2.455 seconds
   Complete requests:      10000
   Failed requests:        278
   (Connect: 0, Receive: 0, Length: 278, Exceptions: 0)
   Total transferred:      264656 bytes
   HTML transferred:       189318 bytes
   Requests per second:    4073.02 [#/sec] (mean)
   Time per request:       2455.179 [ms] (mean)
   Time per request:       0.246 [ms] (mean, across all concurrent requests)
   Transfer rate:          105.27 [Kbytes/sec] received

   Connection Times (ms)
               min  mean[+/-sd] median   max
   Connect:      275 1304 536.5   1388    2083
   Processing:    93  177  55.5    172     366
   Waiting:        0    6  39.6      0     275
   Total:        368 1481 589.4   1559    2449

   Percentage of the requests served within a certain time (ms)
   50%   1559
   66%   1824
   75%   1995
   80%   2087
   90%   2248
   95%   2297
   98%   2433
   99%   2441
   100%   2449 (longest request)
   ```
   * HTML ukuran 20 KB
   ```
   Server Software:        Apache/2.4.29
   Server Hostname:        localhost
   Server Port:            80

   Document Path:          /large.html
   Document Length:        0 bytes

   Concurrency Level:      10000
   Time taken for tests:   2.385 seconds
   Complete requests:      10000
   Failed requests:        278
      (Connect: 0, Receive: 0, Length: 278, Exceptions: 0)
   Total transferred:      5625608 bytes
   HTML transferred:       5549436 bytes
   Requests per second:    4192.63 [#/sec] (mean)
   Time per request:       2385.135 [ms] (mean)
   Time per request:       0.239 [ms] (mean, across all concurrent requests)
   Transfer rate:          2303.33 [Kbytes/sec] received

   Connection Times (ms)
               min  mean[+/-sd] median   max
   Connect:      283 1273 505.3   1343    1999
   Processing:    95  181  57.8    179     377
   Waiting:        0    7  42.9      0     282
   Total:        378 1455 560.0   1521    2377

   Percentage of the requests served within a certain time (ms)
   50%   1521
   66%   1813
   75%   1950
   80%   2012
   90%   2173
   95%   2227
   98%   2359
   99%   2368
   100%   2377 (longest request)
   ```

2. Hasil Pengujian NGINX
   * HTML ukuran 500 bytes
   ```
   Server Software:
   Server Hostname:        localhost
   Server Port:            5050

   Document Path:          /small.html
   Document Length:        0 bytes

   Concurrency Level:      10000
   Time taken for tests:   3.579 seconds
   Complete requests:      10000
   Failed requests:        6000
      (Connect: 0, Receive: 0, Length: 6000, Exceptions: 0)
   Total transferred:      5538000 bytes
   HTML transferred:       4086000 bytes
   Requests per second:    2794.11 [#/sec] (mean)
   Time per request:       3578.956 [ms] (mean)
   Time per request:       0.358 [ms] (mean, across all concurrent requests)
   Transfer rate:          1511.11 [Kbytes/sec] received

   Connection Times (ms)
               min  mean[+/-sd] median   max
   Connect:      616 1811 593.9   1938    2709
   Processing:   255  486 114.4    515     688
   Waiting:        0  205 197.7    188     594
   Total:        871 2297 703.4   2437    3325

   Percentage of the requests served within a certain time (ms)
   50%   2437
   66%   2737
   75%   2917
   80%   3008
   90%   3161
   95%   3219
   98%   3269
   99%   3299
   100%   3325 (longest request)
   ```
   * HTML ukuran 20 KB
   ```
   Server Software:
   Server Hostname:        localhost
   Server Port:            5050

   Document Path:          /large.html
   Document Length:        0 bytes

   Concurrency Level:      10000
   Time taken for tests:   3.306 seconds
   Complete requests:      10000
   Failed requests:        5936
      (Connect: 0, Receive: 0, Length: 5936, Exceptions: 0)
   Total transferred:      119948752 bytes
   HTML transferred:       118494432 bytes
   Requests per second:    3024.79 [#/sec] (mean)
   Time per request:       3306.020 [ms] (mean)
   Time per request:       0.331 [ms] (mean, across all concurrent requests)
   Transfer rate:          35431.56 [Kbytes/sec] received

   Connection Times (ms)
               min  mean[+/-sd] median   max
   Connect:      502 1716 574.0   1811    2540
   Processing:   264  416  80.5    436     578
   Waiting:        0  157 153.5    142     466
   Total:        767 2132 644.9   2254    3042

   Percentage of the requests served within a certain time (ms)
   50%   2254
   66%   2540
   75%   2700
   80%   2777
   90%   2901
   95%   2982
   98%   3019
   99%   3030
   100%   3042 (longest request)
   ```

### Petunjuk Instalasi/Building dan Cara Menjalankan Program Kecil Web Server
1. Program low level library
   * Pastikan _python3_ telah terpasang di perangkat Anda. `sudo apt update && sudo apt install python3 && sudo apt install python3-pip`
   * Install library _pyuv_ `pip3 install pyuv`
   * Jalankan web server `python3 low_level/app.py`

2. Program high level library
   * Pindah ke direktori high_level `cd high_level`
   * Jalankan web server `npm run test` atau `node main.js`

### Hasil Pengujian Program Kecil Web Server
1. Program dengan low level library
   * HTML ukuran 500 bytes
   ```
   Server Software:
   Server Hostname:        localhost
   Server Port:            1234

   Document Path:          /small.html
   Document Length:        0 bytes

   Concurrency Level:      10000
   Time taken for tests:   16.580 seconds
   Complete requests:      8991
   Failed requests:        0
   Total transferred:      767849 bytes
   HTML transferred:       687129 bytes
   Requests per second:    542.29 [#/sec] (mean)
   Time per request:       18440.413 [ms] (mean)
   Time per request:       1.844 [ms] (mean, across all concurrent requests)
   Transfer rate:          45.23 [Kbytes/sec] received

   Connection Times (ms)
               min  mean[+/-sd] median   max
   Connect:      421 2000 798.1   2136    3147
   Processing:   450  697 139.7    698     933
   Waiting:        0    0   0.0      0       0
   Total:       1354 2697 660.9   2835    3597

   Percentage of the requests served within a certain time (ms)
   50%   2834
   66%   3125
   75%   3247
   80%   3334
   90%   3487
   95%   3529
   98%   3563
   99%   3591
   100%   3597 (longest request)
   ```
   * HTML ukuran 20 KB
   ```
   Server Software:
   Server Hostname:        localhost
   Server Port:            1234

   Document Path:          /large.html
   Document Length:        0 bytes

   Concurrency Level:      10000
   Time taken for tests:   5.898 seconds
   Complete requests:      8991
   Failed requests:        0
   Total transferred:      20224396 bytes
   HTML transferred:       20141658 bytes
   Requests per second:    1524.31 [#/sec] (mean)
   Time per request:       6560.349 [ms] (mean)
   Time per request:       0.656 [ms] (mean, across all concurrent requests)
   Transfer rate:          3348.43 [Kbytes/sec] received

   Connection Times (ms)
               min  mean[+/-sd] median   max
   Connect:      428 2006 719.8   2122    3046
   Processing:   194  324  77.5    321     462
   Waiting:        0    0   0.0      0       0
   Total:        622 2330 796.1   2444    3507

   Percentage of the requests served within a certain time (ms)
   50%   2443
   66%   2809
   75%   2998
   80%   3145
   90%   3323
   95%   3408
   98%   3478
   99%   3493
   100%   3507 (longest request)
   ```

   Catatan : Server berhenti beroperasi setelah menangani 8991 request.
   
2. Program dengan high level library
   * HTML ukuran 500 bytes
   ```
   Server Software:
   Server Hostname:        localhost
   Server Port:            8080

   Document Path:          /small
   Document Length:        0 bytes

   Concurrency Level:      10000
   Time taken for tests:   3.934 seconds
   Complete requests:      10000
   Failed requests:        4761
      (Connect: 0, Receive: 0, Length: 4761, Exceptions: 0)
   Total transferred:      3718341 bytes
   HTML transferred:       3242241 bytes
   Requests per second:    2541.77 [#/sec] (mean)
   Time per request:       3934.262 [ms] (mean)
   Time per request:       0.393 [ms] (mean, across all concurrent requests)
   Transfer rate:          922.97 [Kbytes/sec] received

   Connection Times (ms)
               min  mean[+/-sd] median   max
   Connect:      285 1416 559.3   1522    2213
   Processing:   179  752 566.8    276    1439
   Waiting:        0  515 561.6      0    1354
   Total:       1621 2168 264.2   2213    2629

   Percentage of the requests served within a certain time (ms)
   50%   2213
   66%   2330
   75%   2396
   80%   2430
   90%   2487
   95%   2540
   98%   2588
   99%   2617
   100%   2629 (longest request)
   ```
   * HTML ukuran 20 KB
   ```
   Server Software:
   Server Hostname:        localhost
   Server Port:            8080

   Document Path:          /large
   Document Length:        19962 bytes

   Concurrency Level:      10000
   Time taken for tests:   5.492 seconds
   Complete requests:      10000
   Failed requests:        0
   Total transferred:      200620000 bytes
   HTML transferred:       199620000 bytes
   Requests per second:    1820.87 [#/sec] (mean)
   Time per request:       5491.887 [ms] (mean)
   Time per request:       0.549 [ms] (mean, across all concurrent requests)
   Transfer rate:          35674.07 [Kbytes/sec] received

   Connection Times (ms)
               min  mean[+/-sd] median   max
   Connect:      265 1461 595.0   1553    2319
   Processing:  2654 2843  75.5   2869    2915
   Waiting:      695 2002 574.6   2086    2708
   Total:       3175 4304 535.6   4422    4980

   Percentage of the requests served within a certain time (ms)
   50%   4422
   66%   4710
   75%   4807
   80%   4838
   90%   4896
   95%   4919
   98%   4969
   99%   4973
   100%   4980 (longest request)
   ```