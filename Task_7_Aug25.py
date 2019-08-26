class Player:

	def __init__(self, first, last, kit, pay):
		self.first = first
		self.last = last
		self.kit = kit
		self.pay = pay

	def fullname(self):
		return "{} {}".format(self.first, self.last)
	def kitnumber(self):
		return self.kit

plyr_1 = Player("Marcus", "Rashford", 10, 175000)
plyr_2 = Player("Anthony", "Martial", 9, 150000)
plyr_3 = Player("David", "de Gea", 1, 250000)

print()
print("MANCHESTER UNITED NEWS:")
print()
print("{} is Manchester United's new #{}".format(Player.fullname(plyr_1),plyr_1.kit))

print("The Spanish #{} in talks to sign a contract with his club worth reportedly ${}/week".format(Player.kitnumber(plyr_3),plyr_3.pay))

print("{} signed a new contract worth ${}/week".format(Player.fullname(plyr_2), plyr_2.pay))