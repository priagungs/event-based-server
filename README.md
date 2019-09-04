# event-based-server
## Metode Benchmark
Tool Benchmarking yang digunakan adalah _ApacheBench_.
Pengujian dilakukan dengan cara melakukan request sebanyak 100.000 kali, dengan banyaknya konkurensi 10.000 (sesuai c10k). Caranya, cukup memasukkan command 
`ab -n 100000 -c 10000 http://example.com`
* n = banyaknya request
* c = banyaknya konkurensi

### Hasil Pengujian pada NGINX dan Apache
* Hasil Pengujian NGINX
```

```