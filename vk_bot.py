#3be1fc3679dc9b366750ea893cb9cde97c93d4cf920cb522bcffad69ab0f547ed33370a3aba59b946a1c2
#3be1fc3679dc9b366750ea893cb9cde97c93d4cf920cb522bcffad69ab0f547ed33370a3aba59b946a1c2
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

sth_wrong = ['Ты определённо делаешь что-то не так.', 'Попробуй ещё раз', 'Давай ещё разок',
             'Это было близко, но всё-таки не то, что я хочу от тебя услышать.', 'НЕ ТО!!!']

world_list = ['Канон', 'Нереальный Пидорасинг', 'Родомагия +++', 'Все гады']

caracter = []

Yaoi = True
System = False
Luck = False
Regen = False
Mental = False

def main():
    vk_session = vk_api.VkApi(
        token='3be1fc3679dc9b366750ea893cb9cde97c93d4cf920cb522bcffad69ab0f547ed33370a3aba59b946a1c2')

    longpoll = VkBotLongPoll(vk_session, group_id=192035692)

    lpl = longpoll.listen()

    for event in longpoll.listen():

        vk.messages.send(user_id=event.obj.message['from_id'],
                         message=f"Спасибо, что присоединились к нашему проекту 'Попадун'. \n"
                                 f"Чтобы начать новую жизнь, напишите Start \n"
                                 f"Чтобы узнать что это за хрень, напишите Help",
                         random_id=random.randint(0, 2 ** 64))
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                done = False
                while not done:
                    if 'start' in request.lower():
                        write_msg(event.user_id, "Тогда начнём!")
                        done = True
                    elif 'help' in request.lower():
                        write_msg(event.user_id, "'Попадун' - текстовая РПГ, "
                                                 "описывающая жизнь самого обычного попаданца в зеркало мира Гарри Поттера. "
                                                 "И именно вы сможете выбрать, станет ли ваш герой мега-нагибатором, "
                                                 "или же умрёт в первую неделю попадания."
                                                 " Сложный выбор, опасные приключения, искромётный(нет) юмор и,"
                                                 " конечно же, магия! "
                                                 "Для начала вашего попадания напишите Start")
                    else:
                        write_msg(event.user_id, random.choice(sth_wrong))
                gods_to_give_you_POWER(lpl)

def gods_to_give_you_POWER(event):
    write_msg(event.user_id, f'Жил был на свете самый обычный российский ШКОЛЬНИК '
                             f'(oh god, заявка на оригинальность, да?! Не ОРС, А ОРШ!!! Я сама неожиданность!)\n'
                             f'И был он большим фанатом саги о Гарри Поттере. Читал все книги, смотрел все фильмы, '
                             f'и, конечно же, прочёл кучу фанфиков по этому произведению. \n'
                             f'Так что не особо удивился тому, что после смерти от столкновения '
                             f'с развившим приличную скорость '
                             f'грузовиком не оказался в раю, или там аду, а оказался чёрти где, '
                             f'то есть в классической попаданческой темноте. ')
    time.sleep(15)
    write_msg(event.user_id, f'Неожиданно прямо перед рожей нашего героя появился древний на вид свиток, '
                             f'перевязанный чёрной лентой. Раскрыв его, ОРШ смог прочитать '
                             f'(Да, в прочитать в темноте. Это МАГИЯ!) следующий текст:')
    time.sleep(10)
    write_msg(event.user_id, f'Поздравляем! \n'
                             f'Благодаря вашей "огромной" удаче вы были избраны богами для попадания '
                             f'в одно из зеркал мира вашего любимого мира "Поттериана". '
                             f'Так же, будучи нашим миллионным попаданцем, '
                             f'вы можете выбрать себе одну из представленных в списке ниже дополнительных способностей.'
                             f'Выбирайте с умом - от вашего выбора будет зависить ваша новая жизнь! \n \n'
                             f'Подпись: Смерть, Судьба и Магия.')
    time.sleep(15)
    write_msg(event.user_id, f'Список Доступных Способностей:\n'
                             f'1) Система\n'
                             f'2) 100% отсутствие слэша\n'
                             f'3) Удача Божественного Левела\n'
                             f'4) Регенерация "Росомаха нервно курит в сторонке\n"'
                             f'5) Полная защита от ментальных вмешательств\n \n '
                             f'З.Ы. Чтобы выбрать один из пунктов, напишите "беру @номер способности@!".\n'
                             f'Чобы узнать о способности больше, напишите "@номер способности@ что это?"')
    done = False
    while not done:
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                if 'что это' in request.lower():
                    if '1' in request.lower():
                        write_msg(event.user_id, 'Система - интерфейс по типу игрового, '
                                                 'позволяющий удобно делать штуки, '
                                                 'с трудом достающиеся обычным обитателям мира')
                    elif '2' in request.lower():
                        write_msg(event.user_id, 'Никакого яоя и юри! '
                                                 'Никто из парней не посягнёт на вашу мужскую честь. НИКТО.')
                    elif '3' in request.lower():
                        write_msg(event.user_id, 'Пока есть хоть кусочек - вы живы!')
                    elif '4' in request.lower():
                        write_msg(event.user_id, 'Вам везёт во всём! И никто не может ничего с этим поделать')
                    elif '5' in request.lower():
                        write_msg(event.user_id, 'Эта способность даёт вам полную защиту от проникновения ДДД, '
                                                 'Волдеморды и прочих мозгоклюев в ваше сознание.')
                elif 'беру' in request.lower():
                    if '1' in request.lower():
                        System = True
                        universe = random.choose(world_list)
                        done = True
                    elif '2' in request.lower():
                        Yaoi = False
                        universe = random.choose(world_list.remove([1]))
                        done = True
                    elif '3' in request.lower():
                        Regen = True
                        universe = random.choose(world_list)
                        done = True
                    elif '4' in request.lower():
                        Luck = True
                        universe = random.choose(world_list)
                        done = True
                    elif '5' in request.lower():
                        Mental = True
                        universe = random.choose(world_list)
                        done = True

                else:
                    write_msg(event.user_id, random.choice(sth_wrong))


def before_hog_1(sys, reg, luck, mental, universe, event, caracter, yaoi=True):
    write_msg(event.user_id, 'Выбрав наиболее понравившийся ему в списке пункт, '
                             'ОРШ громко прокричал его номер в пустоту. Неожиданоо его закрутило и завертело; '
                             'тело парня скрутило жгучей болью, но он даже не смог облегчить её закричав: '
                             'всё его тело парализовало, и он не мог издать ни звука. '
                             'Но после нескольких мгновений этой пытки, '
                             'растянувшейся для нашего героя на целую вечность, он потерял сознание.')
    time.sleep(15)
    write_msg(event.user_id, 'Очнулся новоиспечённый Гарри Поттер уже в чулане под лестницей. '
                             'По громогласному храпу, доносящемуся сверху, было ясно, что Дурсли ещё спят. '
                             'Что же наш вселенец сделает в первую очередь?')
    if sys:
        write_msg(event.user_id, f'1) Устроить набег на холодильник Дурслей. Жрать хочется - жуть!\n'
                                 f'2) Дождаться пробуждения всего семейства Дурслей.\n'
                                 f'3) Пойти наорать на Дурсля-старшего. Все попаданцы так делают, чем я хуже?!\n'
                                 f'4) Время паники!\n'
                                 f'5) Громко (чтобы уж наверняка) крикнуть "СИСТЕМА"!')
    elif not sys:
        write_msg(event.user_id, f'1) Устроить набег на холодильник Дурслей. Жрать хочется - жуть!\n'
                                 f'2) Дождаться пробуждения всего семейства Дурслей.\n'
                                 f'3) Пойти наорать на Дурсля-старшего. Все попаданцы так делают, чем я хуже?!\n'
                                 f'4) Время паники!')
    done = False
    while not done:
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                if request == '1':
                    if luck:
                        write_msg(event.user_id, 'Поев и не наткнувшись ни на одного представителя семейки, '
                                                 'с членами которой ему ещё жить некоторое время, '
                                                 'Гарри решил оставшееся время до подъёма просидеть в чулане, '
                                                 'уплетая за обе щёки честно добытые припасы.')
                        done = True
                    elif not luck:
                        write_msg(event.user_id, f'Неожиданно, на самом интересном месте '
                                                 f'(поедании какого-то супа прямо из кастрюли) '
                                                 f'в кухню ворвался толстый высокий мужчина с пышными усами. \n'
                                                 f'Дядя Вернон, понял Поттер. \n'
                                                 f'Увидев в руках нашего героя уже почти пустую кастрюлю '
                                                 f'своего любимого крем-супа, Вернон проревел: \n-Убью!\n'
                                                 f'то, что его дни сочтены, Поттер тоже очень хорошо понял, '
                                                 f'а потому резко стартанул в сторону спасительной двери на улицу.\n'
                                                 f'Увы и ах, удача снова оказалась не на стороне нашего героя, '
                                                 f'так что все оставшиеся три недели до своего одиннадцатого '
                                                 f'дня рождения он провёл в больничке, '
                                                 f'где ему лечили несколько переломов, вывихов и сотрясение мозга ')
                        done = True
                elif request == '2':
                    pass
                elif request == '3':
                    if luck:
                        write_msg(event.user_id, f'Нашему герою космически повезло - '
                                                 f'Вернона не было дома, '
                                                 f' и пункт "Наорать на Дурсля" откладывался на неопределённый срок.')
                    else:
                        write_msg(event.user_id, f'Поднявшись на второй этаж, Поттер обнаружил Вернона  ')
                elif request == '4':
                    if sys:
                        write_msg(event.user_id, f'\n ***\n'
                                                 f'Оставшееся до Хогвартса время наш герой провёл в дурке.'
                                                 f' Зато получил звание "Шизоид" и '
                                                 f'хорошо прокачал умение рисовать говном на стенах!')
                    else:
                        write_msg(event.user_id, f'\n ***\n'
                                                 f'Оставшееся до Хогвартса время наш герой провёл в дурке.')
                elif request == '5':
                    if sys:
                        write_msg(event.user_id, f'Для начала нужно разобраться с системой - '
                                                 f'решил новоиспечённый Герой, и громко крикнул '
                                                 f'\n-"СТАТУС"! \n'
                                                 f'\n ***\n'
                                                 f'Оставшееся до Хогвартса время наш герой провёз в дурке.'
                                                 f' Зато получил звание "Шизоид" и '
                                                 f'хорошо прокачал умение рисовать говном на стенах!')
                        done = True
                    else:
                        write_msg(event.user_id, random.choice(sth_wrong))




if __name__ == '__main__':
    main()