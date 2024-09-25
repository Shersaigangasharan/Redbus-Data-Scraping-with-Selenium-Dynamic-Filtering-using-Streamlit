# importing libraries

import pandas as pd
import pymysql
import streamlit as slt
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
import time
import base64
import emoji

# Set pandas options to display all data in each column
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

#all states KE,AP,TG,GOA,RS,HP,AS-1,2(all rtc),UP,WB-1,2,3,4(all rtc),PJ,BI,CTU,JK 

# functionality features
def create_bookings_table():
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='Root75', database='SAI')
        cursor = conn.cursor()

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS bookings (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                Routename TEXT,
                Busname TEXT,
                Bustype TEXT,
                seats INT NOT NULL,
                busid INT NOT NULL,
                Departing_time TIME,
                Duration TEXT,
                Reaching_time TIME,
                Star_rating FLOAT,
                Price DECIMAL(10, 2)
            );
        '''

        cursor.execute(create_table_query)
        conn.commit()
        conn.close()
        slt.write(":orange[Bookings table created successfully]")
    except Exception as e:
        slt.error(f":orange[Error creating bookings table: {e}]")

def fetch_bus_details(bus_id):
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='Root75', database='SAI')
        cursor = conn.cursor()

        query = f'''
            SELECT * FROM bus_routes
            WHERE ID = {bus_id}
        '''
        print("Query:", query)  # Add this line for debugging
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        return result
    except Exception as e:
        slt.error(f":orange[Error fetching bus details: {e}]")
        return None

def insert_booking_data(data):
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='Root75', database='SAI')
        cursor = conn.cursor()

        insert_query = '''
            INSERT INTO bookings (name, email, password, seats, busid, Routename, Busname, Bustype, Departing_time, Duration, Reaching_time, Star_rating, Price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(insert_query, (data['Name'], data['Email'], data['Password'], data['Seats'], data['BusID'], data['Routename'], data['Busname'], data['Bustype'], data['Departing_time'], data['Duration'], data['Reaching_time'], data["Star_rating"], data['Price']))
        conn.commit()
        conn.close()
        slt.write(":orange[Booking data inserted successfully]")
        a = ' '
        b = ' '
        c = ' '
        d = ' '
        e = ' '
    except Exception as e:
        slt.error(f":orange[Error inserting booking data: {e}]")

def main(a, b, c, d, e):
    bus_id = a
    user_name = b
    user_email = c
    user_password = d
    num_seats = e

    create_bookings_table()

    bus_details = fetch_bus_details(bus_id)

    if bus_details:
        combined_data = {
            'Name': user_name,
            'Email': user_email,
            'Password': user_password,
            'Seats': num_seats,
            'BusID': bus_id,
            **dict(zip(["Routename", "Busname", "Bustype", "Departing_time", "Duration", "Reaching_time", "Star_rating", "Price"], bus_details[1:]))
        }

        # Convert Departing_time to string (if needed)
        combined_data['Routename'] = str(bus_details[1])
        combined_data['Busname'] = str(bus_details[3])
        combined_data['Bustype'] = str(bus_details[4])
        combined_data['Departing_time'] = str(bus_details[5])
        combined_data['Duration'] = str(bus_details[6])
        combined_data['Reaching_time'] = str(bus_details[7])
        combined_data['Star_rating'] = str(bus_details[8])
        combined_data['Price'] = str(bus_details[9])
        print(f"""'Route name' = {str(bus_details[1])}, 'Busname' = {str(bus_details[3])}, 'Bustype' = {str(bus_details[4])},'Departing_time' = {str(bus_details[5])},'Duration' = {str(bus_details[6])},'Reaching_time' = {str(bus_details[7])},'Star_rating' = {str(bus_details[8])},'Price' = {str(bus_details[9])}""")

        with open(r"C:/Users/Shers/Desktop/booking_details.txt", 'w') as file:
            for key, value in combined_data.items():
                file.write(f"{key}: {value}\n")

        insert_booking_data(combined_data)  # Insert data into the bookings table

        slt.write(":orange[Booking details saved to booking_details.txt and inserted into the bookings table]")
        slt.header(":blue[congratulations Booking confirmed incase of issues pleas contact support @ 📞 +919*****87899  or  mail us @ ✉️ 'www.yellowbus.com]")
    else:
        slt.warning(":orange[Bus ID not found. Please enter a valid ID.]")

#Telangana bus
lists_T=[]
df_T=pd.read_csv("D:\Scraped_data\df_TG.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])

# kerala bus
lists_k=[]
df_k=pd.read_csv("D:\Scraped_data\df_KE.csv")
for i,r in df_k.iterrows():
    lists_k.append(r["Route_name"])

#Andhra bus
lists_A=[]
df_A=pd.read_csv("D:\Scraped_data\df_AP.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_name"])

#Goa bus
lists_g=[]
df_G=pd.read_csv("D:\Scraped_data\df_GOA.csv")
for i,r in df_G.iterrows():
    lists_g.append(r["Route_name"])

#Rajastan bus
lists_R=[]
df_R=pd.read_csv("D:\Scraped_data\df_RS.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])

# Himachal Pradesh
lists_H=[]
df_H=pd.read_csv("D:\Scraped_data\df_HP.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["Route_name"])

#Assam bus data for both rtc's
df_AS=pd.read_csv("D:\Scraped_data\df_ASSAM.csv")
df_AS2=pd.read_csv("D:\Scraped_data\df_ASSAMkaac.csv")
df_ASall = pd.concat([df_AS, df_AS2], ignore_index=True)
lists_AS=[]
for i,r in df_ASall.iterrows():
    lists_AS.append(r["Route_name"])

#UP bus
lists_UP=[]
df_UP=pd.read_csv("D:\Scraped_data\df_UP.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

#West bengal bus all rtcs
df_WB1=pd.read_csv("D:\Scraped_data\df_WB1.csv")
df_WB2=pd.read_csv("D:\Scraped_data\df_WB2.csv")
df_WB3=pd.read_csv("D:\Scraped_data\df_WB3.csv")
df_WB4=pd.read_csv("D:\Scraped_data\df_WB4.csv")
df_WBall = pd.concat([df_WB1, df_WB2, df_WB3, df_WB4], ignore_index=True)
lists_WB=[]
for i,r in df_WBall.iterrows():
    lists_WB.append(r["Route_name"])

#Punjab bus rtc
lists_PJ=[]
df_PJ=pd.read_csv("D:\Scraped_data\df_PJ.csv")
for i,r in df_PJ.iterrows():
    lists_PJ.append(r["Route_name"])

#Bihar bus
lists_BI=[]
df_BI=pd.read_csv("D:\Scraped_data\df_BIHAR.csv")
for i,r in df_BI.iterrows():
    lists_BI.append(r["Route_name"])

#Chandigarh bus
lists_CTU=[]
df_CTU=pd.read_csv("D:\Scraped_data\df_CTU.csv")
for i,r in df_CTU.iterrows():
    lists_CTU.append(r["Route_name"])

#JK bus
lists_JK=[]
df_JK=pd.read_csv("D:\Scraped_data\df_JAMMU&K.csv")
for i,r in df_JK.iterrows():
    lists_JK.append(r["Route_name"])

#setting up streamlit page
slt.set_page_config(layout="wide")
#commented a swe can pick any of other images based on selected option as background image instead of one background image
# def set_background(image_path):
#     with open(image_path, "rb") as image_file:
#         data = image_file.read()
#     encoded = base64.b64encode(data).decode()
#     page_bg_img = f'''
#     <style>
#     .stApp {{
#         background-image: url("data:image/png;base64,{encoded}");
#         background-size: cover;
#     }}
#     </style>
#     '''
#     slt.markdown(page_bg_img, unsafe_allow_html=True)

# # Specify the path to your image file
# image_path = "D:/IMAGES/r1.jpg"

# # Set the background image
# set_background(image_path)

web=option_menu(menu_title="🚌YellowBus",
                options=["🏠Home","📌🛣️States and Routes","👋😀👉About us"],
                icons=["bus-front","map","info-circle"],
                orientation="horizontal"
                )


def set_background(selected_option):
    # Map option to background image path
    background_images = {
        "🏠Home": "D:/IMAGES/r1.jpg",
        "📌🛣️States and Routes": "D:/IMAGES/_817339d8-be32-4a3c-888e-a610246fee60.jpeg",
        "👋😀👉About us": "D:/IMAGES/re4.png"
    }

    # Get the image path based on the selected option
    image_path = background_images.get(selected_option, "D:/IMAGES/r3.jpg")

    # Read and encode the image
    with open(image_path, "rb") as image_file:
        data = image_file.read()
    encoded = base64.b64encode(data).decode()

    # Apply the background image style
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
    }}
    </style>
    '''
    slt.markdown(page_bg_img, unsafe_allow_html=True)

# Example usage:
selected_option = web  # Assuming `web` contains the selected option
set_background(selected_option)

# Load the image
image = Image.open("D:\IMAGES\yellow bus.png")

# Rotate the image by 180 degrees
# rotated_image = image.rotate(180)
rotated_image = image
# Home page setting
if web=="🏠Home":    
    # Display the rotated image
    slt.image(rotated_image, width=200)
    slt.title(":red[Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit]")
    slt.subheader(":red[Domain:] ")
    slt.subheader(":green[ Transportation]")
    slt.subheader(":red[ Application business usage: ]")
    slt.subheader(":green[ Travel aggregators: Providing real-time bus schedules and seat availability for customers for booking]")
    slt.subheader(":green[ Market analysis: Analyzing travel patterns and preferences for market research by loooking at the bookings table data.]")
    slt.subheader(":green[ Customer service: Enhancing user experience by offering customized travel options based on data insights from bookings table data.]")
    slt.subheader(":green[ Competitor analysis: Comparing pricing and service levels with competitors.]")
    slt.subheader(":red[Objective:] ")
    slt.subheader(":green[The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.]")
    slt.header(":violet[Overview:]")
    slt.subheader(":red[Selenium: ]") 
    slt.subheader(":green[Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages, to collect the desired data.]")
    slt.subheader(":red[Pandas:]")
    slt.subheader(":green[ Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.]")
    slt.subheader(":red[MySQL:]")
    slt.subheader(":green[With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset and the data was efficiently inserted into relevant tables for storage and retrieval.]")
    slt.subheader(":red[Streamlit:]")
    slt.subheader(":green[Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.]")
    slt.subheader(":red[Skill-take:]")
    slt.subheader(":green[Selenium, Python, Pandas, MySQL,pymysql-connector-python, Streamlit.]")
    slt.subheader(":violet[Developed-by:]  ")
    slt.header(":red[Sher sai ganga sharan]")

# States and Routes page setting
if web == "📌🛣️States and Routes":
    #all states KE,AP,TG,GOA,RS,HP,AS-1,2(all rtc),UP,WB-1,2,3,4(all rtc),PJ,BI,CTU,JK 
    S = slt.selectbox(":orange[Lists of States]", ["Telangana (TSRTC)", "Andhra Pradesh (APSRTC)", "Kerala (KSRTC)",
                                          "Goa (KTCL)", "Rajastan (RSRTC)", "Himachal Pradesh (HRTC)",
                                           "Assam all RTC (ASTC, KAAC)", "Uttar Pradesh(UPSRTC)",
                                            "West Bengal all RTC (NBSTC, SBSTC, WBSTC, WBTC)", "Punjab (PEPSU)",
                                             "Bihar (BSRTC)", "Chandigarh Transport Undertaking (CTU RTC)",
                                              "Jammu & Kashmir (JKSRTC)"])
    
    col1,col2=slt.columns(2)
    with col1:
        select_type = slt.radio(":orange[Choose bus type]", ("sleeper", "semi-sleeper", "others"))
    with col2:
        select_fare = slt.radio(":orange[Choose bus fare range]", ("50-1000", "1000-2000", "2000 and above"))
    TIME=slt.time_input(":orange[select the time]")
   

    # Telangana bus fare filtering
    if S == "Telangana (TSRTC)":
        K = slt.selectbox(":orange[List of routes]",lists_T)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        slt.image("D:/IMAGES/512px-TSRTC_LOGO.webp",width=180)
        
        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)
        
        if __name__ == "__main__":
            slt.header(":orange[Fill in your details to book tickets with YellowBus]")
            a = slt.text_input(":orange[Enter Bus ID to book: ]")
            b = slt.text_input(":orange[Enter your name: ]")
            c = slt.text_input(":orange[Enter your email: ]")
            d = slt.text_input(":orange[Enter your password: ]")
            e = slt.text_input(":orange[Enter the number of seats: ]")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)
        
    # Kerala bus fare filtering
    if S == "Kerala (KSRTC)":
        K = slt.selectbox("List of routes",lists_k)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        slt.image("D:/IMAGES/200px-Kerala_State_Road_Transport_Corporation_logo.webp",width=180)
        
        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)

    # Adhra Pradesh bus fare filtering
    if S == "Andhra Pradesh (APSRTC)":
        K = slt.selectbox("List of routes",lists_A)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        slt.image("D:/IMAGES/512px-Andhra_Pradesh_State_Road_Transport_Corporation_logo.webp",width=180)
        
        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)
          

    # Goa bus fare filtering
    if S == "Goa (KTCL)":
        K = slt.selectbox("List of routes",lists_g)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        slt.image("D:/IMAGES/Kadamba_Transport_Corporation_logo.webp")
        
        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)

    # Rajastan bus fare filtering
    if S == "Rajastan (RSRTC)":
        K = slt.selectbox("List of routes",lists_R)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        slt.image("D:/IMAGES/512px-Rajasthan_State_Road_Transport_Corporation_logo.webp",width=180)
        
        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)
          

    # Himachal Pradesh bus fare filtering       
    if S == "Himachal Pradesh (HRTC)":
        K = slt.selectbox("List of routes",lists_H)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        slt.image("D:/IMAGES/512px-HRTCHP.webp",width=180)
        
        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)
    
    # Assam all RTC 1,2 bus fare filtering
    if S == "Assam all RTC (ASTC, KAAC)":
        K = slt.selectbox("List of routes",lists_AS)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        col1,col2 = slt.columns(2,gap='small')
        col1.image("D:/IMAGES/220px-Assam_State_Transport_Corporation_logo1.webp",width=200)
        col2.image("D:/IMAGES/KAAC.webp",width=220)
        
        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)


    # Uttar Pradesh bus fare filtering
    if S == "Uttar Pradesh(UPSRTC)":
        K = slt.selectbox("List of routes",lists_UP)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        slt.image("D:/IMAGES/UPSRTC-Logo.webp",width=200)
        
        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)

    # West Bengal all RTC bus fare filtering
    if S == "West Bengal all RTC (NBSTC, SBSTC, WBSTC, WBTC)":
        K = slt.selectbox("List of routes",lists_WB)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        col1,col2 = slt.columns(2,gap='small')
        col1.image("D:/IMAGES/nbstc-logo3.webp")
        col2.image("D:/IMAGES/South-Bengal-State-Transport-Corp-SBSTC-Customer-Care.webp", width=200)
        col3,col4 = slt.columns(2,gap='small')
        col3.image("D:/IMAGES/15443.png", width=200)
        col4.image("D:/IMAGES/512px-Logo-WBTCBig.webp", width=200)
        
        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)

    # Punjab bus fare filtering
    if S == "Punjab (PEPSU)":
        K = slt.selectbox("List of routes",lists_PJ)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        slt.image("D:/IMAGES/logo-q70v9565hzystcjymnn3mbh85fnyu1xpdt48hw7hb0.webp",width=200)
        
        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)
    
    # Bihar bus fare filtering
    if S == "Bihar (BSRTC)":
        K = slt.selectbox("List of routes",lists_BI)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        slt.image("D:/IMAGES/BSRTC.webp",width=220)

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)
    
    # Chandigarh Transport Undertaking CTU bus fare filtering
    if S == "Chandigarh Transport Undertaking (CTU RTC)":
        K = slt.selectbox("List of routes",lists_CTU)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        slt.image("D:/IMAGES/CTU.webp",width=220)

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)
    
    # Jammu & Kashmir bus fare filtering
    if S == "Jammu & Kashmir (JKSRTC)":
        K = slt.selectbox("List of routes",lists_JK)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host='127.0.0.1', user="root", password="Root75", database="sai")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bustype LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bustype LIKE '%A/c Semi Sleeper%'"
            else:
                bus_type_condition = "Bustype NOT LIKE '%Sleeper%' AND Bustype NOT LIKE '%A/c Semi Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Departing_time >= '{TIME}'
                ORDER BY Price, Departing_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Route_name", "Route_link", "Busname", "Bustype", "Departing_time",
                "Duration", "Reaching_time", "Star_rating", "Price", "Seats_available"
            ])
            return df

        slt.image("D:/IMAGES/JKSRTC.webp",width=220)
        
        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

        if __name__ == "__main__":
            a = slt.text_input("Enter Bus ID to book:")
            b = slt.text_input("Enter your name:")
            c = slt.text_input("Enter your email:")
            d = slt.text_input("Enter your password:")
            e = slt.text_input("Enter the number of seats:")
            if slt.button(":orange[Book]"):
                main(a, b, c, d, e)

if web=="👋😀👉About us":
    slt.header(":red[Yellow Bus provides details of the following state road transportaion coporations by Data Scraping with Selenium & Dynamic Filtering using Streamlit]")    
    col1,col2 = slt.columns(2,gap='small')
    col1.image("D:/IMAGES/512px-TSRTC_LOGO.webp",width=180)
    col2.image("D:/IMAGES/200px-Kerala_State_Road_Transport_Corporation_logo.webp",width=180)
    col3,col4 = slt.columns(2,gap='small')
    col3.image("D:/IMAGES/512px-Andhra_Pradesh_State_Road_Transport_Corporation_logo.webp",width=180)
    col4.image("D:/IMAGES/Kadamba_Transport_Corporation_logo.webp")
    col5,col6 = slt.columns(2,gap='small')
    col5.image("D:/IMAGES/512px-Rajasthan_State_Road_Transport_Corporation_logo.webp",width=180)
    col6.image("D:/IMAGES/512px-HRTCHP.webp",width=180)
    col7,col8 = slt.columns(2,gap='small')
    col7.image("D:/IMAGES/220px-Assam_State_Transport_Corporation_logo1.webp",width=200)
    col8.image("D:/IMAGES/KAAC.webp",width=200)
    col9,col10 = slt.columns(2,gap='small')
    col9.image("D:/IMAGES/UPSRTC-Logo.webp",width=200)
    col10.image("D:/IMAGES/nbstc-logo3.webp")
    col11,col12 = slt.columns(2,gap='small')
    col11.image("D:/IMAGES/South-Bengal-State-Transport-Corp-SBSTC-Customer-Care.webp", width=200)
    col12.image("D:/IMAGES/15443.png", width=200)
    col13,col14 = slt.columns(2,gap='small')
    col13.image("D:/IMAGES/512px-Logo-WBTCBig.webp", width=200)
    col14.image("D:/IMAGES/logo-q70v9565hzystcjymnn3mbh85fnyu1xpdt48hw7hb0.webp",width=200)
    col15,col16 = slt.columns(2,gap='small')
    col15.image("D:/IMAGES/BSRTC.webp",width=220)
    col16.image("D:/IMAGES/CTU.webp",width=220)
    # col17,col18 = slt.columns(2,gap='small')
    slt.image("D:/IMAGES/JKSRTC.webp",width=220)
    slt.header(":green[Please contact us @ 📞 +919*****87899  or  mail us @ ✉️ 'www.yellowbus.com']")

