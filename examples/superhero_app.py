# create a superhero app

import streamlit as st
import random


# Set up the page
st.set_page_config(
    page_title="Superhero App",
    layout="wide", # or wide
    page_icon="🦸🏻‍♀️", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

st.title("Superhero App 🦸🏻🦸🏻‍♀️")
st.divider()

# i want to have a serie of inouts for the user: a text input for the user to wrtie their favourite color, another one for them to type their favorite animal, a number input for them to input their random lucky number and finally a selectbox for them to choose a superpower

color = st.text_input("Enter your favorite color")
animal = st.text_input("Enter your favorite animal")
lucky_number = st.number_input("Enter your lucky number", step=1)
superpower = st.selectbox("Choose a superpower", ["Flying", "Super Strength", "Invisibility", "Telepathy"])

# thank you! now i would like to combine the inputs to generate a unique superhero name

st.write(f"Your superhero name is: {color} {animal} of {lucky_number}")

# i want to add a button to the app that will generate a random superhero name

# if st.button("Generate superhero name"):
#     st.write(f"Your superhero name is: {color} {animal} of {lucky_number}")

# can we also display the superpower chosen?

st.write(f"Your superpower is: {superpower}")

# can you please generate a list of 5 superhero mottos? for example: "I will never give up!", "I am the best!", "I will save the world!", "I will never give up!", "I will never give up!"

mottos = ["I will never give up!", "I am the best!", "I will save the world!", "I will never give up!", "I will never give up!"]

# lets display one of the mottos at random

st.write(f"Your superhero motto is: {random.choice(mottos)}")


