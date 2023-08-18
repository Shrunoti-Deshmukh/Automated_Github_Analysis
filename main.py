import streamlit as st
from helper import most_complex_project


def main():
    st.title("Automated GitHub Analysis")

    project_title = st.text_input("Enter URL:", key="auto_github")

    if project_title:
        username = project_title.split('/')[-1]
        repo = most_complex_project(username)

        st.write(f"The most Complex Project in {username} GitHub is : ")
        st.write(f"Name : {repo['name']}")
        st.write(f"URL : {repo['html_url']}")
        st.write(f"Description : {repo['description']}")

if __name__ == "__main__":
    main()