import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8372372190:AAH2G1dq_tI6A6bGh7QdoV5FaIPJJ71sDwg"

has_bought_token = False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot memecoin prêt ! Je surveille les nouveaux tokens...")

async def buy_token_simulation(update: Update):
    global has_bought_token
    if has_bought_token:
        await update.message.reply_text("J'ai déjà acheté un token, je ne peux pas en acheter plusieurs.")
        return
    has_bought_token = True
    await update.message.reply_text("Achat simulé d'un memecoin !")

async def sell_token_simulation(update: Update):
    global has_bought_token
    if not has_bought_token:
        await update.message.reply_text("Je n'ai rien à vendre pour le moment.")
        return
    has_bought_token = False
    await update.message.reply_text("Vente simulée du memecoin avec bénéfice !")

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await buy_token_simulation(update)

async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await sell_token_simulation(update)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("sell", sell))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
