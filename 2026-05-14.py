import random
def guess_the_number(limit):
    secret_number = random.randint(1, limit)
    attempts = 0 
    print(f"Би 1-ээс {limit} хооронд нэг тоо бодлоо. Таагаарай!")
    while True:  # Хязгааргүй давталт эхлүүлэх
        guess = int(input("Таны таамаг: "))
        attempts += 1 # Оролдолтын тоог нэмэх
        if guess < secret_number:
            print("Илүү их тоо!")
        elif guess > secret_number:
            print("Илүү бага тоо!")
        else:
            print(f"Зөв! Та {attempts} оролдолтоор таалаа.")
            break  # Зөв таасан тул давталтыг хүчээр зогсооно           
    return attempts # Хэдэн оролдолтоор таасныг буцаах
score = guess_the_number(100)
print(f"Тоглоом дууслаа. Таны оноо: {score}")
while True:
    try:
        guess = int(input("Таны таамаг: "))
        attempts += 1

        if guess < secret_number:
            print("Илүү их тоо!")
        elif guess > secret_number:
            print("Илүү бага тоо!")
        else:
            print(f"Зөв! Та {attempts} оролдолтоор таалаа.")
            break

    except ValueError:
        print("Зөвхөн тоо оруулна уу!")
