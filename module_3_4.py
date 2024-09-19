# Объявляем функцию
def single_root_words(root_word, *other_words):
# Создаём пустой список
    same_words = []
    root_word_lower = root_word.lower()
    root_word_lower = root_word.upper()
# Перебор подходящих слов
    for i in other_words:
        other_words_lower = i.lower()
        # Условие при котором добавляются слова в результирующий список
        if root_word_lower in other_words_lower or other_words_lower in root_word_lower:
            same_words.append(i)
        # Возврат образованного функцией списка
    return same_words
# Вызов функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# Вывод результата
print(result1)
print(result2)