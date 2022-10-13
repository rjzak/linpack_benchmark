ALL: linpack_bench_single linpack_bench_double linpack_bench_quad

linpack_bench_single: linpack_bench_s.f90
	gfortran -O3 linpack_bench_s.f90 -o linpack_bench_single

linpack_bench_double: linpack_bench_d.f90
	gfortran -O3 linpack_bench_d.f90 -o linpack_bench_double

linpack_bench_quad: linpack_bench_q.f90
	gfortran -O3 linpack_bench_q.f90 -o linpack_bench_quad

.phony: clean
clean:
	rm -f linpack_bench_single linpack_bench_double linpack_bench_quad
