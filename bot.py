import telebot, random, pyowm, wikipedia, urllib3, string
from telebot import types

import json
# import url_short as sh


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

help = 'Ես կարող եմ քեզ տեղեկացնել եղանակի տեսութեան մասին, կարող եմ քեզ համար վիկիպեդիայից բերել քո ցանկացած թեմայի շուրջ տեղեկութիւն բերել։ Ես աւր աւրի աւելի եմ զարգանում, ինձ ամէն աւր մի նոր բան են սովորեցնում։ Եթե ունես դժգոհութիւններ կամ բողոքներ՝ խնդրում եմ տեղեկացրու ինձ դրա մասն, եւ ես կը փորձեմ ամէնակարճ ժամկետներում շտկել դրանք։'
bot = telebot.TeleBot('1221513545:AAFT9_LzADdcciIT9JgyOyTlv26pKe8coMY')

@bot.message_handler(commands=['search_in_wiki'])
def search(message):
	sti = open('stickers/googleok.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, 'Գրէք ցանկացած բան, եւ ես այն կը փնտրեմ wikipedia.com որոնողական համակարգում։ \n Դրա համար աւգտագործեք @wiki_search Name հրամանը։')	

# @bot.message_handler(commands=['search_in_google'])
# def search(message):
# 	sti = open('stickers/googleok.tgs', 'rb')
# 	bot.send_sticker(message.chat.id, sti)
# 	bot.send_message(message.chat.id, 'Գրեք ցանկացած բառ, եւ ես այն կփնտրեմ wikipedia.com որոնողական համակարգում։')	
@bot.message_handler(commands=['help'])
def welcome(message):
	markup = types.InlineKeyboardMarkup(row_width=2)
	item1 = types.InlineKeyboardButton("Հիանալի է ❤️😁", callback_data='good')
	item3 = types.InlineKeyboardButton("Հրամանները ։)", callback_data='hraman')
	item2 = types.InlineKeyboardButton("Քիչ է, ինձ թուում է ինչ որ բան պակասում է 👎😢👎", callback_data='bad')

	markup.add(item2)
	markup.add(item1, item3)

	bot.send_message(message.chat.id, help, reply_markup=markup)
@bot.message_handler(commands=['start'])
def welcome(message):
	rand = str(random.randint(0,16))
	if rand != '0':
		sti = open('stickers/hello/AnimatedSticker'+ rand + '.tgs', 'rb')
	elif rand == '0':		
		sti = open('stickers/hello/AnimatedSticker.tgs', 'rb')		

	bot.send_sticker(message.chat.id, sti)

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🎲")
	item2 = types.KeyboardButton("😊 Ի՞նչ կարող ես դու անել։")
	item3 = types.KeyboardButton("🌞 Արի խաւսենք եղանակի մասին։")

	markup.add(item1, item2)
	# markup.add(item3);

	bot.send_message(message.chat.id, "Բարի գալուստ յարգելի <b>{0.first_name}</b>!\nԵս <b>Տրիոյի</b> բոտն եմ, եւ կփորձեմ ամէն ինչում աւգնել քեզ: 😁😁😁😁😁😁".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])	

def lalala(message):
	global help
	# markup = types.InlineKeyboardMarkup()
	# btn_my_site= types.InlineKeyboardButton(text='Наш сайт', url='https://habrahabr.ru')
	# markup.add(btn_my_site)
	# bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)
	link = 'https://en.wikipedia.org/wiki/'
	search_x = message.text[:13]
	weather_x = message.text[:9]
	link_short = message.text[:11]
	if message.chat.type == 'private':
		if message.text == '😊 Ի՞նչ կարող ես դու անել։':

			markup = types.InlineKeyboardMarkup(row_width=1)
			item1 = types.InlineKeyboardButton("Հիանալի է ❤️😁", callback_data='good')
			item2 = types.InlineKeyboardButton("Քիչ է, ինձ թուում է ինչ որ բան պակասում է 👎😢👎", callback_data='bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, help, reply_markup=markup)
		# elif link_short == '@short_url ':
			
			

		elif weather_x == '@weather ':
			
			owm = pyowm.OWM('80d409230f9bb45bd0b8dcd4c0f647ba')
			watching = owm.weather_at_place(message.text.replace('@weather ', ''))
			w = watching.get_weather()
			temp = w.get_temperature('celsius')['temp']
			# bot.send_message(message.chat.id, message.text)
			trans = Translator()
			w_stat = w.get_detailed_status()
			t = trans.translate(w_stat, src='en', dest='hy')

			print(f'{t.origin} -> {t.text}')
			answer = u'🌤 <b>' + message.text.replace('@weather ', '').title() + '</b>' + ' քաղաքում հիմա ' + str(temp) + '° է\n'

			if temp < 0:
				answer += 'Հիմա ահաւոր ցուրտ է, տաք կհագնուեք։'
			elif temp < 10:
				answer += 'Եղանակը այդքան էլ տաք չէ, խնդրում եմ տաք հագնուեք։'
			elif temp < 20:
				answer += 'Ներկայ պահին եղանակը նորմալ է, հագնուեք ինչպէս կկամենաք։'
			elif temp > 20:
				answer += 'Ահաւոոոոոոր շոգ է, հագնուեք շատ թեթեւ'
			sti = open('stickers/weather/AnimatedSticker.tgs', 'rb')
			if temp > 20:
				sti = open('stickers/shog.tgs', 'rb')
			bot.send_sticker(message.chat.id, sti)
			bot.send_message(message.chat.id, answer,  parse_mode='html')
		elif search_x == '@wiki_search ':
			# message.text.replace('@wiki_search', '')
		
			
			markup = types.InlineKeyboardMarkup(row_width=1)
			
			item2 = types.InlineKeyboardButton("Դիտել շարունակութիւնը wikipedia.com կայքում", callback_data='wikium')
			markup.add(item2)
			link += message.text.replace('@wiki_search ', '').replace(' ','_')
			print(message.text.replace('@wiki_search ', '').replace(' ','_'))
			bot.send_message(message.chat.id, u'🤘<b>' + message.text.replace('@wiki_search ', '').title() + '</b>🤙', parse_mode='html')
			bot.send_message(message.chat.id, wikipedia.summary(message.text.replace('@wiki_search ', ''), sentences=5),  reply_markup=markup)
			
		# else:
		# 	bot.send_message(message.chat.id, 'Ես նման տեղեկութեան չեմ տիրապետում։')
		# 	bot.send_message(message.chat.id, 'Եթէ ունէք բողոքներ կամ առաջարկներ, խնդրում եմ գրէք այս հարթակում։')
		# 	bot.send_message(message.chat.id, 'https://t.me/for1trio')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	global link
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'Ես ուրախ եմ, որ իմ ունակութիւնները բաւարարում են քո պահանջներին, բայց ես աւրեցաւր աւելի շատ բան եմ սովորում։❤️👍❤️')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'Խնդրում եմ ասա, թե ինչը չի համապատասխանում քո պահանջներին, եւ մաւտ ժամանակներս ես կփորձեմ այդ հարցում եւս աւգնել քեզ։ ❤️😢😏😏')
				bot.send_message(call.message.chat.id, 'Կարող ես քո բոլոր բողոքներն ու առաջարկները գրել այս քննարկման հարթակում։😅')
				bot.send_message(call.message.chat.id, 'https://t.me/for1trio')
			elif  call.data == 'wikium':
				global link
			
				bot.send_message(call.message.chat.id, link)
			elif  call.data == 'hraman':
			
				bot.send_message(call.message.chat.id, 'Դու կարող ես աւգտուել հետեւեալ հրամաններից՝')	
				bot.send_message(call.message.chat.id, '@weather «քաղաքի կամ տարածաշրջանի անունը» - իմանալ տուեալ տարածաշրջանի ջերմաստիճանի մասին։')
				bot.send_message(call.message.chat.id, '@wiki_search «հետաքրքրող թեմայի անունը» - ստանալ տեղեկութիւն հետաքրքրող թեմայի մասին։')
			else:
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😁",
				reply_markup=None)

	except Exception as e:
		print(repr(e))




bot.polling(none_stop=True)