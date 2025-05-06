import subprocess

from aiogram import F, Router, types

router = Router()

@router.message(F.text)
async def call(message: types.Message):
    comand = message.text
    array = []
    for helf in comand.split():
        array.append(f"{helf}")
    result = subprocess.run(
        array,
        capture_output=True,
        text=True,
    )
    await message.answer(result.stdout)
    if result.stderr:
        await message.answer("STDERR:", result.stderr)
