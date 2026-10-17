from typing import List, Tuple

def find_last_min_element_index(arr: List[float]) -> Tuple[float, int]:
    if not arr:
        raise ValueError("Массив пуст")

    min_value = arr[0]
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] <= min_value:
            min_value = arr[i]
            min_index = i

    return min_value, min_index

def sum_between_negatives(arr: List[int]) -> int:

    neg_indices = [idx for idx, val in enumerate(arr) if val < 0]
    
    if len(neg_indices) < 2:
        return 0
        
    first_neg_idx = neg_indices[0]
    last_neg_idx = neg_indices[-1]
    
    return sum(arr[first_neg_idx + 1 : last_neg_idx])


arr = [8, 15, -3, -1, -5, 7, -15, 6]

min_val, min_idx = find_last_min_element_index(arr)

print(f"Исходный массив: {arr}")
print(f"Минимальный элемент: {min_val} (последнее вхождение на индексе {min_idx})")

sum_result = sum_between_negatives(arr)
print(f"Сумма элементов между первым и последним отрицательными числами: {sum_result}")

test_arr = [0, 4, 1, 1, 2]
val, idx = find_last_min_element_index(test_arr)
print(f"\nТест [0, 4, 1, 1, 2]: Минимум {val}, индекс {idx} (должен быть 3)")