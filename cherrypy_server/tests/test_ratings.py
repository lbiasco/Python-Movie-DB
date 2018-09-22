import unittest
import requests
import json

class TestRatings(unittest.TestCase):

	#@classmethod
	#def setUpClass(self):
	SITE_URL = 'http://student04.cse.nd.edu:52011'
	RATINGS_URL = SITE_URL + '/ratings/'
	RESET_URL = SITE_URL + '/reset/'

	def reset_data(self):
		m = {}
		m['apikey'] = 'AAAAAAAB'
		r = requests.put(self.RESET_URL)

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	def test_ratings_get(self):
		self.reset_data()
		movie_id = 32

		r = requests.get(self.RATINGS_URL + str(movie_id))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['rating'], 3.945731303772336)
		self.assertEqual(resp['movie_id'], movie_id)

if __name__ == "__main__":
	unittest.main()

