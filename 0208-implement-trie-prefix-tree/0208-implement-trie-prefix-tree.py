class Trie :

	def __init__( self ) :
		self.children = {}
		self.is_it_end = False

	def insert( self, word: str ) -> None :
		head = self
		for char in word :
			if not char in head.children :
				head.children[char] = Trie()
			head = head.children[char]
		head.is_it_end = True

	def search( self, word: str ) -> bool :
		head = self
		for char in word :
			if not char in head.children :
				return False
			head = head.children[char]
		return head.is_it_end

	def startsWith( self, prefix: str ) -> bool :
		head = self
		for char in prefix :
			if not char in head.children :
				return False
			head = head.children[ char ]
		return True