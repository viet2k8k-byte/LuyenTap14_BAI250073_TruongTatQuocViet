def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
arr = list(map(int, input("Nhập các số tự nhiên (cách nhau bởi dấu cách): ").split()))
odd_numbers = [x for x in arr if x % 2 != 0]
print(f"Các số lẻ: {odd_numbers} - Tổng số lượng: {len(odd_numbers)}")
prime_numbers = [x for x in arr if is_prime(x)]
print(f"Các số nguyên tố: {prime_numbers}")