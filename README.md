Data-Scraping-with-Selenium-Dynamic-Filtering-using-Streamlit

Introduction
•	The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.
Domain

•	TRANSPORTATION
Business Use Cases:

The solution can be applied to various business scenarios including:
•	Travel Aggregators: Providing real-time bus schedules and seat availability for customers.
•	Market Analysis: Analyzing travel patterns and preferences for market research.
•	Customer Service: Enhancing user experience by offering customized travel options based on data insights.
•	Competitor Analysis: Comparing pricing and service levels with competitors.

SKILL-TAKEAWAY
•	Python scripting, Selenium, Data Collection, Web Scraping, Data Management using SQL, Streamlit.

TECHNOLOGY USED
•	Python 3.9.I
•	MySQL 8.0
•	Streamlit
•	Selenium

FEATURES OF APPLICATION

Retrive the Bus Information:
  Selenium is a powerful tool for automating web browsers, which is especially useful for web scraping tasks. If you want to retrieve bus details from RedBus, 
 you can use Selenium to automate the process of searching for buses and extracting the relevant information. This involves interacting with web elements 
 like input fields and buttons, waiting for the page to load, and extracting the desired details from the search results.
 
Store data in database:
•	The collected bus details data was transformed into pandas dataframes. Before that, a new database and tables were created using the MySQL connector. With the help of MySQL, the data was inserted into the respective tables. The database could be accessed and managed in the MySQL environment.

web app - streamlit:
•	With the help of Streamlit, you can create an interactive application similar to RedBus by designing a user-friendly interface that allows users to search for bus routes, view available buses, and get details like departure times and prices and also book the bus ticket based on the id of the bus and aget an txt file which is stoed on desktop or in future made to send as sms and the same being stored in a different bookings table for future reference by project admin/website owner

PACKAGES AND LIBRARIES
•	pandas as pd
•	import pymysql
•	import time
•	from PIL import image
•	import base64
•	import emoji
•	import plotly.express as px
•	streamlit as slt
•	import datetime
•	from streamlit_option_menu import option_menu
•	from selenium import webdriver 




•	Landing page of the yellowbus(application name) application with data extracted from www.redbus.com   
![image](https://github.com/user-attachments/assets/db015ddd-d273-4f5f-be39-6817d1c08726)
![image](https://github.com/user-attachments/assets/87d34089-bc75-40c0-9d74-219941a92746)
![image](https://github.com/user-attachments/assets/d90f6820-8e74-4a3a-89ec-47c08c1d836a)
![image](https://github.com/user-attachments/assets/cdfa4dd0-0cc1-4195-9cbe-a39ac2a627ea)
![image](https://github.com/user-attachments/assets/2d5d0637-a8e0-4fda-9ce5-63ab672109b0)
•	Create txt file with booked details of customer in desktop (location given)
![image](https://github.com/user-attachments/assets/8316c601-1f33-495d-88ef-c4fd8ab3ce48)
•	Created bookings table entry with booked details fo the customer  
![image](https://github.com/user-attachments/assets/7bea2475-1329-4e7f-8459-0e13e64a1aaa)
![image](https://github.com/user-attachments/assets/9cb67589-898f-4697-be70-227aa66bb8c7)

•	About us page of the application       
![image](https://github.com/user-attachments/assets/34bb4f67-8839-4d25-84cc-1d862ae0f1d5)
![image](https://github.com/user-attachments/assets/31a66ef7-4536-4916-9a82-b4a9598dfc83)
![image](https://github.com/user-attachments/assets/604a5361-5c49-41f9-83bc-53949de65746)
![image](https://github.com/user-attachments/assets/53c34c39-d96c-48d4-ae57-60966784a00a)




