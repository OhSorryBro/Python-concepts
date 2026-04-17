magicians = ['alice', 'david', 'caroline']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(f'{magician.title()}, that was an awesome magic spectatle!')
    print(f'We are waiting for your next magic spectatle, dear {magician.title()}.\n')

print('Thank you everyone. That was a trully amazing expirience!')