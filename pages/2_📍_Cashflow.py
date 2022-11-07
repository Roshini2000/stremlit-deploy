
from pickle import NONE
from pickletools import markobject
from re import T
import streamlit as st
import psycopg2
 
st.set_page_config(page_title = 'Cash Flow Summary')
st.title("Cash Flow")
userid = st.text_input("Enter your User ID : ")
conn = psycopg2.connect(**st.secrets["postgres"])
conn.autocommit = True
cur = conn.cursor()

if st.button("SUBMIT"):
    #fetch income
    st.header("CASH FLOW SUMMARY")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" Cash inflow ")
        st.text("Salary 1 (after tax) + bonus + PF")
        st.text("Salary 2 (after tax) + PF")
        st.text("Otherincome")
        st.subheader("Cash Inflow Monthly Total")
       
    with col2:
        st.subheader("Monthly")
        cur.execute("SELECT (usersalary+annualbonus1/12+salary1pf+emp1pf+npssal1) FROM income where userid = %s ",userid)
        salary1 = cur.fetchone()
        st.text(salary1[0])
        cur.execute("SELECT (spousesalary+annualbonus2/12+salary2pf+emp2pf+npssal2) FROM income where userid = %s ",userid)
        salary2 = cur.fetchone()
        if salary2[0] == None:
            salary2 = 0;
        else : 
            salary2 = salary2[0]
        st.text(salary2)
        salary1 = salary1[0]
       ##
        cur.execute("SELECT (otherincome) FROM income where userid = %s ",userid)
        other= cur.fetchone()
        st.text(other[0])
        if other[0] == 'None':
            other = 0;
        else : 
            other = other[0]
            #need to check code 
        sumincome = salary1+salary2+other
        st.subheader(sumincome)
    #display

    st.header(" Cash outflow ")
    col3,col4 = st.columns(2)
    with col3:
        st.subheader("Expenses")
 
        st.text("Core lifestyle - monthly needs")
        st.text("Core lifestyle - annual needs")
        st.text("Life insurance (non ULIP)")
        st.subheader("Ongoing non-regular needs")
        st.text("Regular gifts")
        st.text("Electronics/ appliances/ furniture")
        st.text("Vacations")
        st.text("Charity ")
        st.text("Car upgrade fund")
        st.text("Emergency")
        st.text("Otherneeds")
        st.text("Total monthly outflow")
        st.subheader("MONTHLY CASH FLOW SURPLUS")
 
    with col4:
        st.subheader("Monthly")
    #fetch outflow
        cur.execute("SELECT totalmothly FROM outflowlifestylemonthly where userid = %s ",userid)
        monthlyls = cur.fetchone()
        st.text(monthlyls[0])
        cur.execute("SELECT totalannual FROM outflowannualcorelife where userid = %s ",userid)
        annualcore = cur.fetchone()
        st.text(annualcore[0])
        cur.execute("SELECT (lifeinsurance+reason1)  FROM outflowannualnoncorelife where userid = %s ",userid)
        annualnoncore = cur.fetchone()
        st.text(annualnoncore[0])
        st.write("##")
        st.write("##")
    #ongoing non-regular needs
        cur.execute("SELECT amtfunc/12 FROM ongoingneeds where userid = %s ",userid)
        gifts = cur.fetchone()
        st.text(gifts[0])
        cur.execute("SELECT amtelectronic/12  FROM ongoingneeds where userid = %s ",userid)
        electronic = cur.fetchone()
        st.text(electronic[0])
        cur.execute("SELECT amtvacations/12  FROM ongoingneeds where userid = %s ",userid)
        vacations = cur.fetchone()
        st.text(vacations[0])
        cur.execute("SELECT amtdonation/12  FROM ongoingneeds where userid = %s ",userid)
        charity = cur.fetchone()
        st.text(charity[0])
        cur.execute("SELECT amtcar/12  FROM ongoingneeds where userid = %s ",userid)
        car = cur.fetchone()
        st.text(car[0])
        cur.execute("SELECT amtemer/12  FROM ongoingneeds where userid = %s ",userid)
        emergency = cur.fetchone()
        st.text(emergency[0])
        cur.execute("SELECT amtother/12  FROM ongoingneeds where userid = %s ",userid)
        otherneeds = cur.fetchone()
        st.text(otherneeds[0])
        sumoutflow = monthlyls[0]+annualcore[0]+annualnoncore[0]+gifts[0]+electronic[0]+vacations[0]+charity[0]+car[0]+emergency[0]+otherneeds[0]
        st.text(sumoutflow)
        surplus = sumincome - sumoutflow
        st.subheader(surplus)
    

    st.header("ASSET SUMMARY")
    col5, col6 = st.columns(2)
    with col5:
        st.subheader("Investable assets")
        st.text("Savings accounts")
        st.text("Fixed deposits (FDs)")
        st.text("Recurring deposits (RDs)")
        st.text("Mutual funds - Equity/balanced funds")
        st.text("Mutual fund - Debt funds ")
        st.text("Stocks")
        st.text("PPF Self")
        st.text("NPS")
        st.text("Sukanya Samridhi Yojana")
        st.text("Chit funds (current investment value)")
        st.text("Lending to others")
        st.text("EPF current balance (at work) Self")
        st.text("EPF current balance (at work) Self")
        st.text("Gratuity Self1")
        st.text("Gratuity Self2")
        st.text("Employee share purchase plan (ESPP)")
        st.text("RSUs/ Stock options (vested)")
        st.text("RSUs/ Stock options (unvested)")
        st.text("Monthly surpluses until Dec 2022 (5 months)")
        st.subheader("Total (not in use for goal planning)")
        

    with col6:
        st.subheader(" Approx value ")
    #section 2
        cur.execute("SELECT account FROM investments where userid = %s ",userid)
        account = cur.fetchone()
        st.text(account[0])
        cur.execute("SELECT fds FROM investments where userid = %s ",userid)
        fds = cur.fetchone()
        st.text(fds[0])
        cur.execute("SELECT rds FROM investments where userid = %s ",userid)
        rds = cur.fetchone()
        st.text(rds[0])
        cur.execute("SELECT equity FROM investments where userid = %s ",userid)
        equity = cur.fetchone()
        st.text(equity[0])
        cur.execute("SELECT debtfunds FROM investments where userid = %s ",userid)
        debtfunds = cur.fetchone()
        st.text(debtfunds[0])
        cur.execute("SELECT stocks FROM investments where userid = %s ",userid)
        stocks = cur.fetchone()
        st.text(stocks[0])
        cur.execute("SELECT ppf FROM investments where userid = %s ",userid)
        ppf = cur.fetchone()
        st.text(ppf[0])
        cur.execute("SELECT nps FROM investments where userid = %s ",userid)
        nps = cur.fetchone()
        st.text(nps[0])
        cur.execute("SELECT ssy FROM investments where userid = %s ",userid)
        ssy = cur.fetchone()
        st.text(ssy[0])
        cur.execute("SELECT chitfunds FROM investments where userid = %s ",userid)
        chitfunds = cur.fetchone()
        st.text(chitfunds[0])
        cur.execute("SELECT lending FROM investments where userid = %s ",userid)
        lending = cur.fetchone()
        st.text(lending[0])
        cur.execute("SELECT epf1 FROM investments where userid = %s ",userid)
        epf1 = cur.fetchone()
        st.text(epf1[0])
        cur.execute("SELECT epf2 FROM investments where userid = %s ",userid)
        epf2 = cur.fetchone()
        st.text(epf2[0])
        cur.execute("SELECT gratuity1  FROM investments where userid = %s ",userid)
        gratuity1  = cur.fetchone()
        st.text(gratuity1[0])
        cur.execute("SELECT gratuity2 FROM investments where userid = %s ",userid)
        gratuity2 = cur.fetchone()
        st.text(gratuity2[0])
        cur.execute("SELECT espp FROM investments where userid = %s ",userid)
        espp = cur.fetchone()
        st.text(espp[0])
        cur.execute("SELECT stockvested  FROM investments where userid = %s ",userid)
        stockvested  = cur.fetchone()
        st.text(stockvested[0])
        cur.execute("SELECT stockunvested  FROM investments where userid = %s ",userid)
        stockunvested  = cur.fetchone()
        st.text(stockunvested[0])
        cur.execute("SELECT account+fds+rds+equity+debtfunds+stocks+ppf+nps+ssy+chitfunds+lending+epf1+epf2+gratuity1+gratuity2+espp+stockvested+stockunvested from investments where userid = %s ",userid)
        tinvest = cur.fetchone()
        surplusmonth = surplus*5
        st.text(surplusmonth)
        totalinvestment = tinvest[0]+surplusmonth
        st.subheader(totalinvestment)
        cur.execute("UPDATE investments SET surplusmonth = %s WHERE userid = %s",(surplusmonth,userid))

    
    st.header("Other assets/fixed assets")
    col7,col8,col9 =st.columns(3)
    with col7:
        st.subheader("Assets/fixed assets")
        st.text("Primary home")
        st.text("Property")
        st.text("Land")
        st.text("Jewel")
        st.text("Total")
        st.subheader("FUNDS AVAILABLE THIS YEAR FOR GOALS")

    with col8:
        st.subheader(" Approx value ")
        #other assests 
        cur.execute("SELECT curhome FROM otherasset where userid =%s",userid)
        curhome = cur.fetchone()
        st.text(curhome[0])
        cur.execute("SELECT currentalprop FROM otherasset where userid =%s",userid)
        curprop = cur.fetchone()
        st.text(curprop[0])
        cur.execute("SELECT currland FROM otherasset where userid =%s",userid)
        curland = cur.fetchone()
        st.text(curland[0])
        cur.execute("SELECT currjewel  FROM otherasset where userid =%s",userid)
        curjewel = cur.fetchone()
        st.text(curjewel[0])
        totalas = curhome[0]+curprop[0]+curland[0]+curjewel[0]
        st.text(totalas)
        totalfunds = totalinvestment
        st.subheader(totalfunds)
        cur.execute("UPDATE investments SET totalfunds = %s WHERE userid = %s",(totalfunds,userid))

