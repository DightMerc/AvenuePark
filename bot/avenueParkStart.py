import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram.dispatcher import FSMContext

from messages import Messages

from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions, InputFile
from aiogram.types import ReplyKeyboardRemove

import client

import keyboards
from typing import Optional
import os
import aioredis

import states



logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                     level=logging.DEBUG)


bot = Bot(token=client.GetToken(), parse_mode=types.ParseMode.HTML)
# storage = RedisStorage2(db=6)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'], state="*")
async def process_start_command(message: types.Message, state: FSMContext):
    user = message.from_user.id

    if not client.userExsists(user):
        client.userCreate(message.from_user)

    await state.set_data({})
    
    await states.User.started.set()
    
    await bot.send_chat_action(user, action="typing")

    await bot.send_message(user, Messages(user)['start'].replace("{}", message.from_user.first_name))
    await bot.send_message(user, Messages(user)['language'], reply_markup=keyboards.LanguageKeyboard(user))


@dp.message_handler(state=states.User.started)
async def back_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    await states.User.language_set.set()

    if recieved_text == "🇷🇺 Русский язык":
        client.userSetLanguage(user, "RU")
    elif recieved_text == "🇺🇿 Ўзбек тили":
        client.userSetLanguage(user, "UZ")

    await bot.send_message(user, Messages(user)['menu'], reply_markup=keyboards.MenuKeyboard(user))


@dp.message_handler(state=states.User.language_set)
async def back_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text


    if recieved_text in ["🏘 О комплексе", "🏘 О комплексе"]:
        await states.User.aboutComplex.set()

        await bot.send_message(user, Messages(user)['aboutComplex'], reply_markup=keyboards.ComplexKeyboard(user))

        return

    elif recieved_text in ["📍 Маршрут", "📍 Маршрут"]:
        await states.User.language_set.set()

        await bot.send_location(user, latitude='41.595568', longitude="70.062756", reply_markup=keyboards.MenuKeyboard(user))
        await bot.send_message(user, Messages(user)['zoneLocation'], reply_markup=None)

        
        return

    elif recieved_text in ["О нас",""]:
        await states.User.aboutUs.set()

        await bot.send_message(user, Messages(user)['aboutUs'], reply_markup=keyboards.AboutUsKeyboard(user))

        return


@dp.message_handler(state=states.User.aboutUs)
async def back_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    states.User.aboutComplex.set()

    if recieved_text in ["📍 Как нас найти","📍 Как нас найти"]:
        await bot.send_message(user, Messages(user)['location'], reply_markup=keyboards.MenuKeyboard(user))

        await bot.send_location(user, latitude='41.331297', longitude="69.309561", reply_markup=keyboards.MenuKeyboard(user))

        await states.User.language_set.set()


    elif recieved_text in ["📞 Как связаться","📞 Как связаться"]:
        await bot.send_message(user, Messages(user)['contact'], reply_markup=keyboards.MenuKeyboard(user))

        await states.User.language_set.set()

    elif recieved_text in ["❔ Задать вопрос","❔ Задать вопрос"]:
        await states.User.askQuestion.set()

        await bot.send_message(user, Messages(user)['question'], reply_markup=None)


@dp.message_handler(state=states.User.aboutComplex)
async def back_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text


    if recieved_text in ["➕ Дополнительные услуги","➕ Дополнительные услуги"]:
        await states.User.language_set.set()

        await states.User.addPicture.set()

        await bot.send_message(user, Messages(user)['addService'], reply_markup=keyboards.AddKeyboard(user))

    elif recieved_text in ["🔑 Номера","🔑 Номера"]:
        await states.User.roomPicture.set()

        await bot.send_message(user, Messages(user)['roomPicture'], reply_markup=keyboards.RoomKeyboard(user))
    elif recieved_text in ["Прайс лист",""]:
        await states.User.language_set.set()

        await bot.send_message(user, Messages(user)['priceList'], reply_markup=keyboards.MenuKeyboard(user))


@dp.message_handler(state=states.User.askQuestion)
async def back_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    if not recieved_text in ["Отправить","Отмена", "", ""]:
        async with state.proxy() as data:
            data['question'] = recieved_text


        await bot.send_message(user, Messages(user)['realy'], reply_markup=keyboards.SendKeyboard(user))
        
    elif recieved_text in ["Отправить", ""]:
        await states.User.contact.set()

        await bot.send_message(user, Messages(user)['phone'], reply_markup=keyboards.ContactKeyboard(user))

        
    
    elif recieved_text in ["Отмена", ""]:
        await states.User.language_set.set()

        await bot.send_message(user, Messages(user)['menu'], reply_markup=keyboards.MenuKeyboard(user))


@dp.message_handler(state=states.User.contact, content_types=types.ContentType.CONTACT)
async def user_contact_handler(message: types.Message, state: FSMContext):

    user = message.from_user.id

    phone = message.contact.phone_number

    async with state.proxy() as data:
        data['phone'] = phone
    await states.User.language_set.set()

    await bot.send_message(user, Messages(user)['menu'], reply_markup=keyboards.MenuKeyboard(user))

    async with state.proxy() as data:
        text = f"#вопрос\n{data['phone']}\n\n{data['question']} "
    await bot.send_message(-1001396301873, text=text, reply_markup=None)


@dp.message_handler(state=states.User.addPicture)
async def back_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    # try:
    room = client.getAdd().get(title=recieved_text)


    if client.getUserLanguage(user)=="RU":
        text = room.descriptionRU
    else:
        text = room.descriptionUZ

    room_photoes = room.photoes.all()
    if room_photoes.count()!=1:

        media = []

        for photo in room_photoes:
            

            media.append(InputMediaPhoto(InputFile(os.path.join(client.start_path, "bothelper","media", str(photo.photo).replace("media/", "")))))

        await states.User.language_set.set()

        await bot.send_media_group(user, types.MediaGroup(media))
        await bot.send_message(user, text=text, reply_markup=keyboards.MenuKeyboard(user))

    else:

        await states.User.language_set.set()

        await bot.send_photo(user, InputFile(os.path.join(client.start_path, "bothelper","media", str(room_photoes[0].photo).replace("media/", ""))))
        await bot.send_message(user, text=text, reply_markup=keyboards.MenuKeyboard(user))
    

    # except Exception as e:
    #     await bot.send_message(user, text=str(e), reply_markup=None)

@dp.message_handler(state=states.User.roomPicture)
async def back_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    # try:
    room = client.getRooms().get(title=recieved_text)


    if client.getUserLanguage(user)=="RU":
        text = room.descriptionRU
    else:
        text = room.descriptionUZ

    room_photoes = room.photoes.all()
    if room_photoes.count()!=1:

        media = []

        for photo in room_photoes:
            

            media.append(InputMediaPhoto(InputFile(os.path.join(client.start_path, "bothelper","media", str(photo.photo).replace("media/", "")))))

        await states.User.language_set.set()

        await bot.send_media_group(user, types.MediaGroup(media))
        await bot.send_message(user, text=text, reply_markup=keyboards.MenuKeyboard(user))

    else:

        await states.User.language_set.set()

        await bot.send_photo(user, room.photo.all()[0].photo)
        await bot.send_message(user, text=text, reply_markup=keyboards.MenuKeyboard(user))
    

    # except Exception as e:
    #     await bot.send_message(user, text=str(e), reply_markup=None)
        
    
    


@dp.message_handler(state=states.User.aboutUs)
async def back_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    recieved_text = message.text

    await states.User.aboutComplex.set()

    if recieved_text in ["➕ Дополнительные услуги","➕ Дополнительные услуги"]:
        await bot.send_message(user, Messages(user)['menu'], reply_markup=keyboards.ComplexKeyboard(user))

    elif recieved_text in ["Номера",""]:
        await bot.send_message(user, Messages(user)['menu'], reply_markup=keyboards.ComplexKeyboard(user))
    elif recieved_text in ["Прайс лист",""]:
        await bot.send_message(user, Messages(user)['menu'], reply_markup=keyboards.ComplexKeyboard(user))


@dp.message_handler(text="⏮ Назад", state="*")
async def back_handler(message: types.Message, state: FSMContext):
    user = message.from_user.id
    current_state = await dp.current_state(user=message.from_user.id).get_state()

    if current_state in ["Sale:started", "Rent:started", "OnlineSearch:type_choosen", "OnlineSearch:title_added", "OnlineSearch:region_added", "OnlineSearch:region_added"]:

        await states.User.language_set.set()

        photoes = os.listdir(os.getcwd()+"/Users/"+str(user)+"/")
        for a in photoes:
            os.remove(os.getcwd()+"/Users/"+str(user)+"/" + a)

        text = Messages(user)['choose_action_after_language']
        markup = keyboards.MenuKeyboard(user)
        await bot.send_message(user, text, reply_markup=markup)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'])


@dp.message_handler(state='*', commands=['setstate'])
async def process_setstate_command(message: types.Message):
    argument = message.get_args()
    state = dp.current_state(user=message.from_user.id)
    if not argument:
        await state.reset_state()
        return await message.reply(MESSAGES['state_reset'])

    if (not argument.isdigit()) or (not int(argument) < len(TestStates.all())):
        return await message.reply(MESSAGES['invalid_key'].format(key=argument))

    await state.set_state(TestStates.all()[int(argument)])
    await message.reply(MESSAGES['state_change'], reply=False)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    if not os.path.exists(os.getcwd()+"/Users/"):
        os.mkdir(os.getcwd()+"/Users/", 0o777)
        
    executor.start_polling(dp, on_shutdown=shutdown)