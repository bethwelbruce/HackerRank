n, m = map(int, input().split())
data = []
for _ in range(n):
    row = list(map(int, input().split()))
    data.append(tuple(row))
k = int(input())

def sort_by_kth_attribute(row):
    return row[k]

sorted_data = sorted(data, key=sort_by_kth_attribute)

for row in sorted_data:
    print(" ".join(str(x) for x in row))
