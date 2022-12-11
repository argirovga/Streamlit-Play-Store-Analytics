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

    st.header("Simple plots to understand the data better 🗺")

    st.markdown(
        "<h4 style='color: white'>We are going to build some simple plots, so that we can see how our data looks like.</h4>",
        unsafe_allow_html=True)
    st.markdown(
        "<h4 style='color: white'>Choose a column to analyze 🧐</h4>",
        unsafe_allow_html=True)
    option = st.selectbox('', ('Android apps', 'Price', 'Rating', 'Size', 'Content rating', 'Category plots'))

    if option == 'Android apps':
        android_versions = sorted(
            list(set(map(lambda x: x.replace('Varies with device', '8.0 and up'), list(df["Android Ver"])))))
        count = [len(df[df["Android Ver"] == i]) for i in android_versions]

        fig = px.line(df, x=list(android_versions), y=list(count), title='<b>Number Of Apps Per Android Version</b>',
                      labels={
                          'x': "Android versions",
                          'y': "Number of apps",
                      }, )

        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
        fig.update_traces(line_color='gold')
        fig.update_xaxes(gridcolor='white', zerolinecolor='white')
        fig.update_yaxes(gridcolor='white', zerolinecolor='white')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df.sort_values('Android Ver', ascending=1), x="Android Ver", color="Android Ver",
                           title='<b>Number Of Apps Per Android Version</b>')
        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
        fig.update_xaxes(gridcolor='white', zerolinecolor='white')
        fig.update_yaxes(gridcolor='white', zerolinecolor='white')
        fig.update_layout(showlegend=False)
        fig.update_layout(yaxis_title="Number of apps")
        st.plotly_chart(fig, use_container_width=True)

    if option == 'Price':
        fig = px.histogram(df, x="Type", color="Type", color_discrete_sequence=['darkgreen', 'darkorange'],
                           title="<b>Number Of Free/Paid Apps</b>", labels={'x': "Downloads"})

        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
        fig.update_xaxes(gridcolor='white', zerolinecolor='white')
        fig.update_yaxes(gridcolor='white', zerolinecolor='white')
        fig.update_layout(yaxis_title="Number of apps")
        st.plotly_chart(fig, use_container_width=True)

        fig = px.box(df[df["Price"] != 0], y="Price", title='<b>Price Analytics</b>',
                     color_discrete_sequence=["darkorange"])

        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod",
                          yaxis=dict(range=[0, 50]))
        fig.update_xaxes(gridcolor='white', zerolinecolor='white')
        fig.update_yaxes(gridcolor='white', zerolinecolor='white')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df, x="Price", y="Category", color="Category", title='<b>Price of apps in each category</b>')
        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
        fig.update_xaxes(gridcolor='white', zerolinecolor='white')
        fig.update_yaxes(gridcolor='white', zerolinecolor='white')
        fig.update_layout(showlegend=False)
        fig.update_layout(yaxis_title="Price")
        st.plotly_chart(fig, use_container_width=True)

    if option == 'Rating':
        fig = px.box(df, y="Rating", color="Type", title='<b>Rating Volume For Paid/Free Apps</b>',
                     color_discrete_sequence=['darkgreen', 'darkorange'])

        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
        fig.update_xaxes(gridcolor='white', zerolinecolor='white')
        fig.update_yaxes(gridcolor='white', zerolinecolor='white')
        st.plotly_chart(fig, use_container_width=True)

        fig = ff.create_distplot([df.Rating], ['Rating'], colors=["goldenrod"])

        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod",
                          title='<b>Distribution of rating</b>')
        fig.update_layout(xaxis_title="Rating")
        st.plotly_chart(fig, use_container_width=True)

        fig = px.box(df.sort_values('Rating', ascending=0), y='Rating', x='Category',
                     title='<b>Rating in each category</b>', color="Category")

        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
        fig.update_xaxes(gridcolor='white', zerolinecolor='white')
        fig.update_yaxes(gridcolor='white', zerolinecolor='white')
        fig.update_layout(showlegend=False)
        fig.update_layout(yaxis_title="Rating")
        st.plotly_chart(fig, use_container_width=True)

    if option == 'Size':
        fig = px.violin(df, y="Size", color_discrete_sequence=["darkorange"])
        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod",
                          title='<b>Size analytics</b>')
        st.plotly_chart(fig, use_container_width=True)

        fig = ff.create_distplot([df[df["Rounded Size"] < 200].Size], ['Size'], colors=["goldenrod"])

        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod",
                          title='<b>Distribution of size</b>')
        fig.update_layout(xaxis_title="Size")
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df[df["Rounded Size"] < 200], x="Rounded Size", color="Rounded Size",
                           title="<b>Downloads per size (*rounded)</b>")
        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
        fig.update_xaxes(gridcolor='white', zerolinecolor='white')
        fig.update_yaxes(gridcolor='white', zerolinecolor='white')
        fig.update_layout(showlegend=False)
        fig.update_layout(yaxis_title="Quantity of apps")
        st.plotly_chart(fig, use_container_width=True)

    if option == 'Content rating':
        fig = px.pie(df, names='Content Rating', title='<b>Content Ratings</b>',
                     color_discrete_sequence=["chocolate", "darkgoldenrod", "goldenrod", "gold", "black", "white"])

        fig.update_traces(hoverinfo='label+percent', textinfo='label+percent', textposition='outside', pull=[0.2])
        fig.update_layout(showlegend=False)
        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
        st.plotly_chart(fig, use_container_width=True)

    if option == 'Category plots':
        fig = px.histogram(df, x="Category", color="Category", title='<b>Number of apps per category</b>')
        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
        fig.update_xaxes(gridcolor='white', zerolinecolor='white', categoryorder='total ascending')
        fig.update_yaxes(gridcolor='white', zerolinecolor='white')
        fig.update_layout(showlegend=False)
        fig.update_layout(yaxis_title="Number of apps")
        st.plotly_chart(fig, use_container_width=True)

    separator(3)

    st.header("Detailed overview")

    st.markdown("<h4 style='color: white'>We are going to analize data, by creating more detailed plots with more dependencies.</h4>",
                unsafe_allow_html=True)
    st.markdown(
        "<h5 style='color: white'>1. Let’s see how the prices of apps changed with years.</h5>",
        unsafe_allow_html=True)

    dict_prices = {}

    for i in df["Rounded Date"]:
        if i not in dict_prices.keys():
            dict_prices[i] = df[df["Rounded Date"] == i].Price.sum()

    dict_prices = dict(sorted(dict_prices.items(), key=lambda item: item[0]))
    fig = px.line(x=dict_prices.keys(), y=dict_prices.values(), title='<b>Price off apps through years</b>')

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
    fig.update_traces(line_color='gold')
    fig.update_xaxes(gridcolor='white', zerolinecolor='white')
    fig.update_yaxes(gridcolor='white', zerolinecolor='white')
    fig.update_layout(xaxis_title="Year")
    fig.update_layout(yaxis_title="Sum of prices")

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        "<h5 style='color: white'>It is obvious that with the development of the app market the price rose and the plot proves it.</h5>",
        unsafe_allow_html=True)

    separator()

    st.markdown(
        "<h5 style='color: white'>2. It will be also useful to know how app price correlates with a rating it got.</h5>",
        unsafe_allow_html=True)

    fig = px.area(df[df["Type"] == "Paid"], x="Price", y="Rating", title="<b>Price and rating correlation</b>",
                  color_discrete_sequence=["darkorange"])
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
    fig.update_xaxes(gridcolor='white', zerolinecolor='white')
    fig.update_yaxes(gridcolor='white', zerolinecolor='white')

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        "<h5 style='color: white'>As it can be seen from plot at a low price the rating really depends on the app, "
        "but as price increases and reaches aprox. 380$ the rating it is getting is becoming lower and lower. "
        "However at a much bigger price rating jumps again.</h5>",
        unsafe_allow_html=True)

    separator()

    st.markdown(
        "<h5 style='color: white'>3. Let’s also consider looking on how number of reviews depend on the size of the "
        "app, let’s also take into account whether the app is paid or not.</h5>",
        unsafe_allow_html=True)

    fig = px.scatter(df.sort_values('Android Ver', ascending=1), x="Reviews", y="Size", color="Type",
                     size='Size', color_discrete_sequence=["darkgreen", "darkorange"])
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
    fig.update_xaxes(gridcolor='white', zerolinecolor='white')
    fig.update_yaxes(gridcolor='white', zerolinecolor='white')

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        "<h5 style='color: white'>It is an interesting fact that apps of a bigger size usually get almost no reviews, "
        "while apps with the most reviews are of smaller size and the majority of them are free to install.</h5>",
        unsafe_allow_html=True)

    separator()

    st.markdown(
        "<h5 style='color: white'>4. If we make a scatter plot it will be visible that...</h5>",
        unsafe_allow_html=True)

    fig = px.scatter(df, x="Reviews", y="Rating", color="Type", symbol="Type",
                     color_discrete_sequence=["darkgreen", "darkorange"])
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
    fig.update_xaxes(gridcolor='white', zerolinecolor='white')
    fig.update_yaxes(gridcolor='white', zerolinecolor='white')

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        "<h5 style='color: white'>As it turns out only apps with high rating are getting at least some reviews, "
        "what’s more these apps are completely free.</h5>",
        unsafe_allow_html=True)

    separator()

    st.markdown(
        "<h5 style='color: white'>5. Correlation heatmap is also an interesting graph to look at and to describe "
        "dependencies.</h5>",
        unsafe_allow_html=True)

    fig = px.imshow(df.corr())
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
    fig.update_xaxes(gridcolor='white', zerolinecolor='white')
    fig.update_yaxes(gridcolor='white', zerolinecolor='white')

    st.plotly_chart(fig, use_container_width=True)

    separator()

    st.markdown(
        "<h5 style='color: white'>6. It is also a visible outcome, how the Rating/Reviews/App sizes correlate and "
        "that majority of the apps will have a minimum size and a reasonable number of reviews.</h5>",
        unsafe_allow_html=True)

    layout = pl.graph_objs.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig = pl.express.scatter_3d(df, x='Size', y='Reviews', z='Installs', color='Rating', title="<b>3D scatter</b>")

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font_color="goldenrod")
    fig.update_traces(line_color='gold')
    fig.update_xaxes(gridcolor='black', zerolinecolor='black')
    fig.update_yaxes(gridcolor='black', zerolinecolor='black')
    fig.update_layout(scene_camera=dict(eye=dict(x=1.5, y=1.5, z=2)))

    st.plotly_chart(fig, use_container_width=True)

    separator()


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