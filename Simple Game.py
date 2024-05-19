from tkinter import Tk, Label, Button, Entry
import random

class Game:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        self.score = 0
        self.lives = 3

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        return x // y

    def modulus(self, x, y):
        return x % y

    def play_subtraction(self):
        print("\nLevel Pengurangan")
        while self.lives > 0:
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            question = f"Hasil dari {x} - {y} adalah: "

            answer = int(input(question))
            correct_answer = self.subtraction(x, y)

            if answer == correct_answer:
                self.score += 2
                print("Hore... benar!!! Skor Anda", self.score, "(lives:", self.lives, ")")
            else:
                self.score -= 2
                self.lives -= 1
                print("Wah... salah!!! Skor Anda", self.score, "(lives:", self.lives, ")")

            if self.lives == 0:
                play_again = input("Nyawa Anda habis. Coba lagi? (y/n): ")
                if play_again.lower() == "y":
                    self.lives = 3
                    self.score = 0
                    print("Nyawa dan skor telah direset.")
                else:
                    print("\nTerima kasih telah bermain!")
                    break

    def play_multiplication(self):
        print("\nLevel Perkalian")
        while self.lives > 0:
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            question = f"Hasil dari {x} * {y} adalah: "

            answer = int(input(question))
            correct_answer = self.multiplication(x, y)

            if answer == correct_answer:
                self.score += 2
                print("Hore... benar!!! Skor Anda", self.score, "(lives:", self.lives, ")")
            else:
                self.score -= 2
                self.lives -= 1
                print("Wah... salah!!! Skor Anda", self.score, "(lives:", self.lives, ")")

            if self.lives == 0:
                play_again = input("Nyawa Anda habis. Coba lagi? (y/n): ")
                if play_again.lower() == "y":
                    self.lives = 3
                    self.score = 0
                    print("Nyawa dan skor telah direset.")
                else:
                    print("\nTerima kasih telah bermain!")
                    break

    def play_division(self):
        print("\nLevel Pembagian")
        while self.lives > 0:
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)

            while y == 0 or x % y != 0:
                y = random.randint(-100, 100)

            question = f"Hasil dari {x} / {y} adalah: "

            answer = int(input(question))
            correct_answer = self.division(x, y)

            if answer == correct_answer:
                self.score += 2
                print("Hore... benar!!! Skor Anda", self.score, "(lives:", self.lives, ")")
            else:
                self.score -= 2
                self.lives -= 1
                print("Wah... salah!!! Skor Anda", self.score, "(lives:", self.lives, ")")

            if self.lives == 0:
                play_again = input("Nyawa Anda habis. Coba lagi? (y/n): ")
                if play_again.lower() == "y":
                    self.lives = 3
                    self.score = 0
                    print("Nyawa dan skor telah direset.")
                else:
                    print("\nTerima kasih telah bermain!")
                    break

    def play_modulus(self):
        print("\nLevel Modulus")
        while self.lives > 0:
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)

            while y == 0:
                y = random.randint(-100, 100)

            question = f"Hasil dari {x} % {y} adalah: "

            answer = int(input(question))
            correct_answer = self.modulus(x, y)

            if answer == correct_answer:
                self.score += 2
                print("Hore... benar!!! Skor Anda", self.score, "(lives:", self.lives, ")")
            else:
                self.score -= 2
                self.lives -= 1
                print("Wah... salah!!! Skor Anda", self.score, "(lives:", self.lives, ")")

            if self.lives == 0:
                play_again = input("Nyawa Anda habis. Coba lagi? (y/n): ")
                if play_again.lower() == "y":
                    self.lives = 3
                    self.score = 0
                    print("Nyawa dan skor telah direset.")
                else:
                    print("\nTerima kasih telah bermain!")
                    break

    def play_level(self, level_name, operator):
        print("\nLevel", level_name)
        while self.lives > 0:
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            question = f"Hasil dari {x} {operator} {y} adalah: "

            answer = int(input(question))
            correct_answer = eval(str(x) + operator + str(y))

            if answer == correct_answer:
                self.score += 2
                print("Hore... benar!!! Skor Anda", self.score, "(lives:", self.lives, ")")
            else:
                self.score -= 2
                self.lives -= 1
                print("Wah... salah!!! Skor Anda", self.score, "(lives:", self.lives, ")")

            if self.lives == 0:
                play_again = input("Nyawa Anda habis. Coba lagi? (y/n): ")
                if play_again.lower() == "y":
                    self.lives = 3
                    self.score = 0
                    print("Nyawa dan skor telah direset.")
                else:
                    print("\nTerima kasih telah bermain!")
                    break

    def is_leap_year(self):
        if self.birth_year % 400 == 0:
            return True
        elif self.birth_year % 100 == 0:
            return False
        elif self.birth_year % 4 == 0:
            return True
        else:
            return False


def play_game():
    name = input("Masukkan Nama: ")
    birth_year = int(input("Masukkan Tahun Lahir: "))

    game = Game(name, birth_year)

    print("Selamat datang,", game.name)
    print("Tahun", game.birth_year, "adalah TAHUN KABISAT\n" if game.is_leap_year() else "\n")

    while True:
        print("Menu pilihan level:")
        print("1. Level 1 (Penjumlahan)")
        print("2. Level 2 (Pengurangan)")
        print("3. Level 3 (Perkalian)")
        print("4. Level 4 (Pembagian)")
        print("5. Level 5 (Modulus)")
        print("6. Exit")

        choice = input("Pilih nomor pilihan: ")

        if choice == "1":
            game.play_level("Penjumlahan", "+")
        elif choice == "2":
            game.play_subtraction()
        elif choice == "3":
            game.play_multiplication()
        elif choice == "4":
            game.play_division()
        elif choice == "5":
            game.play_modulus()
        elif choice == "6":
            print("Terima kasih telah bermain!")
            break
        else:
            print("Maaf, pilihan Anda salah.")

        if game.lives == 0:
            play_again = input("Nyawa Anda habis. Coba lagi? (y/n): ")
            if play_again.lower() == "y":
                game.lives = 3
                game.score = 0
                print("Nyawa dan skor telah direset.")
            else:
                print("\nTerima kasih telah bermain!")
                break

play_game()
