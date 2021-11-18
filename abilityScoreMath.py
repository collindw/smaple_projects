import random

level=1
strength=18
dexterity=14
constitution=13
intelligence=12
wisdom=10
charisma=8

if (level >=1 or level<=4):
    initiative=2

hitDice=level*random.randint(0,9)

# modifiers
strModifier=round((strength-10)/2)
dexModifier=round((dexterity-10)/2)
conModifier=round((constitution-10)/2)
intModifier=round((intelligence-10)/2)
wisModifier=round((wisdom-10)/2)
chaModifier=round((charisma-10)/2)

# random roll saving through generator based on ability score
d20=random.randint(1,20)
initiative=dexModifier

strengthCheck=d20+strModifier

if d20==20:
    print('NAT 20 BABY!')
    print('d20 roll is ', d20)
    print('strengthModifier is', strModifier)
    print('strengthCheck is ', strengthCheck)
elif strengthCheck==20:
    print('dirty 20')
    print('d20 roll is ', d20)
    print('strengthModifier is', strModifier)
    print('strengthCheck is ', strengthCheck)
elif d20==1:
    print('nat 1 you suck!')
else:
    print('d20 roll is ', d20)
    print('strengthModifier is', strModifier)
    print('strengthCheck is ', strengthCheck)
