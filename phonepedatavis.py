#Libaries Used
import os
import json
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import create_engine
import pandas as pd
import json
from streamlit_option_menu import option_menu
import streamlit as st
import pymysql
import sqlalchemy
import plotly.express as px
import plotly.graph_objects as go

#Aggregate Transaction Details
path="D:/Data Science/PhonePe/pulse/data/aggregated/transaction/country/india/state/"
agg_trans_list=os.listdir(path)

agg_trans={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in agg_trans_list:
    path_i=path+i+"/"
    Agg_yr=os.listdir(path_i)

    for j in Agg_yr:
        path_j=path_i+j+"/"
        Agg_yr_list=os.listdir(path_j)

        for k in Agg_yr_list:
            path_k=path_j+k
            Data=open(path_k,'r')
            Data1=json.load(Data)
            
            for z in Data1['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              agg_trans['Transaction_type'].append(Name)
              agg_trans['Transaction_count'].append(count)
              agg_trans['Transaction_amount'].append(amount)
              agg_trans['State'].append(i)
              agg_trans['Year'].append(j)
              agg_trans['Quarter'].append(int(k.strip('.json')))

#Converting to dataframe and cleaning
agg_trans_data=pd.DataFrame(agg_trans)
agg_trans_data["State"]=agg_trans_data["State"].str.replace('-',' ')
agg_trans_data["State"]=agg_trans_data["State"].str.title()
agg_trans_data['State']=agg_trans_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
agg_trans_data['State']=agg_trans_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#Aggregate User Details
path2="D:/Data Science/PhonePe/pulse/data/aggregated/user/country/india/state/"
agg_user_list=os.listdir(path)

agg_user={'State':[], 'Year':[],'Quarter':[],'User_Brands':[], 'User_count':[], 'User_Percentage':[]}

for i in agg_user_list:
    path_i=path2+i+"/"
    Agg_yr=os.listdir(path_i)

    for j in Agg_yr:
        path_j=path_i+j+"/"
        Agg_yr_list=os.listdir(path_j)

        for k in Agg_yr_list:
            path_k=path_j+k
            Data=open(path_k,'r')
            Data2=json.load(Data)
            
            try:
                for z in Data2["data"]["usersByDevice"]:
                    brand=z["brand"]
                    count=z["count"]
                    percentage=z["percentage"]
                    agg_user['User_Brands'].append(brand)
                    agg_user['User_count'].append(count)
                    agg_user['User_Percentage'].append(percentage)
                    agg_user['State'].append(i)
                    agg_user['Year'].append(j)
                    agg_user['Quarter'].append(int(k.strip('.json')))
            except:
                pass

#Converting to dataframe and cleaning
agg_user_data=pd.DataFrame(agg_user)
agg_user_data["State"]=agg_user_data["State"].str.replace('-',' ')
agg_user_data["State"]=agg_user_data["State"].str.title()
agg_user_data['State']=agg_user_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
agg_user_data['State']=agg_user_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#Map Transaction Details
path3="D:/Data Science/PhonePe/pulse/data/map/transaction/hover/country/india/state/"
map_trans_list=os.listdir(path)

map_trans={'State':[], 'Year':[],'Quarter':[],'District':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in map_trans_list:
    path_i=path3+i+"/"
    Agg_yr=os.listdir(path_i)

    for j in Agg_yr:
        path_j=path_i+j+"/"
        Agg_yr_list=os.listdir(path_j)

        for k in Agg_yr_list:
            path_k=path_j+k
            Data=open(path_k,'r')
            Data3=json.load(Data)

            for z in Data3["data"]["hoverDataList"]:
                    name=z["name"]
                    count=z["metric"][0]["count"]
                    amount=z["metric"][0]["amount"]
                    map_trans['District'].append(name)
                    map_trans['Transaction_count'].append(count)
                    map_trans['Transaction_amount'].append(amount)
                    map_trans['State'].append(i)
                    map_trans['Year'].append(j)
                    map_trans['Quarter'].append(int(k.strip('.json')))

#Converting to dataframe and cleaning
map_trans_data=pd.DataFrame(map_trans)
map_trans_data["State"]=map_trans_data["State"].str.replace('-',' ')
map_trans_data["State"]=map_trans_data["State"].str.title()
map_trans_data["District"]=map_trans_data["District"].str.title()
map_trans_data['State']=map_trans_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
map_trans_data['State']=map_trans_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#Map User Details
path4='D:/Data Science/PhonePe/pulse/data/map/user/hover/country/india/state/'
map_user_list=os.listdir(path)

map_user={'State':[], 'Year':[],'Quarter':[],'District':[], 'Registered_Users':[], 'App_Opens':[]}

for i in map_user_list:
    path_i=path4+i+"/"
    Agg_yr=os.listdir(path_i)

    for j in Agg_yr:
        path_j=path_i+j+"/"
        Agg_yr_list=os.listdir(path_j)

        for k in Agg_yr_list:
            path_k=path_j+k
            Data=open(path_k,'r')
            Data4=json.load(Data)
            
            for z in Data4["data"]["hoverData"].items():
                district=z[0]
                registeredUsers=z[1]["registeredUsers"]
                appOpens=z[1]["appOpens"]
                map_user['District'].append(district)
                map_user['Registered_Users'].append(registeredUsers)
                map_user['App_Opens'].append(appOpens)
                map_user['State'].append(i)
                map_user['Year'].append(j)
                map_user['Quarter'].append(int(k.strip('.json')))

#Converting to dataframe and cleaning
map_user_data=pd.DataFrame(map_user)
map_user_data["State"]=map_user_data["State"].str.replace('-',' ')
map_user_data["State"]=map_user_data["State"].str.title()
map_user_data['State']=map_user_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
map_user_data['State']=map_user_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#Top Transaction Details
path5="D:/Data Science/PhonePe/pulse/data/top/transaction/country/india/state/"
top_trans_list=os.listdir(path)

top_trans={'State':[], 'Year':[],'Quarter':[],'Pincodes':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in top_trans_list:
    path_i=path5+i+"/"
    Agg_yr=os.listdir(path_i)

    for j in Agg_yr:
        path_j=path_i+j+"/"
        Agg_yr_list=os.listdir(path_j)

        for k in Agg_yr_list:
            path_k=path_j+k
            Data=open(path_k,'r')
            Data5=json.load(Data)

            for z in Data5["data"]["pincodes"]:
                entityName=z["entityName"]
                count=z["metric"]["count"]
                amount=z["metric"]["amount"]
                top_trans['Pincodes'].append(entityName)
                top_trans['Transaction_count'].append(count)
                top_trans['Transaction_amount'].append(amount)
                top_trans['State'].append(i)
                top_trans['Year'].append(j)
                top_trans['Quarter'].append(int(k.strip('.json')))

#Converting to dataframe and cleaning
top_trans_data=pd.DataFrame(top_trans)
top_trans_data["State"]=top_trans_data["State"].str.replace('-',' ')
top_trans_data["State"]=top_trans_data["State"].str.title()
top_trans_data['State']=top_trans_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
top_trans_data['State']=top_trans_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#Top User Details
path6="D:/Data Science/PhonePe/pulse/data/top/user/country/india/state/"
top_user_list=os.listdir(path)

top_user={'State':[], 'Year':[],'Quarter':[],'Pincodes':[],'Registered_Users':[]}

for i in top_user_list:
    path_i=path6+i+"/"
    Agg_yr=os.listdir(path_i)

    for j in Agg_yr:
        path_j=path_i+j+"/"
        Agg_yr_list=os.listdir(path_j)

        for k in Agg_yr_list:
            path_k=path_j+k
            Data=open(path_k,'r')
            Data6=json.load(Data)

            for z in Data6["data"]["pincodes"]:
                pincode=z["name"]
                registeredUsers=z["registeredUsers"]
                top_user['Pincodes'].append(pincode)
                top_user['Registered_Users'].append(registeredUsers)
                top_user['State'].append(i)
                top_user['Year'].append(j)
                top_user['Quarter'].append(int(k.strip('.json')))

#Converting to dataframe and cleaning
top_user_data=pd.DataFrame(top_user)
top_user_data["State"]=top_user_data["State"].str.replace('-',' ')
top_user_data["State"]=top_user_data["State"].str.title()
top_user_data['State']=top_user_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
top_user_data['State']=top_user_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#MySQL connection
my_connection = pymysql.connect(host="localhost",user="root",password="051092")
mycursor = my_connection.cursor()
engine = create_engine("mysql+pymysql://root:051092@localhost/phonepe")

mycursor.execute('create database if not exists phonepe')
mycursor.execute('use phonepe')

# Tables Creation:
mycursor.execute('''create table if not exists aggregate_transaction(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    Transaction_type VARCHAR(500),Transaction_count BIGINT,
                                    Transaction_amount FLOAT)''')

mycursor.execute('''create table if not exists aggregate_user(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    User_Brands VARCHAR(500),User_count BIGINT,
                                    User_Percentage FLOAT)''')

mycursor.execute('''create table if not exists map_transaction(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    District VARCHAR(500),Transaction_count BIGINT,
                                    Transaction_amount FLOAT)''')

mycursor.execute('''create table if not exists map_user(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    District VARCHAR(500),Registered_Users BIGINT,
                                    App_Opens BIGINT)''')

mycursor.execute('''create table if not exists top_transaction(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    Pincodes INT,Transaction_count BIGINT,
                                    Transaction_amount FLOAT)''')

mycursor.execute('''create table if not exists top_user(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    Pincodes INT,Registered_Users BIGINT)''')
#Insert dataframe to sql table
agg_trans_data.to_sql('aggregate_transaction',engine,if_exists='append',index=False)
agg_user_data.to_sql('aggregate_user',engine,if_exists='append',index=False)
map_trans_data.to_sql('map_transaction',engine,if_exists='append',index=False)
map_user_data.to_sql('map_user',engine,if_exists='append',index=False)
top_trans_data.to_sql('top_transaction',engine,if_exists='append',index=False)
top_user_data.to_sql('top_user',engine,if_exists='append',index=False)

my_connection.commit()

#Streamlit Page Creation
st.set_page_config(page_title='Phonepe Pulse Data Visualization and Exploration',
                layout='wide',initial_sidebar_state='expanded')
st.title('#9c2cb1[&emsp;&emsp;&emsp;:bar_chart:**Phonepe Pulse Data Visualization and Exploration**	:bar_chart:]')
st.subheader(':red[Domain :] :blue[Fintech]')
with st.sidebar:
    st.sidebar.image("D:/Data Science/Peimage.jpeg", use_column_width=True)
    st.title(':orange[Project Overview]')
    st.markdown('''The PhonePe Pulse Data Visualization project entails cloning data from a GitHub repository and utilizing it for visualization to improve user comprehension. 
                The data is fetched using the os library and stored in a :red[MySQL] database through :red[PyMySQL].
The project includes creating a dynamic :red[geo map], analyzing the data, and providing :red[visualizations] based on user-selected options.''')
    st.subheader(':orange[Skill Take Away :]')
    st.markdown(''' Github Cloning, Python, Pandas, MySQL,Streamlit, and Plotly''')
    
# Creating connection with mysql workbench
my_connection = pymysql.connect(host="localhost",user="root",password="051092")
mycursor = my_connection.cursor()
engine = create_engine("mysql+pymysql://root:051092@localhost/phonepe")

#Option menu
selected =option_menu(menu_title=None,
                   options=['Home','Charts','Visualization'],
                   icons=['geo-alt','table','file-bar-graph'],
                   orientation='horizontal',
                   menu_icon="cast",
                   default_index=0,)

if selected =='Home':
    col1,col2=st.columns(2)
    with col1:
        type = st.selectbox('',options=['Transactions','Users'],label_visibility='collapsed',
                                          placeholder='Select Transactions or Users',)
    with col2:
        year = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023, 2024], label_visibility='collapsed',
                                placeholder='Select a Year to view',)
# Geo-grapical view for transactions 
    if type == 'Transactions' and year:
        map_query= f'''SELECT State,SUM(Transaction_count) AS Transactions,SUM(Transaction_amount) AS TotalAmount from phonepe.map_transaction
        where Year={year}
        GROUP BY State;'''
        df = pd.read_sql_query(map_query,my_connection)
        fig = px.choropleth(
                            df,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color="Transactions",
                            title=f'PhonePe Transactions - {year}',
                            color_continuous_scale='Rainbow',
                            width=900, height=800, 
                            hover_name='State')
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)
      
# Bar Chart for Top payment type
        st.markdown("## :violet[Top Payment Type]")
        col1,col2= st.columns(2)
        with col1:
            pay_year = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023, 2024], placeholder='Year',
                                label_visibility='collapsed', key='pay_year')
        with col2:
            pay_quarter = st.selectbox('', options=[1, 2, 3, 4], placeholder='Quarter', label_visibility='collapsed',key='pay_quarter')

        payment_type=f'''select Transaction_type, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from phonepe.aggregate_transaction 
        where Year= {pay_year} and Quarter = {pay_quarter} group by Transaction_type order by Transaction_type;'''
        top_payment= pd.read_sql_query(payment_type, my_connection)
        fig = px.bar(top_payment,
                     title='Transaction Types vs Total_Transactions',
                     x="Transaction_type",
                     y="Total_Transactions",
                     orientation='v',
                     color='Total_amount',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=False)
      
# Bar chart for Total transactions - State wise
        st.markdown('### :violet[Select options to explore State-wise trends]')
        col1,col2,col3 =st.columns(3)
        with col1:
            state = st.selectbox('',options=['Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                    'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                    'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
                                    'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                    'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                    'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                    'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                    'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                    'Uttarakhand', 'West Bengal'],placeholder='State',
                                label_visibility='collapsed')
        with col2:
            year = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023, 2024], placeholder='Year',
                                label_visibility='collapsed')
        with col3:
            quarter = st.selectbox('', options=[1, 2, 3, 4], placeholder='Quarter', label_visibility='collapsed')
            
        
        trans_state=f'''select State,Year,Quarter,District,sum(Transaction_count) as Total_count, sum(Transaction_amount) as Total_amount from phonepe.map_transaction 
                         where Year = {year} and Quarter = {quarter} and state = '{state}' group by State, District,Year,Quarter order by State,District;'''
        
        bar_chart_t_state= pd.read_sql_query(trans_state, my_connection)
        
        fig = px.bar(bar_chart_t_state,
                     title=state,
                     x="District",
                     y="Total_count",
                     orientation='v',
                     color='Total_count',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)   

# Geo-grapical view for User 
    elif type == 'Users' and year:
        map_query= f'''SELECT State,SUM(Registered_Users) AS Registered_Users from phonepe.map_user
        where Year={year}
        GROUP BY State;'''
        df = pd.read_sql_query(map_query,my_connection)
        fig = px.choropleth(
                            df,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color="Registered_Users",
                            title=f'PhonePe India Transactions - {year}',
                            color_continuous_scale='Rainbow',
                            width=900, height=800, 
                            hover_name='State')
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)
# Bar chart for Total users - State wise
        st.markdown('### :violet[Select options to explore State-wise trends]')
        col1,col2,col3 =st.columns(3)
        with col1:
            state = st.selectbox('',options=['Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                    'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                    'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
                                    'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                    'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                    'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                    'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                    'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                    'Uttarakhand', 'West Bengal'],placeholder='State',
                                label_visibility='collapsed')
        with col2:
            year = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023, 2024], placeholder='Year',
                                label_visibility='collapsed')
        with col3:
            quarter = st.selectbox('', options=[1, 2, 3, 4], placeholder='Quarter', label_visibility='collapsed')
            
        
        user_state=f'''select State,Year,Quarter,District,sum(Registered_Users) as Total_Users, sum(App_Opens) as Total_App_Opens from phonepe.map_user 
                         where Year = {year} and Quarter = {quarter} and state = '{state}' group by State, District,Year,Quarter order by State,District;'''
        
        bar_chart_state= pd.read_sql_query(user_state, my_connection)
        
        fig = px.bar(bar_chart_state,
                     title=state,
                     x="District",
                     y="Total_Users",
                     orientation='v',
                     color='Total_Users',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)

# Charts-Dashboard  
elif selected == 'Charts':
    st.subheader(':orange[Explore Data]')
    col1,col2,col3 =st.columns(3)
    with col1:
        details = st.selectbox('', options=['Transactions', 'Users'], index=None, placeholder='Type',
                                label_visibility='collapsed')
    with col2:
        year = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023, 2024], placeholder='Year',
                            label_visibility='collapsed')
    with col3:
        quarter = st.selectbox('', options=[1, 2, 3, 4], placeholder='Quarter', label_visibility='collapsed')

#  Transactions overview
    if details == 'Transactions':
        tab1,tab2,tab3=st.tabs(['Transaction Details', 'Categories', 'Top 10'])
        with tab1:
            st.markdown(f':blue[PhonePe Pulse in Q{quarter} - {year}]')
            col1,col2,col3=st.columns(3)
            with col1:
                query1 =f'''SELECT SUM(Transaction_count) AS "All PhonePe Transactions" from phonepe.aggregate_transaction
                where Year={year} and Quarter={quarter};'''
                all_trans= pd.read_sql_query(query1,my_connection)
                st.dataframe(all_trans, hide_index=True)
            with col2:
                query2 = f'''SELECT CONCAT('₹ ',ROUND(SUM(Transaction_amount)/10000000,0),' Cr') AS "Total Payment Value" from phonepe.aggregate_transaction
                where Year={year} and Quarter={quarter};'''
                trans_value = pd.read_sql_query(query2,my_connection)
                st.dataframe(trans_value, hide_index=True)
            with col3:
                query3 = f'''SELECT CONCAT('₹ ',ROUND(SUM(Transaction_Amount)/SUM(Transaction_Count),0)) AS "Average Transaction Value" from phonepe.aggregate_transaction
                where Year={year} and Quarter={quarter};'''
                avg_value = pd.read_sql_query(query3,my_connection)
                st.dataframe(avg_value, hide_index=True)
# Transactions Category-wise split
        with tab2:
            col1,col2 = st.columns(2)
            with col1:
                st.write(f':blue[Transaction Count by Category in Q{quarter} - {year}]')
                query4=f''' SELECT Transaction_type AS Categories, ROUND(SUM(Transaction_count),0) AS "Transaction Count" from phonepe.aggregate_transaction
                where Year={year} and Quarter={quarter} GROUP BY Transaction_type;'''
                category=pd.read_sql_query(query4,my_connection)
                st.dataframe(category,hide_index=True)
            with col2:
                st.write(f':blue[Transaction Amount by Category in Q{quarter} - {year}]')
                query5=f'''SELECT Transaction_type AS Categories, CONCAT('₹ ',ROUND(SUM(Transaction_amount)/10000000,0),' Cr') AS "Transaction Amount" from phonepe.aggregate_transaction
                where Year={year} and Quarter={quarter} GROUP BY Transaction_type;'''
                category_amount=pd.read_sql_query(query5,my_connection)
                st.dataframe(category_amount,hide_index=True)
# Total Transactions: Top-10 State,District,Postalcodes
        with tab3:
            select = st.selectbox('Select Option To View TOP 10 Tables:', options=['Number Of Transactions', 'Total Transaction Amount'])
            if select == "Number Of Transactions":  
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f':blue[Top 10 States in Q{quarter} - {year}]')
                    query6=f'''SELECT DENSE_RANK()OVER(ORDER BY SUM(Transaction_count) DESC) AS RK, State,CONCAT(ROUND(SUM(Transaction_count)/10000000,2),' Cr') AS "Transaction Count" from phonepe.aggregate_transaction 
                    WHERE Year={year} and Quarter={quarter} GROUP BY State ORDER BY RK ASC LIMIT 10;'''
                    top_state = pd.read_sql_query(query6, my_connection)
                    top_state = top_state.drop(columns=['RK'])
                    st.dataframe(top_state, hide_index=True)
                with col2:
                    st.write(f':blue[Top 10 Districts in Q{quarter} - {year}]')
                    query7=f'''SELECT DENSE_RANK()OVER(ORDER BY SUM(Transaction_count) DESC) AS RK, District,CONCAT(ROUND(SUM(Transaction_count)/10000000,2),' Cr') AS "Transaction Count" from phonepe.map_transaction 
                    WHERE Year={year} and Quarter={quarter} GROUP BY District ORDER BY RK ASC LIMIT 10;'''
                    top_district = pd.read_sql_query(query7, my_connection)
                    top_district = top_district.drop(columns=['RK'])
                    st.dataframe(top_district, hide_index=True)
                with col3:
                    st.write(f':blue[Top 10 Postal Codes in Q{quarter} - {year}]')
                    query8=f'''SELECT DENSE_RANK()OVER(ORDER BY SUM(Transaction_count) DESC) AS RK, Pincodes,CONCAT(ROUND(SUM(Transaction_count)/10000000,2),' Cr') AS "Transaction Count" from phonepe.top_transaction 
                    WHERE Year={year} and Quarter={quarter} GROUP BY Pincodes ORDER BY RK ASC LIMIT 10;'''
                    top_pincode = pd.read_sql_query(query8, my_connection)
                    top_pincode = top_pincode.drop(columns=['RK'])
                    st.dataframe(top_pincode,column_config={'Pincodes':'Postal Codes'}, hide_index=True)

# Total Transaction Amount: Top-10 State,District,Postalcodes
            if select == "Total Transaction Amount":
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f':blue[Top 10 States in Q{quarter} - {year}]')
                    query6=f'''SELECT DENSE_RANK()OVER(ORDER BY SUM(Transaction_count) DESC) AS RK, State,CONCAT('₹ ',ROUND(SUM(Transaction_amount)/10000000,0),' Cr') AS "Transaction Amount" from phonepe.aggregate_transaction 
                    WHERE Year={year} and Quarter={quarter} GROUP BY State ORDER BY RK ASC LIMIT 10;'''
                    top_state = pd.read_sql_query(query6, my_connection)
                    top_state = top_state.drop(columns=['RK'])
                    st.dataframe(top_state, hide_index=True)
                with col2:
                    st.write(f':blue[Top 10 Districts in Q{quarter} - {year}]')
                    query7=f'''SELECT DENSE_RANK()OVER(ORDER BY SUM(Transaction_count) DESC) AS RK, District,CONCAT('₹ ',ROUND(SUM(Transaction_amount)/10000000,0),' Cr') AS "Transaction Amount" from phonepe.map_transaction 
                    WHERE Year={year} and Quarter={quarter} GROUP BY District ORDER BY RK ASC LIMIT 10;'''
                    top_district = pd.read_sql_query(query7, my_connection)
                    top_district = top_district.drop(columns=['RK'])
                    st.dataframe(top_district, hide_index=True)
                with col3:
                    st.write(f':blue[Top 10 Postal Codes in Q{quarter} - {year}]')
                    query8=f'''SELECT DENSE_RANK()OVER(ORDER BY SUM(Transaction_count) DESC) AS RK, Pincodes,CONCAT('₹ ',ROUND(SUM(Transaction_amount)/10000000,0),' Cr') AS "Transaction Amount" from phonepe.top_transaction 
                    WHERE Year={year} and Quarter={quarter} GROUP BY Pincodes ORDER BY RK ASC LIMIT 10;'''
                    top_pincode = pd.read_sql_query(query8, my_connection)
                    top_pincode = top_pincode.drop(columns=['RK'])
                    st.dataframe(top_pincode,column_config={'Pincodes':'Postal Codes'}, hide_index=True)
#  Usres overview
    elif details == 'Users':
        tab1,tab2=st.tabs(['User Details', 'Top 10 Users'])
        with tab1:
            col1,col2=st.columns(2)
            with col1:
                st.write(f':blue[Registered PhonePe Users till Q{quarter} - {year}]')
                query9 =f'''SELECT SUM(User_count) AS "Total Number of Users" from phonepe.aggregate_user
                where Year={year} and Quarter={quarter};'''
                all_users= pd.read_sql_query(query9,my_connection)
                st.dataframe(all_users, hide_index=True)
            with col2:
                st.write(f':blue[PhonePe app opens in Q{quarter} - {year}]')
                query10 = f'''SELECT CASE WHEN SUM(App_Opens)=0 THEN 'Unavailable' ELSE SUM(App_Opens) END AS "App Opens" from phonepe.map_user
                where Year={year} and Quarter={quarter};'''
                app_opens = pd.read_sql_query(query10,my_connection)
                st.dataframe(app_opens, hide_index=True)
#  Users: Top-10 State,District,Postalcodes
        with tab2: 
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f':blue[Top 10 States in Q{quarter} - {year}]')
                query11=f'''SELECT DENSE_RANK()OVER(ORDER BY SUM(User_count) DESC) AS RK, State,SUM(User_count) AS "User Count" from phonepe.aggregate_user 
                WHERE Year={year} and Quarter={quarter} GROUP BY State ORDER BY RK ASC LIMIT 10;'''
                top_state = pd.read_sql_query(query11, my_connection)
                top_state = top_state.drop(columns=['RK'])
                st.dataframe(top_state, hide_index=True)
            with col2:
                st.write(f':blue[Top 10 District in Q{quarter} - {year}]')
                query12=f'''SELECT DENSE_RANK()OVER(ORDER BY SUM(Registered_Users) DESC) AS RK, District,SUM(Registered_Users) AS "Registered Users" from phonepe.map_user 
                WHERE Year={year} and Quarter={quarter} GROUP BY District ORDER BY RK ASC LIMIT 10;'''
                top_district = pd.read_sql_query(query12, my_connection)
                top_district = top_district.drop(columns=['RK'])
                st.dataframe(top_district, hide_index=True)
            with col3:
                st.write(f':blue[Top 10 Postal code in Q{quarter} - {year}]')
                query13=f'''SELECT DENSE_RANK()OVER(ORDER BY SUM(Registered_Users) DESC) AS RK, Pincodes,SUM(Registered_Users) AS "Registered Users" from phonepe.top_user 
                WHERE Year={year} and Quarter={quarter} GROUP BY Pincodes ORDER BY RK ASC LIMIT 10;'''
                top_pincode = pd.read_sql_query(query13, my_connection)
                top_pincode = top_pincode.drop(columns=['RK'])
                st.dataframe(top_pincode,column_config={'Pincodes':'Postal Code'}, hide_index=True)
# Visualization
elif selected == 'Visualization':
    st.subheader(':orange[Explore Data]')
    col1,col2,col3 =st.columns(3)
    with col1:
        details = st.selectbox('', options=['Transactions', 'Users'], index=None, placeholder='Type',
                                label_visibility='collapsed')
    with col2:
        year = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023, 2024], placeholder='Year',
                            label_visibility='collapsed')
    with col3:
        quarter = st.selectbox('', options=[1, 2, 3, 4], placeholder='Quarter', label_visibility='collapsed')

    if details == 'Transactions':
        tab1, tab2, tab3 = st.tabs(["States", "Districts", "Postal Codes"])
        with tab1:
            st.markdown("### :violet[States]")
            query14=f'''SELECT State, SUM(Transaction_count) as Total_Transactions_Count, SUM(Transaction_amount) as Total_Transaction_Amount from phonepe.aggregate_transaction 
            where Year = {year} and Quarter = {quarter} group by State order by Total_Transaction_Amount desc limit 10;'''
            top10_state= pd.read_sql_query(query14, my_connection)
            fig = px.pie(top10_state, values='Total_Transaction_Amount',
                            names='State',
                            title='Top 10 State based on Total number of transaction and Total amount',width=1000,height=600,
                            color_discrete_sequence=px.colors.sequential.Cividis,
                            hover_data=['Total_Transactions_Count'],
                            labels={'Total_Transactions_Count':'Total_Transactions_Count'})
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        with tab2:
            st.markdown("### :violet[Districts]")
            query15=f'''select District , SUM(Transaction_count) as Total_Count, SUM(Transaction_amount) as Total_Amount from phonepe.map_transaction 
            where Year = {year} and Quarter = {quarter} group by District order by Total_Amount desc limit 10;'''
            top10_district= pd.read_sql_query(query15, my_connection)
            fig = px.pie(top10_district, values='Total_Amount',
                            names='District',width=1000,height=600,
                            title='Top 10 District based on Total number of transaction and Total amount',
                            color_discrete_sequence=px.colors.sequential.Inferno,
                            hover_data=['Total_Count'],
                            labels={'Total_Count':'Total_Count'})
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        with tab3:
            st.markdown("### :violet[Postal Codes]")
            query16=f'''select Pincodes, sum(Transaction_count) as Total_Transaction_Count, sum(Transaction_amount) as Total_Transaction_Amount from phonepe.top_transaction 
                            where Year = {year} and Quarter = {quarter} group by Pincodes order by Total_Transaction_Amount desc limit 10;'''
            top10_postalcodes= pd.read_sql_query(query16, my_connection)
            fig = px.pie(top10_postalcodes, values='Total_Transaction_Amount',
                            names='Pincodes',width=1000,height=600,
                            title='Top 10 Pincode based on Total number of transaction and Total amount',
                            color_discrete_sequence=px.colors.sequential.Plasma,
                            hover_data=['Total_Transaction_Count'],
                            labels={'Total_Transaction_Count':'Total_Transaction_Count'})
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
    
    elif details == 'Users':
        tab1,tab2,tab3 = st.tabs(["Brands", "Districts","States"])
        with tab1:
            st.markdown("### :violet[Brands]")
            query17=f'''select User_Brands, sum(User_count) as Total_Users, avg(User_Percentage)*100 as Avg_Percentage from phonepe.aggregate_user 
            where Year = {year} and Quarter = {quarter} group by User_Brands order by Total_Users desc limit 10;'''
            top10_mobile_brands= pd.read_sql_query(query17, my_connection)
            fig = px.bar(top10_mobile_brands,
                            title='Top 10 Mobile Brands and Percentage',
                            y="Total_Users",
                            x="User_Brands",
                            color='Avg_Percentage',
                            color_continuous_scale=px.colors.sequential.Viridis)
            st.plotly_chart(fig,use_container_width=True)
        with tab2:
            st.markdown("### :violet[Districts]")
            query18=f'''select District, sum(Registered_Users) as Total_Users, sum(App_Opens) as Total_App_Opens from phonepe.map_user 
            where Year = {year} and Quarter = {quarter} group by District order by Total_Users desc limit 10;'''
            top10_user_districts= pd.read_sql_query(query18, my_connection)
            fig = px.bar(top10_user_districts,
                        title='Top 10 District based on Total app opens frequency by users',
                        y="Total_Users",
                        x="District",
                        color='Total_Users',
                        color_continuous_scale=px.colors.sequential.Blues)
            st.plotly_chart(fig,use_container_width=True)
        with tab3:
            st.markdown("### :violet[States]")
            query19=f'''select State, sum(Registered_Users) as Total_Users, sum(App_Opens) as Total_App_Opens from phonepe.map_user 
            where Year = {year} and Quarter = {quarter} group by State order by Total_Users desc limit 10;'''
            top10_user_postalcodes= pd.read_sql_query(query19, my_connection)
            fig = px.bar(top10_user_postalcodes,
                        title='Top 10 States by users',
                        y='Total_Users',
                        x='State',
                        color='Total_Users', 
                        color_continuous_scale=px.colors.sequential.Turbo)
            st.plotly_chart(fig, use_container_width=True)