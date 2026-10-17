import math

def taylor_exp(x: float, eps: float) -> float:

    current_term = 1.0
    total_sum = current_term
    n = 1  

    while abs(current_term) >= eps:
        current_term *= x / n
        total_sum += current_term
        n += 1

    return total_sum


try:
    eps_input = input("Введите  точность : ")
    x_input = input("Введите  x: ")
    
    eps = float(eps_input)
    x = float(x_input)
    
    if eps <= 0:
        print("Точность >0.")
    else:
        result = taylor_exp(x, eps)
        true_value = math.exp(x) 
        
        print(f"\nРезультаты:")
        print(f"мое e^{x} ≈ {result:.10f}")
        print(f"Точное значение e^{x} = {true_value:.10f}")

except ValueError:
    print("Ошибка.")