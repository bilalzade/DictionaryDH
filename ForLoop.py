# Tapşırıq:
# 1-dən 10-a qədər olan cüt ədədləri çap edən bir döngü yazın.

print("1-den 10-a qeder cut ededler 10 daxil olmaqla:")

#cut ededler ucun bele yaza bilerik eger 10 da daxildirse
for i in range(0, 11, 2):
    print(i, end= " ")

print()

print("1-den 10-a qeder tek ededler:")

#tek ededleri de bele tapa bilirik
for i in range(1, 11, 2):
    print(i, end= " ")

print()

print("1-den 10-a qeder cut ededler 10 xaric:")

#eger 10 ededi daxil deyilse bele yaza bilerik
for i in range(0, 10, 2):
    print(i, end= " ")

print()