# Written by: Levi Biasco (lbiasco)
# Date: 3/4/2018

class _movie_database:

    def __init__(self):
        self.movies = {}
        self.users = {}
        self.ratings = {}

    def load_movies(self, movie_file):
        self.movies = {}
        m_f = open(movie_file, encoding='latin-1')
        movieLines = m_f.read().splitlines()
        for line in movieLines:
            spl = line.split('::')
            self.movies[int(spl[0])] = {'title':spl[1], 'genres':spl[2], 'id':int(spl[0])}
        m_f.close()

    def load_movie(self, movie_file, mid):
        m_f = open(movie_file, encoding='latin-1')
        movieLines = m_f.read().splitlines()
        for line in movieLines:
            spl = line.split('::')
            if(int(spl[0]) == int(mid)):
                self.movies[int(mid)] = {'title':spl[1], 'genres':spl[2], 'id':(spl[0])}
        m_f.close()

    def load_m_images(self, m_image_file):
        m_i_f = open(m_image_file, encoding='latin-1')
        imageLines = m_i_f.read().splitlines()
        for line in imageLines:
            spl = line.split('::')
            if(self.movies[int(spl[0])]):
                self.movies[int(spl[0])]['img'] = spl[2];
            else:
                self.movies[int(spl[0])]['img'] = '/default.jpg'
        m_i_f.close()

    def load_m_image(self, m_image_file, mid):
        m_i_f = open(m_image_file, encoding='latin-1')
        imageLines = m_i_f.read().splitlines()
        changed = False
        for line in imageLines:
            spl = line.split('::')
            if(self.movies[int(spl[0])] == mid):
                self.movies[int(mid)]['img'] = spl[2]
                changed = True
        if(not changed):
            if(self.movies.get(int(mid))):
                self.movies[int(mid)]['img'] = '/default.jpg'
        m_i_f.close()       

    def get_movie(self, mid):
        return self.movies.get(int(mid))

    def get_movies(self):
        return { 'movies':self.movies }

    def set_movie(self, mid, movie):
        self.movies[int(mid)] = movie 

    def delete_movie(self, mid):
        if(int(mid) in self.movies):
            del self.movies[int(mid)]    

    def delete_movies(self):
        self.movies = {}

    def load_users(self, users_file):
        self.users = {}
        u_f = open(users_file, encoding='latin-1')
        userLines = u_f.read().splitlines()
        for line in userLines:
            spl = line.split('::')
            self.users[int(spl[0])] = {'gender':spl[1], 'age':int(spl[2]), 'occupation':int(spl[3]), 'zipcode':spl[4], 'id':int(spl[0])}
        u_f.close()

    def get_user(self, uid):
        return self.users.get(int(uid))

    def get_users(self):
        return { 'users':self.users }

    def set_user(self, uid, user):
        self.users[int(uid)] = user

    def delete_user(self, uid):
        if(int(uid) in self.users):
            del self.users[int(uid)]    

    def delete_users(self):
        self.users = {}

    def load_ratings(self, ratings_file):
        self.ratings = {}
        r_f = open(ratings_file, encoding='latin-1')
        ratingsLines = r_f.read().splitlines()
        for line in ratingsLines:
            spl = line.split('::')
            if(int(spl[1]) not in self.ratings):
                self.ratings[int(spl[1])] = {}
            self.ratings[int(spl[1])][int(spl[0])] = int(spl[2])
        r_f.close()

    def get_rating(self, mid):
        if(int(mid) in self.ratings and len(self.ratings[int(mid)]) != 0):
            return sum(self.ratings[int(mid)].values()) / len(self.ratings[int(mid)])
        else:
            return 0

    def get_highest_rated_movie(self):
        high_r = 0
        mid = -1
        for key in self.ratings:
            r = self.get_rating(key)
            if(r >= high_r):
                if(r > high_r or key < mid):
                    high_r = r
                    mid = key
        return mid 

    def set_user_movie_rating(self, uid, mid, rating):
        if(int(mid) in self.movies and int(uid) in self.users):
            self.ratings[int(mid)][int(uid)] = int(rating)

    def get_user_movie_rating(self, uid, mid):
        if(int(mid) not in self.movies):
            return None
        return self.ratings[int(mid)].get(int(uid))

    def delete_ratings(self, mid):
        if(self.ratings[int(mid)]):
            self.ratings[int(mid)] = {}

    def delete_all_ratings(self):
        for key in self.ratings:
            self.ratings[key] = {}

    def get_recommendation(self, uid):
        seen = []
        while(True):
            high_r = 0
            mid = -1
            for key in self.ratings:
                r = self.get_rating(key)
                if(r >= high_r):
                    if(not key in seen and (r > high_r or key < mid)):
                        high_r = r
                        mid = key
            mid
            if(self.get_user_movie_rating(int(uid), mid) == None):
                return mid
            else:
                seen.append(mid)
            if(len(self.movies) <= len(seen)):
                return None

    def load_all_preset(self):
        self.load_movies('ml-1m/movies.dat')
        self.load_m_images('ml-1m/images.dat')
        self.load_users('ml-1m/users.dat')
        self.load_ratings('ml-1m/ratings.dat')

    def load_movie_preset(self, mid):
        self.load_movie('ml-1m/movies.dat', mid)
        self.load_m_image('ml-1m/images.dat', mid)
