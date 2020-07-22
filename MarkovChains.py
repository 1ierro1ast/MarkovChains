from random import choice

class MarkovChains:
	def __init__(self):
		self.chains = {}

	def addChain(self, key, value):
		if key not in self.chains:
			self.chains[key] = [value]
		else:
			self.chains[key].append(value)
	def generateSequence(self, lenght, auth=None):
		if not auth:
			auth = choice([key for key in self.chains])
		current = self.chains[auth]
		out = []
		for now in range(lenght):
			key = choice(current)
			try:
				current = self.chains[key]
				out.append(key)
			except KeyError:
				return out

		return out

mch = MarkovChains()
test = "пчела ела кашу и запивала соком. Интересные вещи творятся повсюду. И самое главное что рыбы кашу не едят. Но важно учитывать погодные условия и прочие интересные вещи"
test = test.replace(".", " * :").replace(",", "").lower().split(" ")
for i, o in enumerate(test):
	if i < len(test)-1:
		mch.addChain(test[i], test[i+1])
while True:
	o = mch.generateSequence(10)
	print(o)
	if o[0] == "*" and o[len(o)-1] == ":":
		break

def filter(data):
	return " ".join(data).replace(":", "." ).replace("*","").capitalize()

print(filter(o))