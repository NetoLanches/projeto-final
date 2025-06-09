import streamlit as st
from db.banco import create_db

def main():
    create_db()
    dashboard_page = st.Page("frontend/dashboard.py", title="Dashboard", icon="🏠")
    pg = st.navigation([dashboard_page])
    pg.run()


if __name__ == "__main__":
    main()