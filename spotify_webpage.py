import streamlit as st
import requests
import json

YEAR = 2025

col1, col2, col3 = st.columns([5, 1, 5])

with col1:
    st.markdown("<h1 style='color: red;'>Hit predictor</h1>", unsafe_allow_html=True)

    dance = st.slider("Select the danceability", min_value=0.00, max_value=1.00, value=0.50)
    enrg = st.slider("Select the energy", min_value=0.00, max_value=1.00, value=0.50)
    loud = st.slider("Select the loudness", min_value=0.00, max_value=1.00, value=0.50)
    speech = st.slider("Select the speechiness", min_value=0.00, max_value=1.00, value=0.50)
    acoustic = st.slider("Select the acousticness", min_value=0.00, max_value=1.00, value=0.50)
    instrumental = st.slider("Select the instrumentalness", min_value=0.00, max_value=1.00, value=0.50)
    live = st.slider("Select the liveness", min_value=0.00, max_value=1.00, value=0.50)
    val = st.slider("Select the valence", min_value=0.00, max_value=1.00, value=0.50)

    temp = st.slider("Select the Tempo", min_value=0, max_value=250, value=125)


with col3:
    # ky = st.slider("Select the Key", min_value=0, max_value=11, value=0)
    musical_keys = ["C", "C♯/D♭", "D", "D♯/E♭", "E", "F", "F♯/G♭", "G", "G♯/A♭", "A", "A♯/B♭", "B"]
    key_str = st.selectbox("Select the key", musical_keys)
    ky = musical_keys.index(key_str)

    # time_sig = st.slider("Select the Time Signature", min_value=0, max_value=5, value=2)
    time_sig_list = ["3/4", "4/4", "5/4", "6/4", "7/4"]
    time_sig_str = st.radio("Select the time signature", time_sig_list)
    time_sig = time_sig_list.index(time_sig_str)

    # mode_str = st.radio("Select the mode", ["Major", "Minor"])
    # mode_val = 1 if mode_str == "Major" else 0
    # st.write('change the settings to predict a hit!')
    duration = st.number_input("Enter the song duration in seconds", min_value=0, max_value=6000, value=100)

    num_songs = st.number_input("Number of songs by this artist", min_value=0, max_value=999, value=42)
    num_hits = (st.number_input("Number of hits by this artist", min_value=0, max_value=100, value=42))
    if num_songs == 0:
        percent_hits = 0
    else:
        percent_hits = num_hits / num_songs

    # yr = st.selectbox("Choose the year that your music sounds like it comes from? ["2000", "2001", "2002"])
    yr = YEAR

    genr = st.selectbox("Choose a genre", ['acoustic', 'afrobeat', 'alt-rock', 'ambient', 'black-metal', 'blues', 'breakbeat', 'cantopop', 'chicago-house', 'chill', 'classical', 'club', 'comedy', 'country', 'dance', 'dancehall', 'death-metal', 'deep-house', 'detroit-techno', 'disco', 'drum-and-bass', 'dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo', 'folk', 'forro', 'french', 'funk', 'garage', 'german', 'gospel', 'goth', 'grindcore', 'groove', 'guitar', 'hard-rock', 'hardcore', 'hardstyle', 'heavy-metal', 'hip-hop', 'house', 'indian', 'indie-pop', 'industrial', 'jazz', 'k-pop', 'metal', 'metalcore', 'minimal-techno', 'new-age', 'opera', 'party', 'piano', 'pop', 'pop-film', 'power-pop', 'progressive-house', 'psych-rock', 'punk', 'punk-rock', 'rock', 'rock-n-roll', 'romance', 'sad', 'salsa', 'samba', 'sertanejo', 'show-tunes', 'singer-songwriter', 'ska', 'sleep', 'songwriter', 'soul', 'spanish', 'swedish', 'tango', 'techno', 'trance', 'trip-hop'])

    model = st.radio("pick your model", ["Don't miss a hit!", "Don't overestimate"])

    st.write("")

    if st.button("Will it be a hit?"):
        input = {
            "danceability": dance,
            "energy": enrg,
            "loudness": loud,
            "speechiness": speech,
            "acousticness": acoustic,
            "instrumentalness": instrumental,
            "liveness": live,
            "valence": val,
            "tempo": float(temp),
            "duration_ms": float(duration),
            "no_of_songs": float(num_songs),
            "popular_song_percentage": float(percent_hits),
            "year": int(yr),
            "genre": genr,
            "key": ky,
            "time_signature": time_sig,
        }
        # st.write(input)

        if model == "Don't miss a hit!":
            response = requests.post(
                url="http://localhost:8000/dont_miss_hits",
                json=input
            )
        else:
            response = requests.post(
                url="http://localhost:8000/dont_overestimate",
                json=input
            )

        # st.write("Checking...")
        try:
            data = response.json()
            print(data)
            if data['prediction'][0] == 1:
                st.write("CONGRATULATIONS: It's gonna be a hit!")
                st.image("imgs/gonna_be_a_hit.gif")
            else:
                st.write("C'mon that's terrible")
                st.image("imgs/make_it_stop.gif")

        except requests.exceptions.JSONDecodeError:
            print("Server did not return JSON.")
            print("Response text:", response.text)
    