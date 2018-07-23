"""
In this file I'm going to create 6 instances of movie object and I'll put them
in a list called movies. Then I'll use that list to open the movie trailer
webpage by executing the function open_movies_page.
"""
import media
import movie_trailers


# instance of movie object called grandpa
GRANDPA = media.Movie('Dirty Grandpa',
                      "American comedy film about a lawyer who drives his"
                      "grandfather to Florida during spring break",
                      "https://upload.wikimedia.org/wikipedia/en/6/62/"
                      "Dirty_Grandpa_teaser_poster.jpg",
                      "https://www.youtube.com/watch?v=aZSzMIFZT7Q")

CHANGE = media.Movie("Change-up",
                     "Two long-time friends with opposing lifestyles are each "
                     "in the other's shoes",
                     "https://upload.wikimedia.org/wikipedia/en/4/42/"
                     "Change_up_poster.jpg",
                     "https://www.youtube.com/watch?v=43Qc70ZeMFw")

ABIDING = media.Movie("Law abiding citizen",
                      "The story of a man driven to seek justice while "
                      "targeting not only his family's killer but "
                      "also those who have supported a corrupt criminal "
                      "justice system, intending to assassinate "
                      "anyone supporting the system",
                      "https://upload.wikimedia.org/wikipedia/en/9/95/"
                      "Law_abiding_citizen_ver5.jpg",
                      "https://www.youtube.com/watch?v=LX6kVRsdXW4")

TAKERS = media.Movie("Takers",
                     "The film follows a group of professional bank robbers "
                     "who specialize in spectacular robberies",
                     "https://upload.wikimedia.org/wikipedia/en/3/30/"
                     "Takers_poster.jpg",
                     "https://www.youtube.com/watch?v=Z1JXKCProqA")

LEFT = media.Movie("Left Behind",
                   "An airline pilot struggles to save the lives of the "
                   "passengers who remain on his flight, "
                   "while his daughter races to find her brother and mother, "
                   "both of whom have disappeared",
                   "https://upload.wikimedia.org/wikipedia/en/7/70/"
                   "Left_Behind_film_poster.jpg",
                   "https://www.youtube.com/watch?v=GrXe8YDbzYs")

RUN = media.Movie("Run All Night",
                  "The story about an ex-hitman who goes on the run with his "
                  "estranged adult son after he is forced "
                  "to kill the son of a mafia boss",
                  "https://upload.wikimedia.org/wikipedia/en/8/81/"
                  "RunAllNight_TeaserPoster.jpg",
                  "https://www.youtube.com/watch?v=6P_C73BPT7M")

# list of movies
MOVIES = [GRANDPA, CHANGE, ABIDING, TAKERS, LEFT, RUN]

movie_trailers.open_movies_page(MOVIES)
