import random
def check_card_number(cardnumber):
   #if isinstance(cardnumber,int):return false
   modTen=10
   CheckDigit=0
   NmberTemp=0
   while cardnumber/(modTen/10)>0:
      NmberTemp=(cardnumber%modTen)/(modTen/10)*2
      CheckDigit+=NmberTemp/10+NmberTemp%10
      modTen*=100
   modTen=100
   while cardnumber/(modTen/10)>0:
      NmberTemp=(cardnumber%modTen)/(modTen/10)
      CheckDigit+=NmberTemp
      modTen*=100
   return 10-CheckDigit%10
def check_card_number_str(cardnumberStr):
   cardnumberStr=cardnumberStr[::-1]
   #print(cardnumberStr)
   CheckDigit=0
   NmberTemp=0
   for cardnumber in cardnumberStr[0::2]:
      NmberTemp=int(cardnumber)*2
      CheckDigit+=NmberTemp/10+NmberTemp%10
   for cardnumber in cardnumberStr[1::2]:
      CheckDigit+=int(cardnumber)
   return 10-CheckDigit%10
   
def generate_card_number():
   RandTime=random.randint(4,10)
   cardnumberStr='51'
   i=0
   while i<RandTime:
      cardnumberStr+=str(random.randint(0,9) )
      i+=1
   return cardnumberStr
   

print check_card_number(7992739871)
print check_card_number_str('7992739871')
print generate_card_number()
