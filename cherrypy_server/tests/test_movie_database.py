from _movie_database import _movie_database
import unittest

class TestMovieDatabase(unittest.TestCase):
        """unit tests for python primer homework"""

        #@classmethod
        #def setUpClass(self):
        mdb = _movie_database()

        def reset_data(self):
                "reset data is required because we cannot promise an order of test case execution"
                self.mdb.delete_all_ratings()
                self.mdb.load_movies('ml-1m/movies.dat')
                self.mdb.load_users('ml-1m/users.dat')
                self.mdb.load_ratings('ml-1m/ratings.dat')

        def test_get_movie(self):
                self.reset_data()
                movie = self.mdb.get_movie(2)
                self.assertEquals(movie[0], 'Jumanji (1995)')
                self.assertEquals(movie[1], 'Adventure|Children\'s|Fantasy')

        def test_get_movie_null(self):
                self.reset_data()
                movie = self.mdb.get_movie(20000)
                self.assertEquals(movie, None)

        def test_set_movie(self):
                self.reset_data()
                movie = self.mdb.get_movie(2)
                movie[0] = 'ABC'
                self.mdb.set_movie(2, movie)
                movie = self.mdb.get_movie(2)
                self.assertEquals(movie[0], 'ABC')

        def test_delete_movie(self):
                self.reset_data()
                self.mdb.delete_movie(2)
                movie = self.mdb.get_movie(2)
                self.assertEquals(movie, None)

        def test_get_user(self):
                self.reset_data()
                user = self.mdb.get_user(3)
                self.assertEquals(user[1], 25)
                self.assertEquals(user[2], 15)
                self.assertEquals(user[3], '55117')

        def test_set_user(self):
                self.reset_data()
                user = self.mdb.get_user(3)
                user[2] = 6
                self.mdb.set_user(3, user)
                user = self.mdb.get_user(3)
                self.assertEquals(user[1], 25)
                self.assertEquals(user[2], 6)
                self.assertEquals(user[3], '55117')

        def test_delete_user(self):
                self.reset_data()
                self.mdb.delete_user(3)
                user = self.mdb.get_user(3)
                self.assertEquals(user, None)

        def test_get_rating(self):
                self.reset_data()
                rating = self.mdb.get_rating(32)
                self.assertEquals(rating, 3.945731303772336)
                rating = self.mdb.get_rating(110)
                self.assertEquals(rating, 4.234957020057307)
                rating = self.mdb.get_rating(1)
                self.assertEquals(rating, 4.146846413095811)

        def test_get_highest_rated_movie_1(self):
                self.reset_data()
                hrm_mid = self.mdb.get_highest_rated_movie()
                hrm_rating = self.mdb.get_rating(hrm_mid)
                hrm = self.mdb.get_movie(hrm_mid)
                hrm_name = hrm[0]
                self.assertEquals(hrm_mid, 787)
                self.assertEquals(hrm_name, 'Gate of Heavenly Peace, The (1995)')
                self.assertEquals(hrm_rating, 5.0)

        def test_set_user_movie_rating_1(self):
                self.reset_data()
                self.mdb.set_user_movie_rating(41, 787, 2)
                rating = self.mdb.get_rating(787)
                self.assertEquals(rating, 4.25)

        def test_set_user_movie_rating_2(self):
                self.reset_data()
                self.mdb.set_user_movie_rating(41, 787, 2)
                self.mdb.set_user_movie_rating(101, 787, 4)
                rating = self.mdb.get_rating(787)
                self.assertEquals(rating, 4.2)

        def test_set_and_get_movie_ratings(self):
                self.reset_data()
                self.mdb.set_user_movie_rating(41, 787, 2)
                self.mdb.set_user_movie_rating(101, 787, 4)
                hrm_mid = self.mdb.get_highest_rated_movie()
                hrm_rating = self.mdb.get_rating(hrm_mid)
                hrm = self.mdb.get_movie(hrm_mid)
                hrm_name = hrm[0]
                self.assertEquals(hrm_mid, 989)
                self.assertEquals(hrm_name, 'Schlafes Bruder (Brother of Sleep) (1995)')
                self.assertEquals(hrm_rating, 5.0)

        def test_get_user_movie_rating(self):
                self.reset_data()
                rating = self.mdb.get_user_movie_rating(6030, 32)
                self.assertEquals(rating, 5)

if __name__ == "__main__":
    unittest.main()

