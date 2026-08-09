import streamlit as st
import pandas as pd

# 1. Product Header
st.title("🍲 Smart Recipe Recommender")
st.write("Maximizing conversion through Bayesian-sorted dietary nudges.")

# 2. Data Loading (Cached for fast performance)
@st.cache_data
def load_data():
    # Point this to the cleaned sample dataset you generated earlier
    df = pd.read_csv("data/RAW_recipes_sample.csv")
    return df

df = load_data()

# 3. User Input
st.subheader("What's in your fridge?")
search_term = st.text_input("Enter a core ingredient (e.g., chicken, spinach):", "chicken")

# 4. Engine Logic & Display
if search_term:
    # Filter for the ingredient
    # Ensure your 'ingredients' column is properly formatted as a string
    filtered_df = df[df['ingredients'].astype(str).str.contains(search_term, case=False, na=False)]

    # Assuming you exported your bayesian_avg column, you would sort here:
    # sorted_df = filtered_df.sort_values(by='bayesian_avg', ascending=False)

    st.write(f"### Top recommendations for: {search_term}")

    # Display clean, user-friendly columns
    display_cols = ['name', 'minutes', 'n_ingredients'] 
    st.dataframe(filtered_df[display_cols].head(10))
