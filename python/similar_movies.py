import sys, os, copy


# Given: List of Movies - Movie(Name(str), Rating(int), SimilarMovies(list-Movie Names))
# Movies can have transitive dependency for similarity i.e. M5(Similar: M1), M1(Similar: M5)
# Function: get list of similar movies
# Function: get list of movies with the same rating
# Function: get top similar movies for the given count


class MovieHeap(object):
    """ Movie Heap Class """

    def __init__(self):
        self.elements = list()

    def _heapify(self):
        n = len(self.elements)
        i = n - 1
        while i > 0:
            pp = (i - 1) / 2
            if pp < 0:
                pp = 0
            if self.elements[pp] < self.elements[i]:
                self.elements[pp], self.elements[i] = self.elements[i], self.elements[pp]
            i -= 1

    def pop(self):
        ret = self.elements.pop(0)
        self._heapify()
        return ret

    def push(self, movie):
        self.elements.append(movie)
        self._heapify()


def _movie_exists(check_movie, movie_list):
    """ helper to check if movie exists in movie list """
    movie_names = [m.name for m in movie_list]
    return True if check_movie.name in movie_names else False


# Function: get list of movies with the same rating
def get_movies_with_same_rating(movie_list, expected_rating):
    return filter(lambda x: x.rating == expected_rating, movie_list)


# Function: get top similar movies for the given count - SOLUTION-1
def get_top_rating_movies_heap(movie_list, no_movies):
    """
    *** Solution-1 ***
    Put all in max heap, and get first 5
    """
    movie_heap = MovieHeap()
    for movie in movie_list:
        movie_heap.push(movie)
    return_movies = list()
    for _ in range(no_movies):
        return_movies.append(movie_heap.pop())
    return return_movies


# Function: get top similar movies for the given count - SOLUTION-2
def get_top_rating_movies_dict(movie_list, no_movies):
    """
    *** Solution-2 ***
    Put all in dict with keys as rating, and get first 5 when sorted by ratings
    """
    rating_movie_dict = dict()
    for movie in movie_list:
        if movie.rating not in rating_movie_dict.keys():
            rating_movie_dict[movie.rating] = [movie]
        else:
            rating_movie_dict[movie.rating].append(movie)

    top_rating_movies = list()
    for rating in sorted(rating_movie_dict.keys())[::-1]:
        top_rating_movies.extend(rating_movie_dict[rating])
        if len(top_rating_movies) >= no_movies:
            return top_rating_movies[:no_movies]


class Movie(object):
    def __init__(self, name, rating, similar_movies=None):
        self.name = name
        self.rating = rating
        self.similar_movies = similar_movies

    def __repr__(self):
        return '<Movie:{}>'.format(self.name)


import copy


def get_similar_movies(all_movies_list, movie_name):
    n = len(all_movies_list)
    similar_movie_names = list()

    def _get_movie_index(movie_name):
        i = 0
        while i < n:
            if all_movies_list[i].name == movie_name:
                return i
            i += 1

    def _recurse(visited, i):
        if visited[i]:
            return

        visited_local = copy.deepcopy(visited)
        visited_local[i] = True

        similar_movie_names.append(movies[i].name)
        for movie_name in all_movies_list[i].similar_movies:
            _recurse(visited_local, _get_movie_index(movie_name))

    visited = [False for _ in range(n)]
    _recurse(visited, _get_movie_index(movie_name))
    return similar_movie_names[1:]


if __name__ == '__main__':
    movies = [Movie('M0', 5),
              Movie('M1', 5),
              Movie('M2', 3),
              Movie('M4', 5),
              Movie('M3', 4),
              Movie('M5', 5)
              ]

    movies[0].similar_movies = ['M1']  # M0 -> M1
    movies[1].similar_movies = ['M2', 'M3']  # M1 -> M2, M3
    movies[2].similar_movies = ['M4']  # M2 -> M4
    movies[3].similar_movies = ['M2']  # M3 -> M2
    movies[4].similar_movies = ['M3', 'M5']  # M4 -> M3, M5
    movies[5].similar_movies = []  # M5 -> None

    print '**************************'
    for movie in movies:
        print 'Movie={}, Similar Movies={}'.format(movie.name, get_similar_movies(movies, movie.name))

    print '**************************'
    ratings = [3, 4, 5]
    for rating in ratings:
        print 'Rating={}, Movies={}'.format(rating, get_movies_with_same_rating(movies, rating))

    print '**************************'
    counts = [3, 4, 5]
    for count in counts:
        print 'DICT: Count={}, Top Rated Movies={}'.format(count, get_top_rating_movies_dict(movies, count))
        print 'HEAP: Count={}, Top Rated Movies={}'.format(count, get_top_rating_movies_heap(movies, count))
