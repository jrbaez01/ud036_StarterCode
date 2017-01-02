from media import Movie
import fresh_tomatoes
import csv

# A list of Movie instaces that will be created from my favorite_movies_list.csv file
movies = []

# First I open my favorite_movies_list.csv file
with open('favorite_movies_list.csv') as csv_movies_file:
	# Then I need to read my csv, so I use the csv module utilisties.
	#Re: https://docs.python.org/2/library/csv.html
	csv_movies_reader = csv.reader(csv_movies_file) # I get a reader object.
	# I do not need the first row of the csv file because they are the headers.
	# So I skip it for now using the .next() method of the reader object, re: https://docs.python.org/2/library/csv.html#reader-objects
	csv_movies_reader.next()
	# Now I am free to iterate and create the Movie instaces from my favorite_movies_list.csv
	for movie_info in csv_movies_reader:
		title = movie_info[0]
		storyline = movie_info[1]
		poster_image_url = movie_info[2]
		trailer_youtube_url = movie_info[3]
		# Create a Movie instace and append it to my movies list
		movies.append( Movie(title, storyline, poster_image_url, trailer_youtube_url) )

# Now fresh_tomatoes does the rest, it opens a page of my favorite movies.
fresh_tomatoes.open_movies_page(movies)
 