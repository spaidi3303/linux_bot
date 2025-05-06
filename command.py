import os
import subprocess
from aiogram import F, Router, types
router = Router()

@router.message(F.text)
async def execute_command(message: types.Message):
    user_command = message.text.strip()
    if "|" in user_command:
        for half in user_command.split("|"):
            half = half.strip()
            await execute_comm(message, half)
    else:
        await execute_comm(message, user_command)


async def execute_comm(message: types.Message, command: str):
    try:
        if command.strip().startswith('cd '):
            new_dir = os.path.expanduser(command.strip()[3:].strip())
            try:
                os.chdir(new_dir)
                current_dir = os.getcwd()
                await message.answer(f"📂 Текущая директория изменена на:\n<code>{current_dir}</code>",
                                     parse_mode="HTML")
                return
            except Exception as e:
                await message.answer(f"❌ Ошибка cd:\n<code>{str(e)}</code>",
                                     parse_mode="HTML")
                return
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        response = []
        if result.stdout:
            response.append(f"✅ Результат:\n<code>{result.stdout}</code>")
        if result.stderr:
            response.append(f"⚠️ Ошибка:\n<code>{result.stderr}</code>")
        if result.returncode == 0 and not (result.stdout or result.stderr):
            response.append("ℹ️ Команда выполнена успешно (нет вывода)")

        if response:
            await message.answer("\n\n".join(response), parse_mode="HTML")

    except subprocess.TimeoutExpired:
        await message.answer("⌛ Превышено время выполнения команды (10 сек)")
    except FileNotFoundError:
        await message.answer("❌ Команда или файл не найдены")
    except Exception as e:
        await message.answer(f"⛔ Критическая ошибка:\n<code>{str(e)}</code>",
                             parse_mode="HTML")