# Spotify Data Analysis  
Exploring factors that influence song popularity on Spotify using Python, Pandas, Matplotlib, Seaborn, and machine learning.

## Overview  
This project analyzes Spotify song popularity by examining the relationship between features such as tempo, energy, danceability, and loudness. It also includes a machine learning model to predict a song’s popularity and an interactive Streamlit app for user input and experimentation.

## Key Findings  
- Pop is the most popular genre, followed by R&B, Soul, and K-Pop.
- Danceable and energetic songs tend to perform better on popularity charts.
- Mid-tempo songs (100–140 BPM) are more common among top tracks.
- Songs with higher loudness levels (closer to 0 dB) tend to be more popular.
- Popularity is influenced by a combination of audio features rather than a single factor.  

## Technologies Used  
- Python  
- Pandas, Matplotlib, Seaborn
- Scikit-learn (Random Forest Regressor)
- Streamlit (Interactive app) 
- Jupyter Notebook  

## Dataset  
- Sourced from [Kaggle](https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset).  
- Created by **Solomon Ameh**.  
- This dataset is licensed under the **Open Database License (ODbL)**.

## How to Use This Notebook  
1. Clone this repository or download the `.ipynb` file.  
2. Open it in Jupyter Notebook or Google Colab.  
3. Run the code to explore insights and visualizations.  

## Streamlit App
To run the interactive app locally:

1. Make sure you have Streamlit installed:
   
   pip install streamlit
   
2. Run the app in your terminal:
   
   streamlit run spotify_predictor_app.py  

3. Adjust audio feature sliders and view the predicted popularity score.

## Audio Feature Ranges (Used in ML Model)

| Feature           | Description                                                   | Typical Range      |
|-------------------|---------------------------------------------------------------|---------------------|
| **Danceability**  | How suitable a track is for dancing (0 = least, 1 = most)     | 0.0 – 1.0           |
| **Energy**        | Intensity and activity of a track                             | 0.0 – 1.0           |
| **Loudness**      | Overall loudness measured in decibels (dB)                    | -60 dB – 0 dB       |
| **Speechiness**   | Presence of spoken words in a track                           | 0.0 – 1.0           |
| **Acousticness**  | Confidence that a track is acoustic                           | 0.0 – 1.0           |
| **Instrumentalness** | Predicts if a track is instrumental                        | 0.0 – 1.0           |
| **Liveness**      | Presence of audience or live setting                          | 0.0 – 1.0           |
| **Valence**       | Positivity of the musical mood                                | 0.0 – 1.0           |
| **Tempo**         | Speed of the song measured in BPM                             | 40 – 220 BPM        |
