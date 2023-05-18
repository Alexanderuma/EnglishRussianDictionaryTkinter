import re
import random
from tkinter import*


englishList=[]
russianList=[]
vocabularyList=[]


'''
Оформляю окно при помощи Tkinter.
Заведомо не ограничиваю размер окна.
Ограничиваю только размеры кнопок(Button), меток/лейблов(Label) и полей ввода(Entry) только по ширине.

Использую основную метку(lab), как экран для вывода информации.
2 других метки(lab1 и lab2) остаются неизменными, в виде небольших подсказок.

Верхнее поле для ввода(ent1) - исползуется для ввода английских слов. *Или для ввода неправильного слова, если нужно исправить ошибку.

Нижнее поле для ввода(ent2) - используется для ввода русских слов. Или для ввода правильного слова, если нужно исправить ошибку***

Кнопки: 
butVocabulary
butAddWord
butTranslateEng
butTransFromRus
butCorrect

Кнопки срабатывают 1 раз, при нажатии и запускают определенную функцию, привязанную к каждой кнопке при помощи метода Bind.

Для размещения виджетов в окне использовал менеджер геометрии: pack().

'''





def show_Dictionary(event):
    '''
    Функция показывает весь список слов словаря. Английское слово - Русский перевод.
    Слова беруться из отдельного текстового файла для английских слов и текстового файла для русских слов, затем они перезаписывются в общий текстовый файл DictionaryTextFile.txt и считывются и отображаются в лебле(метке: lab), в окне файла.
    '''

    with open("EnglishTextFile.txt",'r') as fileEng:
        for line in fileEng:
            englishList.append(line.strip())

    with open("RussianTextFile.txt",'r') as fileRus:
        for line in fileRus:
            russianList.append(line.strip())

    a = len(englishList)
    b = 0
    for m in range (a):

        engRus = englishList[b] + " - " + russianList[b]
        vocabularyList.append(engRus)
        b+=1


    voc = open("DictionaryTextFIle.txt", "w")
    for item in vocabularyList:
        voc.write(item + "\n")
    voc.close()

    with open("DictionaryTextFIle.txt", "r") as vocabulary:        
        lab['text'] = f"Словарь содержит:\n {vocabulary.read()}"
        

    englishList.clear ()
    russianList.clear ()
    vocabularyList.clear()

    ent1.delete(0,END)
    ent2.delete(0,END)




def add_NewWords(event):
    '''
    Функция записывает новые английские слова и русский перевод, по 1 слову за каждый раз.
    В поле для английского слова вводиться слово на английском в поле для русского слова вводиться слово на русском. Английское и русское слово записываеются в отдельные текстовые файлы: EnglishTextFile.txt и RussianTextFile.txt.
    
    '''

    newWordEng = ent1.get().lower() # Все введеные слова записываются с маленкой буквы, чтобы проще было осуществлять поиск.
    

    newWordRus = ent2.get().lower()
    
    
    if newWordEng.isalpha(): # Проверка, на то, чтобы введенная строка состояла из букв.
        if newWordRus.isalpha(): # Проверяет русское слово, состоит ли оно из букв.
            if (bool(re.search('[a-zA-Z]', newWordEng))) == True and (bool(re.search('[а-яА-Я]', newWordEng))) == False: # Проверяет из каких букв состоит английское слово из Латиницы.
                if (bool(re.search('[а-яА-Я]', newWordRus))) == True and (bool(re.search('[a-zA-Z]', newWordRus))) == False: # Проверяет состоит ли русское слово из Кириллицы.

                    engRus = newWordEng + " - " + newWordRus # Склеивает английское и русское слово и добавляет их в конец списка VocabularyList
                    vocabularyList.append(engRus)
                    englishList.append(newWordEng) # Английское слово и добавляет в конец списка EnglishList
                    russianList.append(newWordRus) # Русское слово в конец списка RussianList

                    eng = open("EnglishTextFile.txt","a") # Переписывает слова из списка в текстовый файл с английскими словами.
                    for item in englishList:
                        eng.write(item + "\n")
                    eng.close()


                    rus = open("RussianTextFile.txt","a") # Переписывает слова из списка в текстовый файл с русскими словами.
                    for item in russianList:
                        rus.write(item + "\n")
                    rus.close()


                    voc = open("DictionaryTextFIle.txt", "a") # Переписывает слова из списка vocabularyList в наглядный текстовый файл словаря.
                    for item in vocabularyList:
                        voc.write(item + "\n")
                    voc.close()

                    ent1.delete(0,END)
                    ent2.delete(0,END)

                    englishList.clear () # Очищаем списки, чтобы при повторном нажатии на кнопку "Словарь", текстовые файлы не задваивались.
                    russianList.clear ()
                    vocabularyList.clear()
                else:
                    ent1.delete(0,END)
                    ent2.delete(0,END)
                    ent2.insert(0,"Напишите перевод кириллицей!") # Выводит подсказку в поле ввода(ent2), если забыли ввести слово русскими буквами.

            else:
                ent1.delete(0,END)
                ent2.delete(0,END)
                ent1.insert(0,"Напишите латиницей!") # Аналогичная подсказка в поле ввода(ent1), если забыли ввести слово англискими буквами.
        else:
            ent1.delete(0,END)
            ent2.delete(0,END)
            ent2.insert(0,"Используй русские буквы!") # Подсказка
    else:
        ent1.delete(0,END)
        ent2.delete(0,END)
        ent1.insert(0,"Используй английские буквы!") # Подсказка
     
        


def translate_WordsFromEnglish(event):
    '''
    Функция переводит с английского на русский.
    Вводится слово на английском в строку для ввода английских слов. Если слово было в английском списке. То функия через индекс ищет перевод(русскоу слово) в списке русских слов.

    '''

    fileRus=open("RussianTextFile.txt","r")
    for line in fileRus:
        russianList.append(line.strip())
    fileRus.close()
        

    fileEng=open("EnglishTextFile.txt","r")       
    for line in fileEng:
        englishList.append(line.strip())
    fileEng.close()
          
    word = ent1.get().lower()

    try:
        n = englishList.index(word)
        findWordEng = englishList[n]
        if word == findWordEng:

            findWordRus = russianList[n]
            lab['text'] = f"{findWordRus}"
            ent2.delete(0,END)
                   
    except:
        lab["text"] = ("Такого слова в словаре нет!\n Либо Вы не ввели слово в текстовое поле\n Либо добавьте новое слово в словарь.")

    russianList.clear()
    englishList.clear()
    



def translate_FromRussian(event):
    '''
    Функция переводит с русского на английский.
    Ищет в списке русских слов то слово, которое было введено строку русских слов. Если русское слово было списке то выводит результат на английском.

    '''

    fileRus=open("RussianTextFile.txt","r") # ,encoding="utf-8-sig" ## Убрал encoding потому что и без него работает.      
    for line in fileRus:
        russianList.append(line.strip())
    fileRus.close()
        
    fileEng=open("EnglishTextFile.txt","r")       
    for line in fileEng:
        englishList.append(line.strip())
    fileEng.close()
        
    wordRus = ent2.get().lower()

    try:
        n = russianList.index(wordRus)
        findWordRus = russianList[n]
        if wordRus == findWordRus:

            findWordEng = englishList[n]
            lab['text'] = f"{findWordEng}"
            ent1.delete(0,END)

    except:
        lab['text'] = ("Такого русского слова в словаре нет!\n Либо Вы не ввели слово в текстовое поле\n Либо добавьте новое слово в словарь.")

    russianList.clear()
    englishList.clear()




def correction(event):
    '''
    Функция позволяет заменить неправильное слово, которое было записано с ошибкой, на правильное.
    Вводиться неправильное слово в верхнюю строчку. Правильное слово в нижнюю строку.
    Функция ищет слово сначала в списке анлийских слов. Затем в списке русских слов. Если находит, то заменяет на правильное. 
    
    '''

    try:
        with open("EnglishTextFile.txt",'r') as fileEng:
            for line in fileEng:
                englishList.append(line.strip())

        with open("RussianTextFile.txt",'r') as fileRus:
            for line in fileRus:
                russianList.append(line.strip())

        wrongWord = ent1.get().lower()

        ### Проверка на нахождение слова в словаре.  
        if wrongWord in englishList:

            n = englishList.index(wrongWord)
            findWordEng = englishList[n]   

            if wrongWord == findWordEng:

                wordIndex = englishList.index(wrongWord)
                englishList.remove(wrongWord)

                correctWord= ent2.get().lower()
                englishList.insert(wordIndex, correctWord)

                eng = open("EnglishTextFile.txt","w") # Переписывает список с измененным словом.
                for item in englishList:
                    eng.write(item + "\n")
                eng.close()

            
                lab['text'] = f"{wrongWord} - было заменено на\n правильное слово: {correctWord}"

        
        else:
           
            n = russianList.index(wrongWord)
            findWordRus = russianList[n] 
            
            if wrongWord == findWordRus:

                wordIndex = russianList.index(wrongWord)
                russianList.remove(wrongWord)

                correctWord= ent2.get().lower()
                russianList.insert(wordIndex, correctWord)

                rus = open("RussianTextFile.txt","w") # Переписывает список с измененным словом.
                for item in russianList:
                    rus.write(item + "\n")
                rus.close()

            

                lab['text'] = f"{wrongWord} - было заменено на\n правильное слово: {correctWord}"
        


    except:
        lab['text'] = "Вы либо не ввели 2 слова в обе строчки.\n Либо слово, которое вы ввели в первую строку,\n нет в списках."
    
    englishList.clear()
    russianList.clear()
    vocabularyList.clear()

               

### Отлично работает в консоли. Но совершенно не работает в Tkinter. Не буду использовать пока. При неободимости, могу показать файл со всеми функциями, который работает в консоли. 
def check_yourKnowledge(): 
    '''
    Функция проверяет знания слов из словаря.
    '''
    print("Проверь свои знания слов из словаря\n")
        

    listForRandom = []
    usedWordsList = []
    count = 0

    with open("RussianTextFile.txt","r") as fileRus:
        for line in fileRus:
            russianList.append(line.strip())

    listForRandom = russianList.copy()
        
        
    for x in range (5):
        while True:
            random.shuffle(listForRandom)
               
            randomWord = random.choice(listForRandom)
            
            if randomWord not in usedWordsList:

                print("Переведи на английский слово:", randomWord)
                usedWordsList.append(randomWord)
                break               

        k = russianList.index(randomWord)

        with open("EnglishTextFile.txt",'r') as fileEng:
            for line in fileEng:
                englishList.append(line.strip())


        engWord = englishList[k]
        while True:
            answerInEng = input("Напишите правильный ответ на английском: ").lower()
            x = answerInEng.isalpha()
            if x == True:
                if (bool(re.search('[a-zA-Z]', answerInEng))) == True and (bool(re.search('[а-яА-Я]', answerInEng))) == False:
                    break
                elif (bool(re.search('[а-яА-Я]', answerInEng))) == True and (bool(re.search('[a-zA-Z]', answerInEng))) == False: 
                    print("Напишите латиницей!")
            elif x == False:
                print("Вы не ввели слово!")

        if answerInEng == engWord:
            print("Правильно!")
            count+=1

        elif answerInEng != engWord:
            print("Ответ не верный")

    knowledge = int(count/5*100)
    print(f"Твоё знание слов: {knowledge}%")
    englishList.clear()
    russianList.clear()




'''
Оформляю окно при помощи Tkinter.
Заведомо не ограничиваю размер окна.
Ограничиваю только размеры кнопок(Button), меток/лейблов(Label) и полей ввода(Entry) только по ширине.

Использую основную метку(lab), как экран для вывода информации.
2 других метки(lab1 и lab2) остаются неизменными, в виде небольших подсказок.

Верхнее поле для ввода(ent1) - исползуется для ввода английских слов. *Или для ввода неправильного слова, если нужно исправить ошибку.

Нижнее поле для ввода(ent2) - используется для ввода русских слов. Или для ввода правильного слова, если нужно исправить ошибку***

Кнопки: 
butVocabulary
butAddWord
butTranslateEng
butTransFromRus
butCorrect

Кнопки срабатывают 1 раз, при нажатии и запускают определенную функцию, привязанную к каждой кнопке при помощи метода Bind.

Для размещения виджетов в окне использовал менеджер геометрии: pack().

'''

root = Tk()


lab = Label(width=40, bg='black', fg='white')
lab1 = Label(width=40, bg='white', fg='black', text = "Английское слово: / *Неправильное слово:"  )
lab2 = Label(width=40, bg='white', fg='black', text = "Русское слово: / *Правильное слово: ")
ent1 = Entry(width=30)
ent2 = Entry(width=30)

butVocabulary = Button(width=20, text="Словарь")
butAddWord = Button(width= 20, text="Добавить слово")
butTranslateEng = Button(width = 20, text = "Перевод с Английского")
butTransFromRus = Button(width = 20, text = "Перевод с Русского")
butCorrect = Button(width=20, text="*Исправить ошибку")
#butRandomWords = Button(width=10, text="Проверь себя") # Не использую, потому как не работает корректно.


 

butVocabulary.bind('<Button-1>', show_Dictionary)
butAddWord.bind('<Button-1>', add_NewWords)
butTranslateEng.bind('<Button-1>', translate_WordsFromEnglish)
butTransFromRus.bind('<Button-1>', translate_FromRussian)
butCorrect.bind('<Button-1>', correction)
#butRandomWords.bind('<Button-1>', check_yourKnowledge) # Не использую, потому как не работает корректно.



lab.pack() 
lab1.pack()
ent1.pack()
lab2.pack()
ent2.pack()
butVocabulary.pack()
butAddWord.pack()
butTranslateEng.pack()
butTransFromRus.pack()
butCorrect.pack()
#butRandomWords.pack() # Не использую, потому как не работает корректно.


root.mainloop()