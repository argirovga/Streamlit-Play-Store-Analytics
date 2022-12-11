import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.add_vertical_space import add_vertical_space

import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import scipy
import plotly as pl
from plotly import express as px
from plotly import figure_factory as ff

import requests

import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


def main():
    
    lottie_book = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_8xvxscne.json")
    st_lottie(lottie_book, speed=1, height=200, key="initial")

    st.markdown("<h1 style='text-align: center; color: white;'>Play Store Analytics</h1>", unsafe_allow_html=True)

    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((0.1, 2, 0.2, 2, 0.1))

    with row0_2:
        add_vertical_space()

    row0_1.subheader(
        "All that you need to know about the Android market, the data is taken from [Kaggle]("
        "https://www.kaggle.com/datasets/lava18/google-play-store-apps)")
    row0_2.subheader(
        "A Streamlit web analytics app by [Georgy Argirov](https://github.com/argirovga)"
    )

    st.sidebar.title("")

    df = load_data()

    st.header("This is our data 🫣")

    st.subheader("Introducing dataframe 📀")
    st.table(df.head())

    separator(2)

    st.subheader("We cleaned our data 🧼🧹")
    st.markdown("<h5 style='text-align: left; color: white;'>We had some unfilled parameters (NaN) in our "
                "dataframe.</h5>", unsafe_allow_html=True)
    show_cleaning()

    separator(2)

    st.subheader("Here are some statistics 🛰")
    show_statistics(df)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


@st.cache
def load_data():
    df = pd.read_csv('/Users/goshaargirov/Downloads/archive/googleplaystore.csv')
    df.dropna(how='any', inplace=True)

    temp_mas = [float(i[:len(i) - 1]) for i in df.Size if i != "Varies with device"]
    average_size = sum(temp_mas) / len(temp_mas)
    df['Size'] = df['Size'].replace(['Varies with device'], str(average_size) + "M")
    df["Size"] = [float(i[:len(i) - 1]) for i in df.Size]

    df["Reviews"] = pd.to_numeric(df["Reviews"])

    price_list = [float(i.replace('$', '')) for i in df["Price"]]
    df["Price"] = price_list

    df["Category"] = [i.replace('_', ' ') for i in df["Category"]]

    df["Rounded Rating"] = round(df["Rating"])

    array = []
    for i in df.Size:
        array.append((round(i) // 10) * 10)
    df["Rounded Size"] = array

    array = []
    for i in df["Last Updated"]:
        array.append(int(i[-4:]))
    df["Rounded Date"] = array

    array = []
    for i in df["Installs"]:
        array.append(int(i[:-1].replace(',', '')))
    df["Installs"] = array

    return df


def show_cleaning():
    df = pd.read_csv('/Users/goshaargirov/Downloads/archive/googleplaystore.csv')

    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    st.table(missing_data.head())

    st.markdown("<h5 style='text-align: left; color: white;'>It is better to delete them in order not to spoil the "
                "statistics.</h5>", unsafe_allow_html=True)
    df.dropna(how='any', inplace=True)

    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    st.table(missing_data.head())


def show_statistics(df):
    col1, col2, col3 = st.columns(3)
    col1.write(
        f"""<h3>Mean rating &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:orange"> {round(df.Rating.mean(), 2)} </span></h3>""",
        unsafe_allow_html=True)
    col2.write(
        f"""<h3>Median rating &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:orange"> {df.Rating.median()} </span></h3>""",
        unsafe_allow_html=True)
    col3.write(
        f"""<h3>STD rating &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:orange"> {round(df.Rating.std(), 2)} </span></h3>""",
        unsafe_allow_html=True)

    separator(1)

    col1, col2, col3 = st.columns(3)
    col1.write(
        f"""<h3>Mean size &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:orange"> {round(df.Size.mean(), 2)} M</span></h3>""",
        unsafe_allow_html=True)
    col2.write(
        f"""<h3>Median size &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:orange"> {df.Size.median()} M</span></h3>""",
        unsafe_allow_html=True)
    col3.write(
        f"""<h3>STD size &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:orange"> {round(df.Size.std(), 2)} M</span></h3>""",
        unsafe_allow_html=True)

    separator(1)

    col1, col2, col3 = st.columns(3)
    col1.write(f"""<h3>Mean reviews <span style="color:orange"> {round(df.Reviews.mean(), 2)} </span></h3>""",
               unsafe_allow_html=True)
    col2.write(f"""<h3>Median reviews <span style="color:orange"> {df.Reviews.median()} </span></h3>""",
               unsafe_allow_html=True)
    col3.write(f"""<h3>STD reviews <span style="color:orange"> {round(df.Reviews.std(), 2)} </span></h3>""",
               unsafe_allow_html=True)

    separator(1)

    col1, col2, col3 = st.columns(3)
    col1.write(f"""<h3>Mean installs <span style="color:orange"> {round(df.Installs.mean(), 2)} </span></h3>""",
               unsafe_allow_html=True)
    col2.write(f"""<h3>Median installs <span style="color:orange"> {df.Installs.median()} </span></h3>""",
               unsafe_allow_html=True)
    col3.write(f"""<h3>STD installs <span style="color:orange"> {round(df.Installs.std(), 2)} </span></h3>""",
               unsafe_allow_html=True)


def separator(number=1):
    for i in range(number):
        st.write(" ")


if __name__ == "__main__":
    main()
