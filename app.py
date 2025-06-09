import streamlit as st

def main():
    dashboard_page = st.Page("frontend/dashboard.py", title="Dashboard", icon="🏠")
    pg = st.navigation([dashboard_page])
    pg.run()


if __name__ == "__main__":
    main()