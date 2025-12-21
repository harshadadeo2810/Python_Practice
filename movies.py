movies_2025 = {}

ch_cast = ["Vicky Kaushal", "Akshay Khanna", "Rashmika Mandanna"]
movies_2025["Chhaava"] = ch_cast  


dh_cast = ["Ranveer Singh", "Akshay Khanna", "Sanjay Dutt"]
movies_2025["Dhurandhar"] = dh_cast

d_cast = ["Siddhant Chaturvedi", "Tripti Dimri", "Zakir Hussain"]
movies_2025["Dhadak 2"] = d_cast  

w_cast = ["Hrithik Roshan", "Kiara Advani"]
movies_2025["War 2"] = w_cast


movies_2024 = {}

f_cast = ["Hrithik Roshan", "Deepika Padukone", "Anil Kapoor"]
movies_2024["Fighter"] = f_cast

b_cast = ["Vicky Kaushal", "Tripti Dimri"]
movies_2024["Bad Newz"] = b_cast

s_cast = ["Shraddha Kapoor", "Rajkummar Rao", "Pankaj Tripathi"]
movies_2024["Stree 2"] = s_cast

bh_cast = ["Kartik Aryan", "Madhuri Dixit", "Tripti Dimri", "Vidya Balan"]
movies_2024["Bhool Bhulaiyaa 3"] = bh_cast


movies_2023 = {}

sh_cast = ["Kartik Aryan", "Kriti Sanon"]
movies_2023["Shehzada"] = sh_cast

t_cast = ["Ranbir Kapoor", "Shraddha Kapoor"]
movies_2023["Tu Jhoothi Main Makkaar"] = t_cast

z_cast = ["Vicky Kaushal", "Sara Ali Khan"]
movies_2023["Zara Hatke Zara Bachke"] = z_cast

sa_cast = ["Kartik Aryan", "Kiara Advani"]
movies_2023["Satyaprem ki katha"] = sa_cast


all_movies = {
    "2025": movies_2025,
    "2024": movies_2024,
    "2023": movies_2023
}



actor_name = input("Enter actor name: ")

count = 0
for year, movies in all_movies.items():
    for movie, cast in movies.items():
        if actor_name in cast:
            print(year, "-", movie)
            count = count + 1

print("Total movies:", count)

## 2025 movies 
# name starts with s
movies_2025 = all_movies["2025"]
                                                       ## Sanjay Dutt ,v Siddhant Chaturvedi
for cast in movies_2025.values():
    for actor in cast:
        if actor.startswith("S"):
            print(actor)





# ends with a
for cast in movies_2025.values():
    for actor in cast:
        if actor.endswith("a"):                    ##Akshay Khanna ,Rashmika Mandanna ,Akshay Khanna  
            print(actor) 



## names starts with consonanats
consonants = "bcdfghjklmnpqrstvwxyz"

for cast in movies_2025.values():
    for actor in cast:                                      
        if actor[-1].lower() in consonants:
            print(actor)                        ## Vicky Kaushal,Ranveer Singh,Sanjay Dutt ,Zakir Hussain ,Hrithik Roshan




# actors in 2025
result = []

for cast in movies_2025.values():          
    for actor in cast:
        if actor not in result:            ## name of actors without repeating the name 
            result.append(actor)
            print(actor)                                   





## movies of 2025
count = 0
for movie in movies_2025.keys():
    print (movie)                                      ## names of movies of 2025 
    count = count + 1 
print("Total movies in 2025:", count)





## to find movie
movie_name = input("Enter movie name: ")

if movie_name in movies_2025:                        ## by entering the name of movie we are getting the result
    print("Movie exists in 2025")
else:
    print("Movie not found")



# Finds the movie in 2025 that has the highest number of actors

max_movie = ""
max_count = 0

for movie, cast in movies_2025.items():
    if len(cast) > max_count:                             
        max_count = len(cast)
        max_movie = movie

print(max_movie, "has", max_count, "actors")



## for 2024 


movies_2024 = all_movies["2024"]

## suranme starts with K
for cast in movies_2024.values():
    for actor in cast:
        surname = actor.split()[-1]              ## Anil Kapoor ,Vicky Kaushal ,Shraddha Kapoor
        if surname.startswith("K"):
            print(actor)


## movie starts with B 
for movie in movies_2024:                          ## Bhool Bhulaiyaa 3 , Bad Newz    
    if movie.startswith("B"):
        print(movie)


## # Prints movies from 2024 that have more than 3 actors

for movie, cast in movies_2024.items():               ## Bhool Bhulaiyaa 3
    if len(cast) > 3:
        print(movie)



## 2023 

movies_2023 = all_movies["2023"]

## movie starts with s and endswith a 
for movie in movies_2023:                                     ##   Shehzada ,Satyaprem ki katha
    name = movie.lower()
    if name.startswith("s") and name.endswith("a"):
        print(movie)

## # Prints the surnames of all actors from 2023 movies

surnames = []

for cast in movies_2023.values():
    for actor in cast:
        surname = actor.split()[-1]
        surnames.append(surname)

print(", ".join(surnames))

## Output : -- Aryan, Sanon, Kapoor, Kapoor, Kaushal, Khan, Aryan, Advani


# Actors starts with K
 
result = []

for cast in movies_2023.values():                                 ## ['Kartik Aryan', 'Kriti Sanon', 'Kiara Advani']   
    for actor in cast:
        if actor.startswith("K") and actor not in result:
            result.append(actor)

print(result)


## # Prints actor names from 2023 whose length is more than 12 characters 

long_names = []

for cast in movies_2023.values():
    for actor in cast:
        if len(actor) > 12:
            long_names.append(actor)

print(", ".join(long_names))
 
 
 ## Output :- Ranbir Kapoor, Shraddha Kapoor, Vicky Kaushal, Sara Ali Khan 
 
 
 
 
 
 






