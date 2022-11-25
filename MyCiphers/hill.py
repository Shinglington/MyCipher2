from MyCiphers.cipher import Cipher


class Hill(Cipher):

	def __init__(self, key="ABCD"):
		Cipher.__init__(self)
		self.size = int(len(key)**0.5)
		assert len(key) == self.size**2, "Key must produce square matrix"

		self.matrix = self.make_matrix(key.upper())
		self.inverse = self.get_inverse(self.matrix)
		assert self.inverse != None

	def encrypt_string(self, string):
		assert len(string) == self.size, "substring must be same size as matrix size"
		old_indices = [self.char_to_int(string[i]) for i in range(self.size)]
		new_indices = self.matrix_multiply(self.matrix, old_indices)
		return ''.join([self.int_to_char(x) for x in new_indices])

	def decrypt_string(self, string):
		assert len(string) == self.size, "substring must be same size as matrix size"
		old_indices = [self.char_to_int(string[i]) for i in range(self.size)]
		new_indices = self.matrix_multiply(self.inverse, old_indices)
		return ''.join([self.int_to_char(x) for x in new_indices])

	def encrypt(self, plaintext, keep_punct=False):
		text = self.remove_punct(plaintext)
		while len(text) % self.size != 0:
			text += "X"
		ciphertext = ""
		for i in range(0, len(text), self.size):
			ciphertext += self.encrypt_string(text[i:i + self.size])

		if keep_punct:
			ciphertext = self.restore_punct(ciphertext, plaintext)
		return ciphertext

	def decrypt(self, ciphertext, keep_punct=False):
		text = self.remove_punct(ciphertext)
		assert len(
		 text) % self.size == 0, "Ciphertext must be a multiple of the matrix size"
		plaintext = ""
		for i in range(0, len(text), self.size):
			plaintext += self.decrypt_string(text[i:i + self.size])

		if keep_punct:
			plaintext = self.restore_punct(ciphertext, plaintext)
		return plaintext

	def make_matrix(self, key):
		matrix = []
		for i in range(self.size):
			matrix.append([
			 self.char_to_int(x) for x in key[i * self.size:i * self.size + self.size]
			])
		return matrix

	def get_inverse(self, matrix):
		adj_matrix = []
		det = self.matrix_determinant(matrix)
		inv_det = None
		for i in range(1, 26, 2):
			if (det * i) % 26 == 1:
				inv_det = i
		assert inv_det != None, "Key matrix must have an inverse"

		if len(matrix) == 2:
			adj_matrix = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
		else:
			adj_matrix = self.transpose_matrix(self.matrix_cofactors(matrix))

		inv_matrix = []
		for row in range(self.size):
			inv_row = [(x * inv_det) % 26 for x in adj_matrix[row]]
			inv_matrix.append(inv_row)

		return inv_matrix

	def matrix_multiply(self, a, b):
		assert len(a[0]) == len(b)
		product = []
		for row in range(len(a)):
			new_row = []
			if isinstance(b[row], int):
				new_item = 0
				for i in range(len(a[row])):
					new_item += a[row][i] * b[i]
				new_row.append(new_item)
			else:
				for col in range(len(b[row])):
					new_item = 0
					for i in range(len(a[row])):
						new_item += a[row][i] * b[i][col]
					new_row.append(new_item)
			if len(new_row) == 1:
				product.append(new_row[0])
			else:
				product.append(new_row)
		return product

	def matrix_determinant(self, matrix):
		if len(matrix) == 2:
			return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
		else:
			determinant = 0
			cofactors = self.matrix_cofactors(matrix)
			for j in range(len(matrix)):
				determinant += matrix[0][j] * cofactors[0][j]
			return determinant

	def matrix_cofactors(self, matrix):
		cofactor_matrix = []
		## find cofactor of each element in matrix
		for row in range(len(matrix)):
			cofactor_row = []
			for col in range(len(matrix)):
				minor = self.matrix_determinant(self.matrix_minor(matrix, row, col))
				cofactor = minor * ((-1)**(row + col))
				cofactor_row.append(cofactor)
			cofactor_matrix.append(cofactor_row)
		return cofactor_matrix

	def matrix_minor(self, matrix, row, col):
		minor = []
		for i in range(len(matrix)):
			if i != row:
				minor_row = []
				for j in range(len(matrix)):
					if j != col:
						minor_row.append(matrix[i][j])
				minor.append(minor_row)
		return minor

	def transpose_matrix(self, matrix):
		transposed = []
		for j in range(len(matrix)):
			new_row = []
			for i in range(len(matrix)):
				new_row.append(matrix[i][j])
			transposed.append(new_row)
		return transposed
