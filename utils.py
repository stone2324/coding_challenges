import timeit

def print_output(funcs):
    for name, func in funcs:
        print(f"{name}: {func()}")

def assert_all_equal(funcs):
    """Ensure all functions return the same output."""
    results = [func() for _, func in funcs]
    first_result = results[0]
    for i, result in enumerate(results[1:], start=1):
        assert result == first_result, f"Mismatch between {funcs[0][0]} and {funcs[i][0]}"
    print("✅ All functions return the same output.")

def benchmark_functions(funcs, n_runs):
    for name, func in funcs:
        elapsed = timeit.timeit(func, number=n_runs)
        print(f"{name}: {elapsed:.6f} seconds for {n_runs} runs")