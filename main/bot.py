import asyncio
from aiogram import Bot
API_TOKEN = "5260989327:AAGMxI_429gf-xggNXqDfsIL8hUYVX4ZsUY"
MY_API = 668618297

async def send_message(message):
    operator = Bot(token=API_TOKEN)
    await operator.send_message(MY_API, message)

def send_form_bot(name,email,tel,company_name,mc,dry_van,reefer,flat_bed,message,need_driver_assistence):
    asyncio.run(send_message(f"\nA NEW QUOTE\n\nNAME:\n{name}\n\nEMAIL:\n{email}\n\nPHONE:\n{tel}\n\nCOMPANY NAME:\n{company_name}\n\nMC# :\n{mc}\n\nDRY VAN:\n{dry_van}\n\nREEFER:\n{reefer}\n\nFLAT BAD:\n{flat_bed}\n\nMESSAGE:\n{message}\n\nNEED DRIVER:\n{need_driver_assistence}"))
