import re as regex

class CardMasking():
   cardNumber = ''
   maskedCardNumber = ''

   # constructor
   def __init__(self, cardNumber):
      self.cardNumber = cardNumber

   # method
   def maskCreditOrDebitCardDetails(
         self,
         digitsToKeep: int = 4,
         maskCharacter = '*'
   ):
      cardNumberTotal = sum(map(str.isdigit, self.cardNumber))
      cardNumberLength = len(self.cardNumber)

      if (cardNumberLength != 16):
         print("Invalid Credit/Debit Card Number.")

      if (cardNumberLength == 16):
         digitsToMask = cardNumberTotal - digitsToKeep
         self.maskedCardNumber = regex.sub(r'\d', maskCharacter, self.cardNumber, digitsToMask)
         
      return self.maskedCardNumber    

# init
newCard = CardMasking(input("Enter you Credit/Debit Card Number: "))
print(newCard.maskCreditOrDebitCardDetails())