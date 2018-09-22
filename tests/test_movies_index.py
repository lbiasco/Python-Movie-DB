import unittest
import requests
import json

class TestMoviesIndex(unittest.TestCase):

	#@classmethod
	#def setUpClass(self):
	#	self.SITE_URL = 'http://student02.cse.nd.edu:40001'
	#	self.MOVIES_URL = self.SITE_URL + '/movies/'
	#	self.RESET_URL = self.SITE_URL + '/reset/'
	SITE_URL = 'http://student04.cse.nd.edu:52011'
	MOVIES_URL = SITE_URL + '/movies/'
	RESET_URL = SITE_URL + '/reset/'

	def reset_data(self):
		m = {}
		m['apikey'] = 'AAAAAAAB'
		r = requests.put(self.RESET_URL, json.dumps(m))

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	def test_movies_index_get(self):
		self.reset_data()
		r = requests.get(self.MOVIES_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())

		testmovie = {}
		testmovie['title'] = 'Blah'
		testmovie['genres'] = 'None'

		movies = resp['movies']
		for movie in movies.values():
			if movie['id'] == 32:
				testmovie = movie

		self.assertEqual(testmovie['title'], 'Twelve Monkeys (1995)')
		self.assertEqual(testmovie['genres'], 'Drama|Sci-Fi')

	def test_movies_index_post(self):
		self.reset_data()

		m = {}
		m['title'] = 'ABC'
		m['genres'] = 'Sci-Fi|Fantasy'
		m['apikey'] = 'AAAAAAAB'
		r = requests.post(self.MOVIES_URL, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['id'], 3953)

		r = requests.get(self.MOVIES_URL + str(resp['id']))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['title'], m['title'])
		self.assertEqual(resp['genres'], m['genres'])

	def test_movies_index_delete(self):
		self.reset_data()

		m = {}
		m['apikey'] = 'AAAAAAAB'
		r = requests.delete(self.MOVIES_URL, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.MOVIES_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		movies = resp['movies']
		self.assertFalse(movies)

if __name__ == "__main__":
	unittest.main()

