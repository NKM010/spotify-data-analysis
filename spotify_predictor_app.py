import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Load & train model
@st.cache_resource
def load_model():
    df = pd.read_csv("high_popularity_spotify_data.csv")
    features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 
                'instrumentalness', 'liveness', 'valence', 'tempo']
    X = df[features]
    y = df["track_popularity"]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model, df, features

model, df, features = load_model()

# App layout
st.title(" Spotify Song Popularity Predictor")
st.write("Predict how popular your song might be based on its audio features!")

# Sidebar input
st.sidebar.header(" Tune Song Features")

# Sliders in sections
st.sidebar.subheader(" Rhythm & Dynamics")
danceability = st.sidebar.slider("Danceability", 0.0, 1.0, 0.5)
energy = st.sidebar.slider("Energy", 0.0, 1.0, 0.5)
loudness = st.sidebar.slider("Loudness", -60.0, 0.0, -10.0)
tempo = st.sidebar.slider("Tempo", 40.0, 220.0, 120.0)

st.sidebar.subheader(" Vocal & Instrumental")
speechiness = st.sidebar.slider("Speechiness", 0.0, 1.0, 0.1)
instrumentalness = st.sidebar.slider("Instrumentalness", 0.0, 1.0, 0.0)
acousticness = st.sidebar.slider("Acousticness", 0.0, 1.0, 0.3)

st.sidebar.subheader(" Mood & Ambience")
liveness = st.sidebar.slider("Liveness", 0.0, 1.0, 0.1)
valence = st.sidebar.slider("Valence", 0.0, 1.0, 0.5)

# Prediction
input_data = np.array([[danceability, energy, loudness, speechiness, acousticness,
                        instrumentalness, liveness, valence, tempo]])
predicted_popularity = model.predict(input_data)[0]

st.markdown(f"### Predicted Popularity Score: **{predicted_popularity:.2f}/100**")

if predicted_popularity > 75:
    st.success(" This one's a banger!")
elif predicted_popularity > 50:
    st.info(" Might just be a hidden gem.")
else:
    st.warning(" Could be niche or experimental...")

# Optional: Feature Importance
st.subheader(" Feature Importance (from the model)")
importances = model.feature_importances_
importance_df = pd.DataFrame({"Feature": features, "Importance": importances})
importance_df = importance_df.sort_values(by="Importance", ascending=False)
st.bar_chart(importance_df.set_index("Feature"))
