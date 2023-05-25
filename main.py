def guess_number_loop():
   odd_sum = 0
   even_sum = 0
   guessed_numbers = []
   for _ in range(2):
       guess = int(input("Guess a number:"))
       guessed_numbers.append(guess)
       if guess % 2 == 0:
           print(f"{guess} is an even number.")
           even_sum+=guess
       else:
           print(f"{guess} is an odd number.")
           odd_sum += guess

   print("Sum of odd numbers:", odd_sum)
   print("Sum of even numbers:", even_sum)
   print("Subtraction of odd and even numbers:", odd_sum - even_sum)
   print("Max value:", max(guessed_numbers))
   print("Min value:", min(guessed_numbers))

guess_number_loop()
