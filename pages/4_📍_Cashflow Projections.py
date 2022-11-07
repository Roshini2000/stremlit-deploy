DB_HOST = "localhost"
DB_NAME = "miniproject"
DB_USER = "postgres"
DB_PASS = "roshini"
 
import streamlit as st
import psycopg2
from datetime import date
import pandas as pd
import matplotlib.pyplot as mp


st.set_page_config(page_title = 'Cash Flow Projections')
st.title("Cash Flow Projections")
userid = st.text_input("Enter your User ID : ")
conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host = DB_HOST)
conn.autocommit = True
cur = conn.cursor()
todays_date = date.today() 
tab1, tab2, tab3 = st.tabs(["Cash projection Financials", "Income Projections ","Monthly and Annual Projections"])

with tab1:
    inflation = st.number_input("Inflation rate in precent :")
    if st.button("SUBMIT"):
        st.subheader('Financials')
        startyear = todays_date.year
        cur.execute("CREATE OR REPLACE VIEW tempview AS SELECT A.userid, A.years,A.yourage,A.spouseage,B.totalmothly+C.totalannual AS corelifestyleexpenses,D.lifeinsurance+D.reason1 AS annualnoncore FROM timetable A INNER JOIN outflowlifestylemonthly B ON A.userid = B.userid INNER JOIN outflowannualcorelife C ON B.userid = C.userid INNER JOIN outflowannualnoncorelife D ON C.userid = D.userid AND A.years = %s AND B.userid = %s",(startyear,userid))
        end = startyear + 50
        year =[]
        yourage = []
        spouseage = []
        corelifestyleexpenses =[]
        annualnoncore =[]
        cur.execute("SELECT yourage FROM tempview where userid = %s ",userid)
        youragen = cur.fetchone()
        youragen = int(youragen[0])
        cur.execute("SELECT spouseage FROM tempview where userid = %s ",userid)
        spouseagen = cur.fetchone()
        spouseagen = int(spouseagen[0])
        cur.execute("SELECT corelifestyleexpenses FROM tempview where userid = %s ",userid)
        corelifestyleexpensesn = cur.fetchone()  
        corelifestyleexpensesn = int(corelifestyleexpensesn[0])
        cur.execute("SELECT annualnoncore FROM tempview where userid = %s ",userid)
        annualnoncoren = cur.fetchone()
        annualnoncoren = int(annualnoncoren[0])
        for startyear in range(startyear,end):
            year.append(startyear)
            yourage.append(youragen) 
            spouseage.append(spouseagen)
            corelifestyleexpenses.append(corelifestyleexpensesn)
            annualnoncore.append(annualnoncoren)
            startyear = startyear +1 
            youragen = youragen +1
            spouseagen = spouseagen+1
            corelifestyleexpensesn = corelifestyleexpensesn+(corelifestyleexpensesn*(inflation/100))
            annualnoncoren = annualnoncoren+(annualnoncoren*(inflation/100))
        df = pd.DataFrame(
        {'Years': year,
        'Your Age': yourage,
        'Spouse Age': spouseage,
        'Core Life Expenses': corelifestyleexpenses,
        'Annual Non Core ':annualnoncore
        })
        st.dataframe(df,1000,1500)
        st.line_chart(df,x = 'Your Age',y= ['Core Life Expenses','Annual Non Core '])
        
        st.write("")
        st.subheader("Other ongoing need")
        startyear = todays_date.year
        cur.execute("CREATE OR REPLACE VIEW tempviewongoing AS SELECT OG.userid,tt.years AS Year,tt.yourage AS Yourage,tt.spouseage AS Spouseage,OG.amtemer AS EmergencyAmt, OG.amtcar AS CarAmt,OG.amtother AS OtherAmt,OG.amtfunc AS FunctionAmt,OG.amtelectronic AS ElectronicAmt,OG.amtvacations AS VacationAmt,OG.amtdonation AS DonationAmt FROM ongoingneeds OG INNER JOIN timetable TT ON OG.userid = TT.userid AND tt.years = %s AND OG.userid = %s",(startyear,userid))
        cur.execute("SELECT EmergencyAmt FROM tempviewongoing where userid = %s ",userid)
        EmergencyAmt = cur.fetchone()
        EmergencyAmt = int(EmergencyAmt[0])
        cur.execute("SELECT CarAmt FROM tempviewongoing where userid = %s ",userid)
        CarAmt = cur.fetchone()
        CarAmt = int(CarAmt[0])
        cur.execute("SELECT OtherAmt FROM tempviewongoing where userid = %s ",userid)
        OtherAmt = cur.fetchone()
        OtherAmt = int(OtherAmt[0])
        cur.execute("SELECT FunctionAmt FROM tempviewongoing where userid = %s ",userid)
        FunctionAmt = cur.fetchone()
        FunctionAmt = int(FunctionAmt[0])
        cur.execute("SELECT ElectronicAmt FROM tempviewongoing where userid = %s ",userid)
        ElectronicAmt = cur.fetchone()
        ElectronicAmt = int(ElectronicAmt[0])
        cur.execute("SELECT VacationAmt FROM tempviewongoing where userid = %s ",userid)
        VacationAmt = cur.fetchone()
        VacationAmt = int(VacationAmt[0])
        cur.execute("SELECT DonationAmt FROM tempviewongoing where userid = %s ",userid)
        DonationAmt = cur.fetchone()
        DonationAmt = int(DonationAmt[0])
        EmergencyAmtn= [] 
        CarAmtn= []
        OtherAmtn =[]
        FunctionAmtn=[]
        ElectronicAmtn=[]
        VacationAmtn=[]
        DonationAmtn=[]
        end = startyear + 50
        for startyear in range(startyear,end):
            EmergencyAmtn.append(EmergencyAmt)
            CarAmtn.append(CarAmt)
            OtherAmtn.append(OtherAmt)
            FunctionAmtn.append(FunctionAmt)
            ElectronicAmtn.append(ElectronicAmt)
            VacationAmtn.append(VacationAmt)
            DonationAmtn.append(DonationAmt)
            startyear = startyear +1 
            EmergencyAmt = EmergencyAmt+(EmergencyAmt*(inflation/100))
            CarAmt = CarAmt+(CarAmt*(inflation/100))
            OtherAmt = OtherAmt+(OtherAmt*(inflation/100))
            FunctionAmt = FunctionAmt+(FunctionAmt*(inflation/100))
            ElectronicAmt = ElectronicAmt+(ElectronicAmt*(inflation/100))
            VacationAmt = VacationAmt+(VacationAmt*(inflation/100))
            DonationAmt = DonationAmt+(DonationAmt*(inflation/100))
        dfongoingneeds = pd.DataFrame(
        {'Years': year,
        'Your Age': yourage,
        'Spouse Age': spouseage,
        'Emergency Amt' : EmergencyAmtn,
        'Car Amt' : CarAmtn,
        'Other Amt' : OtherAmtn,
        'Function Amt' : FunctionAmtn,
        'Electronic Amt' : ElectronicAmtn,
        'Vacation Amt' : VacationAmtn,
        'Donation Amt' : DonationAmtn
        })
        st.dataframe(dfongoingneeds,1000,1500)
        st.line_chart(dfongoingneeds,x = 'Your Age',y= ['Emergency Amt','Car Amt','Other Amt','Function Amt','Electronic Amt','Vacation Amt','Donation Amt'])

        st.write("")
        st.subheader("Long Term Needs")
        startyear = todays_date.year
        cur.execute("CREATE OR REPLACE VIEW tempviewlongterm AS SELECT bg.userid,tt.years,tt.yourage,tt.spouseage,bg.otheramt1,bg.otheramt2,bg.amtmar,bg.amtff,bg.amtreno,bg.amtcar FROM biggoals bg  INNER JOIN timetable TT ON bg.userid = TT.userid AND tt.years = %s  AND tt.userid = %s",(startyear,userid))
        cur.execute("SELECT otheramt1 FROM tempviewlongterm where userid = %s ",userid)
        otheramt1 = cur.fetchone()
        otheramt1 = int(otheramt1[0])
        cur.execute("SELECT otheramt2 FROM tempviewlongterm where userid = %s ",userid)
        otheramt2 = cur.fetchone()
        otheramt2 = int(otheramt2[0])
        cur.execute("SELECT amtmar FROM tempviewlongterm where userid = %s ",userid)
        amtmar = cur.fetchone()
        amtmar = int(amtmar[0])
        cur.execute("SELECT amtff FROM tempviewlongterm where userid = %s ",userid)
        amtff = cur.fetchone()
        amtff = int(amtff[0])
        cur.execute("SELECT amtreno FROM tempviewlongterm where userid = %s ",userid)
        amtreno = cur.fetchone()
        amtreno = int(amtreno[0])
        cur.execute("SELECT amtcar FROM tempviewlongterm where userid = %s ",userid)
        amtcar = cur.fetchone()
        amtcar = int(amtcar[0])
        otheramt1n = []
        otheramt2n =[]
        amtmarn =[]
        amtffn = []
        amtrenon = []
        amtcarn =[]
        end = startyear + 50
        for startyear in range(startyear,end):
            otheramt1n.append(otheramt1)
            otheramt2n.append(otheramt2)
            amtmarn.append(amtmar)
            amtffn.append(amtff)
            amtrenon.append(amtreno)
            amtcarn.append(amtcar)
            startyear = startyear +1 
            otheramt1 = otheramt1+(otheramt1*(inflation/100))
            otheramt2 = otheramt2+(otheramt2*(inflation/100))
            amtmar = amtmar+(amtmar*(inflation/100))
            amtff = amtff+(amtff*(inflation/100))
            amtcar = amtcar+(amtcar*(inflation/100))
            amtreno = amtreno+(amtreno*(inflation/100))
        dflongterm = pd.DataFrame(
        {'Years': year,
        'Your Age': yourage,
        'Spouse Age': spouseage,
        'Other Expenses 1' : otheramt1n,
        'Other Expenses 2': otheramt2n,
        'Amount of Car upgrad' : amtcarn,
        'Amount of Children Marriage': amtmarn,
        'Amount for Home Renovation':amtrenon,
        'Amount neede for Financial Freedom':amtffn
        })
        st.dataframe(dflongterm,1000,1500)
        st.line_chart(dflongterm,x = 'Your Age',y= ['Other Expenses 1','Other Expenses 2','Amount of Car upgrad','Amount of Children Marriage','Amount for Home Renovation','Amount neede for Financial Freedom'])
        

        st.subheader('Total Expenses')
        dftotal = pd.DataFrame(
        {'Years': year,
        'Your Age': yourage,
        'Spouse Age': spouseage,
        'Total Expenses': df['Core Life Expenses']+ df['Annual Non Core '] + dfongoingneeds['Emergency Amt']+ dfongoingneeds['Car Amt']+
        dfongoingneeds['Other Amt']+ dfongoingneeds['Function Amt']+ dfongoingneeds['Electronic Amt']+ dfongoingneeds['Vacation Amt']+ dfongoingneeds['Donation Amt']+
        dflongterm['Other Expenses 1']+dflongterm['Other Expenses 2']+dflongterm['Amount of Car upgrad']+dflongterm['Amount of Children Marriage']+
        dflongterm['Amount for Home Renovation']+dflongterm['Amount neede for Financial Freedom']
        })
        st.dataframe(dftotal,1000,1500)
        st.line_chart(dftotal,x = 'Your Age',y= ['Total Expenses'])

with tab2:
    insal1 = st.number_input("Enter the percentage increase in Salary 1: ")
    insal2 = st.number_input("Enter the percentage increase in Salary 2: ")
    otsal = st.number_input("Enter the percentage increase in Other Income source: ")
    if st.button("Submit"):
        cur.execute("SELECT (usersalary+annualbonus1/12+salary1pf+emp1pf+npssal1) FROM income where userid = %s",userid)
        incsal1 = cur.fetchone()
        if incsal1[0] == 'None':
            incsal1 = 0;
        else : 
            incsal1 = incsal1[0]
        cur.execute("SELECT (spousesalary+annualbonus2/12+salary2pf+emp2pf+npssal2) FROM income where userid = %s ",userid)    
        incsal2 = cur.fetchone()
        incsal2 = incsal2[0]
        if incsal2 == None:
            incsal2 = 0;
        else : 
            incsal2 = incsal2[0]
        cur.execute("SELECT (otherincome) FROM income where userid = %s ",userid)
        othersal = cur.fetchone()
        if othersal[0] == 'None':
            othersal = 0;
        else : 
            othersal = othersal[0]
        cur.execute("SELECT yourage FROM tempview where userid = %s ",userid)
        youragen = cur.fetchone()
        youragen = int(youragen[0])
        cur.execute("SELECT spouseage FROM tempview where userid = %s ",userid)
        spouseagen = cur.fetchone()
        spouseagen = int(spouseagen[0])
        year =[]
        spouseage =[]
        yourage = []
        incsal1n =[]
        incsal2n =[]
        othersaln =[]
        startyear = todays_date.year
        end = startyear + 50
        for startyear in range(startyear,end):
            year.append(startyear)
            yourage.append(youragen) 
            spouseage.append(spouseagen)
            incsal1n.append(incsal1)
            incsal2n.append(incsal2)
            othersaln.append(othersal)
            startyear = startyear +1 
            youragen = youragen +1
            spouseagen = spouseagen+1
            incsal1 = incsal1+(incsal1*(insal1/100))
            incsal2 = incsal2+(incsal2*(insal2/100))
            othersal = othersal+(othersal*(otsal/100))
        dfincomesub = pd.DataFrame(
            {'Years': year,
            'Your Age': yourage,
            'Spouse Age': spouseage,
            'Salary 1' : incsal1n,
            'Salary 2' : incsal2n,
            'Other Income' : othersaln})
        dfincometotal = pd.DataFrame(
            {'Total Income' : dfincomesub['Salary 1']+dfincomesub['Salary 2']+dfincomesub['Other Income']
            }
        )
        dfincome = pd.DataFrame(
            {'Years': year,
            'Your Age': yourage,
            'Spouse Age': spouseage,
            'Salary 1' : incsal1n,
            'Salary 2' : incsal2n,
            'Other Income' : othersaln,
            'Total Income' : dfincometotal['Total Income']
            }
        )
        st.dataframe(dfincome,1000,1500)
        st.line_chart(dfincome,x = 'Your Age',y= ['Salary 1','Salary 2','Other Income'])

with tab3:
    inflation = st.number_input("Inflation Rate in precent :")
    insal1 = st.number_input("Enter the percentage Increase in Salary 1: ")
    insal2 = st.number_input("Enter the percentage Increase in Salary 2: ")
    otsal = st.number_input("Enter the percentage Increase in Other Income source: ")
    roinc = st.number_input("Enter the expected after tax return when inflation is as given above:")
    if st.button("SUbmit"):
        startyear = todays_date.year
        cur.execute("CREATE OR REPLACE VIEW tempview AS SELECT A.userid, A.years,A.yourage,A.spouseage,B.totalmothly+C.totalannual AS corelifestyleexpenses,D.lifeinsurance+D.reason1 AS annualnoncore FROM timetable A INNER JOIN outflowlifestylemonthly B ON A.userid = B.userid INNER JOIN outflowannualcorelife C ON B.userid = C.userid INNER JOIN outflowannualnoncorelife D ON C.userid = D.userid AND A.years = %s AND B.userid = %s",(startyear,userid))
        end = startyear + 50
        year =[]
        yourage = []
        spouseage = []
        corelifestyleexpenses =[]
        annualnoncore =[]
        cur.execute("SELECT yourage FROM tempview where userid = %s ",userid)
        youragen = cur.fetchone()
        youragen = int(youragen[0])
        cur.execute("SELECT spouseage FROM tempview where userid = %s ",userid)
        spouseagen = cur.fetchone()
        spouseagen = int(spouseagen[0])
        cur.execute("SELECT corelifestyleexpenses FROM tempview where userid = %s ",userid)
        corelifestyleexpensesn = cur.fetchone()  
        corelifestyleexpensesn = int(corelifestyleexpensesn[0])
        cur.execute("SELECT annualnoncore FROM tempview where userid = %s ",userid)
        annualnoncoren = cur.fetchone()
        annualnoncoren = int(annualnoncoren[0])
        for startyear in range(startyear,end):
            year.append(startyear)
            yourage.append(youragen) 
            spouseage.append(spouseagen)
            corelifestyleexpenses.append(corelifestyleexpensesn)
            annualnoncore.append(annualnoncoren)
            startyear = startyear +1 
            youragen = youragen +1
            spouseagen = spouseagen+1
            corelifestyleexpensesn = corelifestyleexpensesn+(corelifestyleexpensesn*(inflation/100))
            annualnoncoren = annualnoncoren+(annualnoncoren*(inflation/100))
        df = pd.DataFrame(
        {'Years': year,
        'Your Age': yourage,
        'Spouse Age': spouseage,
        'Core Life Expenses': corelifestyleexpenses,
        'Annual Non Core ':annualnoncore
        })

        startyear = todays_date.year
        cur.execute("CREATE OR REPLACE VIEW tempviewongoing AS SELECT OG.userid,tt.years AS Year,tt.yourage AS Yourage,tt.spouseage AS Spouseage,OG.amtemer AS EmergencyAmt, OG.amtcar AS CarAmt,OG.amtother AS OtherAmt,OG.amtfunc AS FunctionAmt,OG.amtelectronic AS ElectronicAmt,OG.amtvacations AS VacationAmt,OG.amtdonation AS DonationAmt FROM ongoingneeds OG INNER JOIN timetable TT ON OG.userid = TT.userid AND tt.years = %s AND OG.userid = %s",(startyear,userid))
        cur.execute("SELECT EmergencyAmt FROM tempviewongoing where userid = %s ",userid)
        EmergencyAmt = cur.fetchone()
        EmergencyAmt = int(EmergencyAmt[0])
        cur.execute("SELECT CarAmt FROM tempviewongoing where userid = %s ",userid)
        CarAmt = cur.fetchone()
        CarAmt = int(CarAmt[0])
        cur.execute("SELECT OtherAmt FROM tempviewongoing where userid = %s ",userid)
        OtherAmt = cur.fetchone()
        OtherAmt = int(OtherAmt[0])
        cur.execute("SELECT FunctionAmt FROM tempviewongoing where userid = %s ",userid)
        FunctionAmt = cur.fetchone()
        FunctionAmt = int(FunctionAmt[0])
        cur.execute("SELECT ElectronicAmt FROM tempviewongoing where userid = %s ",userid)
        ElectronicAmt = cur.fetchone()
        ElectronicAmt = int(ElectronicAmt[0])
        cur.execute("SELECT VacationAmt FROM tempviewongoing where userid = %s ",userid)
        VacationAmt = cur.fetchone()
        VacationAmt = int(VacationAmt[0])
        cur.execute("SELECT DonationAmt FROM tempviewongoing where userid = %s ",userid)
        DonationAmt = cur.fetchone()
        DonationAmt = int(DonationAmt[0])
        EmergencyAmtn= [] 
        CarAmtn= []
        OtherAmtn =[]
        FunctionAmtn=[]
        ElectronicAmtn=[]
        VacationAmtn=[]
        DonationAmtn=[]
        end = startyear + 50
        for startyear in range(startyear,end):
            EmergencyAmtn.append(EmergencyAmt)
            CarAmtn.append(CarAmt)
            OtherAmtn.append(OtherAmt)
            FunctionAmtn.append(FunctionAmt)
            ElectronicAmtn.append(ElectronicAmt)
            VacationAmtn.append(VacationAmt)
            DonationAmtn.append(DonationAmt)
            startyear = startyear +1 
            EmergencyAmt = EmergencyAmt+(EmergencyAmt*(inflation/100))
            CarAmt = CarAmt+(CarAmt*(inflation/100))
            OtherAmt = OtherAmt+(OtherAmt*(inflation/100))
            FunctionAmt = FunctionAmt+(FunctionAmt*(inflation/100))
            ElectronicAmt = ElectronicAmt+(ElectronicAmt*(inflation/100))
            VacationAmt = VacationAmt+(VacationAmt*(inflation/100))
            DonationAmt = DonationAmt+(DonationAmt*(inflation/100))
        dfongoingneeds = pd.DataFrame(
        {'Years': year,
        'Your Age': yourage,
        'Spouse Age': spouseage,
        'Emergency Amt' : EmergencyAmtn,
        'Car Amt' : CarAmtn,
        'Other Amt' : OtherAmtn,
        'Function Amt' : FunctionAmtn,
        'Electronic Amt' : ElectronicAmtn,
        'Vacation Amt' : VacationAmtn,
        'Donation Amt' : DonationAmtn
        })

        startyear = todays_date.year
        cur.execute("CREATE OR REPLACE VIEW tempviewlongterm AS SELECT bg.userid,tt.years,tt.yourage,tt.spouseage,bg.otheramt1,bg.otheramt2,bg.amtmar,bg.amtff,bg.amtreno,bg.amtcar FROM biggoals bg  INNER JOIN timetable TT ON bg.userid = TT.userid AND tt.years = %s  AND tt.userid = %s",(startyear,userid))
        cur.execute("SELECT otheramt1 FROM tempviewlongterm where userid = %s ",userid)
        otheramt1 = cur.fetchone()
        otheramt1 = int(otheramt1[0])
        cur.execute("SELECT otheramt2 FROM tempviewlongterm where userid = %s ",userid)
        otheramt2 = cur.fetchone()
        otheramt2 = int(otheramt2[0])
        cur.execute("SELECT amtmar FROM tempviewlongterm where userid = %s ",userid)
        amtmar = cur.fetchone()
        amtmar = int(amtmar[0])
        cur.execute("SELECT amtff FROM tempviewlongterm where userid = %s ",userid)
        amtff = cur.fetchone()
        amtff = int(amtff[0])
        cur.execute("SELECT amtreno FROM tempviewlongterm where userid = %s ",userid)
        amtreno = cur.fetchone()
        amtreno = int(amtreno[0])
        cur.execute("SELECT amtcar FROM tempviewlongterm where userid = %s ",userid)
        amtcar = cur.fetchone()
        amtcar = int(amtcar[0])
        otheramt1n = []
        otheramt2n =[]
        amtmarn =[]
        amtffn = []
        amtrenon = []
        amtcarn =[]
        end = startyear + 50
        for startyear in range(startyear,end):
            otheramt1n.append(otheramt1)
            otheramt2n.append(otheramt2)
            amtmarn.append(amtmar)
            amtffn.append(amtff)
            amtrenon.append(amtreno)
            amtcarn.append(amtcar)
            startyear = startyear +1 
            otheramt1 = otheramt1+(otheramt1*(inflation/100))
            otheramt2 = otheramt2+(otheramt2*(inflation/100))
            amtmar = amtmar+(amtmar*(inflation/100))
            amtff = amtff+(amtff*(inflation/100))
            amtcar = amtcar+(amtcar*(inflation/100))
            amtreno = amtreno+(amtreno*(inflation/100))
        dflongterm = pd.DataFrame(
        {'Years': year,
        'Your Age': yourage,
        'Spouse Age': spouseage,
        'Other Expenses 1' : otheramt1n,
        'Other Expenses 2': otheramt2n,
        'Amount of Car upgrad' : amtcarn,
        'Amount of Children Marriage': amtmarn,
        'Amount for Home Renovation':amtrenon,
        'Amount neede for Financial Freedom':amtffn
        })

        dftotal = pd.DataFrame(
        {'Years': year,
        'Your Age': yourage,
        'Spouse Age': spouseage,
        'Total Expenses': df['Core Life Expenses']+ df['Annual Non Core '] + dfongoingneeds['Emergency Amt']+ dfongoingneeds['Car Amt']+
        dfongoingneeds['Other Amt']+ dfongoingneeds['Function Amt']+ dfongoingneeds['Electronic Amt']+ dfongoingneeds['Vacation Amt']+ dfongoingneeds['Donation Amt']+
        dflongterm['Other Expenses 1']+dflongterm['Other Expenses 2']+dflongterm['Amount of Car upgrad']+dflongterm['Amount of Children Marriage']+
        dflongterm['Amount for Home Renovation']+dflongterm['Amount neede for Financial Freedom']
        })
        cur.execute("SELECT (usersalary+annualbonus1/12+salary1pf+emp1pf+npssal1) FROM income where userid = %s",userid)
        incsal1 = cur.fetchone()
        if incsal1[0] == 'None':
            incsal1 = 0;
        else : 
            incsal1 = incsal1[0]
        cur.execute("SELECT (spousesalary+annualbonus2/12+salary2pf+emp2pf+npssal2) FROM income where userid = %s ",userid)    
        incsal2 = cur.fetchone()
        incsal2 = incsal2[0]
        if incsal2 == None:
            incsal2 = 0;
        else : 
            incsal2 = incsal2[0]
        cur.execute("SELECT (otherincome) FROM income where userid = %s ",userid)
        othersal = cur.fetchone()
        if othersal[0] == 'None':
            othersal = 0;
        else : 
            othersal = othersal[0]
        cur.execute("SELECT yourage FROM tempview where userid = %s ",userid)
        youragen = cur.fetchone()
        youragen = int(youragen[0])
        cur.execute("SELECT spouseage FROM tempview where userid = %s ",userid)
        spouseagen = cur.fetchone()
        spouseagen = int(spouseagen[0])
        year =[]
        spouseage =[]
        yourage = []
        incsal1n =[]
        incsal2n =[]
        othersaln =[]
        startyear = todays_date.year
        end = startyear + 50
        for startyear in range(startyear,end):
            year.append(startyear)
            yourage.append(youragen) 
            spouseage.append(spouseagen)
            incsal1n.append(incsal1)
            incsal2n.append(incsal2)
            othersaln.append(othersal)
            startyear = startyear +1 
            youragen = youragen +1
            spouseagen = spouseagen+1
            incsal1 = incsal1+(incsal1*(insal1/100))
            incsal2 = incsal2+(incsal2*(insal2/100))
            othersal = othersal+(othersal*(otsal/100))
        dfincomesub = pd.DataFrame(
            {'Years': year,
            'Your Age': yourage,
            'Spouse Age': spouseage,
            'Salary 1' : incsal1n,
            'Salary 2' : incsal2n,
            'Other Income' : othersaln})
        dfincometotal = pd.DataFrame(
            {'Total Income' : dfincomesub['Salary 1']+dfincomesub['Salary 2']+dfincomesub['Other Income']
            }
        )
        dfincome = pd.DataFrame(
            {'Years': year,
            'Your Age': yourage,
            'Spouse Age': spouseage,
            'Salary 1' : incsal1n,
            'Salary 2' : incsal2n,
            'Other Income' : othersaln,
            'Total Income' : dfincometotal['Total Income']
            }
        )
        dffinancial = pd.DataFrame(
            {'Years': year,
            'Your Age': yourage,
            'Spouse Age': spouseage,
            'Total Expenses': dftotal['Total Expenses'],
            'Total Income' : dfincometotal['Total Income'],
            'Monthly Difference' : dfincometotal['Total Income']-dftotal['Total Expenses'],
            'Annual Difference':(-(dfincometotal['Total Income']-dftotal['Total Expenses']))*12
            }
        )

        cur.execute("SELECT amtmar FROM biggoals where userid =%s",userid)
        maramt= cur.fetchone()
        maramt= maramt[0]
        currentyear = date.today().year
        cur.execute("SELECT yrmar FROM biggoals where userid =%s",userid)
        maryear= cur.fetchone()
        maryear = maryear[0]
        noofyears = maryear - currentyear
        fundneed = maramt *((1+inflation/100) **noofyears )
        fundneed = int(fundneed)
        cur.execute("SELECT amtreno FROM biggoals where userid =%s",userid)
        amtreno= cur.fetchone()
        amtreno= amtreno[0]
        cur.execute("SELECT yrreno FROM biggoals where userid =%s",userid)
        yrreno= cur.fetchone()
        yrreno = yrreno[0]
        noofyearsreno = yrreno - currentyear
        fundneedreno = amtreno *((1+inflation/100)**noofyearsreno)
        fundneedreno = int(fundneedreno)
        cur.execute("SELECT amtff FROM biggoals where userid =%s",userid)
        amtff= cur.fetchone()
        amtff= amtff[0]
        cur.execute("SELECT yrff FROM biggoals where userid =%s",userid)
        yrff= cur.fetchone()
        yrff = yrff[0]
        noofyearsff = yrff - currentyear
        fundneedff = amtff *((1+inflation/100)**noofyearsff )
        fundneedff = int(fundneedff)
        cur.execute("SELECT amtcar FROM biggoals where userid =%s",userid)
        amtcar= cur.fetchone()
        amtcar= amtcar[0]
        cur.execute("SELECT yrnexcar  FROM biggoals where userid =%s",userid)
        yrnexcar = cur.fetchone()
        yrnexcar  = yrnexcar [0]
        noofyearscar = yrnexcar  - currentyear
        fundneedcar = amtcar *((1+inflation/100)**noofyearscar )
        fundneedcar = int(fundneedcar)
        funtotal = fundneed+fundneedreno+fundneedff+fundneedcar
        startyear = todays_date.year
        end = startyear + 50
        appreturn = []
        appcb =[]
        cur.execute("SELECT balanceleft FROM investments where userid = %s",userid)
        bb= cur.fetchone()
        bb=bb[0]
        if bb<=0:
            appreturnvalue = 0
        else:
            appreturnvalue = bb- dffinancial.iloc[0]['Annual Difference']
        for startyear in range(startyear,end):
            appreturn.append(appreturnvalue)
            if appreturnvalue <=0:
                appreturnvalue = 0
            else:
                i=1
                appreturnvalue= (appreturnvalue - dffinancial.iloc[i]['Annual Difference'])*(roinc/100)
                i=i+1
            startyear = startyear+1

        dfpassiveinc = pd.DataFrame(
            {'Years': year,
            'Your Age': yourage,
            'Spouse Age': spouseage,
            'Annual Difference':(-(dfincometotal['Total Income']-dftotal['Total Expenses']))*(12),
            'App Interest/Return': appreturn
            }
        )
        eoy =[]
        calculation= bb+dfpassiveinc.iloc[0]['App Interest/Return']- dffinancial.iloc[0]['Annual Difference']
        startyear = todays_date.year
        end = startyear + 50
        for startyear in range(startyear,end):
            eoy.append(calculation)
            i=1
            calculation = calculation + dfpassiveinc.iloc[i]['App Interest/Return']- dffinancial.iloc[i]['Annual Difference']
            i =i +1
            startyear = startyear+1

        dfpassiveincfinal = pd.DataFrame(
            {'Years': year,
            'Your Age': yourage,
            'Spouse Age': spouseage,
            'Annual Difference':(dfincometotal['Total Income']-dftotal['Total Expenses'])*(12),
            'App Interest/Return': appreturn,
            'Annual Income Needed': (-(dfincometotal['Total Income']-dftotal['Total Expenses']))*(12),
            'Approx corpus balance (EOY)':eoy
            }
        )
        dfgraph = pd.DataFrame(
            {
            'Your Age': yourage,
            'Approx corpus balance (EOY)':eoy
            }
        )


        tab11, tab22, tab33 = st.tabs(["Monthly", "Annual","Passive Income"])
        with tab11:
            st.line_chart(dffinancial,x = 'Your Age',y= ['Total Expenses','Total Income','Monthly Difference'])
            st.dataframe(dffinancial,1000,1500)
        with tab22:
            st.line_chart(dffinancial,x = 'Your Age',y= ['Total Expenses','Total Income','Annual Difference'])
            st.dataframe(dffinancial,1000,1500)
        with tab33:
            st.line_chart(dfpassiveincfinal,x = 'Your Age',y= ['Annual Difference','Approx corpus balance (EOY)'])
            st.dataframe(dfpassiveincfinal,1000,1500)
            st.area_chart(dfgraph)
