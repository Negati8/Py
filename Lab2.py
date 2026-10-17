def are_digits_unique(num: int) -> bool:
    s = str(abs(num))
    return len(s) == len(set(s))

def is_prime(num: int) -> bool:
    if num < 2:
        return False  
    if num == 2:
        return True   
    if num % 2 == 0:
        return False 
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_perfect(num: int) -> bool:
    if num <= 1:
        return False 
    
    divisor_sum = 1 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:  
                divisor_sum += num // i
                
    return divisor_sum == num

def find_perfect_numbers(start: int, end: int) -> list:
    perfect_nums = []  
    for i in range(start, end + 1):
        if is_perfect(i):
            perfect_nums.append(i)
    return perfect_nums

def can_be_obtained_by_deleting(source: int, target: int) -> bool:

    s_source = str(source)
    s_target = str(target)
    
    idx_target = 0  
    len_target = len(s_target)
    
    if len_target == 0:
        return True
        
    for char in s_source:
        if char == s_target[idx_target]:
            idx_target += 1
            if idx_target == len_target:
                return True 
                
    return False



num1 = 123
num2 = 122
print(f"Цифры числа {num1} различны: {are_digits_unique(num1)}")  
print(f"Цифры числа {num2} различны: {are_digits_unique(num2)}")  

print(f"\nЧисло 5 простое: {is_prime(5)}")  
print(f"Число 1 простое: {is_prime(1)}")   
print(f"Число 6 простое: {is_prime(6)}")   

a, b = 34, 41
print(f"\nМожно ли получить {a} из {b} вычеркиванием? {can_be_obtained_by_deleting(b, a)}") 

a2, b2 = 12, 132
print(f"Можно ли получить {a2} из {b2} вычеркиванием? {can_be_obtained_by_deleting(b2, a2)}")

start, end = 1, 666
perfect_list = find_perfect_numbers(start, end)
print(f"\nСовершенные числа от {start} до {end}: {perfect_list}")