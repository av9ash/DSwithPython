# Complete the detector function below.
def detector(tweets):
    print('hi')
    print(len(tweets))
    codes = []
    all_palins=[]
    sums = [];  score = 0




    for i in range(0, len(tweets)):
        codes.append(tweets[i][-3:])
        all_palins.append(get_palindromes(tweets[i][:-3]))

    j = 0; score = [0,0,0]
    for palins in all_palins:
       for palin in palins:
            score[j] = score[j]+len(palin)
       j+=1

    print(list(score))


def check_palin(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 * (i + 1)]:
            return False
    return True


def get_palindromes(string):
    left, right = 0, len(string)
    j = right
    results = set()

    while left < right - 1:
        temp = string[left:j]
        j -= 1

        if check_palin(temp):
            if len(temp)>=3 :
                results.add(temp)

        if j < left + 2:
            left += 1
            j = right

    print(list(results))
    return list(results)


if __name__ == '__main__':
    tweets = ['xxxayyySPY','xxxxxxbzzzzzzIVV','xaxaxDJI']
    detector(tweets)