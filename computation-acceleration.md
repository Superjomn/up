# Several methods to accelerate loop computation

## Memory locality
To fit the cache, the inner loop should visit continuous memory, 
if a row-wise matrix is visited by col-wise inner loop, that will be in a bad performance.

For example, to calculate the dot sum of two vectors

$$
c_{i,l} = \sum_m a_{i,m}b_{m,l}
$$

the loop variable `m` walks the columns of A and rows of B, A is best stored in row-major order,
while B is best stored in column-major order.

## Loop unrolling
The compiler can help to optimize the code, so if we unroll the loop and take the compiler to optimize it,
that should get a better performance.

For example, a loop

```c++
for (int i = 0; i < 1000; i++) {
  c += a[i] * b[i];
}
```

one can partially unroll the computation by accumulating multiple elements at a time:

```c++
for (int i = 0; i < 1000; i+=4) {
  c += a[i]*b[i] + a[i+1]*b[i+1] + a[i+2]*b[i+2] + a[i+3]*b[i+3];
}
```

A second technique is to use multiple accumulators in parallel:

```c++
int c0 = c1 = c2 = c3 = 0;
for (int i = 0; i < 1000; i+=4) {
  c0 += a[i] * b[i];
  c1 += a[i+1] * b[i+1];
  c2 += a[i+2] * b[i+2];
  c3 += a[i+3] * b[i+3];
}

int c = c0 + c1 + c2 + c3;
```
## SIMD(Single instruction, multiple data)
SIMD instructions are the fundamental building blocks of low-level parallelization on CPUs. 
They typically operate on 16 bytes worth of data at a time: 2 doubles, 4 floats, 8 shorts or 16 bytes at a time. 

<p align="center">
  <img src="./wiki-images/1.png" />
</p>

```c++
#include <mmintrin.h>
__m128 c = _mm_add_ps(a, b);
```

TODO more examples and references.

These instructions preform multiple operations in parallel on continuous data, making the issues of data locality even more critical, so

1. the memory should be 16-byte aligned.
2. if a data vector is not a multiple of 16 bytes in size, one will have to deal with edge effects, zero-padding at the end.

SIMD instructions generally operate faster on 16 byte blocks that are 16-byte aligned in memory.

TODO more example


# Benchmark
[benchmark](./benchmarks.ipynb)
