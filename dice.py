import random as r

number_of_faces = int(input("サイコロの面の数は?: "))
m_times = int(input("何回振りますか?: "))

results = [r.randint(1, number_of_faces) for _ in range(m_times)]

print(results)
