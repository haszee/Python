favourite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

add_movie = input("Would you like to add a movie to your favourites? (y/n) ")

if add_movie == 'y':
	movie_name_add = input("Enter a movie to add to your favourites: ")
	favourite_movies.append(movie_name_add)
	print(f"\n{movie_name_add} has been added to your favourites!\n")
else:
	print("\nNo problem!\n")

remove_movie = input("Would you like to remove a movie from your favourites? (y/n) ")

if remove_movie == 'y':
	movie_name_remove = input(f"\nPlease select a movie to remove from your favourites:\n\n{'\n'.join(f"{item}" for item in favourite_movies)}: \n\n")

	favourite_movies.remove(movie_name_remove)
	print(f"\n{movie_name_remove} has been removed from your favourites!\n")
else:
	print("\nYou got it!\n")

favourite_movies.sort()

print(f"Total number of movies in your favourites: {len(favourite_movies)}\n")

print(f"Your favourite movies are:\n\n{'\n'.join(f"{item}" for item in favourite_movies)}" )


