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

def merge_sort(A:list,p,r):
    if p < r :
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)


def merge(A:list,p,q,r):
    L=[]
    R=[]

    for i in range(p,q+1):
        L.append(A[i])
    L.append(999999999999)
    for j in range(q+1,r+1):
        R.append(A[j])
    R.append(999999999999)

    i=0
    j=0

    for k in range(p,r+1):
        if(L[i]<R[j]):
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1

start = time.time()
merge_sort(numbers,0,len(numbers)-1)  
end = time.time()

print(f"زمان مرتب‌سازی: {end - start:.10f} ثانیه")




