#Напишите функцию hello_user(), которая с помощью функции input() 
# спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
#Перепишите функцию hello_user() из задания про while, 
# чтобы она перехватывала KeyboardInterrupt, 
# писала пользователю "Пока!" и завершала работу 
# при помощи оператора break

def hello_user():
    try:
        while True:
            str1=input("Как дела?\n")
            if str1 == "Хорошо":
                break
    except KeyboardInterrupt:
        print("Пока!")

if __name__ == "__main__":
    hello_user()

