filename=input('Введите имя файла')
try:
    with open(f'{filename}.txt',encoding='utf8') as myFile:
        text=myFile.read()
        text_letter=''
        for i in text:
            if i not in ('1234567890-+!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'):
                text_letter+=i
        list_of_words=text_letter.split()
except Exception as error:
    print('Файл с указанным именем не найден', error)
#ищем среди слов с длиной более трех букв самое часто встречающееся
#сначала поместим в новый список все слова с длиной более трех букв
list_of_words_more_3=[]
for i in list_of_words:
    if len(i)>3:
        list_of_words_more_3.append(i)
# среди слов с длиной более трех букв (если они есть) ищем самое часто встречающееся,
# создадим словарь где будут ключи - слова, значения - количества их повторений
if list_of_words_more_3==[]:
    print("Все слова в тексте имеют длину менее трех букв")
else:
    word_len_more_3={}
    for i in list_of_words_more_3:
        if i in word_len_more_3:
            word_len_more_3[i]+=1
        else:
            word_len_more_3[i]=1
    max_value=max(word_len_more_3.values())
    max_dict ={k: v for k, v in word_len_more_3.items() if v == max_value}
    print('Чаще всего в тексте встречается(ются) слово (слова):',list(max_dict.keys()))

# ищем самое длинное английское слово, для этого надо сначала в отдельный список поместить все английские слова
list_of_words_eng=[]
for i in list_of_words:
    ch = 0
    for j in range(len(i)):
        if ('a' <= i[j] <= 'z') or ('A' <= i[j] <= 'Z'):
            ch+=1
    if len(i)==ch:
        list_of_words_eng.append(i)

# создадим словарь, где по ключам будут английские слова (если они есть), а по значениям - их длины
if list_of_words_eng==[]:
    print('В тексте нет английских слов')
else:
    len_eng={}
    for i in list_of_words_eng:
        len_eng[i]=len(i)
# теперь создадим список из ключей, имеющих наибольшие значения
    len_eng_max=[key for key,value in len_eng.items() if value==max(len_eng.values())]
    print('Английское(ие) слово(а), имеющее(ие) наибольшую длину:',len_eng_max)











