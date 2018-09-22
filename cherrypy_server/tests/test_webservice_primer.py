from _webservice_primer import _webservice_primer
import unittest

class TestWebServicePrimer(unittest.TestCase):

	#@classmethod
	#def setUpClass(self):
	MID = 32 # CHANGE TO YOUR MID
	MNAME = 'Twelve Monkeys (1995)' # CHANGE TO YOUR MOVIE NAME
	ws = _webservice_primer()

	def reset_movie(self):
		# needed because we cannot promise an execution order
		self.ws.reset_movie(self.MID)

	def test_get_movie(self):
		self.reset_movie()
		movie = self.ws.get_movie(self.MID)
		self.assertEqual(movie['title'], self.MNAME)

	def test_set_movie_title(self):
		self.reset_movie()
		movie = self.ws.get_movie(self.MID)
		movie['title'] = 'Something Else'
		self.ws.set_movie_title(self.MID, movie['title'])
		movie = self.ws.get_movie(self.MID)
		self.assertEqual(movie['title'], 'Something Else')

	def test_delete_movie(self):
		self.reset_movie()
		self.ws.delete_movie(self.MID)
		movie = self.ws.get_movie(self.MID)
		self.assertEqual(movie['result'], 'error')

if __name__ == "__main__":
	unittest.main()

