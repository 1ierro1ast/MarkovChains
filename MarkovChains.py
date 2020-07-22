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
