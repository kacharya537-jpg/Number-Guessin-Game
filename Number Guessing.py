import random
import time

while True:
    print("""
      ===================================
      -----ℕ𝕦𝕞𝕓𝕖𝕣 𝔾𝕦𝕖𝕤𝕤𝕚𝕟𝕘 𝔾𝕒𝕞𝕖------
      ===================================
      """)
    print("Choose A Mode :")
    print("1. Easy 😁")
    print("2. Normal 🍀")
    print("3. Hard 🔥(30 attempts)")
    print("4. Insane ❤️‍🔥(20 attempts)")
    print("5. Extreme 🎆(15 attempts)")

    mode = input("Enter Mode/Level: ").strip().lower()

    if mode == "1" or mode == "01" or mode == "Easy" or mode == "easy" or mode == "EASY":
        num = random.randint(1, 50)
        _range = 50
        _attempts = None 
        print("🙂 • You chose The Easy Mode")
        time.sleep(0.3)
        print("Entering Easy Mode\n")
        time.sleep(0.5)
        print("""
          -------------------------------------------------
          ===========🙂 • Ｅａｓｙ Ｍｏｄｅ • 🙂===========
          -----------------------------------------------
          """)

    elif mode == "2" or mode == "02" or mode == "Normal" or mode == "normal" or mode == "NORMAL":
        num = random.randint(1, 100)
        _range = 100
        _attempts = None 
        print("🍀 • You chose Normal Mode • 🍀\n")
        print("Entering 🍀 • Normal Mode • 🍀\n")
        time.sleep(0.5)
        print("""
          ----------------------------------------------------
          ===========🍀 • Ｎｏｒｍａｌ Ｍｏｄｅ • 🍀===========
          -------------------------------------------------
          """)

    elif mode == "3" or mode == "03" or mode == "Hard" or mode == "HARD" or mode == "hard":
        num = random.randint(1, 1000)
        _range = 1000
        _attempts = 30
        print("🔥 • You Chose Hard Mode • 🔥")
        print("Entering 🔥 • Hard Mode\n")
        time.sleep(0.5)
        print("""
          -----------------------------------------------
          ===========🔥 •  Ｈａｒｄ Ｍｏｄｅ • 🔥===========
          -----------------------------------------------
          """)

    elif mode == "4" or mode == "04" or mode == "Insane" or mode == "INSANE" or mode == "insane":
        num = random.randint(1, 1000)
        _range = 1000
        _attempts = 20
        print("🔥 • You Chose Insane Mode • 🔥")
        print("Entering ❤️‍🔥 • Insane Mode\n")
        time.sleep(1)
        print("""
          -----------------------------------------------------
          ===========❤️‍🔥 •  Ｉｎｓａｎｅ Ｍｏｄｅ • ❤️‍🔥===========
          ----------------------------------------------------
          """)

    elif mode == "5" or mode == "05" or mode == "Extreme" or mode == "EXTREME" or mode == "extreme":
        num = random.randint(1, 10000)
        _range = 10000
        _attempts = 15
        print("🔥 • You Chose Extreme Mode • 🔥")
        print("Entering ❤️‍🔥 • Extreme Mode\n")
        time.sleep(1)
        print("""
          --------------------------------------------------
          =========❤️‍🔥 •  Ｅｘｔｒｅｍｅ Ｍｏｄｅ• ❤️🎆=========
          --------------------------------------------------
          """)

    else:
        time.sleep(0.5)
        print("👂 Enter In A Valid Format ⌛")
        continue

    print(f"Guess the number between 1 and {_range}!")

    guess = None
    attempts = 0

    while guess != num:
        if _attempts is not None and attempts >= _attempts:
            print(f"0️⃣ • No Attempts Left, The number was {num}.")
            print("Mode =", mode)
            print("Attempts taken =", attempts)
            print("Attempts Given =", _attempts)
            break

        guess_input = input("Enter your guess: ").strip()
        if not guess_input.isdigit():
            print("⚠️ Please enter a valid ++ number!")
            continue

        guess = int(guess_input)
        if guess < 1 or guess > _range:
            print(f"⚠️ Please enter a number between 1 and {_range}.")
            continue

        attempts += 1

        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
        else:
            print(f"🎉 • Congrats You guessed it in {attempts} attempts.")
            print("Mode =", mode)
            print("Attempts taken =", attempts)
            print("Attempts Given =", _attempts if _attempts is not None else "Unlimited")
            break

    responses = ["y","yh","yes",
                 "yeah","sure","ok",
                 "okay","ya","ye","yep",
                 "yuh","why not","okie","Oki","OKI","OKIE"]
    _responses = ["n","no",
                  "nope","nah",
                  "never","exit","quit","nuh"]

    while True:
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again in responses or again.startswith("y") or again.startswith("o") and again is not "Oh Hell Nah" or again.startswith("O"):
            break
        elif again in _responses or again.startswith("n"):
            print("👋 Thanks for playing! Goodbye!")
            exit()
        else:
            print(" I didn’t understand that,Type Yes/No.")

