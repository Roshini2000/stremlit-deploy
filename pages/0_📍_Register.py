 
from re import T
import streamlit as st
import psycopg2
 
st.set_page_config(page_title = 'Retirement Page')
st.title("Registration")
conn = psycopg2.connect(**st.secrets["postgres"])
conn.autocommit = True
usermailid = st.text_input("Enter your Mail ID:")
usercontact = st.text_input("Enter your contact:")

if st.button("SUBMIT"):
        cur = conn.cursor()
        cur.execute("INSERT INTO userdata (usermail,usercontact) VALUES (%s,%s)",(usermailid,usercontact))
        cur.close() 
        st.write("##")
        st.write("Successfully Registered", usermailid)
        cur = conn.cursor()
        userid = cur.execute("SELECT max(userid) FROM userdata")
        userid = cur.fetchone()
        st.write("Your User ID",userid[0])
        cur.close();
