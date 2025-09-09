import database
import datetime

menu = """Veuillez sélectionner l'une des options suivantes :
1) Ajouter un nouveau film.
2) Voir les films à venir.
3) Voir tous les films
4) Regarder un film
5) Voir les films visionnés.
6) Ajouter un utilisateur
7) Quitter.
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
    for movie in enumerate(movies):
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        human_date = movie_date.strftime("%d %b %Y")
        print(f'{movie[0]} - {movie[1]} le {human_date}')
    print("---- \n")

def prompt_show_watched_movies():
    username2 = input("Nom d'utilisateur : ")
    movies2 = database.get_watched_movie(username2)
    if movies2:
        print(f'---- FILMS VISIONNES PAR {username2} -----')
        for number, movie in enumerate(movies2):
            print(f'{number} - {movie[1]} le')
        print("---- \n")
    else:
        print("Cet utilisateur n'a pas visionné de film !")

def prompt_set_watched():
    id = input("ID du film : ")
    user = input("Qui a regardé ? : ")
    database.watch_movie(user, id)

def prompt_add_user():
    username = input("Nom de l'utilisateur :")
    database.add_user(username)


while (user_input := input(menu)) != "7":
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
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    else:
        print("Entrée invalide, veuillez réessayer !")