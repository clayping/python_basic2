row = int(input("行数を入力してください: "))
collumn = int(input("列数を入力してください: "))

for i in range(1, row + 1):
    for j in range(1, collumn + 1):
        print(f"{i} x {j} ={i*j:>3}", end="|")
    print()
