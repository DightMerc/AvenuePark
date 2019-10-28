from aiogram.dispatcher.filters.state import State, StatesGroup


class User(StatesGroup):
    started = State() 
    language_set = State() 

    aboutComplex = State()
    path = State()
    aboutUs = State()

    askQuestion = State()
    addService = State()
    roomPicture = State()
    priceList = State()

    ammount_set = State()
    add_info = State()
    contact = State()
    edit = State()