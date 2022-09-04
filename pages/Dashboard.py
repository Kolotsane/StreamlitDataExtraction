import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import PyPDF2
import os

st.set_page_config(
    page_title="Dashboard",
    page_icon="🌏",
    layout="wide"
)

with st.sidebar:
    # images
    img = Image.open("logo.png")
    st.image(img, width=300)

    # Text/Title
    st.write("Home")
    st.write("About")
    st.write("Services")
    st.write("Contacts")
    st.write("Logout")


def extract_insert_to_xlsx_file():
    # counting number of processed documents
    count = 0
    # Extracting data from the multiple pdf files
    for file_name in os.listdir('invoices'):
        # st.write(file_name)
        load_pdf = open(r'C:\\Users\\KOLOTSANE\\PycharmProjects\\DataExtraction\\invoices\\' + file_name, 'rb')
        read_pdf = PyPDF2.PdfFileReader(load_pdf, strict=False)
        count += 1
    st.subheader("Documents Processed  " + str(count))
    # accurately_processed = 5
    # notgood = 2
    # st.pyplot(plot_pie(accurately_processed, notgood))


def pie_chart_create():
    # read by default 1st sheet of an excel file
    dataframe1 = pd.read_excel('Invoice_Information.xlsx')
    dataframe1.dropna(axis=0, how='any', inplace=True)
    dataframe1[dataframe1.columns[1:]] = dataframe1[dataframe1.columns[1:]].apply(lambda x: x.str.replace('$', ''))
    dataframe1[dataframe1.columns[1:]] = dataframe1[dataframe1.columns[1:]].apply(lambda x: x.str.replace(',', ''))
    company = dataframe1["Company Name"]
    values = dataframe1["Total"]
    st.pyplot(plot_pie(company, values))


def line_chart_plot():
    # read by default 1st sheet of an excel file
    dataframe1 = pd.read_excel('Invoice_Information.xlsx')
    dataframe1.dropna(axis=0, how='any', inplace=True)
    dataframe1[dataframe1.columns[1:]] = dataframe1[dataframe1.columns[1:]].apply(lambda x: x.str.replace('$', ''))
    dataframe1[dataframe1.columns[1:]] = dataframe1[dataframe1.columns[1:]].apply(lambda x: x.str.replace(',', ''))
    # dataframe1.sort_values(by='Total')
    values = dataframe1["Total"]
    invoice_date = dataframe1['Date']
    # date_col = pd.DatetimeIndex(dataframe1['Date'])
    # dataframe1['Year'] = date_col.year
    # st.write(dataframe1)
    st.pyplot(plot_line(invoice_date, values))


def plot_pie(labels, sizes):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    max_size = max(sizes)
    explode = [0.1 if i == max_size else 0 for i in sizes]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=['#6da7cc', '#ffb58a'])

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    return fig1


def plot_line(labels, sizes):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:

    fig1, ax1 = plt.subplots()
    ax1.plot(labels, sizes)

    return fig1


# st.subheader("Number Of Processed Documents")
extract_insert_to_xlsx_file()
pie_chart_create()
# line_chart_plot()

