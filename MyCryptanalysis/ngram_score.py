import math


## Initialise default English frequencies
class ngram_score():
	TEXTFILE_NAMES = [
	 "monograms.txt", "bigrams.txt", "trigrams.txt", "quadgrams.txt"
	]
	

	def __init__(self, default=True):

		folder = "MyCryptanalysis/ngram_freqs/"
		if default:
			folder += "default/"
		else:
			folder += "custom/"
		## setup list to store dictionaries of ngram counts
		## ngrams[i] returns n = i+1 ngrams
		self.ngrams = [{}, {}, {}, {}]
		self.totals = [0, 0, 0, 0]
		self.log_probs = [{}, {}, {}, {}]
		for i in range(len(self.ngrams)):
			self.ngrams[i] = self.load_ngram_file(folder + self.TEXTFILE_NAMES[i])
			self.totals[i] = sum([int(x) for x in self.ngrams[i].values()])
			self.log_probs[i] = self.load_log_probs(self.ngrams[i], self.totals[i])

	def load_ngram_file(self, filename, sep=' '):
		ngram_dict = {}
		for line in open(filename):
			key, count = line.split(sep)
			ngram_dict.update({key: count.strip("\n")})
		return ngram_dict

	def load_log_probs(self, ngram_dict, total):
		log_probs = {}
		for key in ngram_dict.keys():
			log_probs[key] = math.log10(float(ngram_dict[key]) / total)
		return log_probs

	def get_ngram_dict(self, n):
		if n > 0 and n < 5:
			return self.ngrams[n - 1]
		else:
			return {}

	def get_ngram_totals(self, n):
		if n > 0 and n < 5:
			return self.totals[n - 1]
		else:
			return 0

	def calc_fitness(self, text, n=4):
		score = 0
		for i in range(len(text) - n):
			string = text[i:i + n]
			if string in self.log_probs[n - 1].keys():
				score += self.log_probs[n - 1][string]
			else:
				score += math.log10(0.01 / self.totals[n - 1])
		return score


## GLOBAL NGRAM COUNTER
expected_ngrams = ngram_score()


def calc_score(text):
	return expected_ngrams.calc_fitness(text)

def get_expected_ngrams(n):
	return expected_ngrams.get_ngram_dict(n)
