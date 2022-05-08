from ast import parse
import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot("5361614607:AAHGAneYPT5lpih3Rm-fASWT5xivUHDTUu8")

conn = sqlite3.connect('D://bazadb//altentsentrbaza.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id, name, phone, username, course):
	cursor.execute('INSERT INTO altentsentr (user_id, name, phone, username, course) VALUES (?, ?, ?, ?, ?)', (user_id, name, phone, username, course))
	conn.commit()

def db_table_update_phone(user_id, phone):
    cursor.execute('UPDATE altentsentr SET phone=(?) WHERE user_id=(?);', (phone, user_id))
    conn.commit()

def db_table_update_course(user_id, course):
    cursor.execute('UPDATE altentsentr SET course=(?) WHERE user_id=(?);', (course, user_id,))
    conn.commit()

def ism_yoz(message):    
    user_id = message.from_user.id
    name = message.text
    phone = "000"
    course = "000"
    username = message.from_user.username
    
    db_table_val(user_id, name=name, phone=phone, course=course, username=username)
    text = "Raxmat, Endi siz bilan bog'lanishimiz uchun raqamingizni kiriting:"
    text+="Namuma: <b>+998991234567</b>"
    
    bot.send_message(message.chat.id,text, parse_mode="html")
    bot.register_next_step_handler(message, raqam_yoz)

def raqam_yoz(message):
    raqam = message.text
    user_id = message.from_user.id
    db_table_update_phone(user_id, raqam)
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton("Backend")
    itembtn2 = types.KeyboardButton("Frontent")
    itembtn3 = types.KeyboardButton("Ingliztili")
    itembtn4 = types.KeyboardButton("Matematika")
    # itembtn5 = types.KeyboardButton('Ortga')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    text = "Ajoyib, Endi quyidagi kurslarimizdan birini tanlang:"

    bot.send_message(message.chat.id,text, reply_markup=markup,parse_mode="html")
    bot.register_next_step_handler(message, kurs_yoz)
def kurs_yoz(message):
    course = message.text
    user_id = message.from_user.id
    db_table_update_course(user_id, course)

    text7 = "Ro'yxatdan o'tish yakunlandi.Aloqaga chiqamiz."

    bot.send_message(message.chat.id,text7)
    bot.register_next_step_handler(message)

# def db_table_update_phone(user_id, phone):
#   cursor.execute('UPDATE altentsentr SET phone=? WHERE user_id=?',(phone, user_id))
#   conn.commit()

# def db_table_update_course(user_id, course):
#   cursor.execute('UPDATE altentsentr SET course=? WHERE user_id=?,'(course, user_id))
#   conn.commit()
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    itembtn1 = types.KeyboardButton('♻️Kurslarimiz haqida ma\'lumot')
    itembtn2 = types.KeyboardButton('📝Kursga yozlish')
    itembtn3 = types.KeyboardButton('☎️Aloqa va Manzil')
    itembtn4 = types.KeyboardButton('🌐Ijtimoiy Tarmoqlarimiz')
    itembtn5 = types.KeyboardButton('🎥Qisqacha vidyolavha')

    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
        
    bot.send_message(message.chat.id,"Assalomu Alaykum <b>ALTENT</B> o'quv markazining ro'yxatdan o'tish telegram botiga xush kelibsiz", parse_mode="html", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == "♻️Kurslarimiz haqida ma\'lumot":
        markup2 = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
        itembtn11 = types.KeyboardButton('💻Backend')
        itembtn22 = types.KeyboardButton('💻Frontent')
        itembtn33 = types.KeyboardButton('🇱🇷-Ingliz tili')
        itembtn44 = types.KeyboardButton('📈Matematika')
        itembtn55 = types.KeyboardButton('🔙Ortga')
        markup2.add(itembtn11, itembtn22, itembtn33, itembtn44,itembtn55)
        bot.send_message(message.chat.id,'''🖥Bizning kurslarimiz:

 💻Backend
 💻Frontent
 🇱🇷-Ingliz tili
 📈Matematika  ''', reply_markup = markup2)
    elif message.text == "🔙Ortga":
        markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        itembtn1 = types.KeyboardButton('♻️Kurslarimiz haqida ma\'lumot')
        itembtn2 = types.KeyboardButton('📝Kursga yozlish')
        itembtn3 = types.KeyboardButton('☎️Aloqa va Manzil')
        itembtn4 = types.KeyboardButton('🌐Ijtimoiy Tarmoqlarimiz')
        itembtn5 = types.KeyboardButton('🔙Ortga')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
        text4 = "Menyu"
        bot.send_message(message.chat.id,text4, reply_markup = markup) 
    elif message.text == "📝Kursga yozlish":
        markup3 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
        itembtn11 = types.KeyboardButton('Rad etish')
        text="Ism va familyangiz:"
        bot.send_message(message.chat.id,"📩 Bu yerda siz bizning kurslarimizga ariza yozib qoldirishingiz mumkin:\nQuyidagi so'ralgan formani aniq qilib to'ldiring va sizga admin tez orada aloqaga chiqadi:")
        bot.send_message(message.chat.id, text, reply_markup=markup3)
        bot.register_next_step_handler(message, ism_yoz)
        # bot.register_next_step_handler(message, raqam_yoz )
        # bot.register_next_step_handler(message, kurs_yoz ) 
    elif message.text == "💻Backend":
        txt1 = '''💻Backend

📆 Kurs davomiyligi: 6 oy
🗓 1 haftada 3 kun dars
🕒 1 kunda 2 soat

💰 Kurs narxi: 800 ming so'm
💳 To'lov usuli: Naqd/ PayMe/ Bank.'''
        bot.send_message(message.chat.id, txt1)
    elif message.text == "💻Frontent":
        txt2 = '''💻Frontent

📆 Kurs davomiyligi: 6 oy
🗓 1 haftada: 3 kun dars
🕒 1 kunda: 2 soat

💰 Kurs narxi: 800 ming so'm/oyiga
💳 To'lov usuli: Naqd/PayMe/ Bank.'''
        bot.send_message(message.chat.id, txt2)
    elif message.text == "🇱🇷-Ingliz tili":
        txt3 = '''🇱🇷Ingliz tili

📆 Kurs davomiyligi: 6oy
🗓 1 haftada 3 kun dars
🕒 1 kunda 2 soat

💰 Kurs narxi: 600 ming so'm/oyiga
💳 To'lov usuli: Naqd/PayMe/ Bank.'''
        bot.send_message(message.chat.id, txt3)
    elif message.text == "📈Matematika":
        txt4 = '''📈Matematika
 
📆 Kurs davomiyligi: 6oy
🗓 1 haftada 5 kun dars
🕒 1 kunda 2 soat

💰 Kurs narxi: 600 ming so'm/oyiga
💳 To'lov usuli: Naqd/PayMe/Bank.'''
        bot.send_message(message.chat.id, txt4)
    elif message.text == "☎️Aloqa va Manzil":
        bot.send_message(message.chat.id,''' ALTENT o\'quv markazi

⏰Ish vaqti: 08:00 dan 22:00 gacha
📞 TEL:+998555009005
📨 Admin bilan bog\'lanish:@altent_admin1
📍 Mo\'ljal:Chilonzor metro bekati Integro binosi 8-qavat
📍 Locatsiya:https://maps.apple.com/maps?ll=41.276044190303686,69.20484611106673&q=41.276044190303686,69.20484611106673&t=m''')
    elif message.text == "🌐Ijtimoiy Tarmoqlarimiz":
        bot.send_message(message.chat.id,'''🌐Bizning ijtimoy tarmoqlarimiz

✔️Telegram: https://t.me/altent_lc
✔️InStagram: https://www.instagram.com/altent_lc/
✔️TikTok: https://vt.tiktok.com/ZSd5SWqRX/
✔️Facebook: https://m.facebook.com/altent.lc
✔️YouTube:https://youtube.com/channel/UCMOgpz8rewPf8ZRXN3nkZQA''')
    elif message.text == "🎥Qisqacha vidyolavha":
        
        video = open('D://telegram загруски//3b18a4afd177479088cc30f21e0531ce.mp4', 'rb')
        bot.send_video(message.chat.id, video)

bot.infinity_polling()