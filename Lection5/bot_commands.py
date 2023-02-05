from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *

async def hi_command (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!\n/Please choose your your security type')
    await update.message.reply_text(f'/bond\n/stock')

async def help_command (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/help\n/sum')

async def bond_command (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print(msg)
    item = msg.split() # /sum 123 534543
    PV = int(item[1])
    BondLength = int(item[2])
    await update.message.reply_text(f'PV = {int(item[1])},\n Length = {int(item[1])},\n Bond Yield to Maturity = {(((1000/PV)**(1/BondLength)-1)*100)//1.0}%')
    if (1000/PV)**(1/BondLength)-1 > 0.1:
        await update.message.reply_text(f'Your Bond return is high')
    else:
        await update.message.reply_text(f'You should invest in stocks or use deposit accounts')

async def stock_command (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        log(update, context)
        await update.message.reply_text(f'/Multiple\n/DCF')
    
    
    
async def multiple_command (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Write /Multiple then EBIDTA of your Company, Industry Multiple and Net Debt')
    msg = update.message.text
    print(msg)
    item = msg.split()
    EBITDA = int(item[1])
    Indusrty_Multiple = int(item[2])
    Net_Debt = int(item[3])
    await update.message.reply_text(f'EBITDA = {int(item[1])},\nIndutry Multiple = {int(item[2])},\nNet Debt = {int(item[3])}, \nMarket Cap = {EBITDA*Indusrty_Multiple - Net_Debt}')

async def dcf_command (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Write /dcf then EBIT of your Company, Tax rate, Net Working Capital, WACC, Terminal Growth Rate, Net Debt')
    msg = update.message.text
    print(msg)
    item = msg.split()
    EBIT = int(item[1])
    Tax_Rate = int(item[2])
    NWC = int(item[3])
    WACC = int(item[4])
    TGR = int(item[5])
    Net_Debt = int(item[6])
    await update.message.reply_text(f'EBIT = {int(item[1])},\n Tax Rate = {int(item[2])},\n Net WC = {int(item[3])},\n WACC = {int(item[4])},\n TGR = {int(item[5])},\n Net Debt = {int(item[6])} \n Market Cap = {(EBIT*(1-Tax_Rate)+NWC)*(1+TGR)/(WACC-TGR) - Net_Debt}')
