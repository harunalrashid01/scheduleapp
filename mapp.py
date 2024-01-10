from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os
import telebot
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from reportlab.pdfgen import canvas
from telegram.ext import MessageHandler, filters, CallbackContext
from datetime import datetime
import pytz

indian_timezone = pytz.timezone('Asia/Kolkata')  # for time
BOT_TOKEN = os.environ.get('BOT_TOKEN')
json_keyfile_path = 'haroon-407613-66e3e3185c68.json'
spreadsheet_name = "Mentor's Attendance Sheet"
sheet_name = 'Haroon'

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_path, scope)
gc = gspread.authorize(credentials)
spreadsheet = gc.open(spreadsheet_name)

sheet = spreadsheet.worksheet(sheet_name)

bot = telebot.TeleBot(BOT_TOKEN)
current_date = datetime.now()
day_of_month = current_date.strftime("%d")
time = current_date.strftime("%H:%M:%S")
cell=123+int(day_of_month)


#         print(f'Cell {cell_to_update} updated with: {new_value}')
@bot.message_handler(commands=['login'])
def login(message):
    lst=["HAROON",time]
    a=1
    for i in lst:
        new_value = i
        u = chr(ord("A")+a)+ str(cell)
        cell_to_update = u
        a+=1      
        sheet.update_acell(cell_to_update, new_value)

    bot.reply_to(message, f"YOUR  LOGIN TIME IS UPDATED {time}")
    # bot.register_next_step_handler(message, check_password)    
@bot.message_handler(commands=['logout'])
def login(message):
    lst=[time]
    a=1
    for i in lst:
        new_value = i
        u = chr(ord("C")+a)+ str(cell)
        cell_to_update = u
        a+=1      
        sheet.update_acell(cell_to_update, new_value)

    bot.reply_to(message, f"YOUR LOG OUT TIME IS UPDATED {time} NOW PLEASE ENTER A TASK")
    bot.register_next_step_handler(message, task)    


def task(message):
    update=message.text
    lst=[update]
    a=1
    for i in lst:
        new_value = i
        u = chr(ord("D")+a)+ str(cell)
        cell_to_update = u
        a+=1      
        sheet.update_acell(cell_to_update, new_value)

    bot.reply_to(message, f"YOUR {update} is updated")    
bot.infinity_polling()    