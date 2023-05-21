# # Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# # *Пример:*

# # **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# #     **Вывод:** Парам пам-пам  


def is_rhythm (rhytm_set: list) -> bool:
    total = 0
    result_list = list()
    vowels = ("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я")
    for i in range (len(rhytm_set)):
        words = list(rhytm_set[i].split())
        # print(words)

        for k in range(len(words)):
            temp_list = list(words[k])
            # print(temp_list)
            for j in range(len(temp_list)):
                if temp_list[j] in vowels:
                    total +=1
                    # print(total)
            result_list.append(total)
            total = 0

    for n in range(len(result_list)-1):
        if result_list[n] != result_list[n+1]:
            return False
    return True


poem = list(input("Введите стих, который нужно проверить на ритмичность: ").split())
# print(rhythm_set)

if is_rhythm(poem):
    print("ритмично")
else:
    print("неочень ритмично")
        

