def fast_exp(a, x, p):
    y = 1
    s = a
    multiplications = 0
    binary_x = bin(x)[2:]
    print(f"\nBinary representation of x: {binary_x}")
    print("\nComputation trace:")
    print(f"{'Step':<5} | {'Bit':<5} | {'y (before)':<10} | {'s (before)':<10} | {'Action':<20} | {'s (after)':<10} | {'Multiplication'}")
    print("-" * 85)

    step = 0
    for bit in reversed(binary_x):
        x_i = int(bit)
        print(f"{step:<5} | {x_i:<5} | {y:<10} | {s:<10} | ", end="")

        if x_i == 1:
            y = (y * s) % p
            multiplications += 1
            action = f"y = y*s = {y}"
            print(f"{action:<20} | ", end="")
        else:
            print(f"{'Skipping':<20} | ", end="")

        s = (s * s) % p
        multiplications += 1
        print(f"{s:<10} | {multiplications}")
        step += 1

    print(f"\nResult: {a}^{x} mod {p} = {y}")
    print(f"Total number of multiplications: {multiplications}")
    return y


def main():
    print("Enter parameters for computing a^x mod p:")
    a = int(input("Base (a): "))
    x = int(input("Exponent (x): "))
    p = int(input("Modulus (p): "))
    fast_exp(a, x, p)


if __name__ == "__main__":
    main()
