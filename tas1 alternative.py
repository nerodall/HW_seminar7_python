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
        