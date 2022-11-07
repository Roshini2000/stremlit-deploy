
from datetime import date
from re import T
import streamlit as st
import psycopg2
 
st.set_page_config(page_title = 'Goal Planing')
st.title("Goal Plannig")
userid = st.text_input("Enter your User ID : ")
inflation = st.number_input("Inflation rate in precent :")
conn = psycopg2.connect(**st.secrets["postgres"])
conn.autocommit = True
cur = conn.cursor()

if st.button("SUBMIT"):
    st.header("Quantifying each goal")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Children marriage")
        st.markdown("Funds needed for the goal (in today's value)")
        st.markdown("Inflation rate ")
        st.markdown("After tax investment return expected")
        st.markdown("Funds should be ready for goal by end of")
        st.markdown("Funds needed in with inflation")
        st.markdown("Investment from available investable assets curret availability")
        st.markdown("Monthly investment needed starting from current year")

    with col2:
        st.subheader("Need")
        cur.execute("SELECT amtmar FROM biggoals where userid =%s",userid)
        maramt= cur.fetchone()
        st.text(maramt[0])
        maramt= maramt[0]
        st.text(inflation)
        st.text(inflation)
        currentyear = date.today().year
        cur.execute("SELECT yrmar FROM biggoals where userid =%s",userid)
        maryear= cur.fetchone()
        st.text(maryear[0])
        maryear = maryear[0]
        noofyears = maryear - currentyear
        fundneed = maramt *((1+inflation/100) **noofyears )
        fundneed = int(fundneed)
        st.text(fundneed) 
        st.write("##")
        st.text(maramt)
        r = (inflation/100)
        numfundneed = r/12 * (fundneed-maramt*((1+r/12)**(noofyears*12)))
        denofundneed = ((1+r/12)**(noofyears*12) - 1)
        mfundneed = numfundneed/denofundneed
        mfundneed = int(mfundneed)
        st.write("##")
        st.text(mfundneed)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Home Renovation")
        st.markdown("Funds needed for the goal (in today's value) ")
        st.markdown("Inflation rate ")
        st.markdown("After tax investment return expected")
        st.markdown("Funds should be ready for goal by end of")
        st.markdown("Funds needed in with inflation")
        st.markdown("Investment from available investable assets curret availability")
        st.markdown("Monthly investment needed starting from current year")

    with col2:
        st.subheader("Need")
        cur.execute("SELECT amtreno FROM biggoals where userid =%s",userid)
        amtreno= cur.fetchone()
        st.text(amtreno[0])
        amtreno= amtreno[0]
        st.text(inflation)
        st.text(inflation)
        cur.execute("SELECT yrreno FROM biggoals where userid =%s",userid)
        yrreno= cur.fetchone()
        st.text(yrreno[0])
        yrreno = yrreno[0]
        noofyearsreno = yrreno - currentyear
        fundneedreno = amtreno *((1+inflation/100)**noofyearsreno)
        fundneedreno = int(fundneedreno)
        st.text(fundneedreno)
        st.write("##")
        st.text(amtreno)
        #monhtly payment
        r = (inflation/100)
        numfundneedreno = r/12 * (fundneedreno-amtreno*((1+r/12)**(noofyearsreno*12)))
        denofundneedreno = ((1+r/12)**(noofyearsreno*12) - 1)
        mfundneedreno = numfundneedreno/denofundneedreno
        mfundneedreno = int(mfundneedreno)
        st.write("##")
        st.text(mfundneedreno)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Special Function Needs")
        st.markdown("Funds needed for the goal (in today's value) ")
        st.markdown("Inflation rate ")
        st.markdown("After tax investment return expected")
        st.markdown("Funds should be ready for goal by end of")
        st.markdown("Funds needed in with inflation")
        st.markdown("Investment from available investable assets curret availability")
        st.markdown("Monthly investment needed starting from current year")

    with col2:
        st.subheader("Need")
        cur.execute("SELECT amtff FROM biggoals where userid =%s",userid)
        amtff= cur.fetchone()
        st.text(amtff[0])
        amtff= amtff[0]
        st.text(inflation)
        st.text(inflation)
        cur.execute("SELECT yrff FROM biggoals where userid =%s",userid)
        yrff= cur.fetchone()
        st.text(yrff[0])
        yrff = yrff[0]
        noofyearsff = yrff - currentyear
        fundneedff = amtff *((1+inflation/100)**noofyearsff )
        fundneedff = int(fundneedff)
        st.text(fundneedff)
        st.write("##")
        st.text(amtff)
        #monhtly payment
        r = (inflation/100)
        numfundneedff = r/12 * (fundneedff-amtff*((1+r/12)**(noofyearsff*12)))
        denofundneedff = ((1+r/12)**(noofyearsff*12) - 1)
        mfundneedff = numfundneedff/denofundneedff
        mfundneedff = int(mfundneedff)
        st.write("##")
        st.text(mfundneedff)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Buying Car")
        st.markdown("Funds needed for the goal (in today's value) ")
        st.markdown("Inflation rate ")
        st.markdown("After tax investment return expected")
        st.markdown("Funds should be ready for goal by end of")
        st.markdown("Funds needed in with inflation")
        st.markdown("Investment from available investable assets curret availability")
        st.markdown("Monthly investment needed starting from current year")

    with col2:
        st.subheader("Need")
        cur.execute("SELECT amtcar FROM biggoals where userid =%s",userid)
        amtcar= cur.fetchone()
        st.text(amtcar[0])
        amtcar= amtcar[0]
        st.text(inflation)
        st.text(inflation)
        cur.execute("SELECT yrnexcar  FROM biggoals where userid =%s",userid)
        yrnexcar = cur.fetchone()
        st.text(yrnexcar [0])
        yrnexcar  = yrnexcar [0]
        noofyearscar = yrnexcar  - currentyear
        fundneedcar = amtcar *((1+inflation/100)**noofyearscar )
        fundneedcar = int(fundneedcar)
        st.text(fundneedcar)
        st.write("##")
        st.text(amtcar)
        #monhtly payment
        r = (inflation/100)
        numfundneedcar = r/12 * (fundneedcar-amtcar*((1+r/12)**(noofyearscar*12)))
        denofundneedcar = ((1+r/12)**(noofyearscar*12) - 1)
        mfundneedcar = numfundneedcar/denofundneedcar
        mfundneedcar = int(mfundneedcar)
        st.write("##")
        st.text(mfundneedcar)

    st.header("Summary of Resource Allocation for Goals")
    col1, col2,col3 = st.columns(3)
    with col1:
        st.text("Category")
        st.markdown("Children Marriage")
        st.markdown("Home Renovation")
        st.markdown("Special Function Needs")
        st.markdown("Buying a car")
        st.markdown("Total")
        st.markdown("Available Funds:")
        st.markdown("Balance left for Financial Freedom")

    with col2:
        st.text("2022 lump sum investment")
        st.markdown(fundneed)
        st.markdown(fundneedreno)
        st.markdown(fundneedff)
        st.markdown(fundneedcar)
        funtotal = fundneed+fundneedreno+fundneedff+fundneedcar
        st.markdown(funtotal)
        cur.execute("SELECT totalfunds FROM investments where userid = %s",userid)
        totalfunds= cur.fetchone()
        st.markdown(totalfunds[0])
        bb = totalfunds[0] - funtotal
        cur.execute("UPDATE investments SET balanceleft=%s WHERE userid =%s",(bb,userid))
        st.markdown(bb)

    with col3:
        st.markdown("Monthly investment needed")
        st.markdown(mfundneed)
        st.markdown(mfundneedreno)
        st.markdown(mfundneedff)
        st.markdown(mfundneedcar)
        mfuntotal = mfundneed +mfundneedreno+mfundneedff+mfundneedcar
        st.markdown(mfuntotal)
        cur.execute("SELECT surplusmonth FROM investments where userid = %s",userid)
        surplusmonth= cur.fetchone()
        st.markdown(surplusmonth[0])
        

