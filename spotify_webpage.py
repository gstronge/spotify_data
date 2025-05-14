import streamlit as st
from flask import Flask, request, jsonify

import requests
import json

app = Flask(__name__)




st.title('Hit predictor')
st.write('predict a hit!')


dance = st.slider("Select the danceability", min_value=0.00, max_value=1.00, value=0.50)
enrg = st.slider("Select the energy", min_value=0.00, max_value=1.00, value=0.50)
loud = st.slider("Select the loudness", min_value=-1.00, max_value=1.00, value=0.00)
speech = st.slider("Select the speechiness", min_value=0.00, max_value=1.00, value=0.50)
acoustic = st.slider("Select the acousticness", min_value=0.00, max_value=1.00, value=0.50)
instrumental = st.slider("Select the instrumentalness", min_value=0.00, max_value=1.00, value=0.50)
live = st.slider("Select the liveness", min_value=0.00, max_value=1.00, value=0.50)
val = st.slider("Select the valence", min_value=0.00, max_value=1.00, value=0.50)

temp = st.slider("Select the Tempo", min_value=0, max_value=250, value=125)

duration = st.number_input("Enter the song duration in seconds", min_value=0, max_value=6000, value=0)

num_songs = st.number_input("Number of songs by this artist", min_value=0, max_value=999, value=42)
percent_hits = (st.number_input("Number of hits by this artist", min_value=0, max_value=100, value=42))/num_songs

yr = st.selectbox("Choose a genre", ["2000", "2001", "2002"])

genr = st.selectbox("Choose a genre", ["Rock", "Blues", "Pop"])
# st.write("You selected:", genr)

ky = st.slider("Select the Key", min_value=0, max_value=11, value=0)
# mode_str = st.radio("Select the mode", ["Major", "Minor"])
# mode_val = 1 if mode_str == "Major" else 0

time_sig = st.slider("Select the Time Signature", min_value=0, max_value=5, value=2)

if st.button("Will it be a hit?"):
    data = {
        "inputs": [
            {
                "danceability": dance,
                "energy": enrg,
                "loudness": loud,
                "speechiness": speech,
                "acousticness": acoustic,
                "instrumentalness": instrumental,
                "liveness": live,
                "valence": val,
                "tempo": temp,
                "duration_ms": duration,
                "no_of_songs": num_songs,
                "popular_song_percentage": percent_hits,
                "year": yr,
                "genre": genr,
                "key": ky,
                "time_signature": time_sig,
            }
        ]
    }
    response = requests.post(
        url="http://localhost:5000/invocations",
        headers={"Content-Type": "application/json"},
        data=json.dumps(data)
    )

    print(response.json())
    st.write("Checking...")
    # Insert model training code here

# mlflow-artifacts:/811932844240729824/3028e01f53df44a792c46490c946b2cd/artifacts/model/MLmodel