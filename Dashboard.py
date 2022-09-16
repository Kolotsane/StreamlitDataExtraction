from pickletools import float8
from tkinter.font import names
from turtle import title, width
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import PyPDF2
import os
import plotly.express as px
import seaborn as sns
from streamlit_option_menu import option_menu
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plost
import altair as alt
import base64
from datetime import date, datetime

st.set_page_config(
    page_title="Dashboard",
    page_icon="🌏",
    layout="wide"
)


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_markup_for_logo(
        png_file,
        background_position="50% 10%",
        margin_top="10%",
        image_width="100%",
        image_height="",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )


def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )


add_logo("lg.png")


# with st.sidebar:
#     # images
#     img = Image.open("logo.png")
#     st.image(img, width=300)
#     # Text/Title
#     st.write("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Fascinate');
#     html, body, [class*="css"]  {
#    font-family: 'Verdana', cursive;
#    background: white;
#     }
#     </style>
#     """, unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Home", "About Us", "Services", "Contact Us", "Logout"],
    icons=["house", "book", "gear", "envelope", "key"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# if selected == "Home"
#     st.write("Home")
#     st.write("About")
#     st.write("Services")
#     st.write("Contacts")
#     st.write("Logout")


# def extract_insert_to_xlsx_file():
#     # counting number of processed documents
#     count = 0
#     # Extracting data from the multiple pdf files
#     for file_name in os.listdir('invoices'):
#         # st.write(file_name)
#         load_pdf = open(r'C:\\Users\\KOLOTSANE\\PycharmProjects\\DataExtraction\\invoices\\' + file_name, 'rb')
#         read_pdf = PyPDF2.PdfFileReader(load_pdf, strict=False)
#         count += 1
#     st.subheader("Documents Processed  " + str(count))
#     # st.pyplot(plot_pie(accurately_processed, notgood))

# NEW MODIFICATION
def doc_table():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        excel_file= 'Invoice_Information.xlsx'
        df1=pd.read_excel(excel_file)
        all_documents = int(len(df1.index))
        df1.dropna(inplace=True)
        df1["Total"] = df1["Total"].str.replace("$","",regex=False).astype(float)
        df1['Date'] = pd.to_datetime(df1['Date'])
        accurately_processed = int(len(df1.index))
        inaccurately_processed = all_documents - accurately_processed
        col1, col2, col3 = st.columns(3)
        col1.metric("All Processed Documents", all_documents,"100%")
        col2.metric("Accurately Processed Documents", accurately_processed,str(round(float(accurately_processed/all_documents * 100),1)) + "%")
        col3.metric("Inaccurately Processed Documents", inaccurately_processed,str(round(float(inaccurately_processed/all_documents *100),1)) +"%")
        #st.dataframe(df1)

def pie_chart():
    excel_file= 'Invoice_Information.xlsx'
    df1=pd.read_excel(excel_file)
    all_documents = int(len(df1.index))
    df1.dropna(inplace=True)
    df1["Total"] = df1["Total"].str.replace("$","",regex=False).astype(float)
    df1['Date'] = pd.to_datetime(df1['Date'])
    accurately_processed = int(len(df1.index))
    inaccurately_processed = all_documents - accurately_processed
    df2=df1.assign(processed_docs = [all_documents,0,0,0,0,0,0])
    df3=df2.assign(accurate_docs=[accurately_processed,0,0,0,0,0,0])
    df4=df3.assign(inaccurate_docs=[inaccurately_processed,0,0,0,0,0,0])
    pie_chart1 = px.pie(df4,names='processed_docs')
    pie_chart1.update_layout(height=300,
                       width=500,
                       margin={'l': 20, 'r': 20, 't': 0, 'b': 0},
                       legend=dict(
                           yanchor="top",
                           y=0.99,
                           xanchor="right",
                           x=0.99)
                       )
    st.title("Uploaded Documents Overview")
    st.plotly_chart(pie_chart1)
    st.dataframe(df2)


def cat_bar_chart():
    excel_file= 'Invoice_Information.xlsx'
    df1=pd.read_excel(excel_file)
    all_documents = int(len(df1.index))
    df1.dropna(inplace=True)
    df1["Total"] = df1["Total"].str.replace("$","",regex=False).astype(float)
    df1['Date'] = pd.to_datetime(df1['Date'])

def image_function():
    image = Image.open('Tiny people doing priorities checklist flat vector illustration.jpg')
    st.image(image,width=700)

def chart_label():
    excel_file= 'Invoice_Information.xlsx'
    df1=pd.read_excel(excel_file)
    df1.dropna(inplace=True)
    df1["Total"] = df1["Total"].str.replace("$","",regex=False).astype(float)
    df1['Date'] = pd.to_datetime(df1['Date'])
    fig=plt.figure()
    sns.barplot(x="Total",y="Company Name",data=df1)
    st.pyplot(fig)
    #chart_data = pd.DataFrame(df1,
    #columns=['All processed', 'Accurately processed', 'Inaccurately processed'])
    #st.line_chart(chart_data)

def pie_chart_create():
    # read by default 1st sheet of an excel file
    dataframe1 = pd.read_excel('Invoice_Information.xlsx')
    dataframe1[dataframe1.columns[1:]] = dataframe1[dataframe1.columns[1:]].apply(lambda x: x.str.replace('$', ''))
    dataframe1[dataframe1.columns[1:]] = dataframe1[dataframe1.columns[1:]].apply(lambda x: x.str.replace(',', ''))
    company = dataframe1["Company Name"]
    values = dataframe1["Total"]
    st.pyplot(plot_pie(company, values))


def line_chart_plot():
    # read by default 1st sheet of an excel file
    df1 = pd.read_excel('Invoice_Information.xlsx')
    all_documents = int(len(df1.index))
    st.write("All processed documents  =" + str(all_documents))
    accurately_processed = int(len(df1.index))
    st.write("Accurately processed documents  =" + str(accurately_processed))
    inaccurately_processed = all_documents - accurately_processed
    st.write("Inaccurately processed documents  =" + str(inaccurately_processed))
    st.pyplot(plot_pie([all_documents, accurately_processed, inaccurately_processed]))



def plot_pie(sizes):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    max_size = max(sizes)
    explode = [0.1 if i == max_size else 0 for i in sizes]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=['#6da7cc', '#ffb58a'],width = 200)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    return fig1


def plot_line(sizes):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:

    fig1, ax1 = plt.subplots()
    ax1.plot(sizes)

    return fig1


# st.subheader("Number Of Processed Documents")
# extract_insert_to_xlsx_file()
# pie_chart_create()
doc_table()
#pie_chart()
#chart_label()
#line_chart_plot()

#image_function()

def graph_refiner(df4, x="date", y="documents"):
    # Create a selection that chooses the nearest point & selects based on x-value
    hover = alt.selection_single(
        fields=[x],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(df4)
        .mark_line(point="transparent")
        .encode(x=x, y=y)
        .transform_calculate(color='datum.delta < 0 ? "red" : "green"')
    )

    # Draw points on the line, highlight based on selection, color based on delta
    points = (
        lines.transform_filter(hover)
        .mark_circle(size=65)
        .encode(color=alt.Color("color:N", scale=None))
    )

    # Draw an invisible rule at the location of the selection
    tooltips = (
        alt.Chart()
        .mark_rule(opacity=0)
        .encode(
            x=x,
            y=y,
            tooltip=[x, y, alt.Tooltip("delta", format=".2%")],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()

col4, col5 = st.columns(2)

with col4:
    df1 = pd.read_excel('Invoice_Information.xlsx')
    all_documents = len(df1)

    start = st.date_input(
        "Select start date",
        date(2022, 1, 1),
        # min_value=date.strptime("2022-01-01", "%Y-%m-%d"),
        # max_value=date.now(),
        )
    nodays = len(df1[df1["Processed Date"] == str(start)])

    fig, ax = plt.subplots(figsize=(2, 1))

    ax.pie([all_documents,  nodays],
           wedgeprops={'width':0.3},
           startangle=90,
           colors=['white', '#90e0ef'])

    plt.show()
    # st.pyplot(fig)
with col5:
    time_frame = st.selectbox(
            "Select daily, weekly or monthly documents", ("daily","weekly", "monthly")
        )
st.header("Documents Overview")

#st.altair_chart(
        #graph_refiner(), use_container_width=True
  #  )
#ANOTHER MODIFICATION
excel_file= 'Invoice_Information.xlsx'
df1=pd.read_excel(excel_file)
c3,c4 = st.columns((1,1))
with c3:
    all_documents = int(len(df1.index))
    df1.dropna(inplace=True)
    df1["Total"] = df1["Total"].str.replace("$","",regex=False).astype(float)
    df1['Date'] = pd.to_datetime(df1['Date'])
    accurately_processed = int(len(df1.index))
    inaccurately_processed = all_documents - accurately_processed
    df2=df1.assign(Overall=[all_documents,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    df3=df2.assign(Accurate=[accurately_processed,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    df4=df3.assign(Inaccurate=[inaccurately_processed,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    data = pd.DataFrame({
    'Documents':['orange', 'blue', 'red'],
    'Number': [all_documents, accurately_processed, inaccurately_processed],
    'colors':  ['All Processed', 'Accurately Processed', 'Inaccurately Processed']
        })
    chart = alt.Chart(data).mark_bar().encode(
    x='Documents',
    y='Number',
    color='colors'

        ).properties(width=550)

    st.altair_chart(chart)
    # pie_chart1 = px.pie(df4, names='processed_docs')
    #st.markdown('### Accurate Documents Overview')
    #plost.donut_chart(
    #data=df4,
    #theta='accurate_docs',
    #color='#5DADE2')
    #st.plotly_chart(pie_chart1)
    #st.dataframe(df4)
    #fig, ax = plt.subplots(figsize=(5, 1))

    #ax.pie([all_documents,accurately_processed],
           #wedgeprops={'width':0.3},
           #startangle=90,
           #colors=['#515A5A', '#5DADE2'])
    #plt.show()
    #st.pyplot(fig)
with c4:
    st.line_chart(df4[['Overall', 'Accurate', 'Inaccurate']])
    #st.markdown('### Inaccurate Documents Overview')
    #plost.donut_chart(
    #data=df4,
    ##theta='inaccurate_docs',
    #color='#008631')
    #fig, ax = plt.subplots(figsize=(5, 1))

    #ax.pie([all_documents,inaccurately_processed],
          # wedgeprops={'width':0.3},
          # startangle=90,
          # colors=['#008631', '#515A5A'])
    #plt.show()
    #st.pyplot(fig)


