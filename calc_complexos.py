import numpy as np

def solve_linear_system(coefficients, constants):
    # Converte as listas em arrays numpy
    A = np.array(coefficients, dtype=np.complex128)
    B = np.array(constants, dtype=np.complex128)

    try:
        # Resolve o sistema linear usando np.linalg.solve
        solution = np.linalg.solve(A, B)
        return solution
    except np.linalg.LinAlgError as e:
        return str(e)

def main():
    print("Calculadora de Sistemeas Lineares com Números Complexos")
    n = int(input("Digite o número de equações (2 ou 3): "))

    if n not in [2, 3]:
        print("Apenas sistemas de 2 ou 3 equações são suportados.")
        return

    coefficients = []
    for i in range(n):
        row = []
        for j in range(n):
            coef = complex(input(f"Digite o coeficiente A[{i+1}][{j+1}] (em formato a+bj): "))
            row.append(coef)
        coefficients.append(row)

    constants = []
    for i in range(n):
        const = complex(input(f"Digite a constante B[{i+1}] (em formato a+bj): "))
        constants.append(const)

    solution = solve_linear_system(coefficients, constants)

    if isinstance(solution, np.ndarray):
        print("\nA solução do sistema é:")
        for i in range(n):
            print(f"x[{i+1}] = {solution[i]}")
    else:
        print("\nErro ao resolver o sistema:", solution)

if __name__ == "__main__":
    main()