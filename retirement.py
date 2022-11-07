DB_HOST = "localhost"
DB_NAME = "miniproject"
DB_USER = "postgres"
DB_PASS = "roshini"
 
from re import T
import ssl
import streamlit as st
import psycopg2
from datetime import date

st.set_page_config(page_title = 'Retirement Page')
st.title("Retirement Planning")
 
conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host = DB_HOST)
conn.autocommit = True
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Basic Info", "Income details", "Outflow Info","Assets and Liabilities","Goals and Anticipated Expense"])
 
with tab1:
    st.header("Basic Info")
    st.write("Enter the details as a new user")
    userid =  st.text_input("Enter your User Id:")
    name = st.text_input("Enter your Name:")
    spousename = st.text_input("Enter your Spouse Name:")
    namechild1 = st.text_input("Enter name of child 1 :")
    namechild2 = st.text_input("Enter name of child 2 :")
 
    dob = st.text_input("Enter your Year of Birth:")
    spousedob = st.text_input("Enter your Spouse Year of Birth:")
    dobchild1 = st.text_input("Enter Year of Birth of child 1 :")
    dobchild2 = st.text_input("Enter Year of Birth of child 2 :")
 
    occ = st.text_input("Enter your Occupation:")
    spouseocc = st.text_input("Enter your Spouse Occupation:")
    occchild1 = st.text_input("Enter Occupation of child 1 :")
    occchild2 = st.text_input("Enter Occupation of child 2 :")
    todays_date = date.today()

    if st.button("SUBMIT"):
        cur = conn.cursor()
        cur.execute("INSERT INTO biodata (userid,username,spousename,namechild1,namechild2,dob,spousedob,dobchild1,dobchild2,occu,spouseoccu,occuchild1,occuchild2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (userid,name,spousename,namechild1,namechild2,dob,spousedob,dobchild1,dobchild2,occ,spouseocc,occchild1,occchild2))
        cur.close()
        startyear = todays_date.year
        dob = int(dob)
        spousedob=int(spousedob)
        dobchild1 = int(dobchild1)
        dobchild2 = int(dobchild2)
        
        if dobchild1 == 0:
            child1age = 0;
        else :
            child1age = int(dobchild1)

        if dobchild2 == 0:
            child2age = 0;
        else :
            child2age = int(dobchild2)
        wanted = 50 
        endyear = startyear + wanted
        for startyear in range(startyear,endyear):
            cur = conn.cursor()
            cur.execute("INSERT INTO timetable (userid,years,yourage,spouseage,child1age,childage2) VALUES (%s,%s,%s,%s,%s,%s)", 
            (userid,startyear,startyear-dob,startyear-spousedob,startyear - child1age,child2age))
            startyear = startyear+1
            cur.close()

        st.write("##")
        st.write("Data Successfully Registered for the user",userid)
 
with tab2:
    st.header("Income Details")
    option = st.selectbox(
     'What details would you like to register?',
     ('Select an option','My Salary', 'Spouse Salary','Other Income'))
 
    if option == 'My Salary':
        userid =  st.text_input("Enter your user Id:")
        usersalary = int(st.number_input("Monthly Salary after Tax & Deductions in Rs:"))
        userannualbonus = int(st.number_input("Annual Bonus if any in Rs:"))
        selfpf = int(st.number_input("Your monthly PF contribution in Rs:"))
        empselfpf = int(st.number_input("Employer's monthly PF contribution in Rs:"))
        npssal1 = int(st.number_input("NPS contributions (if made through salary) in Rs:"))
        if st.button("SUBMIT YOUR SALARY"):
            cur = conn.cursor()
            cur.execute("INSERT INTO income (userid,usersalary,annualbonus1,salary1pf,emp1pf,npssal1) VALUES (%s,%s,%s,%s,%s,%s)",
            (userid,usersalary,userannualbonus,selfpf,empselfpf,npssal1))
            cur.close()
            st.write("##")
            st.write("Income Details Successfully Registered for the user",userid)
 
    if option == 'Spouse Salary':
        userid =  st.text_input("Enter your user Id:")
        salary2 = int(st.number_input("Monthly Salary after Tax & Deductions in Rs:"))
        annualbonus2 = int(st.number_input("Annual Bonus if any in Rs:"))
        selfpfsal2 = int(st.number_input("Your monthly PF contribution in Rs:"))
        empselfpfsal2 = int(st.number_input("Employer's monthly PF contribution in Rs:"))
        npssal2 = int(st.number_input("NPS contributions (if made through salary) in Rs:"))
        if st.button("SUBMIT SPOUSE SALARY"):
            cur = conn.cursor()
            cur.execute("UPDATE income SET spousesalary =%s,annualbonus2 =%s,salary2pf=%s,emp2pf =%s,npssal2=%s WHERE userid = %s",
            (salary2,annualbonus2,selfpfsal2,empselfpfsal2,npssal2,userid))
            cur.close()
            st.write("##")
            st.write("Income of Spouse Details Successfully Registered for the user",userid)

    if option == 'Other Income':
        userid =  st.text_input("Enter your user Id:")
        category = st.text_input("What kind of other Income:")
        incomeothercat = st.number_input("Total other Income in Rs:")
        if st.button("SUBMIT OTHER INCOME DETAILS"):
            cur = conn.cursor()
            cur.execute("UPDATE income SET catotherincome =%s,otherincome  =%s WHERE userid = %s",
            (category,incomeothercat,userid))
            cur.close()
            st.write("##")
            st.write("Other Income Details Successfully Registered for the user",userid)


with tab3:
    st.header("Outflow Info")
    option = st.selectbox(
     'Case Outflow Details:',
     ('Select an option','Lifestyle Expense','Annual Expenses','Loan Payments'))
 
    if option == 'Lifestyle Expense':
        userid =  st.text_input("Enter your user id:")
        rent = int(st.number_input("Monthly Rent for house:"))
        apartment = int(st.number_input("Monthly Apartment maintenance : "))
        maidsalary = int(st.number_input("Monthly Maid Salary : "))
        dhobi = int(st.number_input("Monthly Amount spend for Dhobi : "))
        electricity = int(st.number_input("Monthly Electricity Bill: "))
        water = int(st.number_input("Monthly Water Bill : "))
        tv = int(st.number_input("Monthly Amount for TV/cable : "))
        internet = int(st.number_input("Monthly Amount spend for Internet : "))
        cellphone = int(st.number_input("Monthly Amount spend for Mobile Phone : "))
        newspaper = int(st.number_input("Monthly Newspaper Bill : "))
        groceries = int(st.number_input("Monthly Amount spend for Groceries : "))
        diningout= int(st.number_input("Monthly Amount spend for Dining Out : "))  
        vehiclefuel= int(st.number_input("Monthly Amount spend for Vehicle Fuel : "))
        givingspouse= int(st.number_input("Monthly Amount Give to Spouse : "))
        entertainment = int(st.number_input("Monthly Amount spend for Entertainment(movies,etc,.) : "))
        sports= int(st.number_input("Monthly Amount spend for Sports/Gym/Hobbies: "))
        shopping= int(st.number_input("Monthly Amount spend for Shopping : "))
        medicines= int(st.number_input("Monthly Amount spend for Medicinies : "))
        miscellaneous = int(st.number_input("Monthly Amount spend for Miscellaneous : "))
        other = st.text_input("Other Expense: ")
        reasonamt =int(st.number_input("Amount For other Lifestyle Expenses"))
        givingfamily= int(st.number_input("Monthly Amount Give to family(parents,etc,.) : "))  
        if st.button("SUBMIT OUTFLOW DETAILS"):
            cur = conn.cursor()
            cur.execute("INSERT INTO outflowlifestylemonthly (userid,rent,apartment,maidsalary,dhobi,electricity,water,tv,internet,cellphone,newspaper,groceries,diningout,vehiclefuel,givingspouse,entertainment,sports,shopping,medicines,miscellaneous,other,reasonamt,givingfamily, totalmothly) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (userid,rent,apartment,maidsalary,dhobi,electricity,water,tv,internet,cellphone,newspaper,groceries,diningout,vehiclefuel,givingspouse,entertainment,sports,shopping,medicines,miscellaneous,other,reasonamt,givingfamily,
            (rent+apartment+maidsalary+dhobi+electricity+water+tv+internet+cellphone+newspaper+groceries+diningout+vehiclefuel+givingspouse+entertainment+sports+shopping+medicines+miscellaneous+reasonamt+givingfamily)))
            cur.close()
            st.write("##")
            st.write("Monthly Cash Outflow Updated Successfully for the user",userid)

       
    if option =='Annual Expenses':
        userid =  st.text_input("Enter user id:")
        apropertytax = int(st.number_input("Annual Amount You pay for Property Tax : "))
        amedicalinsurancepremiums = int(st.number_input("Annual Amount You pay for Medical insurance premiums: "))
        avehiclemaintenanceandinsurance= int(st.number_input("Annual Amount You spend for Vehicle maintenance and insurance : "))
        afestivalexpenses = int(st.number_input("Annual Amount You spend for Festival expenses (crackers, maid bonus, etc)  : "))
        aclubevents = int(st.number_input("Annual Amount You spend for Club/Professional or memberships/events : "))
        adental = int(st.number_input("Annual Amount You spend for Dental/eyecare/glasses etc : "))
        adoctorvisits = int(st.number_input("Annual Amount You spend for Doctor visits : "))
        aother = st.text_input("Annual Spendings Category/Type:")
        aotheramt = int(st.number_input("Amount For other Annual Expenses"))
        totalannual = apropertytax+amedicalinsurancepremiums+avehiclemaintenanceandinsurance+afestivalexpenses+aclubevents+adental+adoctorvisits+aotheramt
        totalmonthly = apropertytax/12+amedicalinsurancepremiums/12+avehiclemaintenanceandinsurance/12+afestivalexpenses/12+aclubevents/12+adental/12+adoctorvisits/12+aotheramt/12
        if st.button("SUBMIT ANNUAL OUTFLOW DETAILS"):
            cur = conn.cursor()
            cur.execute("INSERT INTO outflowannualcorelife (userid,apropertytax,amedicalinsurancepremiums,avehiclemaintenanceandinsurance,afestivalexpenses,aclubevents,adental,adoctorvisits,mpropertytax,mmedicalinsurancepremiums,mvehiclemaintenanceandinsurance,mfestivalexpenses,mclubevents,mdental,mdoctorvisits,aother,aotheramt,totalannual,totalmonthly) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (userid,apropertytax,amedicalinsurancepremiums,avehiclemaintenanceandinsurance,afestivalexpenses,aclubevents,adental,adoctorvisits,apropertytax/12,amedicalinsurancepremiums/12,avehiclemaintenanceandinsurance/12,afestivalexpenses/12,aclubevents/12,adental/12,adoctorvisits/12,aother,aotheramt,totalannual,totalmonthly))
            cur.close()
            st.write("##")
            st.write("Annual Expenses Updated Successfully for the user",userid)
            
        st.subheader('Non-Lifestyle Expense')
        lifeinsurance= int(st.number_input("Annual Amount You pay for Life insurance premiums : "))
        other1payments = st.text_input("Annual Non-Lifestyle Expense Type :")
        reason1 = int(st.number_input("Amount For others Non-LifeStyle Expenses"))
        if st.button("SUBMIT NON LIFESTYLE EXPENSES"):
            cur = conn.cursor()
            cur.execute("INSERT INTO outflowannualnoncorelife (userid,lifeinsurance, other1payments ,reason1) VALUES (%s,%s,%s,%s)",
            (userid,lifeinsurance, other1payments ,reason1))
            cur.close()
            st.write("##")
            st.write("Annual Non- Life Style Expenses Updated Successfully for the user",userid)
        
 
    if option == 'Loan Payments':
        userid =  st.text_input("Enter User Id:")
        homeloan= int(st.number_input("Monthly Amount You pay for Home Loan : "))
        carloan= int(st.number_input("Monthly Amount You pay for Car Loan : "))
        personalloan= int(st.number_input("Monthly Amount You pay for Personal Loan : "))
        creditcardloan= int(st.number_input("Monthly Amount You pay for Credit card loan (ignore if you pay off full balance every month): "))
        if st.button("SUBMIT OUTFLOW DETAILS"):
            cur = conn.cursor()
            cur.execute("INSERT INTO outflowloan (userid,homeloan,carloan,personalloan,creditcardloan ) VALUES (%s,%s,%s,%s,%s)",
            (userid,homeloan,carloan,personalloan,creditcardloan ))
            cur.close()
            st.write("##")
            st.write("Loan Payment outflow Updated Successfully for the user",userid)


with tab4:
    st.header("Assets and Liabilities")
    option = st.selectbox(
     'Select a option :',
     ('Select an option','Investment','Other Assets', 'Insurance','loan'))
    if option == 'Investment':
        userid =  st.text_input("Enter user Id:")
        st.subheader("Name")
        account = int(st.number_input("Amount you have in Savings accounts : "))
        fds = int(st.number_input("Amount you have in Fixed deposits (FDs) : "))
        rds = int(st.number_input("Amount you need for Recurring deposits (RDs) : "))
        equity = int(st.number_input("Amount you spend in Mutual funds - Equity/balanced funds: "))
        debtfunds = int(st.number_input("Amount you spend in Mutual fund - Debt funds : "))
        stocks = int(st.number_input("Amount you spend in Stocks: "))
        st.write("##")
        ppf = int(st.number_input("Amount you spend in PPF: "))
        nps = int(st.number_input("Amount you spend in NPS: "))
        ssy = int(st.number_input("Amount you spend in Sukanya Samridhi Yojana : "))
        st.write("##")
        chitfunds = int(st.number_input("Amount you spend in Chit funds (current investment value) : "))
        lending = int(st.number_input("Amount you spend in Lending to others : "))
        st.write("##")
        epf1 = int(st.number_input("EPF current balance (at work) 1 : "))
        epf2 = int(st.number_input("EPF current balance (at work) 2 : "))
        st.write("##")
        gratuity1 = int(st.number_input("Gratuity 1 : "))
        gratuity2 = int(st.number_input("Gratuity 2 : "))
        st.write("##")
        espp = int(st.number_input("Employee share purchase plan (ESPP) : "))
        stockvested = int(st.number_input("RSUs/ Stock options (vested) : "))
        stockunvested = int(st.number_input("RSUs/ Stock options (unvested) : "))
        if st.button("SUBMIT INVESTMENT DETAILS"):
            cur = conn.cursor()
            cur.execute("INSERT INTO investments (userid,account,fds,rds,equity,debtfunds,stocks,ppf,nps,ssy,chitfunds,lending,epf1,epf2,gratuity1,gratuity2,espp,stockvested,stockunvested) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (userid,account,fds,rds,equity,debtfunds,stocks,ppf,nps,ssy,chitfunds,lending,epf1,epf2,gratuity1,gratuity2,espp,stockvested,stockunvested))
            cur.close()
            st.write("##")
            st.write("Investmets Updated Successfully for the user",userid)
 
    if option =='Other Assets':
        userid =  st.text_input("Enter user Id:")
        col1,col2,col3,col4 = st.columns(4)
        with col1 :
            st.markdown('Asset')
            Home= st.markdown("Primary home : ")
            st.write("##")
            Pro = st.markdown("Rental property : ")
            st.write("##")
            LK = st.markdown("Land : ")
            st.write("##")
            Jewel = st.markdown("Jewel: ")
 
        with col2 :
             curhome= int(st.number_input("Approx. current value: "))
             currentalprop= int(st.number_input("current value: "))
             currland= int(st.number_input("Current value: "))
             currjewel= int(st.number_input("Current Value: "))
 
        with col3:
           
            incomehome= int(st.number_input("Monthly income from asset: "))
            incomerentalprop= int(st.number_input("Monthly income from Asset: "))
            incomeland= int(st.number_input("Monthly Income from asset: "))
            incomejewel= int(st.number_input("monthly income from asset: "))
 
        with col4:
            
                loanonhome = st.selectbox(
            "Is there a loan on the asset?",
            ('Yes','No'))
                loanonrentalprop = st.selectbox(
            "Is there a Loan on the asset?",
            ('Yes','No'))
                loanonland = st.selectbox(
            "Is there a loan on the Asset?",
            ('Yes','No'))
                loanonjewel = st.selectbox(
            "Is There a loan on the asset?",
            ('Yes','No'))
    
        if st.button("SUBMIT ASSET DETAILS"):
            cur = conn.cursor()
            cur.execute("INSERT INTO otherasset (userid,curhome,currentalprop,currland,currjewel,incomehome,incomerentalprop,incomeland,incomejewel,loanonhome,loanonrentalprop,loanonland,loanonjewel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (userid,curhome,currentalprop,currland,currjewel,incomehome,incomerentalprop,incomeland,incomejewel,loanonhome,loanonrentalprop,loanonland,loanonjewel))
            cur.close()
            st.write("##")
            st.write("Other Assest Updated Successfully for the user",userid) 
 
    if option == 'Insurance':
        st.subheader("Life Insurance")
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            policyname = st.text_input("Life insurance policy name :")
            premiumamt = st.number_input("Annual Premium amount :")

        with col2:
            company = st.text_input("Insurance company :")
            commdate = st.text_input("Policy Commenement date:")
 
        with col3:
            insured = st.text_input("Who is insured :")
            matdate = st.text_input("Maturity date :")
 
        with col4:
            suminsured = int(st.number_input("Sum Assured amount :"))
        if st.button("SUBMIT INSURANCE DETAILS"):
            cur = conn.cursor()
            cur.execute("INSERT INTO insurance (userid,policyname,premiumamt,company,commdate,insured,matdate,suminsured) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (userid,policyname,premiumamt,company,commdate,insured,matdate,suminsured))
            cur.close()
            st.write("##")
            st.write("Insurance details Updated Successfully for the user",userid) 

 
        st.subheader("Medical/critical illness insurance policies")
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            policyname = st.text_input("Policy Name :")
            preamt = st.number_input("Anual Premium Amount :")
       
        with col2:
            comp = st.text_input("Insurance-company :")
 
        with col3:
            covered = st.text_input("Who is Covered:")
 
        with col4:
            coveramount = int(st.number_input("Cover amount :"))
        if st.button("SUBMIT MEDICAL INSURANCE DETAILS"):
            cur = conn.cursor()
            cur.execute("INSERT INTO medinsurance (userid,policyname,preamt,comp,covered,coveramount) VALUES (%s,%s,%s,%s,%s,%s)",
            (userid,policyname,preamt,comp,covered,coveramount))
            cur.close()
            st.write("##")
            st.write("Medical Insurance details Updated Successfully for the user",userid) 

    if option == 'loan':
        st.subheader('Type of Loans')
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            st.markdown("Home loan: ")
            st.write("##")
            st.write("##")
            st.markdown("Car loan : ")
            st.write("##")
            st.write("##")
            st.markdown("Personal loan : ")
            st.write("##")
            st.write("##")
            st.markdown("Education loan : ")
 
        with col2:
            curprinhomeloan = int(st.number_input("Current principal balance:"))
            st.write("##")
            curprincarloan = int(st.number_input("Current principal balance :"))
            st.write("##")
            curprinpersonalloan = int(st.number_input("Current Principal balance:"))
            st.write("##")
            curprineduloan = int(st.number_input("Current principal Balance:"))
 
        with col3:
            roihomeloan = int(st.number_input("Rate of interest"))
            st.write("##")
            roicarloan = int(st.number_input("Rate of Interest"))
            st.write("##")
            roipersonalloan = int(st.number_input("rate of interest"))
            st.write("##")
            roieduloan = int(st.number_input("Rate Of Interest"))
 
        with col4:
             yearhomeloan = st.slider("Loan Payoff Year",2022,2040)
             yearcarloan = st.slider("Annual year",2022,2040)
             st.write("##")
             yearpersonalloan = st.slider("Annual Year",2022,2040)
             st.write("##")
             yeareduloan = st.slider("Annual-Year",2022,2040)

        if st.button("SUBMIT LOAN DETAILS"):
            cur = conn.cursor()
            cur.execute("INSERT INTO liabilityloan (userid,curprinhomeloan,curprincarloan,curprinpersonalloan,curprineduloan,roihomeloan,roicarloan,roipersonalloan,roieduloan,yearhomeloan,yearcarloan,yearpersonalloan,yeareduloan) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (userid,curprinhomeloan,curprincarloan,curprinpersonalloan,curprineduloan,roihomeloan,roicarloan,roipersonalloan,roieduloan,yearhomeloan,yearcarloan,yearpersonalloan,yeareduloan))
            cur.close()
            st.write("##")
            st.write("Loan details Updated Successfully for the user",userid)

with tab5:
    st.header("Goals and Anticipated Expense ")
    userid =  st.text_input("Enter user ID:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Big goals")
       
        st.markdown("Amount you need for Children's Marriage : ")
        st.write("##")
        st.markdown("Amount you need for Financial Freedom(Optional) : ")
        st.write("##")
        st.markdown("Amount You need for Renovating existing home : ")
        st.write("##")
        st.markdown("Amount You need for Next car purchase : ")
        otherneed1 = st.text_input("Other expenses 1:")
        otherneed2 = st.text_input("Other expenses 2:")   
        

    with col2:
        st.write("##")
        yrmar = st.slider("Select the Year",2022,2040)
        yrff = st.slider("Select year",2022,2040)
        yrreno = st.slider("Year",2022,2040)
        yrnexcar = st.slider("year",2022,2040)
        otheramt1 = int(st.number_input("Enter the amount needed:"))
        otheramt2 = int(st.number_input("Enter the Amount needed:"))
 
       
    with col3:
        st.write("##")
        amtmar= int(st.number_input("Amount in Today's value : "))
        amtff= int(st.number_input(""))
        st.write("##")
        amtreno =  int(st.number_input("Amount"))
        st.write("##")
        amtcar = int(st.number_input("amonut"))
 
    st.write("##")    
 
    col1, col2, col3 = st.columns(3)
    with col1:
       st.subheader("On-going Needs")
       st.markdown("Amount you need for Emergency/Medical fund : ")
       st.markdown("Amount you need for Car upgrade fund: ")
       otherneed = st.text_input("Others")
    with col2:
        st.write("##")
   
        optemer = st.selectbox(
        "Select the Timing",
        ('Immediate','On going','After some time','Monthly','NA'))
        optcar = st.selectbox(
        'Timing',
        ('Immediate','On going','After some time','Monthly','NA'))
        optother = st.selectbox(
        "",
        ('Immediate','On going','After some time','Monthly','NA'))
 
    with col3:
        st.write("##")
        amtemer= int(st.number_input("Amount Today's value : "))
        amtcar= int(st.number_input("AMOUNT"))
        amtother= int(st.number_input("Other Amount"))
   
    st.write("##")
     
    st.subheader("Other yearly needs (average)")
    amtfunc = int(st.number_input("Amount you need for Regular gifts (for relatives, functions etc) : "))
    amtelectronic = int(st.number_input("Amount you need for Electronics/appliances/furniture & other home upgrades : "))
    amtvacations = int(st.number_input("Amount you need for Vacations : "))
    amtdonation = int(st.number_input("Amount you need for Charity donations : "))

    if st.button("SUBMIT GOAL DETAILS"):
        cur = conn.cursor()
        cur.execute("INSERT INTO biggoals (userid,otherneed1,otherneed2,otheramt1,otheramt2,yrmar,yrff,yrreno,yrnexcar,amtmar,amtff,amtreno,amtcar) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (userid,otherneed1,otherneed2,otheramt1,otheramt2,yrmar,yrff,yrreno,yrnexcar,amtmar,amtff,amtreno,amtcar))
        cur.execute("INSERT INTO ongoingneeds (userid,optemer,optcar,otherneed,optother,amtemer,amtcar,amtother,amtfunc,amtelectronic,amtvacations,amtdonation) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (userid,optemer,optcar,otherneed,optother,amtemer,amtcar,amtother,amtfunc,amtelectronic,amtvacations,amtdonation))
        cur.close()
        st.write("##")
        st.write("Goal details Updated Successfully for the user",userid)
 
 
     
 
   
 
 
 
   
     
 
 
       
 
       
           


