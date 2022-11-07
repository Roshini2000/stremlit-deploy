DB_HOST = "localhost"
DB_NAME = "miniproject"
DB_USER = "postgres"
DB_PASS = "roshini"
 
import psycopg2
from datetime import date
import pandas as pd
import matplotlib.pyplot as mp
from re import T
import streamlit as st
import psycopg2
import pandas as pd

st.set_page_config(page_title = 'Risk')
conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host = DB_HOST)
conn.autocommit = True
cur = conn.cursor()
st.title("Risk Tolarance")
userid = st.text_input("Enter your Userid:")
age = int(st.number_input("Age :"))
status = st.selectbox(
     'Income status :',
     ('Select a option','salaried', 'Self employed', 'Retired', 'Student', 'Other'))

networth = st.selectbox(
     'Approx net worth : ',
     ('Select a option','<50 lakhs', '50lakhs to 1 crore', '1-3 crore','3-10 crore', '>10 crore'))
ques1 = st.radio(
    "Which of these have you invested in before or are currently investes in?",
     ('Fixed deposits/bonds','Life insurance','Govt. Savings','Mutual funds','Stocks/Shares','None of the Above'))


ques2 = st.radio(
    "Compared to other investors, how would you rate your current willingess to take on investment risk?",
    ('very low risk taker','low risk taker','average risk taker','high risk taker','very high risk taker'))
if ques2 == 'very low risk taker':
    ques2score = 0
elif ques2 == 'low risk taker':
    ques2score = 1
elif ques2 == 'average risk taker':
    ques2score = 2
elif ques2 == 'high risk taker':
    ques2score = 3
elif ques2 == 'very high risk taker':
    ques2score = 4

ques3 = st.radio(
    "Higher returns generally mean taking on greater risks. When investing for the long term,some year will have positive returns and some years may have negative returns. Amongst these sample scenarios, which one is most acceptable to you?",
    ('I am  willing to accept no capital fall/drop in any year.','I am willing to accept a small capital fall/drop(i.e, in a negative year, I will be comfortable with a 0.5% drop in value)','I am willing to accept a moderate capital fall/drop(i.e, in a negative year, I will be conformable with a 6-15% drop in value)',
    'I am willing to accept a high capital fall/drop(i.e, in a negative year, I will be comfortable with a 16-35% drop in value)',
    'I am willing to accept a significant capital fall/drop(i.e, in a negative year, I will be comfortable with a potential 36% or higher drop in value)'))     
if ques3 == 'I am  willing to accept no capital fall/drop in any year.':
    ques3score = 0
elif ques3 == 'I am willing to accept a small capital fall/drop(i.e, in a negative year, I will be comfortable with a 0.5% drop in value)':
    ques3score = 1
elif ques3 == 'I am willing to accept a moderate capital fall/drop(i.e, in a negative year, I will be conformable with a 6-15% drop in value)':
    ques3score = 2
elif ques3 == 'I am willing to accept a high capital fall/drop(i.e, in a negative year, I will be comfortable with a 16-35% drop in value)':
    ques3score = 3
elif ques3 == 'I am willing to accept a significant capital fall/drop(i.e, in a negative year, I will be comfortable with a potential 36% or higher drop in value)':
    ques3score = 4

ques4 = st.radio(
    "you invest for a certain period of time to achieve your goal, large fluctuations during the period are likely. What would you do if your porfolio fell by 25% in a short period of time, say a month?",
    ('Take my money out immediately so that I do not lose more',
    'Sell a portion of the portfolio to cut losses and invest in more secure investments',
    'Seeking for knowlegde and invest more in recommended socks',
    'Hold and sell nothing, expecting performance to improve.',
    'Invest or allocate more funds to lower your average investment cost.'))
if ques4 == 'Take my money out immediately so that I do not lose more':
    ques4score = 0
elif ques4 == 'Sell a portion of the portfolio to cut losses and invest in more secure investments':
    ques4score = 1
elif ques4 == 'Seeking for knowlegde and invest more in recommended socks':
    ques4score = 2
elif ques4 == 'Hold and sell nothing, expecting performance to improve.':
    ques4score = 3
elif ques4 == 'Invest or allocate more funds to lower your average investment cost.':
    ques4score = 4

ques5= st.radio(
    "What is your primary objective when you invest generally for a long term goal?",
    ('Security - The safety of my capital is the biggest priority, even though the returns may not be enough to keep up with inflation.',
    'inflation protection - While I want my portfolio to grow, I am uncomfortable with flucuating returns.',
    'Growth & security - I want a balance between growth and safety and am comfortable with small fluctuations in returns year to year, but no negative returns in any year',
    'Growth - My primary goal is growth and will be comfortable with moderate fluctuations, sometimes negative returns in certain years.',
    'Maximium growth - My sole objective is maximum growth, knowing that I could have significant negative returns in certain years.')
)    
if ques5 == 'Security - The safety of my capital is the biggest priority, even though the returns may not be enough to keep up with inflation.':
    ques5score = 0
elif ques5 == 'inflation protection - While I want my portfolio to grow, I am uncomfortable with flucuating returns.':
    ques5score = 1
elif ques5 == 'Growth & security - I want a balance between growth and safety and am comfortable with small fluctuations in returns year to year, but no negative returns in any year':
    ques5score = 2
elif ques5 == 'Growth - My primary goal is growth and will be comfortable with moderate fluctuations, sometimes negative returns in certain years.':
    ques5score = 3
elif ques5 == 'Maximium growth - My sole objective is maximum growth, knowing that I could have significant negative returns in certain years.':
    ques5score = 4

ques6 = st.radio(
    "How secure do you feel about your present and future financial position considering your income from salary,business, other incomes, debts, health etc?",
    ('Not secure, I see myself accessing these funds for other financial reasons quickly.',
    'somewhat secure, I may need to access the funds for other financial reasons during the investment period.',
    'Secure,May need to access partial funds',
    'fairly secure. I do not see the need to acess these funds for other financial reasons',
    'Very secure. i will not need to access these funds during the investment period for reasons other than then goal being invested for ')
)
if ques6 == 'Not secure, I see myself accessing these funds for other financial reasons quickly.':
    ques6score = 0
elif ques6 == 'somewhat secure, I may need to access the funds for other financial reasons during the investment period.':
    ques6score = 1
elif ques6 == 'Secure,May need to access partial funds':
    ques6score = 2
elif ques6 == 'fairly secure. I do not see the need to acess these funds for other financial reasons':
    ques6score = 3
elif ques6 == 'Very secure. i will not need to access these funds during the investment period for reasons other than then goal being invested for ':
    ques6score = 4

totalscore = ques2score+ques3score+ques4score+ques5score+ques6score
averagescore = totalscore/5
if st.button("SUBMIT"):
    cur.execute("INSERT INTO risk (userid,age,status,networth,ques1,ques2score,ques3score,ques4score,ques5score,ques6score,totalscore,averagescore) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(userid,age,status,networth,ques1,ques2score,ques3score,ques4score,ques5score,ques6score,totalscore,averagescore))
    st.subheader('Risk Taking Ability as an Average Score')
    st.subheader(averagescore)