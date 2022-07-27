import numpy as np
import pandas as pd
import streamlit as st 
import requests
import pickle

model=pickle.load(open('model.pkl', 'rb'))


st.title("IMDb Score Prediction for Movies")



def predict(content_rating,genre,voted_users,duration,budget,movie_facebook_likes,gross,actor_1_facebook_likes,cast_crew_total_facebook_likes,facenumber_in_poster,critic_review_ratio):
 
     if content_rating == 'PG-13':
          content_rating = 0
     elif content_rating =='PG':
          content_rating = 1
     elif content_rating =='G':
          content_rating = 2
     elif content_rating =='R':
          content_rating = 3
     elif content_rating =='TV-14':
          content_rating = 4
     elif content_rating =='Not Rated':
          content_rating = 5
     elif content_rating =='Unrated':
          content_rating = 6
     elif content_rating =='Approved':
          content_rating = 7
     elif content_rating =='NC-17':
          content_rating = 8
     elif content_rating =='X':
          content_rating = 9
     elif content_rating =='GP':
          content_rating = 10
     elif content_rating =='Passed':
          content_rating = 11
     elif content_rating =='M':
          content_rating = 12
     elif content_rating =='TV-G':
          content_rating = 13
     elif content_rating =='TV-PG':
          content_rating = 14

     if genre== 'Action':
        genre = 0
     elif genre =='Adventure':
        genre = 1
     elif genre =='Drama':
        genre = 2
     elif genre =='Animation':
        genre = 3
     elif genre =='Comedy':
        genre = 4
     elif genre =='Mystery':
        genre = 5
     elif genre =='Crime':
        genre = 6
     elif genre =='Biography':
        genre = 7
     elif genre =='Fantasy':
        genre = 8
     elif genre =='Documentary':
        genre = 9 
     elif genre =='Sci-Fi':
            genre = 10
     elif genre =='Horror':
            genre = 11
     elif genre =='Romance':
            genre = 12
     elif genre =='Thriller':
            genre = 13
     elif genre =='Family':
            genre = 14 
     elif genre =='Music':
            genre = 15
     elif genre =='Western':
            genre = 16
     elif genre =='Musical':
            genre = 17
     elif genre =='Film-Noir':
            genre = 18   

     prediction = model.predict(pd.DataFrame([[content_rating,genre,voted_users,duration,budget,movie_facebook_likes,gross,actor_1_facebook_likes,cast_crew_total_facebook_likes,facenumber_in_poster,critic_review_ratio]], columns=['content_rating','genres','num_voted_users','duration', 'budget', 'movie_facebook_likes', 'gross', 'actor_1_facebook_likes','cast_crew_total_facebook_likes','facenumber_in_poster','critic_review_ratio']))
     return prediction

content_rating= st.selectbox('content_rating:',['PG-13', 'PG', 'G', 'R', 'TV-14', 'Not Rated', 'Unrated', 'Approved', 'NC-17', 'X', 'GP', 'Passed', 'M', 'TV-G', 'TV-PG'])
genre = st.selectbox('genres:',['Action', 'Adventure', 'Drama', 'Animation', 'Comedy', 'Mystery', 'Crime', 'Biography','Fantasy', 'Documentary', 'Sci-Fi', 'Horror','Romance', 'Thriller', 'Family', 'Music', 'Western', 'Musical', 'Film-Noir'])
voted_users  = st.number_input('num_voted_users:',min_value=0.0, max_value=10000.0)
duration = st.number_input('duration:',min_value=10.0, max_value=500.0)
budget = st.number_input('budget:',min_value=100.0, max_value=100000000.0)
movie_facebook_likes = st.number_input('movie_facebook_likes:',min_value=10.0, max_value=10000.0)
gross = st.number_input('gross:',min_value=100.0, max_value=100000000.0)
actor_1_facebook_likes = st.number_input('actor_1_facebook_likes:',min_value=0.0, max_value=10000.0)
cast_crew_total_facebook_likes = st.number_input('cast_crew_total_facebook_likes:',min_value=0.0, max_value=100000.0)
facenumber_in_poster = st.number_input('facenumber_in_poster:',min_value=0.0, max_value=50.0)
critic_review_ratio = st.number_input('critic_review_ratio:',min_value=0.0, max_value=10000.0)


if st.button("PREDICT IMDb SCORE"):
    imdb_score=predict(content_rating,genre,voted_users,duration,budget,movie_facebook_likes,gross,actor_1_facebook_likes,cast_crew_total_facebook_likes,facenumber_in_poster,critic_review_ratio)
    output = round(imdb_score[0], 1)
    st.write(output)
