
# def choice_to_number(choice):
#     if choice == 'Usain':
#         return 1
#     elif choice == 'Me':
#         return 2
#     else:
#         return 3

# def number_to_choice(number):
#     if number == 1:
#         return 'Usain'
#     elif number == 2:
#         return 'Me'
#     elif number == 3:
#         return 'Aybek'

# def test_choice_to_number():
#   assert choice_to_number('Usain') == 1
#   assert choice_to_number('Me') == 2
#   assert choice_to_number('Aybek') == 3

# def test_number_to_choice():
#   assert number_to_choice(1) == 'Usain'
#   assert number_to_choice(2) == 'Me'
#   assert number_to_choice(3) == 'Aybek'

# def test_all():
#   try:
#     test_choice_to_number()
#     test_number_to_choice()

#   except AssertionError:
#     print('import wrong')

#   else:
#     print('import success')

# test_all()

# def transaction():

#     print("Do the transaction here")

# def getuserinput():

#     userInput = "";
#     up = "";
#     D = "";
#     print("Start")
#     while "no" not in userInput:

#         userInput = input("Would you like to start a new transaction?")
#         userInput = userInput.lower()
#         if "no" not in userInput and "yes" not in userInput:
#             print("yes or no please")
#         if "yes" in userInput:
#             transaction()
#     print("Good bye")

# getuserinput()




# public  static  void  main ( String []  args )  { 
#         Scanner  sc  =  новый  сканер ( System . in ); 
#         int  n  =  sc . nextInt (); 
#         Строка  s  =  sc . следующий ();
        
#         int  v  =  0 ;      // количество долин 
#         int  lvl  =  0 ;    // текущий уровень 
#         для ( char  c  :  s . toCharArray ()) { 
#             if ( c  ==  'U' )  ++ lvl ; 
#             if ( c  ==  'D' )  - lvl ;
            
#             // если мы только что поднялись до уровня моря 
#             if ( lvl  ==  0  &&  c  ==  'U' ) 
#                 ++ v ; 
#         } 
#         Система . из . печать ( v ); 
#     }


# steps = input("Enter steps")
        
# v  ==  0    # количество долин 
# lvl  ==  0   # текущий уровень  
# if steps == 'U':
#   return +1
# elif steps == 'D':
#   return -1
            
#           #если мы только что поднялись до уровня моря 
#   if ( lvl  ==  0 and c  ==  'U' ):
#   return v +=1
#   print(v)

N = int(input("Enter").strip())

String = input("U P").strip()

level = 0
count = 0

for i in String:
    if i == 'U':
        level += 1
    elif i == 'D':
        level -= 1
    if level == 0:
        if prev < level:
            count += 1
    prev = level

print (count)
        
        
print(V)