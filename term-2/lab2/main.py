class Movie:
    def __init__(self, title: str = None, director: str = None, release_year: int = None) -> None:
        if title == None or director == None or release_year == None:
            raise ValueError("Все аргументы должны быть переданы в конструктор")
        self.__ttl = title
        self.__drctr = director
        self.__rls_year = release_year
    
    def __str__(self) -> str:
        return f"\"{self.__ttl}\", {self.__drctr}, {self.__rls_year}"

    def get_title(self) -> str:
        return self.__ttl
    
    def get_director(self) -> str:
        return self.__drctr
    
    def get_release_year(self) -> int:
        return self.__rls_year

class MovieCollection:
    def __init__(self) -> None:
        self.__lib: list = []
    
    def __str__(self) -> str:
        res = ""
        for i in self.__lib:
            res += str(i) + '\n'
        return f"Полный список фильмов:\n{res}"

    def new_movie(self, mov: Movie = None) -> None:
        if (mov != None) or (mov in self.__lib):
            self.__lib += [mov]
    
    def remove_movie(self, mov: Movie = None) -> None:
        if (mov != None) or (mov in self.__lib):
            self.__lib.remove(mov)
    
    def find_movie_by_director(self, director: str = None) -> Movie:
        if director != None:
            for mov in self.__lib:
                if mov.get_director() == director:
                    return mov

    def sort_movies_by_year(self) -> None:
        self.__lib.sort(key = lambda mov: mov.get_release_year())

# int main() :)
if __name__ == "__main__":

    mc = MovieCollection()

    m1 = Movie("Аватар", "Дж. Кэмерон", 2009)
    m2 = Movie("Звёздные войны: новая надежда", "Дж. Лукас", 1977)
    m3 = Movie("Звёздные войны: пробуждение силы", "Дж. Дж. Абрамс", 2015)

    mc.new_movie(m1)
    mc.new_movie(m3)
    mc.new_movie(m2)

    print(mc)

    print(mc.find_movie_by_director(director="Дж. Кэмерон"), end='\n\n')

    mc.sort_movies_by_year()

    print(mc)

    mc.remove_movie(m1)

    print(mc)