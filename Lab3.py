import numpy as np

def solve_task(matrix: np.ndarray) -> None:
    has_zero_mask = np.any(matrix == 0, axis=0)
    
    col_sums = matrix.sum(axis=0)
    
    zero_sums = col_sums[has_zero_mask]
    
    if zero_sums.size > 0:
        print(f"Суммы столбцов содержащих нули: {zero_sums}")
    else:
        print("В матрице нет столбцов с нулями.")
    
    sort_matrix = matrix.copy()
    
    sort_matrix[::2, :] = np.sort(sort_matrix[::2, :], axis=1)
    
    sort_matrix[1::2, :] = np.sort(sort_matrix[1::2, :], axis=1)[:, ::-1]

    print("\nИсходная матрица:")
    print(matrix)
    
    print("\nОбработанная матрица:")
    print("(Четные строки отсортированы по возрастанию нечетные  по убыванию)")
    print(sort_matrix)

if __name__ == "__main__":
    random_matrix = np.random.randint(-2, 5, size=(6, 8))
    
    solve_task(random_matrix)