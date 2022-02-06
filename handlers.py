from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, state

from app import dp
from states import *
from functions import *

################################## show ############################################


@dp.message_handler(Command("show"))
async def add_menu(message: types.Message):
    await message.answer(f'Вес(гр) | Продукт \n{show_food()}')
    await message.answer(f"Cодержание нутриентов в суточном рационе: \n{show_calculate(calculate())}")


################################## add ############################################

@dp.message_handler(Command("add"))
async def add_menu(message: types.Message):
    await message.answer('Write food for adding:')
    await actions.find.set()


@dp.message_handler(state=actions.find)
async def find_menu(message: types.Message, state: FSMContext):
    find_row = find_food(message.text)
    if show_find_food(find_row) is False:
        await message.answer('продукты не найдены, повторите поиск')
        return

#    elif len(show_find_food(find_row)) > 1000:
#        await message.answer('найдено очень много продуктов, повторите поиск')
#        return

    await state.update_data({
            'row': find_row,
            })

    await message.answer('choose and write number of food:')
    await message.answer(show_find_food(find_row))

    await actions.choose.set()


@dp.message_handler(state=actions.choose)
async def weight_menu(message: types.Message, state: FSMContext):
    data = await state.get_data()
    row_food = data.get("row")


    if str(message.text).isdigit == False or int(message.text) not in row_food:
        await message.answer(f'ошибка при вводе! Доступные номера: {row_food}')
        return


    await message.answer('write weight for it (g):')

    row_food = message.text
    await state.update_data({
            'food': row_food,
            })
    await actions.weight.set()


@dp.message_handler(state=actions.weight)
async def weight_menu(message: types.Message, state: FSMContext):

    data = await state.get_data()
    row_food = data.get("food")
    if message.text.isdigit() == False:
        await message.answer('ошибка, введите массу')
        return

    weight = message.text

    save_food(row_food, weight)
    await message.answer(f'Успешно добавлено! Ваша таблица продуктов:')
    await message.answer(f'Вес(гр) | Продукт \n{show_food()}')

    # await message.answer("Cодержание нутриентов в суточном рационе:")
    # await message.answer(show_calculate(calculate()))

    await state.finish()


################################## del  ############################################

@dp.message_handler(Command("del"))
async def weight_menu(message: types.Message, state: FSMContext):
    await message.answer(show_del_food())
    await message.answer("Выбрерите номер для удаления")
    await actions.remove.set()


@dp.message_handler(state=actions.remove)
async def weight_menu(message: types.Message, state: FSMContext):
    if str(message.text).isdigit == False:
        await message.answer(f'ошибка при вводе! Доступные номера:')
        return
    del_food(int(message.text))
    await message.answer("Успешно удалено!")
    await message.answer(show_del_food())
    await state.finish()




################################## commands ############

@dp.message_handler()
async def add_menu(message: types.Message):
    await message.answer('Доступные команды \n/show\n/add\n/del')





