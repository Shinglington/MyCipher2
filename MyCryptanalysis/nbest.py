

class nbest:
	# Keeps n best items 
	def __init__(self, N = 100, reverse = True):
		self.items = []
		self.N = N
		self.reverse = reverse



	def add(self, item, score):
		self.items.append((item, score))
		self.items.sort(key=lambda x : x[1], reverse = self.reverse)
		self.items = self.items[:self.N]

	def __getitem__(self, k):
		return self.items[k]

	def __len__(self):
		return len(self.items)