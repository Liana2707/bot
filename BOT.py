
from telebot import types
import telebot

import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

#params = {'access_key': '27f47f7266ba207c922fad485394b51f'}
params = {'access_key': '1c2256e16558fb7d66a1a21874b2476d'}
bot = telebot.TeleBot('1710915632:AAHDC6AH1UKCUvztXm8-eRrClXfb9iOTetg')

def get_data(name):
    a = []
    dates = []



    cur_date = datetime.now()
    for _ in range(30):


        cur_date -= timedelta(days=1)


        url = 'http://api.marketstack.com/v1/tickers/' + name + '/eod/' + cur_date.strftime('%Y-%m-%d')



        res = requests.get(url, params).json()



        if not res:
            continue



        a.append(res['close'])
        dates.append(cur_date.strftime('%Y-%m-%d'))


    return {'data': a[::-1], 'dates': dates[::-1]}

def plot(d):


    import matplotlib
    matplotlib.use('Agg')
    plt.style.use('dark_background')
    plt.grid(True)
    plt.xticks(rotation=90)

    plt.plot(d['dates'], d['data'])

    plt.savefig('plot.png', bbox_inches='tight')
    plt.cla()

    return d



@bot.message_handler(commands=['Apple'])
def apple(message):
    plot(get_data('AAPL'))
    photo1 = open('plot.png', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['Microsoft'])
def msft(message):
    plot(get_data('MSFT'))
    photo2 = open('plot.png', 'rb')
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['Google'])
def ggl(message):
    plot(get_data('GOOGL'))
    photo3 = open('plot.png', 'rb')
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['Amazon'])
def amzn(message):
    plot(get_data('AMZN'))
    photo4 = open('plot.png', 'rb')
    bot.send_photo(message.chat.id, photo4)
    bot.send_photo(message.chat.id, "FILEID")


@bot.message_handler(commands=['Facebook'])
def fb(message):
    plot(get_data('FB'))
    photo5 = open('plot.png', 'rb')
    bot.send_photo(message.chat.id, photo5)
    bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вся информация, представленная здесь, носит информационный характер и не призывает к каким-либо действиям. Инвестирование на бирже сопряжено с риском.')
    photo = open('Привет!.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    markupstart = telebot.types.InlineKeyboardMarkup()
    markupstart.add(telebot.types.InlineKeyboardButton(text='1.Типы инвесторов', callback_data='1.Типы инвесторов'))
    markupstart.add(telebot.types.InlineKeyboardButton(text='2.Акции', callback_data='2.Акции'))
    markupstart.add(telebot.types.InlineKeyboardButton(text='3.Облигации', callback_data='3.Облигации'))
    markupstart.add(telebot.types.InlineKeyboardButton(text='4.Фонды', callback_data='4.Фонды'))
    markupstart.add(telebot.types.InlineKeyboardButton(text='5.Комиссии', callback_data='5.Комиссии'))
    markupstart.add(telebot.types.InlineKeyboardButton(text='6.Налоги и льготы', callback_data='6.Налоги и льготы'))

    bot.send_message(message.chat.id, text="Привет! О чём вы хотите узнать подробнее?", reply_markup=markupstart)
    bot.send_message(message.chat.id, text='Хочешь построить график? Используй /Menu')

@bot.message_handler(commands=['Menu'])
def key_buttons(message):

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    apple = telebot.types.KeyboardButton('/Apple')
    microsoft = telebot.types.KeyboardButton('/Microsoft')
    google=telebot.types.KeyboardButton('/Google')
    amazon=telebot.types.KeyboardButton('/Amazon')
    facebook=telebot.types.KeyboardButton('/Facebook')
    startb = telebot.types.KeyboardButton('/start')
    markup.row(apple, microsoft,google)
    markup.row(amazon,facebook)
    markup.row(startb)
    bot.send_message(message.chat.id,'Выбери компанию', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def step_four(call):
    try:
        if call.message:
            id1 = call.message.chat.id
        if call.data == '/Menu':
            bot.send_message(id1, '/Menu', reply_markup=markup)
        if call.data == '1.Типы инвесторов':
            photo = open('Типы инвесторов.jpg', 'rb')
            bot.send_photo(id1, photo)
            bot.send_message(id1, '1. Типы инвесторов \n'
                                  ' Чтобы определиться с тем, какой ты инвестор, нужно понять, сколько времени ты готов тратить'
                                  'на инвестирование и как сильно готов рисковать.' 
                                  ' Выделяют 3 основных типа инвесторов: \n 1)Консерваторы \n 2)Среднестатистические инвесторы '
                                  '\n 3)Трейдеры \n Поговорим о каждом подробнее')
            bot.send_message(id1, 'Консерваторы \n Речь идёт про людей, которые не разбираются в устройстве биржи, не рассчитывают на '
                                  'большую доходность, практически не рискуют. Их основная цель - сохранить деньги. '
                                  'Основной тип инструментов на бирже - облигации. ')
            bot.send_message(id1, 'Среднестатистические инвесторы \n Эти ребята уже готовы на больший риск по сравнению с консерваторами, '
                                  'но всё также они не хотят уделять много времени бирже. Их основной инструмент - фонды. Также как и консерваторы'
                                  'среднестатистические инвесторы готовы к долгосрочным инвестициям ')
            bot.send_message(id1, 'Трейдеры \n Спекулятивную стратегию не советуют новичкам, потому что она требует серьёзной '
                                  'вовлечённости и знаний об устройстве рынка. Однозначно, придерживаясь этой стратегии, люди очень сильно '
                                  'рискуют. Новички могут потерять много денег, занимаясь трейдингом. Но если человек опытен, то его доходность на '
                                  'бирже будет самой высокой. Основной инструмент трейдеров - акции')


        if call.data == '2.Акции':
            photo = open('Акции.jpg', 'rb')
            bot.send_photo(id1,photo)
            bot.send_message(id1, '2. Акции \n Поговорим о ценных бумагах, которые дают возможность учавствовать в управлении компанией.'
                                  ' По сути, покупая акцию, вы становитесь совладельцом компании. У вас появляются возможности:\n'
                                  '1) Право получать дивиденды(часть прибыли компании)\n'
                                  '2) Право получить часть имущества компании в случае ее ликвидации.\n'
                                  '3) Право голосовать на собрании акционеров(например, по поводу выплаты дивидендов)')
            bot.send_message(id1, 'Доход с акций - это дивиденды и рост цены акции. Размер выплаты дивидендов обсуждается на акционерном собрании.'
                                  'Это, в первую очередь, вопрос стратегии:\n'
                                  'Высокие дивиденды привлекают акционеров, но компании нужно тратить деньги на их выплату. Низкие'
                                  ',наоборот, не привлекают акционеров, но компании не нужно тратить деньги.\n'
                                  'Существуют акции роста и акции стоимости. Заработок с первых из них можно осуществить за счёт их перепродаж, а основной'
                                  'доход со вторых - дивиденды. Цена бумаги также зависит от выплаты дивидендов по ней. Также акции бывают '
                                  'обыкновенные(дают прямое право голосовать) и привилегированные(у владельцев нет права голосовать, но у них есть преимущество при'
                                  'выплате дивидендов, т.е. прибыль может быть увеличена в зависимости от решения компании')
        if call.data == '3.Облигации':
            photo = open('Облигации.jpg', 'rb')
            bot.send_photo(id1, photo)
            bot.send_message(id1, '3. Облигации \n Так называют бумаги, по которым вы даёте компании, государству или региону в долг.'
                                  'Иммитентами считают тех, кому можно дать в долг. Доход с облигаций - выплата процентов, как в банке.'
                                  '\n Доходность по облигациям(в %) публичная оценка стоимости долга компании. Чем надёжнее компания, которой'
                                  'вы даёте в долг, тем стоимость долга для неё ниже. ')
            bot.send_message(id1, 'Чем же отличаются облигации и депозиты в банке? '
                                  'Банки: \n ✅Есть страхование \n ✅Нельзя закрыть раньше срока без потери процентов \n ✅Процент ниже чем по облигациям'
                                  '\n ✅Дороже обходятся банкам \n Облигации: \n ✅Нет страхования \n ✅Есть возможность продать бумагу досрочно без потери процентов'
                                  '\n ✅Процент выше \n ✅Дешевле обходятся банкам \n ✅Более рискованно')
            bot.send_message(id1, 'Акции и облигации по-разному зависят от бизнеса. Акции могут расти, даже если бизнес не имееет огромной'
                                  'выручки. Это происходит потому, что стоимость акций в большей степени зависит от веры людей.')
        if call.data == '4.Фонды':
            photo = open('Фонды.jpg', 'rb')
            bot.send_photo(id1, photo)
            bot.send_message(id1, '4.Фонды \n Зачастую возникают сложности с управлением собственным портфелем и покупкой акций иностранных'
                                  'компаний ввиду высокой стоимости. Именно поэтому можно поручить управление человеку, который будет в этом разбираться.'
                                  'Для этого создан специальный инструмент, называемый "фонды". Так называют готовые портфели, покупая '
                                  'которые вы преобретаете маленькие кусочки акций и облигаций. Иностранные фонды получили название Exchange Traded Funds (ETF).'
                                  'Некоторые фонды выплачивают купоны и дивиденды, но зачастую они реинвестируются обратно в фонд. То есть на эти деньги'
                                  'покупаются новые ценные бумаги. ')

        if call.data == '5.Комиссии':
            photo = open('Комиссии.jpg', 'rb')
            bot.send_photo(id1, photo)
            bot.send_message(id1, '5. Комиссии \n Для того, чтобы преобретать на бирже ценные бумаги, необходимо выбрать брокера.'
                                  'Брокер - посредник между инвестором и биржей. Он необходим по законодательству. Чаще всего, '
                                  'банки предоставляют брокерское обслуживание. Комиссии обычно меньше, если банк и броккер и ваш личный банк'
                                  ' - одно юридическое лицо.'
                                  'Основным доходом брокера являются комиссии. Когда мы покупаем акции, мы должны заплатить комиссию как брокеру(0,005 - 0,3 %), так и бирже(0,01 % от операций)'
                                  'Существуют брокеры, которые выставляют единый счёт за комисии, есть те, которые выставляют раздельно. ')
        if call.data == '6.Налоги и льготы':
            photo = open('Налоги.jpg', 'rb')
            bot.send_photo(id1, photo)
            bot.send_message(id1, '6. Налоги \n Налоги выплачиваются в конце календарного года(13%). Их считает брокер. Если нет фиксированной прибыли, то нужно писать '
                                  'декларацию в налоговую. Дивиденды облагаются налогом сразу. \n Если в конце календарного года прибыли нет, то бумагу выгодно продать, зафиксировав убыток, чтобы бумага не облагалась налогом'
                                  ' Фонды не платят налог на прибыль. Если вы стали долгосрочным инвестором, купили и заработали на росте ценных бумаг, льгота позволяет не платить налог на доход.'
                                  ' Опять-таки, в случае долгосрочного инвестирования нужно подать декларацию в налоговую. ')
            bot.send_message(id1, ' Самый популярный способ не платить налоги - открыть ИИС(индивидуальный инвестиционный счёт). Он бывает двух типов: \n'
                                  '1) Тип А. На него можно взносить до 1 млн рублей, налоговая возвращает вам 13%, но не более чем 52 тысячи рублей. Актуально только для тех, у кого есть официальный доход\n'
                                  '2) Тип В. Вы не платите налог на доход с биржевых сделок. ИИС типа Б оформляется после закрытия счета и вывода денег.')
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True, interval=0)






