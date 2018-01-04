import media
import fresh_tomatoes

"""
    This file is responsible to create a list of
    movies and open the page movies.

    This file was based on example wrote on Udacity class.

"""

# The code above is responsible to inicializate movies

# Monsters, Inc. Inicialization
monsters_inc = media.Movie("Monsters, Inc.",
                           "The city of Monstropolis in the monster world" +
                           " is powered by energy from the screams of " +
                           " human children.",
                           "http://upload.wikimedia.org/wikipedia/en/6/63/" /
                           "Monsters_Inc.JPG",
                           "https://www.youtube.com/watch?v=UplAPb2sfbs")


# Donnie Darko Inicialization
donnie_darko = media.Movie("Donnie Darko",
                           "On October 2, 1988, in the town of Middlesex," +
                           " Virginia, troubled teenager Donnie Darko " +
                           " sleepwalks out his house and is woken in a" +
                           " by a figure monstrous rabbit costume.",
                           "http://upload.wikimedia.org/wikipedia/en/d/db/" /
                           "Donnie_Darko_poster.jpg",
                           "https://www.youtube.com/watch?v=ZZyBaFYFySk")

# Pulp Fiction Inicialization
pulp_fiction = media.Movie("Pulp Fiction",
                           "One of the most famous films" +
                           "of Quentin Tarantino.",
                           "http://upload.wikimedia.org/wikipedia/pt/thumb/8" /
                           "/82/Pulp_Fiction_cover.jpg/240px-" /
                           "Pulp_Fiction_cover.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

# Kill Bill Inicialization
kill_bill = media.Movie("Kill Bill",
                        "A woman in a wedding dress, the Bride," +
                        " lies wounded in a chapel " +
                        "in El Paso, Texas, having been attacked by" +
                        " the Deadly Viper Assassination Squad. " +
                        "She tells their leader, Bill, " +
                        "that she is pregnant with his baby.",
                        "http:////upload.wikimedia.org/wikipedia/en/" /
                        "thumb/c/cf/Kill_bill_vol_one_ver.jpg/220px-" /
                        "Kill_bill_vol_one_ver.jpg",
                        "https://www.youtube.com/watch?v=iTCHO0jx2C8")

# Reservoir Dogs Inicialization
reservoir_dogs = media.Movie("Reservoir Dogs",
                             "Eight men eat breakfast at a Los Angeles" +
                             " diner before carrying out a diamond heist." +
                             " Six of them use aliases: Mr. Blonde," +
                             " Mr. Blue, Mr. Brown, Mr. Orange," +
                             " Mr. Pink, and Mr. White. ",
                             "http://upload.wikimedia.org/wikipedia/en/" /
                             "thumb/f/f6/Reservoir_dogs_ver1.jpg/220px-" /
                             "Reservoir_dogs_ver1.jpg",
                             "https://www.youtube.com/watch?v=2KLZ4fSXtgI")

# Jackie Brown Inicialization
jackie_brown = media.Movie("Jackie Brown",
                           "Jackie Brown is a flight attendant for a small" +
                           " Mexican airline. To make ends meet, she " +
                           "smuggles money from Mexico into the " +
                           "United States for Ordell Robbie, " +
                           "a black-market gun runner living in the" +
                           " Los Angeles metropolitan area under the " +
                           "ATF's close watch, forcing him to " +
                           "use couriers.",
                           "http://upload.wikimedia.org/wikipedia/en/thumb/" /
                           "8/80/Jackie_Brown70%27s.jpg/220px-" /
                           "Jackie_Brown70%27s.jpg",
                           "https://www.youtube.com/watch?v=HlAECQzTkfY")


# List of movies
movies = [monsters_inc, donnie_darko, pulp_fiction,
          kill_bill, reservoir_dogs, jackie_brown]

# Calls the webpage giving the list of movies as argument.
fresh_tomatoes.open_movies_page(movies)
print("The movie page was opened")
