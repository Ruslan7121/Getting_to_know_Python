print("Введите предложение и в двух словах вставьте сочетание букв \"абв:\"", end=' ')
sentence_with_errors = input().split()
need_to_delete = 'абв'
result = list(filter(lambda x: not need_to_delete in x, sentence_with_errors))
print(result)