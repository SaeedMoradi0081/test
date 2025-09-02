import time

FILENAME = "random_numbers.txt"
LIMIT = 100_000  # تعداد اعدادی که می‌خواهیم بخوانیم

numbers = []

with open(FILENAME, "r") as f:
    for i, line in enumerate(f):
        if i >= LIMIT:
            break
        number = int(line.strip())
        numbers.append(number)

print(f"✅ خوانده شد: {len(numbers)} عدد")
print("🔹 چند عدد اول:", numbers[:10])

def insertion_sort(A:list):
    n=len(A)
    for j in range(1,n):
        key = A[j]
        i=j-1
        while (i>-1 and A[i] > key) :
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key


    return A

start = time.time()
insertion_sort(numbers)
end = time.time()

print(f"زمان مرتب‌سازی: {end - start:.10f} ثانیه")