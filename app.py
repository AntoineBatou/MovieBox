import database
import datetime

menu = """Veuillez sélectionner l'une des options suivantes :
1) Ajouter un nouveau film.
2) Voir les films à venir.
3) Voir tous les films
4) Regarder un film
5) Voir les films visionnés.
6) Quitter.
Your selection: """
welcome = "Bienvenue dans l'application watchlist !"

print(welcome)

database.create_tables()

def prompt_add_movie():
    title = input("Titre du film : ")
    release_date = input("Date de sortie (jj-mm-aaaa) : ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_movie(title, timestamp)

def print_movie_list(heading, movies):
    print(f'---- FILMS {heading} -----')
    for number, movie in enumerate(movies):
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%d %b %Y")
        print(f'{number} - {movie[0]} le {human_date}')
    print("---- \n")

def print_watched_movies(heading, movies):
    print(f'---- FILMS VISIONNES PAR {heading} -----')
    for number, movie in enumerate(movies):
        print(f'{number} - {movie[1]} le')
    print("---- \n")

def prompt_set_watched():
    title = input("Titre du film : ")
    user = input("Qui a regardé ? : ")
    database.watch_movie(user, title)

while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("A VENIR", movies)
    elif user_input == "3":
        movies = database.get_movies(False)
        print_movie_list("SORTIS", movies)
    elif user_input == "4":
        prompt_set_watched()
    elif user_input == "5":
        username = "Quel utilisateur ? : "
        movies = database.get_watched_movie(username)
        print_watched_movies(username, movies)
    else:
        print("Entrée invalide, veuillez réessayer !")