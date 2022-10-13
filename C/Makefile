ALL: linpack_bench

linpack_bench: linpack_bench.c
	gcc -Wall linpack_bench.c -O3 -o linpack_bench

linpack_bench.wasm: linpack_bench.c
	/opt/wasi-sdk/bin/clang linpack_bench.c -o linpack_bench.wasm -O3 -D_WASI_EMULATED_PROCESS_CLOCKS -lwasi-emulated-process-clocks

.phony: clean
clean:
	rm -f linpack_bench linpack_bench.wasm
