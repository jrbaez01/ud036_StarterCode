from media import Movie
import fresh_tomatoes
import urllib
import csv

# A list of Movie instaces that will be created from my favorite_movies_list.csv
movies = []

# First I open my favorite_movies_list.csv file. 
# I figured out how to export and get it from google spreadsheet API
movie_list_source = "https://docs.google.com/spreadsheets/export?format=csv&id=1r1LxIisry01G0_RyGpKYRzZVGyY5st8t_cDzROhgQbo&gid=0"  # NOQA
csv_movies_response = urllib.urlopen(movie_list_source)

# Then I need to read my csv, so I use the csv module utilities.
# Re: https://docs.python.org/2/library/csv.html
csv_movies_reader = csv.reader(csv_movies_response)  # I get a reader object.

# I do not need the first row of the csv file because they are the headers.
# So I skip it for now using the .next() method of the reader object.
# re: https://docs.python.org/2/library/csv.html#reader-objects
csv_movies_reader.next()

# Now I am free to iterate and create the Movie instaces
for movie_info in csv_movies_reader:
	title = movie_info[0]
	storyline = movie_info[1]
	poster_image_url = movie_info[2]
	trailer_youtube_url = movie_info[3]

	# Create a Movie instace and append it to my movies list
	movies.append(
		Movie(title, storyline, poster_image_url, trailer_youtube_url)
	)

# Now fresh_tomatoes does the rest, it opens a page of my favorite movies.
fresh_tomatoes.open_movies_page(movies)
