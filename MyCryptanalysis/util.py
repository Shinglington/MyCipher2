import MyCryptanalysis.ngram_score as ngram_score

def Calc_Ioc(text, alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
	freqs = Get_MonoFrequencies(text)
	ioc = 0
	for c in freqs:
		c_count = freqs[c]
		charIOC = (c_count * (c_count - 1)) / (len(text) * (len(text) - 1))
		ioc += charIOC
	return ioc


def Calc_Chi_Squared(text):
	freqs = Get_MonoFrequencies(text)
	expected_freqs = ngram_score.get_expected_ngrams(1)
	expected_total = sum(expected_freqs.values())
	chi_squared = 0
	for c in expected_freqs:
		expected_prob = int(expected_freqs[c] / expected_total)
		expected_count = len(text) * expected_prob
		
		actual_count = 0
		if c in freqs:
			actual_count = freqs[c]
			
		result = ((actual_count - expected_count)**2) / expected_count
		chi_squared += result
	return chi_squared

def Get_MonoFrequencies(text, alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
	freqs = {}
	for l in alphabet:
		freqs.update({l:0})

	for c in text:
		if c in alphabet:
			freqs.update({c:freqs[c] + 1})
	return freqs