class Spreadsheet :

	def __init__( self, rows: int ) :
		self.grid = [ [ 0 for i in range( 26 ) ] for i in range( rows ) ]

	def setCell( self, cell: str, value: int ) -> None :
		column = ord( cell[ 0 ] ) - ord("A")
		row = int( cell[ 1 : ] ) - 1
		self.grid[ row ][ column ] = value

	def resetCell( self, cell: str ) -> None :
		self.setCell( cell, 0 )

	def getCellValue( self, cell: str ) :
		column = ord( cell[ 0 ] ) - ord("A")
		row = int( cell[ 1 : ] ) - 1
		return self.grid[ row ][ column ]

	def is_num( self , x : str ) -> bool :
		try :
			int( x )
			return True
		except ValueError :
			return False

	def getValue( self, formula: str ) -> int :

		formula = formula[1:]
		a , b = formula.split("+")

		a_val = int( a ) if self.is_num( a ) else self.getCellValue( a )

		b_val = int( b ) if self.is_num( b ) else self.getCellValue( b )

		return a_val + b_val

