import asyncio
from aiogram import Bot
API_TOKEN = "5260989327:AAGMxI_429gf-xggNXqDfsIL8hUYVX4ZsUY"
# MY_API = 668618297 #Abduraxmonaka
# MY_API = 1270941892 #Abdulazizaka
MY_API = 1144957860 #Abdukarim

async def send_message(message):
    operator = Bot(token=API_TOKEN)
    await operator.send_message(MY_API, message)

def send_form_bot(title,name,email,tel,company_name,mc,dry_van,reefer,flat_bed,message,need_driver_assistence):
    asyncio.run(send_message(f"\nA NEW {title}\n\nNAME:\n{name}\n\nEMAIL:\n{email}\n\nPHONE:\n{tel}\n\nCOMPANY NAME:\n{company_name}\n\nMC# :\n{mc}\n\nDRY VAN:\n{dry_van}\n\nREEFER:\n{reefer}\n\nFLAT BAD:\n{flat_bed}\n\nMESSAGE:\n{message}\n\nNEED DRIVER:\n{need_driver_assistence}"))


def send_form_bot_drivers(title,first_name,last_name ,email,phone,driver_license,state,driving_information ,how_many_years,previus_employer,which_position):
    asyncio.run(send_message(f"\nA NEW {title}\n\nFIRST NAME:\n{first_name}\n\nLAST NAME:\n{last_name}\n\nEMAIL:\n{email}\n\nPHONE NUMBER:\n{phone}\n\nDRIVER LICENSE:\n{driver_license}\n\nSTATE:\n{state}\n\nDRIVING INFORMATION:\n{driving_information}\n\nHow many years of verifiable commercial truck driving experience do you have?:\n{how_many_years}\n\nPREVIUS EMPLOYER:\n{previus_employer}\n\nWHICH POSITION:\n{which_position}"))