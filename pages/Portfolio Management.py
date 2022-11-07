
from matplotlib import ticker
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as pyplot
import streamlit as st
from tabulate import tabulate
import psycopg2
from PIL import Image


conn = psycopg2.connect(**st.secrets["postgres"])
conn.autocommit = True
cur = conn.cursor()
st.header("Portfolio Management")
st.subheader("Asset Allocation")
st.write("Asset allocation means spreading your investments across various asset classes. Broadly speaking, that means a mix of stocks, bonds, and cash or money market securities.")
image = Image.open('aggressive.png')
st.image(image, caption='Aggresive')
col1, col2 = st.columns(2)

with col1:
    st.subheader("A Conservative Portfolio")
    st.write("Conservative model portfolios generally allocate a large percentage of the total to lower-risk securities such as fixed-income and money market securities. The main goal of a conservative portfolio is to protect the principal value of your portfolio. ")
    imagec = Image.open('conservative.png')
    st.image(imagec, caption='Conservative Portfolio')

    st.write("##")
    st.write("##")
    st.write("##")
    st.subheader("A Moderately Aggressive Portfolio")
    st.write("Moderately aggressive model portfolios are often referred to as balanced portfolios because the asset composition is divided almost equally between fixed-income securities and equities. The balance is between growth and income. Because moderately aggressive portfolios have a higher level of risk than conservative portfolios, this strategy is best for investors with a longer time horizon (generally more than five years) and a medium level of risk tolerance.")
    imagema = Image.open('maggressive.png')
    st.image(imagema, caption='A Moderately Aggressive Portfolio')

with col2:
    st.subheader("A Moderately Conservative Portfolio")
    st.write("A moderately conservative portfolio works for the investor who wishes to preserve most of the portfolio's total value but is willing to take on some risk for inflation protection. A common strategy within this risk level is called current income. With this strategy, you choose securities that pay a high level of dividends or coupon payments.")
    imagemc = Image.open('mconservative.png')
    st.image(imagemc, caption='Moderately Conservative Portfolio')

    st.write("##")
    st.write("##")
    st.subheader("An Aggressive Portfolio ")
    st.write("Aggressive portfolios mainly consist of equities, so their value can fluctuate widely from day to day. If you have an aggressive portfolio, your main goal is to achieve long-term growth of capital. The strategy of an aggressive portfolio is often called a capital growth strategy. To provide diversification, investors with aggressive portfolios usually add some fixed-income securities. ")
    imagea = Image.open('aggressive.png')
    st.image(imagea, caption='An Aggressive Portfolio')

st.write("##")
st.write("##")
st.subheader("A Very Aggressive Portfolio ")
st.write("Very aggressive portfolios consist almost entirely of stocks. With a very aggressive portfolio, your goal is strong capital growth over a long time horizon.  Because these portfolios carry considerable risk, the value of the portfolio will vary widely in the short term.")
imageva = Image.open('veraggressive.png')
st.image(imageva, caption='A Very Aggressive Portfolio')


st.header("To Know More!!! Proceed below")
userid = st.text_input('Enter Your User id:')
def cfLevel(ticker):
    stk  = yf.download(ticker, start="2016-01-01", end="2022-06-30")
    stk_close = stk['Adj Close'].pct_change()
    stk_close.sort_values(inplace=True, ascending=True)
    VaR_95 = stk_close.quantile(0.05).round(4)# for 95%
    return VaR_95
if st.button("SUBMIT"):

    cur.execute("SELECT averagescore from risk where userid =%s",userid)
    averagescore = cur.fetchone()
    averagescore = averagescore[0]

    if averagescore < 1:
        category = "A Conservative Portfolio"
        st.subheader(category)
        st.image(imagec, caption='Conservative Portfolio')
    if averagescore in range(1,2):
        category = "A Moderately Conservative Portfolio"
        st.subheader(category)
        st.image(imagemc, caption='Moderately Conservative Portfolio')
    if averagescore in range(2,3):
        category = "A Moderately Aggressive Portfolio"
        st.subheader(category)
        st.image(imagema, caption='Moderately Aggressive Portfolio')
    if averagescore in range(3,4):
        category = "An Aggressive Portfolio"
        st.subheader(category)
        st.image(imagea, caption='An Aggressive Portfolio')
    if averagescore == 4:
        category = "A Very Aggressive Portfolio"
        st.subheader(category)
        imageva = Image.open('veraggressive.png', caption='A Very Aggressive Portfolio')

    cur.execute("SELECT balanceleft FROM investments where userid = %s",userid)
    bb= cur.fetchone()
    bb=bb[0]
    st.subheader("Your Balance left for financial Freedom can be split into various pattern and invested according to your portfolio")
    st.subheader(bb)
    if averagescore < 1:
        category = "A Conservative Portfolio"
        fixed = bb*0.6
        equities = bb*0.3
        cash = bb*0.1
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("Investment into Fixed Income Securities")
            st.subheader(fixed)
        with col2:
            st.subheader("Investment into Equities")
            st.write("##")
            st.subheader(equities)
        with col3:
            st.subheader("Investment into Cash and Equivalents")
            st.subheader(cash)
    if averagescore in range(1,2):
        category = "A Moderately Conservative Portfolio"
        fixed = bb*0.55
        equities = bb*0.35
        cash = bb*0.1
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("Investment into Fixed Income Securities")
            st.subheader(fixed)
        with col2:
            st.subheader("Investment into Equities")
            st.write("##")
            st.subheader(equities)
        with col3:
            st.subheader("Investment into Cash and Equivalents")
            st.subheader(cash)
    if averagescore in range(2,3):
        category = "A Moderately Aggressive Portfolio"
        fixed = bb*0.4
        equities = bb*0.5
        cash = bb*0.1
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("Investment into Fixed Income Securities")
            st.subheader(fixed)
        with col2:
            st.subheader("Investment into Equities")
            st.write("##")
            st.subheader(equities)
        with col3:
            st.subheader("Investment into Cash and Equivalents")
            st.subheader(cash)
    if averagescore in range(3,4):
        category = "An Aggressive Portfolio"
        fixed = bb*0.3
        equities = bb*0.6
        cash = bb*0.1
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("Investment into Fixed Income Securities")
            st.subheader(fixed)
        with col2:
            st.subheader("Investment into Equities")
            st.write("##")
            st.subheader(equities)
        with col3:
            st.subheader("Investment into Cash and Equivalents")
            st.subheader(cash)
    if averagescore == 4:
        category = "A Very Aggressive Portfolio"
        fixed = bb*0.1
        equities = bb*0.8
        cash = bb*0.1
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("Investment into Fixed Income Securities")
            st.subheader(fixed)
        with col2:
            st.subheader("Investment into Equities")
            st.write("##")
            st.subheader(equities)
        with col3:
            st.subheader("Investment into Cash and Equivalents")
            st.subheader(cash)
    
    tik = pd.read_csv(r'C:/Users/Admin/Desktop/ticker.csv')
    st.title("Stock")

    name = []
    cf95 = []
    for i in range(0,50):
        name.append(tik.Ticker[i])
        cf95.append(cfLevel(tik.Ticker[i]))

    cfdata = pd.DataFrame({
        'Ticker': name,
        'Risk': cf95
    })
    st.dataframe(cfdata)
    if averagescore < 1:
        st.dataframe((cfdata[cfdata.Risk>=0.02]))
    if averagescore in range(1,2):
        st.dataframe((cfdata[cfdata.Risk>=0]) & (cfdata[cfdata.Risk<0.02]),800,600)
    if averagescore in range(2,3):
        st.dataframe((cfdata[cfdata.Risk>=-0.03]),600,400)
    if averagescore in range(3,4):
        st.dataframe((cfdata[cfdata.Risk>=-0.03]) & (cfdata[cfdata.Risk<-0.01]),400,200)
    if averagescore == 4:
        st.dataframe((cfdata[cfdata.Risk>=-0.05]) & (cfdata[cfdata.Risk<-0.03]),400,200)
 
