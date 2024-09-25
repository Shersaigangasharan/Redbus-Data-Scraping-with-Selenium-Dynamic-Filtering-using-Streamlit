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
•	With the help of Streamlit, you can create an interactive application similar to RedBus by designing a user-friendly interface that allows users to search for bus routes, view available buses, and get details like departure times and prices and also book the bus ticket based on the id of the bus and aget an txt file which is stoed on desktop or in future made to send as sms and the same being stored in a different bookings table for future reference by project admin/website ownerv
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
