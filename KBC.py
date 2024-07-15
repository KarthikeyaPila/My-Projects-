import random
game_on = True
total_sum = 0
def money(sum):
    print("Your total net worth now is:", sum)


while game_on == True:

    Questions = [ "Which mammal is known for its incredible jumping ability and is often seen in the Australian outback? " , 
                "What is the largest species of shark currently living in the oceans? " , 
                "Which bird is known for its impressive mimicry skills, including imitating human speech? " , 
                'Which animal is known as the "ship of the desert"?' ,  
                'Which of these animals is known for its black and white striped pattern?' , 
                'What is the fastest land animal?' , 
                'Which marine animal has eight arms and is known for its intelligence and ability to change color?', 
                'Which animal is known for having a trunk?' , 
                'Which of these animals is a marsupial?'
    ]

    Options = [ 'A) Kangaroo B) Koala C) Wombat D) Platypus',
                'A) Great White Shark B) Hammerhead Shark C) Whale Shark D) Tiger Shark',
                'A) Eagle B) Parrot C) Owl D) Penguin',
                'A) Camel B) Elephant C) Horse D) Llama', 
                'A) Tiger B) Zebra C) Leopard D) Giraffe',
                'A) Cheetah B) Lion C) Gazelle D) Horse',
                'A) Octopus B) Squid C) Jellyfish D) Starfish',
                'A) Rhinoceros B) Elephant C) Hippopotamus D) Buffalo' , 
                'A) Rabbit B) Kangaroo C) MonkeyD) Dog'
    ]

    correct_option = (['a' , 'kangaroo'], 
                    ['c' , 'whale shark'] , 
                    ['b' , 'parrot'], 
                    ['a' , 'camel'], 
                    ['b' , 'zebra'] , 
                    ['a' , 'cheetah'] , 
                    ['a' , 'octopus'] , 
                    ['b' , 'elephant'],
                    ['b' , 'kangaroo']
                    )


    inedex_question = random.randint(0,8)

    print(Questions[inedex_question])  
    print(Options[inedex_question])

    user_input = input((" what do you think the correct option is?? " "\n ")).lower().strip()


    if user_input in correct_option[inedex_question]:
        print("congrats you won!")
        total_sum += 1000000
        money(total_sum)
        continue_playin = input("do you still wanna chance it? (yes/no) ").lower().strip()
        if continue_playin != "yes".strip():
            game_on = False
    else: 
        print("you lost the chance to become a crorepati looserrr LLLLL")
        game_on = False

