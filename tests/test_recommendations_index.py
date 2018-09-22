import unittest
import requests
import json

class TestRecommendationsIndex(unittest.TestCase):

	#@classmethod
	#def setUpClass(self):
	SITE_URL = 'http://student04.cse.nd.edu:52011'
	RECOMMENDATIONS_URL = SITE_URL + '/recommendations/'
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

	def test_recommendations_index_delete(self):
		self.reset_data()

		m = {}
		m['apikey'] = 'AAAAAAAB'
		r = requests.delete(self.RECOMMENDATIONS_URL, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

if __name__ == "__main__":
	unittest.main()

