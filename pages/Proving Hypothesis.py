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

import warnings

from Overview import load_lottieurl

warnings.filterwarnings("ignore", category=FutureWarning)


def main():

    st.markdown("<h1 style='text-align: center; color: white;'>Play Store Analytics</h1>", unsafe_allow_html=True)

    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((0.1, 2, 0.2, 2, 0.1))

    with row0_2:
        add_vertical_space()

    row0_1.subheader(
        "So, what to expect from market when building an android app? What is important to take into account?")
    row0_2.subheader(
        "We are going to use plots and tables to prove some hypothesis."
    )

    st.sidebar.title("")

    df = load_data()

    st.header("Hypothesis 1")

    st.markdown("<h4 style='color: white'>Let's check whether the <p4 style='color: orange;'>larger</p4> the size of "
                "the app, the <p4 style='color: orange;'>lower</p4> the rating it will receive.</h4>",
                unsafe_allow_html=True)
    st.markdown("<h5 style='color: white'>We are going to build a scatter plot with <p5 style='color: orange;'>Size</p5> parameter on "
                "the <p5 style='color: coral;'>y</p5> axis and a <p5 style='color: orange;'>Rating</p5> parameter on "
                "the <p5 style='color: coral;'>x</p5> axis while the <p5 style='color: orange;'>Type</p5> will define the <p5 style='color: coral;'>color</p5>.</h5>",
                unsafe_allow_html=True)

    fig = px.scatter(df, x="Size", y="Rating", color="Type", color_discrete_sequence=['darkgreen', 'darkorange'],
                     title="<b>Rating and size correlation</b>")
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        "<h5 style='color: white'>It turns out, that rating <p5 style='color: orange;'>doesn't</p5> really depend on size, even more, apps of a "
        "bigger size usually get a higher rating.</h5>",
        unsafe_allow_html=True)

    separator(3)

    st.header("Hypothesis 2")

    st.markdown("<h4 style='color: white'>Now let's check whether the <p4 style='color: orange;'>larger</p4> the rating and the number of reviews of "
                "the app, the <p4 style='color: orange;'>bigger</p4> will be the number of installs.</h4>",
                unsafe_allow_html=True)
    st.markdown("<h5 style='color: white'>We are going to build a bubble plot with <p5 style='color: orange;'>Rating</p5> parameter on "
                "the <p5 style='color: coral;'>y</p5> axis and a <p5 style='color: orange;'>Reviews</p5> parameter on "
                "the <p5 style='color: coral;'>x</p5> axis while the <p5 style='color: orange;'>Type</p5> will define "
                "the <p5 style='color: coral;'>color</p5> and <p5 style='color: orange;'>Installs</p5> will define the "
                "<p5 style='color: coral;'>Size</p5> of the bubble.</h5>",
                unsafe_allow_html=True)

    fig = px.scatter(df.sort_values('Android Ver', ascending=1), x="Reviews", y="Rating", color="Type",
                     size='Installs', color_discrete_sequence=["darkgreen", "darkorange"])
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
    fig.update_xaxes(gridcolor='white', zerolinecolor='white')
    fig.update_yaxes(gridcolor='white', zerolinecolor='white')

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        "<h5 style='color: white'>As it can be seen from the plot, out hypothesis was <p5 style = 'color: orange;' > true </p5> and the number of installs directly depend on the quantity of reviews and on the rating, if the rating "
        "is high and the reviews are high, the installations will be also high. It is also important to mention that apps with a big number of installations are completely free.</h5>",
        unsafe_allow_html=True)

    separator(3)

    st.header("Hypothesis 3")

    st.markdown("<h4 style='color: white'>Now let's check whether the <p4 style='color: orange;'>most popular</p4> "
                "apps on the market were made by <p4 style='color: orange;'>big tech</p4>.</h4>",
                unsafe_allow_html=True)
    st.markdown("<h5 style='color: white'>We are going to build a table with <p5 style='color: orange;'>top apps</p5> of the market.</h5>",
                unsafe_allow_html=True)

    df_top_aps = df.sort_values("Installs", ascending=False).head(10)
    st.table(df_top_aps)
    separator()

    st.markdown("<h5 style='color: white'>Also a bubble plot will be useful with <p5 style='color: orange;'>Reviews</p5> parameter on "
                "the <p5 style='color: coral;'>y</p5> axis and a <p5 style='color: orange;'>Name of the app</p5> parameter on "
                "the <p5 style='color: coral;'>x</p5> axis while the <p5 style='color: orange;'>Rating</p5> will define "
                "the <p5 style='color: coral;'>Size</p5> of the bubble.</h5>",
                unsafe_allow_html=True)
    fig = px.scatter(df_top_aps, x="App", y="Reviews", color="App",
                     size='Rating')
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
    fig.update_xaxes(gridcolor='white', zerolinecolor='white')
    fig.update_yaxes(gridcolor='white', zerolinecolor='white')

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        "<h5 style='color: white'>From the table and the plot we can conclude that all top apps were made by <p5 "
        "style = 'color: orange;' >big comanies</p5>  and <p5 style = 'color: orange;' >not</p5> by <p5 style = 'color: orange;' >small startups</p5>, "
        "one can say that Google one day was also a startup, but nowadays the market is at state when it is really "
        "hard to get on top.</h5>",
        unsafe_allow_html=True)


def separator(number=1):
    for i in range(number):
        st.write(" ")


@st.cache
def load_data():
    df = pd.read_csv('../googleplaystore.csv')

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


if __name__ == "__main__":
    main()