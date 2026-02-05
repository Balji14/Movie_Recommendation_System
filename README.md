# 🎬 Movie Recommendation System (Streamlit)

A **content-based movie recommendation system** built using **Python and Streamlit**.  
This application recommends movies based on similarity scores and allows users to search using **partial or full movie names**.

---

## 🌟 Highlights

✔ Content-based filtering  
✔ Keyword / partial name search  
✔ Fast recommendations using precomputed similarity matrix  
✔ Clean and interactive Streamlit UI  
✔ Beginner-friendly project structure  

---

## 🧠 How the Recommendation Works

1. Movie metadata is vectorized (offline)
2. Cosine similarity is calculated between movies
3. A similarity matrix is stored using Pickle
4. When a user enters a movie name:
   - The closest matching title is found
   - Top **5 most similar movies** are recommended

> ⚠️ This system does **not** use user ratings or collaborative filtering.

---

## 🛠️ Tech Stack

| Category | Tools |
|--------|------|
| Language | Python 3 |
| Frontend | Streamlit |
| Data Handling | Pandas |
| Model Storage | Pickle |
| ML Concept | Cosine Similarity |

---


