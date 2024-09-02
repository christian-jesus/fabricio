# app/recommendations.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def load_data():
    # Carga de datos (debe estar en la misma carpeta o proporcionar la ruta correcta)
    df = pd.read_csv('courses.csv')
    return df

def recommend_courses(course_name, df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['course_description'])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(df.index, index=df['course_title']).drop_duplicates()

    idx = indices[course_name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5

    course_indices = [i[0] for i in sim_scores]
    return df['course_title'].iloc[course_indices].tolist()
