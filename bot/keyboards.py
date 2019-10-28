from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import client


def LanguageKeyboard(user):

    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('Ўзбек тили'),
        KeyboardButton('Русский язык')
)

def PriceSetKeyboard(user):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        KeyboardButton('1'),
        KeyboardButton('2'),
        KeyboardButton('3'),
        KeyboardButton('4'),
        KeyboardButton('5'),)
        if client.getUserLanguage(user)=="RU":
                keyboard.add(KeyboardButton('⏮ Назад'))
        else:
                keyboard.add(KeyboardButton('⏮ Ортга'))
        return keyboard

def OnlineKeyboard(user):
        online = client.getAllOnline()
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

        for a in online:
               keyboard.add(KeyboardButton(a.name))

        if client.getUserLanguage(user)=="RU":
                keyboard.add(KeyboardButton('⏮ Назад'))
        else:
                keyboard.add(KeyboardButton('⏮ Ортга'))
        return keyboard

def OnlineKeyboardApply(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True
                        ).add(KeyboardButton("Сделать заказ")
                        ).add(KeyboardButton('⏮ Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True
                        ).add(KeyboardButton("Буюртма бериш")
                        ).add(KeyboardButton('⏮ Ортга'))


def AboutUsKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Как нас найти'),
                                KeyboardButton('Как связаться')
                        ).add(KeyboardButton('Задать вопрос'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Как нас найти'),
                                KeyboardButton('Как связаться')
                        ).add(KeyboardButton('Задать вопрос'))


def SendKeyboard(user):
	if client.getUserLanguage(user)=="RU":
		return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
						KeyboardButton('Отправить')
				).add(KeyboardButton('Отмена'))
	else:
		return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
						KeyboardButton('Отправить')
				).add(KeyboardButton('Отмена'))


def RoomKeyboard(user):
	if client.getUserLanguage(user)=="RU":
			buttons = []
			for region in client.getRooms():
					buttons.append(KeyboardButton("{}".format(region.title)))
			return ReplyKeyboardMarkup(keyboard=build_menu(buttons, 2, footer_buttons=KeyboardButton('⏮ Назад')),one_time_keyboard=True, resize_keyboard=True)
	else:
			buttons = []
			for region in client.getRooms("UZ"):
					buttons.append(KeyboardButton("{}".format(region.title)))
			return ReplyKeyboardMarkup(keyboard=build_menu(buttons, 2, footer_buttons=KeyboardButton('⏮ Ортга')),one_time_keyboard=True, resize_keyboard=True)

def ComplexKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Дополнительные услуги'),
                                KeyboardButton('Номера')
                        ).add(KeyboardButton('Прайс лист'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Дополнительные услуги'),
                                KeyboardButton('Номера')
                        ).add(KeyboardButton('Прайс лист'))


def MenuKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('О комплексе'),
                                KeyboardButton('Маршрут')
                        ).add(KeyboardButton('О нас'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('О комплексе'),
                                KeyboardButton('Маршрут')
                        ).add(KeyboardButton('О нас'))
    
def MoreKeyboard(user, num):
        if client.getUserLanguage(user)=="RU":
                return InlineKeyboardMarkup().add( 
                        InlineKeyboardButton(text='Ещё', callback_data=num))
        else:
                return InlineKeyboardMarkup().add(
                        InlineKeyboardButton(text='Яна', callback_data=num))

def SaleAndRentKeyboard(user):
# Эълон бериш

        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Подать объявление'),
                        KeyboardButton('Поиск 🔍')
                ).add(KeyboardButton('⏮ Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Эълон бериш'),
                        KeyboardButton('Қидирув 🔍')
                ).add(KeyboardButton('⏮ Ортга'))
    

def SaleSearchAndannouncementKeyboard(user):

        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('🏠 Участок'),
                        KeyboardButton('🏬 Квартира')
                ).row(
                        KeyboardButton('🏡 Участок земли'),
                        KeyboardButton('🏗 Коммерческая недвижимость')
                ).add(KeyboardButton('⏮ Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('🏠 Ховли'),
                        KeyboardButton('🏬 Квартира')
                ).row(
                        KeyboardButton('🏡 Ер'),
                        KeyboardButton('🏗 Тижорат кўчмас мулки')
                ).add(KeyboardButton('⏮ Ортга'))

    

def OnlineSaleAndRentKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Продажа'),
                                KeyboardButton('Аренда')
                        ).add(KeyboardButton('Поиск 🔍')
                        ).add(KeyboardButton('⏮ Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Сотув'),
                                KeyboardButton('Ижара')
                        ).add(KeyboardButton('Қидирув 🔍')
                        ).add(KeyboardButton('⏮ Ортга'))
        

def EditApplyKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Изменить'),
                        KeyboardButton('Отправить')
                ).add(KeyboardButton('⏮ Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Ўзгартириш'),
                        KeyboardButton('Юбориш')
                ).add(KeyboardButton('⏮ Ортга'))
        

def AdminApplyKeyboard(mode, num):
        return InlineKeyboardMarkup().row(
        InlineKeyboardButton(text='Подтвердить',callback_data="apply {} {}".format(mode, num)),
        InlineKeyboardButton(text='Удалить', callback_data="delete {} {}".format(mode, num)))

def SearchKeyboard(mode, user):
        if client.getUserLanguage(user)=="RU":
                if mode=="Участок":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Цена'),
                                KeyboardButton('Район'),
                                KeyboardButton('Комнаты'),
                                KeyboardButton('Сотки')).row(
                                        KeyboardButton('Поиск 🔍'),
                                        KeyboardButton('Очистить'),

                                ).add(
                                        KeyboardButton('⏮ Назад'),
                                )
                elif mode=="Квартира":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Цена'),
                                KeyboardButton('Район'),
                                KeyboardButton('Комнаты')).row(
                                        KeyboardButton('Поиск 🔍'),
                                        KeyboardButton('Очистить'),

                                ).add(
                                        KeyboardButton('⏮ Назад'),
                                )
                elif mode == "Участок земли":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Цена'),
                                KeyboardButton('Район'),
                                KeyboardButton('Комнаты'),
                                KeyboardButton('Сотки')).row(
                                        KeyboardButton('Поиск 🔍'),
                                        KeyboardButton('Очистить'),

                                ).add(
                                        KeyboardButton('⏮ Назад'),
                                )
                elif mode == "Коммерческая недвижимость":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Цена'),
                                KeyboardButton('Район'),
                                KeyboardButton('Комнаты'),
                                KeyboardButton('Сотки')).row(
                                        KeyboardButton('Поиск 🔍'),
                                        KeyboardButton('Очистить'),

                                ).add(
                                        KeyboardButton('⏮ Назад'),
                                )
        else:
                if mode=="Участок":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Нарх'),
                                KeyboardButton('Туман'),
                                KeyboardButton('Xoналар'),
                                KeyboardButton('Соток')).row(
                                        KeyboardButton('Қидирув 🔍'),
                                        KeyboardButton('Тозалаш'),

                                ).add(
                                        KeyboardButton('⏮ Ортга'),
                                )
                elif mode=="Квартира":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Нарх'),
                                KeyboardButton('Туман'),
                                KeyboardButton('Xoналар')).row(
                                        KeyboardButton('Қидирув 🔍'),
                                        KeyboardButton('Тозалаш'),

                                ).add(
                                        KeyboardButton('⏮ Ортга'),
                                )
                elif mode == "Участок земли":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Нарх'),
                                KeyboardButton('Туман'),
                                KeyboardButton('Xoналар'),
                                KeyboardButton('Соток')).row(
                                        KeyboardButton('Қидирув 🔍'),
                                        KeyboardButton('Тозалаш'),

                                ).add(
                                        KeyboardButton('⏮ Ортга'),
                                )
                elif mode == "Коммерческая недвижимость":
                        return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                                KeyboardButton('Нарх'),
                                KeyboardButton('Туман'),
                                KeyboardButton('Xoналар'),
                                KeyboardButton('Соток')).row(
                                        KeyboardButton('Қидирув 🔍'),
                                        KeyboardButton('Тозалаш'),

                                ).add(
                                        KeyboardButton('⏮ Ортга'),
                                )
        

def PhotoPaginationKeyboard(length, current, user):
        keyboard = InlineKeyboardMarkup()
        if current!=1:
                if current==length:
                        keyboard.row(
                                InlineKeyboardButton(text="<<", callback_data="pagination prev {}".format(current-1)),
                                InlineKeyboardButton(text="{}/{}".format(current, length), callback_data="pagination None"),
                                InlineKeyboardButton(text=">>", callback_data="pagination next {}".format(current+1)))
                else:
                        keyboard.row(
                                InlineKeyboardButton(text="<<", callback_data="pagination prev {}".format(current-1)),
                                InlineKeyboardButton(text="{}/{}".format(current, length), callback_data="pagination None"),
                                InlineKeyboardButton(text=">>", callback_data="pagination next {}".format(current+1)))
        else:
                keyboard.row(
                        InlineKeyboardButton(text="<<", callback_data="pagination prev {}".format(current-1)),
                        InlineKeyboardButton(text="{}/{}".format(current, length), callback_data="pagination None"),
                        InlineKeyboardButton(text=">>", callback_data="pagination next {}".format(current+1)))

        if client.getUserLanguage(user)=="RU":
                keyboard.row(InlineKeyboardButton(text="Изменить", callback_data="pagination change {}".format(current)),
                        InlineKeyboardButton(text="Удалить", callback_data="pagination delete {}".format(current)))
                keyboard.add(InlineKeyboardButton(text="Отмена", callback_data="pagination cancel"))
        else:
                keyboard.row(InlineKeyboardButton(text="Ўзгартириш", callback_data="pagination change {}".format(current)),
                        InlineKeyboardButton(text="Удалить", callback_data="pagination delete {}".format(current)))
                keyboard.add(InlineKeyboardButton(text="Бекор килиш", callback_data="pagination cancel"))
        
        


        return keyboard

        

def EditOnlineMarkup(data, user):
        _type = data[0]
        _property = data[1]
        _title = data[2]
        _region = data[3]
        _reference = data[4]
        _location = data[5]
        _room_count = data[6]
        _square = data[7]
        _area = data[8]
        _state = data[9]
        _ammount = data[10]
        _add_info = data[11]
        _contact = data[12]

        keyboard = InlineKeyboardMarkup()

        if client.getUserLanguage(user)=="RU":
                if _property == "Участок":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference"),
                                InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Состояние", callback_data="edit prop_state")
                        ).row(
                                InlineKeyboardButton(text="Площадь", callback_data="edit square"),
                                InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard

                elif _property == "Квартира":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference"),
                                InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Состояние", callback_data="edit prop_state")
                        ).add(
                                InlineKeyboardButton(text="Площадь", callback_data="edit square")
                        ).row(
                                InlineKeyboardButton(text="Этажи в доме", callback_data="edit main_floor"),
                                InlineKeyboardButton(text="Этаж квартиры", callback_data="edit floor")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Участок земли":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Состояние", callback_data="edit prop_state")
                        ).row(
                                InlineKeyboardButton(text="Площадь", callback_data="edit square"),
                                InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Коммерческая недвижимость":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard
        else:
                if _property == "Участок":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference"),
                                InlineKeyboardButton(text="Ҳоналар сони", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Даража", callback_data="edit prop_state")
                        ).row(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square"),
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard

                elif _property == "Квартира":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference"),
                                InlineKeyboardButton(text="Ҳоналар сони", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Даража", callback_data="edit prop_state")
                        ).add(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square")
                        ).row(
                                InlineKeyboardButton(text="Жами қаватлар", callback_data="edit main_floor"),
                                InlineKeyboardButton(text="Квартирангиз қавати", callback_data="edit floor")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Участок земли":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Даража", callback_data="edit prop_state")
                        ).add(
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Коммерческая недвижимость":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard


def EditOnlineSearchMarkup(data, user):
        _type = data[0]
        _property = data[1]
        _title = data[2]
        _region = data[3]
        _reference = data[4]
        _location = data[5]
        _room_count = data[6]
        _square = data[7]
        _area = data[8]
        _state = data[9]
        _ammount = data[10]
        _add_info = data[11]
        _contact = data[12]

        keyboard = InlineKeyboardMarkup()

        if client.getUserLanguage(user)=="RU":
                if _property == "Участок":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference"),
                                InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Состояние", callback_data="edit prop_state")
                        ).row(
                                InlineKeyboardButton(text="Площадь", callback_data="edit square"),
                                InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard

                elif _property == "Квартира":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference"),
                                InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Состояние", callback_data="edit prop_state")
                        ).add(
                                InlineKeyboardButton(text="Площадь", callback_data="edit square")
                        ).row(
                                InlineKeyboardButton(text="Этажи в доме", callback_data="edit main_floor"),
                                InlineKeyboardButton(text="Этаж квартиры", callback_data="edit floor")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Участок земли":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Состояние", callback_data="edit prop_state")
                        ).row(
                                InlineKeyboardButton(text="Площадь", callback_data="edit square"),
                                InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Коммерческая недвижимость":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard
        else:
                if _property == "Участок":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference"),
                                InlineKeyboardButton(text="Ҳоналар сони", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Даража", callback_data="edit prop_state")
                        ).row(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square"),
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard

                elif _property == "Квартира":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference"),
                                InlineKeyboardButton(text="Ҳоналар сони", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Даража", callback_data="edit prop_state")
                        ).add(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square")
                        ).row(
                                InlineKeyboardButton(text="Жами қаватлар", callback_data="edit main_floor"),
                                InlineKeyboardButton(text="Квартирангиз қавати", callback_data="edit floor")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Участок земли":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Даража", callback_data="edit prop_state")
                        ).add(
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Коммерческая недвижимость":
                        keyboard.add(
                                InlineKeyboardButton(text="Риелтор", callback_data="edit master"),
                        ).add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard      

def EditMarkup(data, user):
        _type = data[0]
        _property = data[1]
        _title = data[2]
        _region = data[3]
        _reference = data[4]
        _location = data[5]
        _room_count = data[6]
        _square = data[7]
        _area = data[8]
        _state = data[9]
        _ammount = data[10]
        _add_info = data[11]
        _contact = data[12]

        keyboard = InlineKeyboardMarkup()

        if client.getUserLanguage(user)=="RU":
                if _property == "Участок":
                        keyboard.add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference"),
                                InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).row(
                                InlineKeyboardButton(text="Площадь", callback_data="edit square"),
                                InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard

                elif _property == "Квартира":
                        keyboard.add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference"),
                                InlineKeyboardButton(text="Количество комнат", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Площадь", callback_data="edit square")
                        ).row(
                                InlineKeyboardButton(text="Этажи в доме", callback_data="edit main_floor"),
                                InlineKeyboardButton(text="Этаж квартиры", callback_data="edit floor")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Участок земли":
                        keyboard.add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).row(
                                InlineKeyboardButton(text="Площадь", callback_data="edit square"),
                                InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Коммерческая недвижимость":
                        keyboard.add(
                                InlineKeyboardButton(text="Недвижимость", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Описание", callback_data="edit title"),
                                InlineKeyboardButton(text="Район", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Ориентир", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Информация", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Количество соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Цена", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Контакты", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Подтвердить", callback_data="edit cancel"),
                        )
                        return keyboard
        else:
                if _property == "Участок":
                        keyboard.add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference"),
                                InlineKeyboardButton(text="Ҳоналар сони", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).row(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square"),
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard

                elif _property == "Квартира":
                        keyboard.add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).row(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference"),
                                InlineKeyboardButton(text="Ҳоналар сони", callback_data="edit room_count")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Умумий майдон", callback_data="edit square")
                        ).row(
                                InlineKeyboardButton(text="Жами қаватлар", callback_data="edit main_floor"),
                                InlineKeyboardButton(text="Квартирангиз қавати", callback_data="edit floor")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Участок земли":
                        keyboard.add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard
                elif _property == "Коммерческая недвижимость":
                        keyboard.add(
                                InlineKeyboardButton(text="Кўчмас мулк", callback_data="edit property"),
                        ).row(
                                InlineKeyboardButton(text="Тавсифи", callback_data="edit title"),
                                InlineKeyboardButton(text="Туман", callback_data="edit region")
                        ).add(
                                InlineKeyboardButton(text="Mўлжал", callback_data="edit reference")
                        ).add(
                                InlineKeyboardButton(text="Локация", callback_data="edit location")
                        ).add(
                                InlineKeyboardButton(text="Қўшимча  маълумот", callback_data="edit add_info")
                        ).add(
                                InlineKeyboardButton(text="Соток", callback_data="edit area")
                        ).row(
                                InlineKeyboardButton(text="Нарх", callback_data="edit ammount"),
                                InlineKeyboardButton(text="Телефон", callback_data="edit phone")
                        ).add(
                                InlineKeyboardButton(text="Фото", callback_data="edit photo"),
                        ).add(
                                InlineKeyboardButton(text="Тасдиқланг", callback_data="edit cancel"),
                        )
                        return keyboard



def BackKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('⏮ Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('⏮ Ортга'))


def RegionKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                buttons = []
                for region in client.getRegions():
                        buttons.append(KeyboardButton("#{}".format(region.title)))
                return ReplyKeyboardMarkup(keyboard=build_menu(buttons, 2, footer_buttons=KeyboardButton('⏮ Назад')),one_time_keyboard=True, resize_keyboard=True)
        else:
                buttons = []
                for region in client.getRegions():
                        buttons.append(KeyboardButton("#{}".format(region.title)))
                return ReplyKeyboardMarkup(keyboard=build_menu(buttons, 2, footer_buttons=KeyboardButton('⏮ Ортга')),one_time_keyboard=True, resize_keyboard=True)
        


def LocationKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('📍 Отправить геолокацию', request_location=True)).add(
                        KeyboardButton('Дальше')).add(
                        KeyboardButton('⏮ Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('📍 Геолокация юбориш', request_location=True)).add(
                        KeyboardButton('Ўтказиб юбориш')).add(
                        KeyboardButton('⏮ Ортга'))

def LocationKeyboardBack(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('📍 Отправить геолокацию', request_location=True)).add(
                        KeyboardButton('⏮ Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('📍 Геолокация юбориш', request_location=True)).add(
                        KeyboardButton('⏮ Ортга'))

    

def ContactKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Отправить свой контакт', request_contact=True)).add(
                    KeyboardButton('⏮ Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Телефон рақамингизни юбориш', request_contact=True)).add(
                    KeyboardButton('⏮ Ортга'))
    

def YesOrNoKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                        KeyboardButton('Продолжить')
                        ).add(
                        KeyboardButton('Отмена'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                        KeyboardButton('Давом еттириш')
                        ).add(
                        KeyboardButton('Бекор килиш'))
        

def RoomCountKeyboard(user):
        a= 1
        room_count = []
        while a<13:
                room_count.append(KeyboardButton(a))
                a+=1

        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(keyboard=build_menu(room_count, 4, footer_buttons=KeyboardButton('⏮ Назад')),one_time_keyboard=True, resize_keyboard=True)
        else:
                return ReplyKeyboardMarkup(keyboard=build_menu(room_count, 4, footer_buttons=KeyboardButton('⏮ Ортга')),one_time_keyboard=True, resize_keyboard=True)
        


def FreeAreaKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Строится'),
                        KeyboardButton('Новое')
                ).add(KeyboardButton('⏮ Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
                        KeyboardButton('Курилаётган'),
                        KeyboardButton('Янги')
                ).add(KeyboardButton('⏮ Назад'))
        


def BackNextKeyboard(user):
        if client.getUserLanguage(user)=="RU":
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                        KeyboardButton('Дальше')
                ).add(
                        KeyboardButton('⏮ Назад'))
        else:
                return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                        KeyboardButton('Ўтказиб юбориш')
                ).add(
                        KeyboardButton('⏮ Ортга'))
        


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu



                

    

SaleSearchAndannouncementKeyboardList = ['🏠 Участок', '🏬 Квартира', '🏡 Участок земли', '🏗 Коммерческая недвижимость', '🏠 Ховли', '🏡 Ер', '🏗 Тижорат кўчмас мулки']



    
    