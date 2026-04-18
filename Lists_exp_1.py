invited_people =['Ada','Barbara','Coyote','Delta']
for person in invited_people:
    print(f"Feel invited for dinner dear{person}")

print(f' Invitation of: {invited_people[3]} failed.')
failed_to_invite = invited_people[3]
invited_people.remove(failed_to_invite)
invited_people.append('Eve')
print(invited_people)
for person in invited_people:
    print(f"Feel invited for dinner dear {person}")


print(f'Bigger table has been found, 3 extra people can be invited')
invited_people.insert(0,'Frank')
invited_people.insert(2,'George')
invited_people.append('Jesus')
print(f' Feel invited for dinner dear {invited_people[0]}')
print(f' Feel invited for dinner dear {invited_people[1]}')
print(f' Feel invited for dinner dear {invited_people[2]}')
print(f' Feel invited for dinner dear {invited_people[3]}')
print(f' Feel invited for dinner dear {invited_people[4]}')
print(f' Feel invited for dinner dear {invited_people[5]}')
print(f' Feel invited for dinner dear {invited_people[6]}')

print(f' Information from restaurant: COVID-26 attacks, only 2 guests are allowed. Choose two extra people to invite to come with you')
message = "sorry, there are new rules. We cannot meet at the restaurant."
invitation_c26 = 'I still want to meet you. Please come to x at 11:00 on the next saturday'
print(f'{invited_people.pop(6)} {message}')
print(f'{invited_people.pop(5)} {message}')
print(f'{invited_people.pop(4)} {message}')
print(f'{invited_people.pop(3)} {message}')
print(f'{invited_people.pop(2)} {message}')
print(f'{invited_people[1]} {invitation_c26}')
print(f'{invited_people[0]} {invitation_c26}')
print(f' There were {len(invited_people)} invited people.')
del invited_people[1]
del invited_people[0]
print(invited_people)
