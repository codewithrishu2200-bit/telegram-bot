import random 
import asyncio

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram import ChatPermissions


import os
TOKEN = os.environ.get("BOT_TOKEN", "8683383164:AAFCxnpxReLC36SnsPG8U48-AGP4TK4AHDE")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    userid = update.effective_user.id
    with open("data.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data.txt","a") as f:
            f.write(f"user id ; {userid}\n")

    await update.message.reply_text(f"hello {name} bhai!!\n use /help to know what this bot can do..")


async def help(update: Update , context:ContextTypes.DEAFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        contentchat = f.read()
    if str(chatid) not in contentchat:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n\n")
    await update.message.reply_text(
        "🚨disclaimer !!! bot slow hai....\n\n"
        "♥what this bot can do....  \n \n \n"
        "1. 🤬 gaali gloj \n       "
        " /surprise [name] \n\n\n" 
        "2. 🟰 calculation \n      " 
        "/cal x () y \n            " 
        "() can be + , - , * , / , ^ \n      " 
        "/sum x y\n      " 
        "/sub x y\n      " 
        "/mul x y\n      " 
        "/div x y\n\n      "
        "/table x --- table of x\n\n      "
        "/prime x --- to check x is prime or not \n\n\n"
        "3. rock🪨 , paper 🗒 , scissor✂ \n      " 
        "/rps [choice] --- choice = r/p/s\n            " 
        "eg /rps r---- (rock chossed)\n\n\n" 
        "4. 🎲 roll a dice & 🪙 toss a coin \n      " \
        "/roll --- dice roll\n      " \
        "/toss --- coin toss\n\n\n" \
        "5. 🤞 truth and dare\n      " \
        "/truth --- truth\n      " \
        "/dare --- dare\n\n\n" \
        "🕹 number guess game\n      "
        "/numguess -- to play" )
    

#=========================== buttons =======================
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        contentchat = f.read()
    if str(chatid) not in contentchat:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    keyboard = [
        [InlineKeyboardButton("rock🪨 , paper 🗒 , scissor✂", callback_data="rps"),
         InlineKeyboardButton("number guess", callback_data="numgame"),
         InlineKeyboardButton("truth and dare 🤞", callback_data="truthdare")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "games available here....🎮",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "rps":
        await query.message.reply_text(
            "/rps <r/p/s>"
        )

    elif query.data == "numgame":
        await query.message.reply_text(
            "start with /numguess"
        )
    elif query.data == "truthdare":
         await query.message.reply_text(
              " play with /truth and /dare"
         )

# ============= broadcast ===========================

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ADMIN_ID = 8518689952
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("Access Denied ❌\n u r not admin")
        return

    msg = " ".join(context.args)

    with open("data.txt", "r") as f:
        users = f.readlines()

    success = 0

    for user in users:
        try:
            userid = user.split(" ; ")[1].strip()

            await context.bot.send_message(
                chat_id=int(userid),
                text=msg
            )

            success += 1

        except Exception as e:
            print(e)

    await update.message.reply_text(
        f"Broadcast Complete ✅\nSent to {success} users."
    )

#============ chota broadcast =====================

async def cbroadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
     userid = 8654125707
     msg = " ".join(context.args)

     try:
            userid = 8654125707

            await context.bot.send_message(
                chat_id= userid ,
                text=msg
            )

            success += 1

     except Exception as e:
            print(e)
     await update.message.reply_text(
        f"Broadcast Complete ✅\nSent to users."
     )

# total users 
async def totalusers(update , context):
    with open("data.txt","r") as f:
          users = f.readlines()
          count = len(users)
    await update.message.reply_text(f"total users ; {count}")

# ============== grp broadcast =============

async def gbroadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
     grpid = -1003262453436
     msg = " ".join(context.args)

     try:
            grpid = -1003262453436

            await context.bot.send_message(
                chat_id= grpid ,
                text=msg
            )

            success += 1

     except Exception as e:
            print(e)
     await update.message.reply_text(
        f"Broadcast Complete ✅\nSent to this grp."
     )


# ========= basic commands ==========
async def hi(update: Update , context:ContextTypes.DEAFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        contentchat = f.read()
    if str(chatid) not in contentchat:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    await update.message.reply_text("namaste bro")

async def bye(update: Update , context:ContextTypes.DEAFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        contentchat = f.read()
    if str(chatid) not in contentchat:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    await update.message.reply_text("bye bro....")

async def luck(update: Update , context:ContextTypes.DEAFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    await update.message.reply_text(f"your luck is {random.randint(1,101)}%")


#calculator

async def sum(update: Update , context:ContextTypes.DEAFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    a = int(context.args[0])
    b = int(context.args[1])
    c = a + b
    await update.message.reply_text(f"{a} + {b} = {a+b}")

async def mul(update, context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    a = int(context.args[0])
    b = int(context.args[1])

    await update.message.reply_text(f"{a} x {b} = {a*b}")

async def div(update, context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    a = int(context.args[0])
    b = int(context.args[1])

    await update.message.reply_text(f"{a}/{b} = {a/b}")

async def sub(update, context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    a = int(context.args[0])
    b = int(context.args[1])

    await update.message.reply_text(f"{a} - {b} = {a-b}")


# calculator all in one

async def cal(update, context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")


    a = int(context.args[0])
    op = context.args[1]
    b = int(context.args[2])

    if op == "+":
        result = a + b

    elif op == "-":
        result = a - b

    elif op == "*":
        result = a * b

    elif op == "/":
        result = a / b

    elif op == "^":
        result = a**b

    else:
        await update.message.reply_text("Invalid Operator")
        return

    await update.message.reply_text(str(result))





# dice roll

async def roll(update, context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")


    num = random.randint(1, 6)

    await update.message.reply_text(f"🎲 {num}")

# toss a coin 

async def toss(update, context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    coin = ["🪙 heads","🪙 tails"]
    

    resul = random.choice(coin)

    await update.message.reply_text(f" {resul}")



# prime number check


async def prime(update, context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    a = int(context.args[0])

    for i in range(2,a):

        if(a%i == 0):
            await update.message.reply_text("number is not prime")
            break
            i = i + 1
        

    else:
        await update.message.reply_text("number is prime") 
        
            
# ========== truth dare ===========

async def truth(update, context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    truths = [
    "Who in this group would you date if you had no other option?",
    "Who is the most annoying person in this group?",
    "What's your biggest red flag?",
    "Who was your last crush?",
    "What's the pettiest reason you've stopped talking to someone?",
    "Who in this group would survive the least in a horror movie?",
    "What's the most embarrassing thing in your gallery?",
    "Have you ever stalked someone for more than 30 minutes?",
    "Who in this group would make the worst partner?",
    "What's the biggest lie you've told this year?",
    "What's your most toxic trait?",
    "Who here would be the first to sell their friend for money?",
    "What's the weirdest thing you've searched online?",
    "What's your biggest insecurity?",
    "Who would you trust least with your phone?",
    "What's the most childish thing you still do?",
    "Have you ever had a crush on a friend's crush?",
    "Who here is secretly the smartest?",
    "What's your worst habit?",
    "What's the dumbest thing you've done for attention?",
    "Who in this group would get cancelled first?",
    "What's your most embarrassing school memory?",
    "What's a secret you've never told your parents?",
    "Who would you switch lives with for a week?",
    "What's the weirdest dream you've ever had?",
    "Who here would make the best villain?",
    "What's the biggest rumor you've heard about yourself?",
    "What's your biggest regret?",
    "Who in this group gives fake nice vibes?",
    "Have you ever lied to get out of plans?",
    "What's your worst fashion mistake?",
    "Who here would win a reality show?",
    "What's the longest you've gone without bathing?",
    "Who would be the worst roommate here?",
    "What's your biggest fear?",
    "What's the meanest thing you've done?",
    "Who here would survive a zombie apocalypse?",
    "What's the weirdest thing you've done when alone?",
    "Who in this group is most likely to become famous?",
    "What's the most awkward DM you've sent?",
    "What's your most irrational fear?",
    "Who do you secretly envy?",
    "What's the most embarrassing thing you've said to a crush?",
    "Who here would get arrested first?",
    "What's your biggest first impression fail?",
    "Who would you trust with a huge secret?",
    "What's your weirdest habit?",
    "What's the most desperate thing you've done?",
    "Who here would be terrible at parenting?",
    "What's one thing nobody here knows about you?"
        "What's the most embarrassing nickname you've ever had?",
    "Who in this group would you never go on a trip with?",
    "What's the worst excuse you've used for being late?",
    "Who was the last person you stalked online?",
    "What's the weirdest thing you've done out of boredom?",
    "Who here would be the worst boss?",
    "What's your biggest guilty pleasure?",
    "What's the most awkward family moment you've witnessed?",
    "Who in this group would survive the longest without a phone?",
    "What's the most useless talent you have?",
    "Who here would accidentally start a fire?",
    "What's your weirdest food combination?",
    "What's the dumbest thing you've spent money on?",
    "Who in this group is the biggest drama magnet?",
    "What's the funniest lie you've ever told?",
    "What's the most awkward thing you've done in public?",
    "Who here would make the worst detective?",
    "What's the strangest compliment you've received?",
    "What's the biggest misunderstanding you've been involved in?",
    "Who here would forget their own wedding date?",
    "What's the weirdest thing you've kept for sentimental reasons?",
    "Who in this group would be terrible at keeping secrets?",
    "What's your most embarrassing autocorrect fail?",
    "What's the longest you've pretended to listen?",
    "Who here would be the first to get lost in a new city?",
    "What's your biggest social media regret?",
    "What's the weirdest thing you've done to impress someone?",
    "Who in this group would be the most annoying celebrity?",
    "What's the most embarrassing thing you've done at work or school?",
    "Who here would survive a week without internet?",
    "What's the worst advice you've ever followed?",
    "What's your funniest childhood memory?",
    "Who in this group would cry first during a scary movie?",
    "What's the weirdest thing you've done while half asleep?",
    "What's the most awkward phone call you've ever had?",
    "Who here would make the worst spy?",
    "What's your biggest irrational pet peeve?",
    "What's the most embarrassing thing you've accidentally liked online?",
    "Who here would spend all their money in one day?",
    "What's the weirdest thing you've Googled recently?",
    "What's your biggest overreaction story?",
    "Who in this group would be the first to quit a reality show?",
    "What's the strangest dream you still remember?",
    "What's the most awkward thing you've overheard?",
    "Who here would accidentally leak a secret?",
    "What's the funniest thing you've done when nervous?",
    "What's the weirdest excuse you've heard?",
    "Who in this group would make the worst teacher?",
    "What's your most embarrassing shopping experience?",
    "What's the most awkward compliment you've ever given?",
    "Who here would get kicked out of a fancy event first?",
    "What's the weirdest thing you've done to avoid someone?",
    "What's the funniest thing you've believed as a child?",
    "Who in this group would be terrible at living alone?",
    "What's your most embarrassing voice note?",
    "What's the weirdest thing you've said while sleepy?",
    "Who here would survive the least amount of time in the wild?",
    "What's your most awkward crush story?",
    "What's the biggest risk you've taken?",
    "Who in this group would be the worst wedding planner?",
    "What's the weirdest thing you've done during a video call?",
    "What's your most embarrassing screenshot?",
    "Who here would be the first to get scammed?",
    "What's the funniest thing you've done for a dare?",
    "What's the weirdest thing you've carried in your bag?",
    "Who in this group would be the worst superhero?",
    "What's your biggest fear that sounds silly?",
    "What's the most awkward thing you've texted by mistake?",
    "Who here would spend an hour taking one selfie?",
    "What's the weirdest thing you've eaten?",
    "What's the most embarrassing thing you've done while trying to look cool?",
    "Who in this group would be terrible at customer service?",
    "What's your funniest fail story?",
    "What's the weirdest thing you've done in a lift/elevator?",
    "Who here would be the first to lose their passport?",
    "What's your biggest lazy moment?",
    "What's the strangest thing you've found on the street?",
    "Who in this group would make the worst judge?",
    "What's your funniest online shopping fail?",
    "What's the weirdest thing you've forgotten somewhere?",
    "Who here would get into the most arguments?",
    "What's the biggest misunderstanding caused by you?",
    "What's your weirdest lucky charm?",
    "Who in this group would be the worst tour guide?",
    "What's the funniest thing you've done while sick?",
    "What's the most awkward thing you've said to the wrong person?",
    "Who here would get caught in a lie first?",
    "What's the weirdest thing you've done at midnight?",
    "What's your biggest accidental embarrassment?",
    "Who in this group would survive a week in jail best?",
    "What's the weirdest thing you've celebrated?",
    "What's the funniest thing you've done to avoid work?",
    "Who here would be terrible at acting?",
    "What's the most awkward thing you've done in front of relatives?",
    "What's your weirdest fear from childhood?",
    "Who in this group would be the first to start a conspiracy theory?",
    "What's the weirdest thing you've done in a classroom?",
    "What's the funniest thing you've done by accident?",
    "Who here would forget an important anniversary?",
    "What's the biggest mess you've ever made?",
    "What's your weirdest habit nobody knows about?",
    "Who in this group would be the worst news reporter?",
    "What's the funniest thing you've done in a queue?",
    "What's your most embarrassing laugh moment?",
    "Who here would be the worst cook?",
    "What's the weirdest thing you've done while waiting for someone?",
    "What's the funniest thing you've said without thinking?",
    "Who in this group would make the worst pilot?",
    "What's your most awkward encounter with a stranger?",
    "What's the weirdest thing you've done in a supermarket?",
    "Who here would spend the longest choosing food?",
    "What's the funniest thing you've broken?",
    "What's your weirdest school punishment?",
    "Who in this group would be the worst game show contestant?",
    "What's the most awkward thing you've done in a photo?",
    "What's your biggest 'I immediately regretted that' moment?",
    "Who here would be terrible at hiding?",
    "What's the weirdest thing you've done because of a bet?",
    "What's the funniest thing you've done in public transport?",
    "Who in this group would get lost using Google Maps?",
    "What's your most embarrassing dance moment?",
    "What's the weirdest thing you've argued about?",
    "Who here would make the worst roommate?",
    "What's the funniest thing you've done in a library?",
    "What's your biggest brain-fade moment?",
    "Who in this group would be the worst babysitter?",
    "What's the weirdest thing you've worn in public?",
    "What's the funniest thing you've done before an exam?",
    "Who here would make the worst secret agent?",
    "What's your most awkward family gathering memory?",
    "What's the weirdest thing you've done on a holiday?",
    "Who in this group would be the first to panic in an emergency?",
    "What's the funniest thing you've done with the wrong confidence?",
    "What's your weirdest coincidence story?",
    "Who here would make the worst lawyer?",
    "What's the most embarrassing thing you've done with confidence?",
    "What's your weirdest travel story?",
    "Who in this group would be terrible at poker?",
    "What's the funniest thing you've done while tired?",
    "What's your weirdest misunderstanding?",
    "Who here would accidentally reveal spoilers?",
    "What's the biggest mistake you've laughed about later?",
    "What's your weirdest friendship story?",
    "Who in this group would be the worst host?",
    "What's the funniest thing you've forgotten?",
    "What's your weirdest 'why did I do that?' moment?",
    "Who here would spend the most time talking to themselves?",
    "What's your funniest accidental text?",
    "What's the weirdest thing you've done for free food?",
    "Who in this group would be the worst referee?"
        "Who in this group would most likely become a millionaire?",
    "Who here would survive the shortest time on a deserted island?",
    "What's the weirdest thing you've done to avoid studying?",
    "Who in this group would be the worst roommate?",
    "What's the most embarrassing thing you've done in front of a crowd?",
    "Who would you never trust with your phone unlocked?",
    "What's your most useless skill?",
    "Who in this group would accidentally start a fight?",
    "What's the funniest lie you've ever believed?",
    "Who here is most likely to become famous for something stupid?",
    "What's the weirdest thing you've done when nobody was watching?",
    "Who in this group would make the worst teacher?",
    "What's the most awkward thing you've said by mistake?",
    "Who would you call first if you got arrested?",
    "What's the most childish argument you've had recently?",
    "Who in this group is secretly the most judgmental?",
    "What's the weirdest thing you've done for free food?",
    "Who would be the worst person to get stuck in a lift with?",
    "What's your most embarrassing social media moment?",
    "Who in this group would be the first to panic during an emergency?",
    "What's the biggest misunderstanding you've caused?",
    "Who here would be terrible at keeping a straight face?",
    "What's the weirdest thing you've ever bought?",
    "Who would survive the longest in a zombie apocalypse?",
    "What's the most embarrassing thing you've done while trying to impress someone?",
    "Who in this group would be the worst secret agent?",
    "What's the strangest dream you've had recently?",
    "Who here would be most likely to join a cult?",
    "What's the funniest thing you've done when half asleep?",
    "Who in this group would make the worst politician?",
    "What's your biggest irrational fear?",
    "Who here would spend an hour choosing what to eat?",
    "What's the weirdest thing you've done at 2 AM?",
    "Who would be the first to lose their passport on a trip?",
    "What's your funniest exam fail story?",
    "Who here would be the worst driver?",
    "What's the weirdest thing you've Googled?",
    "Who in this group would accidentally reveal a secret?",
    "What's the biggest overreaction you've ever had?",
    "Who here would be the worst detective?",
    "What's the weirdest excuse you've used to avoid someone?",
    "Who would survive the least amount of time without their phone?",
    "What's the most embarrassing thing you've worn in public?",
    "Who here would make the worst game show contestant?",
    "What's the strangest coincidence that's happened to you?",
    "Who would you trust the least with ₹1 lakh?",
    "What's the weirdest thing you've argued about?",
    "Who here would get caught sneaking around first?",
    "What's the funniest thing you've done while bored?",
    "Who would make the worst wedding planner?",
    "What's the most awkward compliment you've received?",
    "Who here would be the first to get lost in a mall?",
    "What's your most embarrassing childhood memory?",
    "Who in this group would be terrible at acting?",
    "What's the weirdest thing you've found in your pocket?",
    "Who would be the worst travel partner?",
    "What's your funniest autocorrect fail?",
    "Who here would be most likely to start drama accidentally?",
    "What's the most awkward thing you've overheard?",
    "Who in this group would be terrible at customer service?",
    "What's the weirdest thing you've done while on a call?",
    "Who would make the worst babysitter?",
    "What's your biggest 'I regret this immediately' moment?",
    "Who here would be the first to believe fake news?",
    "What's the funniest thing you've broken?",
    "Who would be the worst person to share a room with?",
    "What's the weirdest thing you've done to save money?",
    "Who here would be most likely to sleep through an earthquake?",
    "What's your funniest family story?",
    "Who would make the worst chef?",
    "What's the weirdest thing you've done on public transport?",
    "Who in this group would survive a horror movie?",
    "What's the most embarrassing thing you've done at a wedding?",
    "Who here would be the worst stand-up comedian?",
    "What's the weirdest thing you've done to get attention?",
    "Who would be the first to get scammed?",
    "What's your funniest misunderstanding?",
    "Who here would be the worst referee?",
    "What's the weirdest thing you've done in a supermarket?",
    "Who would make the worst news anchor?",
    "What's your most embarrassing voice crack moment?",
    "Who here would forget their own anniversary?",
    "What's the weirdest thing you've done during an online class?",
    "Who would be the worst motivational speaker?",
    "What's your funniest school punishment story?",
    "Who here would panic first during a power cut?",
    "What's the weirdest thing you've done while waiting for someone?",
    "Who would make the worst magician?",
    "What's the funniest thing you've said confidently but was completely wrong?",
    "Who in this group would be the first to get kicked out of a fancy event?",
    "What's the weirdest thing you've done to avoid work?",
    "Who would make the worst lawyer?",
    "What's your funniest travel fail story?",
    "Who here would be most likely to lock themselves out of their house?",
    "What's the weirdest thing you've done after waking up suddenly?",
    "Who would make the worst judge?",
    "What's the funniest thing you've done while sick?",
    "Who here would survive the least in the wilderness?",
    "What's the weirdest thing you've done with complete confidence?",
    "Who would make the worst influencer?",
    "What's the funniest thing you've done before an interview?",
    "Who in this group would accidentally spoil a surprise?",
    "What's the weirdest thing you've forgotten somewhere?",
    "Who would make the worst bodyguard?",
    "What's the funniest thing you've done while nervous?",
    "Who here would be most likely to marry for money?",
    "What's the weirdest thing you've done to look cool?",
    "Who would make the worst tour guide?",
    "What's your funniest bad luck story?",
    "Who here would be the first to get banned from a group chat?",
    "What's the weirdest thing you've done during a family function?",
    "Who would make the worst principal?",
    "What's the funniest thing you've done to avoid embarrassment?",
    "Who in this group would be terrible at poker?",
    "What's the weirdest thing you've done because of a dare?",
    "Who would make the worst doctor?",
    "What's your funniest 'caught red-handed' moment?",
    "Who here would accidentally become famous?",
    "What's the weirdest thing you've done in a hotel?",
    "Who would make the worst roommate for a year?",
    "What's your funniest lazy moment?",
    "Who in this group would be the first to betray their team in a game?",
    "What's the weirdest thing you've done while trying to stay awake?",
    "Who would make the worst police officer?",
    "What's your funniest moment in a queue?",
    "Who here would most likely get addicted to a reality show?",
    "What's the weirdest thing you've done while hungry?",
    "Who would make the worst school monitor?",
    "What's your funniest gym fail story?",
    "Who in this group would forget where they parked their vehicle?",
    "What's the weirdest thing you've done while alone at home?",
    "Who would make the worst singer?",
    "What's your funniest festival memory?",
    "Who here would be most likely to accidentally go viral?",
    "What's the weirdest thing you've done after losing a bet?",
    "Who would make the worst coach?",
    "What's your funniest friendship story?",
    "Who in this group would be the first to get fooled by a prank?",
    "What's the weirdest thing you've done because you were bored?"
        "Who in this group would you secretly date but never admit publicly?",
    "If everyone here rated you honestly, what score would you get out of 10?",
    "Who in this group would you NOT leave alone with your best friend?",
    "What's the harshest truth someone has ever told you?",
    "Who here has the biggest ego?",
    "If you had to remove one person from this group forever, who would it be?",
    "What's something you've done that you'd deny even with proof?",
    "Who in this group do you think judges people the most?",
    "What's your most embarrassing late-night mistake?",
    "Who here would be the worst person to date?",
    "What's the most attention-seeking thing you've ever done?",
    "Who in this group would be your enemy in another life?",
    "What's the biggest secret you're hiding from your family?",
    "Who here would betray everyone for enough money?",
    "What's the worst thing you've done and gotten away with?",
    "Who in this group acts innocent but definitely isn't?",
    "What's the most manipulative thing you've ever done?",
    "Who here would be the first to fake being sick?",
    "What's your biggest 'thank god nobody found out' moment?",
    "Who in this group would be terrible at marriage?",
    "What's something you pretend to like but actually hate?",
    "Who here has the most main-character syndrome?",
    "What's the worst advice you've ever given?",
    "Who would you trust the least with a huge secret?",
    "What's the dumbest thing you've done because of a crush?",
    "Who here is most likely to be secretly rich one day?",
    "What's your biggest jealousy story?",
    "Who in this group would survive a breakup the worst?",
    "What's something you've never told your best friend?",
    "Who here would be the most dangerous with power?",
    "What's the most awkward thing you've done while trying to flirt?",
    "Who in this group would be the easiest to prank?",
    "What's the biggest fake excuse you've ever used?",
    "Who here would be the worst parent?",
    "What's the most embarrassing thing you've done for popularity?",
    "Who in this group would secretly enjoy being famous?",
    "What's your biggest self-sabotage moment?",
    "Who here would start a fight over something stupid?",
    "What's a truth about yourself that sounds fake?",
    "Who in this group is the most likely to become a meme?",
    "What's the biggest misunderstanding people have about you?",
    "Who here would be most likely to leak private chats?",
    "What's the most childish thing you've done recently?",
    "Who in this group would make a terrible leader?",
    "What's the weirdest thing you've done when nobody was home?",
    "Who here would get cancelled first if all their chats leaked?",
    "What's your biggest social media addiction habit?",
    "Who in this group would survive the least in prison?",
    "What's the meanest thought you've had today?",
    "Who here would definitely fail a lie detector test?",
    "What's something you're glad your parents don't know?",
    "Who in this group acts smart but isn't?",
    "What's your biggest friendship regret?",
    "Who here is most likely to forget your birthday?",
    "What's the most embarrassing thing you've ever done in public?",
    "Who in this group would be the worst wingman/wingwoman?",
    "What's the pettiest revenge you've ever taken?",
    "Who here would make the worst influencer?",
    "What's your most toxic friendship story?",
    "Who in this group would definitely snitch first?",
    "What's the most desperate text you've ever sent?",
    "Who here would be the first to cry during an argument?",
    "What's the biggest rumor you've secretly enjoyed hearing about yourself?",
    "Who in this group would be most likely to fake confidence?",
    "What's something you've done that still keeps you awake sometimes?",
    "Who here would be the first to quit during a challenge?",
    "What's the biggest lie you've told to avoid trouble?",
    "Who in this group has the worst taste in people?",
    "What's the most embarrassing thing you've ever posted?",
    "Who here would be most likely to accidentally go viral?",
    "What's the weirdest thing you've done because you were jealous?",
    "Who in this group would survive fame the worst?",
    "What's your most embarrassing phone call story?",
    "Who here would spend all their money in one day?",
    "What's the biggest overreaction you've ever had?",
    "Who in this group would be terrible at keeping a relationship?",
    "What's something you judge people for but also do yourself?",
    "Who here would get addicted to fame fastest?",
    "What's the most awkward compliment you've ever received?",
    "Who in this group would be the biggest bridezilla/groomzilla?",
    "What's the weirdest thing you've done to avoid a conversation?",
    "Who here would definitely lose a reality show?",
    "What's the biggest mistake you've made while angry?",
    "Who in this group would get caught cheating in a game first?",
    "What's the most embarrassing thing you've searched recently?",
    "Who here is secretly more emotional than they look?",
    "What's your biggest trust issue story?",
    "Who in this group would be most likely to disappear for a month?",
    "What's the weirdest thing you've done after getting rejected?",
    "Who here would be terrible at living alone?",
    "What's the most embarrassing thing you've done to impress someone?",
    "Who in this group would be the first to start a rumor?",
    "What's your biggest accidental betrayal story?",
    "Who here would survive a horror movie but die in the sequel?",
    "What's something you wish nobody remembered about you?",
    "Who in this group would make the worst detective?",
    "What's the most awkward thing you've done at a family function?",
    "Who here would definitely open a message and ignore it?",
    "What's your biggest 'I thought I was cool' moment?",
    "Who in this group would lose their phone the fastest?",
    "What's something you've done that you'd never recommend to anyone?",
    "Who here would make the worst therapist?",
    "What's the funniest thing you've done while nervous?",
    "Who in this group would be most likely to join a cult accidentally?",
    "What's the most embarrassing thing you've done at school/work?",
    "Who here would get scammed first?",
    "What's the weirdest thing you've ever lied about?",
    "Who in this group would survive the longest without social media?",
    "What's your biggest cringe memory?",
    "Who here would be terrible at being famous?",
    "What's something you secretly compete with your friends about?",
    "Who in this group would be the first to break a promise?",
    "What's the biggest lesson you learned the hard way?",
    "Who here would get caught snooping first?",
    "What's the weirdest thing you've done to look busy?",
    "Who in this group would accidentally reveal a surprise party?",
    "What's your most embarrassing confidence fail?",
    "Who here would be most likely to fake being productive?",
    "What's something you've done that nobody would expect from you?",
    "Who in this group would survive on charm alone?",
    "What's the weirdest thing you've done out of boredom?",
    "Who here would be terrible at poker?",
    "What's the biggest risk you've taken that paid off?",
    "Who in this group would be most likely to get famous on the internet?",
    "What's your funniest lie-gone-wrong story?",
    "Who here would be the worst roommate for a year?",
    "What's the most embarrassing thing you've said to the wrong person?",
    "Who in this group would accidentally become a villain?",
    "What's the biggest thing you've pretended to understand?",
    "Who here would be most likely to become a conspiracy theorist?",
    "What's the weirdest thing you've done when sleep deprived?",
    "Who in this group would be terrible at keeping secrets?",
    "What's the biggest assumption people make about you?",
    "Who here would survive a zombie apocalypse through pure luck?",
    "What's the most awkward thing you've done in a group chat?",
    "Who in this group would make the worst boss?",
    "What's your biggest lucky escape story?",
    "Who here would be most likely to get roasted in a debate?",
    "What's the funniest thing you've done while trying to act mature?",
    "Who in this group would definitely read everyone's chats if they could?",
    "What's something you've done that you'd never admit offline?"
]
    
    qt = random.choice(truths)
    await update.message.reply_text(qt)

async def dare(update, context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")


    dares = [
    "Change your Telegram name for 10 minutes.",
    "Send your last selfie in the group.",
    "Type using only emojis for the next 5 messages.",
    "Reveal your screen time.",
    "Send the 5th photo from your gallery.",
    "Use CAPS LOCK for the next 10 messages.",
    "Tell a joke so bad that everyone groans.",
    "Share your most used emoji.",
    "Change your bio to 'Professional Fool' for 1 hour.",
    "Write a poem about the admin.",
    "Roast yourself in 3 lines.",
    "Compliment everyone who replies to you.",
    "Reveal your last Google search.",
    "Send a voice note singing any song.",
    "Talk like a robot for 10 messages.",
    "Use only GIFs for the next 5 minutes.",
    "Rate yourself honestly out of 10.",
    "Share your wallpaper.",
    "Send a random meme from your gallery.",
    "Tell your most embarrassing school story.",
    "Tag the funniest person in the group.",
    "Tag the most dangerous person in the group.",
    "Describe yourself in 3 words.",
    "Change your profile picture to a potato for 15 minutes.",
    "Reveal the last thing you copied.",
    "Write a fake motivational quote.",
    "Pretend you're famous for 5 messages.",
    "Tell everyone your weirdest habit.",
    "Make up a conspiracy theory about the group.",
    "Reply only with 'yes boss' for 10 minutes.",
    "Tell a cringe pickup line.",
    "Act like the group admin for 5 messages.",
    "Share your oldest screenshot.",
    "Use only one-word replies for 10 messages.",
    "Reveal your favorite guilty pleasure song.",
    "Write a dramatic breakup message to pizza.",
    "Send a random sticker and explain it seriously.",
    "Speak in third person for 5 messages.",
    "Make a fake movie title about your life.",
    "Type with your eyes closed.",
    "Give everyone a superhero name.",
    "Send the most random image in your gallery.",
    "Create a fake news headline about yourself.",
    "Describe your day using movie titles.",
    "Act like a motivational speaker.",
    "Write a love letter to chai/coffee.",
    "Use only questions for the next 5 messages.",
    "Reveal the weirdest thing in your room.",
    "Tell your worst fashion mistake.",
    "Act like you're running for president.",

    "Tag someone and compliment them.",
    "Tag someone and roast them politely.",
    "Reveal your last YouTube search.",
    "Speak like a pirate for 10 messages.",
    "Send a photo of your desk.",
    "Create a slogan for yourself.",
    "Reveal your weirdest nickname.",
    "Tell your biggest irrational fear.",
    "Pretend you're a weather reporter.",
    "Explain how to make tea like a scientist.",
    "Type everything backwards for 3 messages.",
    "Write a rap about the group.",
    "Reveal your most-used app.",
    "Send a voice note laughing for 10 seconds.",
    "Describe the admin as a movie character.",
    "Act like a news anchor.",
    "Write a poem about Monday.",
    "Pretend you're an alien visiting Earth.",
    "Share your funniest autocorrect fail.",
    "Reveal your most embarrassing typo.",
    "Talk like a villain for 10 messages.",
    "Describe yourself as a product.",
    "Create a fake holiday and explain it.",
    "Write a dramatic review of water.",
    "Reveal the last thing you bought.",
    "Act like a detective solving a mystery.",
    "Invent a new word and define it.",
    "Send a random voice note.",
    "Tell everyone your favorite snack.",
    "Describe the group as a TV show.",
    "Use only animal sounds for 5 messages.",
    "Make up a fake talent.",
    "Reveal your oldest contact name.",
    "Send your latest screenshot.",
    "Write a movie trailer for your life.",
    "Pretend you're 80 years old.",
    "Describe your mood as a food.",
    "Create a fake advertisement for yourself.",
    "Reveal your most embarrassing search.",
    "Tell your funniest family story.",
    "Pretend you're a celebrity being interviewed.",
    "Write a breakup message to homework.",
    "Give yourself a royal title.",
    "Describe everyone in the group using fruits.",
    "Explain your life using cricket terms.",
    "Talk like a cartoon character.",
    "Pretend you're a billionaire.",
    "Write a dramatic speech about sleeping.",
    "Reveal the last game you played.",
    "Describe your best friend badly.",

    "Change your bio to 'I lost a dare' for 30 minutes.",
    "Tell a secret that isn't too serious.",
    "Reveal the weirdest dream you remember.",
    "Send a voice note saying tongue twisters.",
    "Write a fake horoscope for the group.",
    "Describe yourself as a meme.",
    "Pretend you're a teacher scolding the group.",
    "Reveal your favorite childhood cartoon.",
    "Use only movie quotes for 5 messages.",
    "Act like you're stuck in 2010.",
    "Write a thank-you speech for absolutely nothing.",
    "Reveal the oldest app on your phone.",
    "Tell your funniest fail story.",
    "Speak like Shakespeare for 5 messages.",
    "Create a fake warning label for yourself.",
    "Reveal your biggest pet peeve.",
    "Act like a sports commentator.",
    "Tell everyone your most useless skill.",
    "Describe your life as a clickbait title.",
    "Make a fake prediction for tomorrow.",
    "Reveal your most used slang word.",
    "Pretend you're a tour guide of your room.",
    "Describe your personality as a restaurant.",
    "Create a fake award and give it to yourself.",
    "Explain a banana like it's advanced technology.",
    "Reveal your most recent emoji.",
    "Act like you're trapped in a soap opera.",
    "Write a dramatic message to your alarm clock.",
    "Tell everyone a random fact.",
    "Pretend you're a magician.",
    "Describe your phone as a person.",
    "Write a song title about your life.",
    "Reveal the last person you texted.",
    "Talk like a politician for 5 messages.",
    "Create a fake app and describe it.",
    "Describe the group in one savage sentence.",
    "Reveal the funniest contact name in your phone.",
    "Pretend you're narrating a wildlife documentary.",
    "Write a review of your own personality.",
    "Describe yourself using only emojis.",
    "Reveal your favorite excuse for being late.",
    "Make up a fake law everyone must follow.",
    "Act like a game show host.",
    "Describe your day like a horror movie.",
    "Write a dramatic goodbye message and then continue chatting.",
    "Reveal your most embarrassing saved photo.",
    "Create a fake superhero power for yourself.",
    "Pretend you're an AI trying to be human.",
    "Rate the group chaos level out of 10.",
    "End every message with 'bro' for 10 minutes."
]
    
    qd = random.choice(dares)
    await update.message.reply_text(qd)

# gaali laddder 


async def spam(update, context,a):
    gaali_list = [
        "Ch*tiya",
        "B*sdk",
        "Chutiya",
        "Gadha",
        "Bewakoof",
        "Pagal",
        "Bhosdike",
        "Madarchod",
        "Behenchod",
        "Harami",
        "Kamine",
        "Kutte",
        "Saale",
        "Ullu",
        "Ullu ka pattha",
        "Jhantu",
        "Lodu",
        "Chut ke gulam",
        "Bakchod",
        "Gawar",
        "Chipkali ke gote",
        "Besharam",
        "Badtameez",
        "Kotha no. 12 ki rnd",
        "Faltu",
        "Chhapri",
        "Tharki",
        "Badtamiz insaan",
        "Dimaag se paidal",
        "Akal ka dushman",
        "fate kondom ki glti",
        "Number one gend ka baal",
        "Hawa-baaz",
        "Circus ka joker",
        "Keemti bevakoof",
        "lund buddhi",
        "lunch me aand bhat khane wale"
        "Ch*tiya",
        "B*sdk",
        "M*dk",
        "B*nchod",
        "M*nchod",
        "G*ndu",
        "H*rami",
        "K*mina",
        "Ch*nal",
        "R*ndi",
        "T*tti",
        "L*nd",
        "B*hen ke l*de",
        "M* ke l*de",
        "G*nd ka dhakkan",
        "Bh*sad",
        "Ch*tiye",
        "B*klol",
        "Nalayak",
        "Gadha",
        "Bandar",
        "Ullu",
        "Ullu ka p*tha",
        "Kutte",
        "Kutte ki aulad",
        "Suar",
        "Suar ki aulad",
        "Kamine",
        "Haramkhor",
        "Nikamma",
        "Pagal",
        "Baklol",
        "Chirkut",
        "Tapori",
        "Besharam",
        "Dhokebaaz",
        "Faltu aadmi",
        "Akal ka dushman",
        "Dimag se paidal"
        "Bina battery ka robot",
        "Zero IQ",
        "Legend-level chutiya"
      ]
    for i in range(1,100):

        a = context.args[0]
        gali = random.choice(gaali_list)
        await update.message.reply_text(f"{a} {gali}")
        i+= 1
    await update.message.reply_text(f"aaj k liye bas itna hi \n aapki tarah mai bhi mayus hu \n ||aage ka khud complete kr le||")
async def surprise(update,context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")


    a = context.args[0]
    asyncio.create_task(spam(update,context,a))
    await update.message.reply_text("ok saaarr")
    
# ============ pickup line =============
async def flirt(update, context):
    pickup_lines = [
        "Pata nahi tum special ho ya meri nazar, par tum par aake ruk jaati hai.",    
        "Main usually kisi ko message karne ka reason dhoondta hu, tum exception lagti ho.",    
        "Tumse baat karke lagta hai din thoda better ho gaya.",    
        "Sach bolu? Tumhari vibe hi alag hai.",    
        "Tum wo insaan lagti ho jisse roz baat karne ki aadat lag sakti hai.",    
        "Aaj tak bahut log mile, par tum thodi yaad reh jaane wali lagti ho.",    
        "Tumhari smile ka koi side effect hai kya? Baar baar yaad aa jaati hai.",    
        "Tumse baat karne ke baad dusre chats thode boring lagne lagte hain.",    
        "Tumhari problem ye hai ki tum normal bilkul nahi lagti.",    
        "Pehle mujhe lagta tha achhi conversations kismat se milti hain.",    
        "Tumhari DP achhi hai, par shayad tumhari baatein usse bhi better hongi.",    
        "Tumse baat karne ka mann reason nahi maangta.",    
        "Agar tum playlist hoti na, to definitely repeat pe chalti.",    
        "Tumhare replies ka wait karna mujhe pasand nahi... phir bhi karta hu.",    
        "Tumhari ek 'hmm' bhi kai logon ke paragraph se better lagti hai.",    
        "Mujhe tum pasand ho ya tumhari aadat lag rahi hai, abhi tak samajh nahi aaya.",    
        "Tumhara naam notification me dikhe to mood automatically better ho jaata hai.",    
        "Tum wo distraction ho jise main avoid bhi nahi karna chahta.",    
        "Tumhari baat alag hai... aur ye line main sabko nahi bolta.",      
        "Agar overthinking ek sport hota, to main champion hota. Aur zyadaatar tumhari wajah se.",
        "Tumse baat karke lagta hai din waste nahi gaya.",
        "Sach bolu? Tumhari vibe hi alag level ki hai.",
        "Tumhara naam screen pe dikhe to smile aa hi jaati hai.",
        "Tum wo notification ho jise ignore karne ka mann nahi karta.",
        "Pata nahi tum mein kya baat hai, par baat karne ka mann karta rehta hai.",
        "Tumse baat karna aadat ban sakta hai.",
        "Tumhari smile ka competition abhi tak kisi ne nahi jeeta.",
        "Tum normal nahi ho, aur ye compliment hai.",
        "Tumhare replies ka wait karna bhi achha lagta hai.",
        "Tumhari ek 'hmm' bhi interesting lagti hai.",
        "Tumse baat shuru karna easy hai, khatam karna mushkil.",
        "Tumhari energy kaafi addictive hai.",
        "Tum wo insaan lagti ho jo yaad reh jaati hai.",
        "Tumhari baaton mein ajeeb sa sukoon hai.",
        "Tumhare saath boring topic bhi interesting ho sakta hai.",
        "Tumhara taste achha hai, mujhe choose kiya na.",
        "Agar mood ek jagah hota, to mera tumhare paas hota.",
        "Tumhari hasi genuine lagti hai, aur wahi best part hai.",
        "Tumhari profile dekh kar curiosity hui, baat karke confirm ho gayi.",
        "Tumhe dekh kar lagta hai universe kabhi kabhi effort karta hai.",
        "Tumhare baare mein jitna pata chalta hai, utni curiosity badh jaati hai.",
        "Tumhare saath time fast chalta hai.",
        "Tumhari presence noticeable hai.",
        "Tum wo reason ho jiski wajah se phone baar baar check hota hai.",
        "Tumhari baat alag hai, bas samjha nahi sakta.",
        "Tumhari aankhon mein confidence achha lagta hai.",
        "Tumse baat karne ke baad dusri chats thodi boring lagti hain.",
        "Tumhare replies short ho sakte hain, impact nahi.",
        "Tumhare saath awkward silence bhi theek lagega.",
        "Tumhari vibe expensive lagti hai.",
        "Tumhari smile dekh kar lagta hai sab theek ho jayega.",
        "Tumhari attention mil jaye to din ban jaata hai.",
        "Tumhari problem ye hai ki tum pasand aa jaati ho.",
        "Tumse milne ke baad standards thode high ho gaye.",
        "Tumhare jaisa calm confidence rare hai.",
        "Tumhari baaton mein honesty feel hoti hai.",
        "Tumhari yaad random time par aa jaati hai.",
        "Tumse baat karne ka koi reason nahi chahiye.",
        "Tumhare saath coffee ho ya silence, dono chalega.",
        "Tumhari personality looks se bhi zyada achhi hogi, feeling aa rahi hai.",
        "Tumhari choice achhi hai... abhi mujhse baat jo kar rahi ho.",
        "Tumhari smile ka screenshot hona chahiye.",
        "Tumhari presence se crowd bhi background lagta hai.",
        "Tumhari tareef karne mein exaggeration ki zarurat nahi padti.",
        "Tumhare saath conversations save karne ka mann karta hai.",
        "Tumhare naam mein kuch to baat hai.",
        "Tumhari vibe green flag wali lagti hai.",
        "Tumhe dekh kar lagta hai ki luck kabhi kabhi kaam karta hai.",
        "Tumhari baat karte karte time ka pata nahi chalta.",
        "Tumhari simplicity hi tumhari best quality hai."
    ]
    a = random.choice(pickup_lines)
    b = context.args[0]
    await update.message.reply_text(f"{b} {a}")



#tables 

async def table(update, context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    kela = context.args[0]
    n = int(kela)
    for i in range(1,11):
        await update.message.reply_text(f"{n} x {i} = {n*i}")
    i += 1




#rock paper scissors


async def rps(update, context):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

        you = context.args[0]
        c = random.choice([1,-1,0])
        youdic = {"r":1 , "p":0 , "s":-1}

        if(you in youdic):
            younum = youdic[you]
            revdic = {1:"rock",0:"paper",-1:"scissor"}

            if(younum==1 and c==1):
                    await update.message.reply_text(f" draw 🟰 \n your choice {revdic[younum]} 🪨 , computers choice {revdic[c]}🪨") 
    
            elif(younum==1 and c==0):
                    await update.message.reply_text(f" you lost ❌  \n your choice {revdic[younum]} 🪨 , computers choice {revdic[c]} 🗒")
    
                        
            elif(younum==1 and c==-1):
                    await update.message.reply_text(f" you won .✅. \n your choice {revdic[younum]} 🪨 , computers choice {revdic[c]}✂")


            elif(younum==0 and c==0): 
                    await update.message.reply_text(f" draw 🟰 \n your choice {revdic[younum]} 🗒 , computers choice {revdic[c]} 🗒")

                    
            elif(younum==0 and c==-1):
                    await update.message.reply_text(f" you lost ❌  \n your choice {revdic[younum]} 🗒 , computers choice {revdic[c]}✂")


            elif(younum==0 and c==1):
                    await update.message.reply_text(f" you won .✅. \n your choice {revdic[younum]} 🗒 , computers choice {revdic[c]} 🪨") 


            elif(younum==-1 and c==-1):
                    await update.message.reply_text(f" draw 🟰 \n your choice {revdic[younum]}✂ , computers choice {revdic[c]}")

                    
            elif(younum==-1 and c==1):
                    await update.message.reply_text(f" you lost ❌  \n your choice {revdic[younum]} ✂, computers choice {revdic[c]} 🪨 ") 

                    
            elif(younum==-1 and c==0):
                    await update.message.reply_text(f" you won .✅. \n your choice {revdic[younum]}✂ , computers choice {revdic[c]} 🗒")


        else:
                await update.message.reply_text("kuch to gdbd h daya")
                        



# ================number guessing game ================
games = {}
async def numguess(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")


    user_id = update.effective_user.id

    games[user_id] = {
        "number": random.randint(1,100),
        "attempts": 0
    }

    await update.message.reply_text(
        "🎯 I chose a number between 1 and 100.\nGuess using /guess <number>"
    )
             
async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if user_id not in games:
        await update.message.reply_text(
            "Pehle /numguess karo 😎"
        )
        return

    if len(context.args) != 1:  
        await update.message.reply_text(
            "Usage: /guess 69"
        )
        return

    guessed_num = int(context.args[0])

    games[user_id]["attempts"] += 1

    secret_num = games[user_id]["number"]

    if guessed_num > secret_num:

        await update.message.reply_text(
            "📉 Guess lower number than this"
        )

    elif guessed_num < secret_num:

        await update.message.reply_text(
            "📈 Guess higher number than this"
        )

    else:

        attempts = games[user_id]["attempts"]

        await update.message.reply_text(
            f"🎉 You won in {attempts} chances!\n\t/numguess to play again"
        )

        del games[user_id]

#============== notes app ===============

async def save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    note = " ".join(context.args)
    userid = update.effective_user.id
    with open(f"notesDATA/data_{userid}","a") as f:
         f.write(f"{note} \n" )
    
    await update.message.reply_text("aapka sman save ho gaya h .., \n kripya /mynotes se dekhe kya kya save h ")


async def mynotes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userid = update.effective_user.id
    with open(f"notesDATA/data_{userid}","r") as f:
         content = f.read()
    await update.message.reply_text(content)
    await update.message.reply_text(" / delete will delete ur all notes")




async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userid = update.effective_user.id
    with open(f"notesDATA/data_{userid}","w") as f:
        f.write(" ")
    await update.message.reply_text("deleted all notes")

# ==== fun ===============


async def nude(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    await update.message.reply_text("⠄⠄⠄⣀⣠⣤⣤⣤⣄⡀⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⣴⣿⣿⣿⡿⣿⡿⣗⢌⢳⡀⠄⠄⠄ ⠄⠄⠄⠄⠄⣼⣿⡇⣿⠹⡸⡹⣷⡹⡎⣧⢳⠄⠄⠄ ⠄⠄⠄⠄⠄⣿⣿⠱⡙⠰⣢⡱⢹⡇⡷⢸⢸⠄⠄⠄ ⠄⠄⠄⠄⠄⢿⢸⡈⣉⣤⠠⣴⡄⡇⠁⠄⢸⠄⠄⠄ ⠄⠄⠄⠄⠄⠸⡆⡃⡙⢍⣹⡿⢓⠄⠤⣐⡟⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠙⠾⠾⠮⣵⢸⡔⢷⣍⠉⠄⠄⠄⠄ ⠄⠄⠄⠄⢀⣴⣾⣿⣷⡺⡋⢞⣎⣚⣛⣳⣴⣶⣤⡀ ⠄⠄⠄⠄⢘⣛⣩⣾⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣷ ⠄⠄⣀⠺⣿⣿⣿⠟⣡⣾⠿⢿⣿⣿⡎⢋⠻⣿⣿⣿ ⠄⠄⣉⣠⣿⣿⡏⣼⣿⠁⠶⠄⣿⣿⡇⡼⠄⠈⠛⢿ ⠄⠄⣈⠻⠿⠟⢁⠘⢿⣷⣶⣾⣿⠟⡰⠃⠄⠄⠄⠄ ⠄⣴⣿⣧⢻⣿⣿⣷⣦⣬⣉⣩⣴⠞⠁⠄⠄⠄⠄⠄ ⠄⠘⠿⠿⢸⣿⣿⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄ ⠄⢤⡝⣧⢸⣿⣿⣿⣿⣿⣿⠟⠄⠄⠄⠄⠄⠄⠄⠄ ⣜⢧⠻⣀⢿⣿⣿⣿⣿⣿⠏⣾⣧⡀⠄⠄⠄⠄⠄⠄ ⠹⢂⣾⣿⠸⣿⣿⣿⣿⡏⣼⣿⣿⣷⠄⠄⠄⠄⠄⠄ ⠄⣿⣿⣿⣧⠹⣿⢻⡿⢰⣿⣿⣿⣿⣇⠄⠄⠄⠄⠄ ⢸⣿⣿⣿⣿⣇⢹⢸⢁⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄ ⢸⣿⣿⣿⣿⣿⣆⠄⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄ ⠸⣿⣿⣿⣿⣿⣿⠄⢿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄ ⠄⣿⣿⣿⣿⣿⣿⠄⠈⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄ ⠄⢹⣿⣿⣿⣿⡟⠄⠄⠹⣿⣿⣿⣿⣿⡇")


# =========say =======================

async def say100(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    mess = " ".join(context.args)
    i = 1
    for i in range(0,100):
        await update.message.reply_text(mess)
        i = i = 1


async def say(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        conten = f.read()
    if str(userid) not in conten:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        content = f.read()
    if str(chatid) not in content:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    mess = " ".join(context.args)

    await update.message.reply_text(mess)





# =================rose=================\


#### admin check new====

async def is_admin(update, context):
     user = await context.bot.get_chat_member( update.effective_chat.id, update.effective_user.id )
     return user.status in ["administrator", "creator"]

async def admin_only(update, context):

    user_id = update.effective_user.id

    # Specific user block
    BLOCKED_USERS = [8603238069]
    if user_id in BLOCKED_USERS:
        await update.message.reply_text(
            "😔 Sorry Moh,\n\n"
            "Aap is command ko use nahi kar sakte.\n"
            "Ye suvidha aapke liye uplabdh nahi hai. 🙏\n" \
            "kyuki hamneaapse bada madarshot insaan nhi dekha "
        )
        return False

    # Admin check
    if not await is_admin(update, context):
        await update.message.reply_text("❌ ixuseme saar is command ko use karne ke liye aapka admin hona bhot jroori h \n mere khyaal se aap admin nhi h \n\n to plz apni aukat me rhe..\n\n\t dhanyawaad ,,, apka pyara bharosewallahbot,, meow")
        return False

    return True




# async def admin_only(update, context):

#     if not await is_admin(update, context):
#         await update.message.reply_text("❌ ixuseme saar is command ko use karne ke liye aapka admin hona bhot jroori h \n mere khyaal se aap admin nhi h \n\n to plz apni aukat me rhe..\n\n\t dhanyawaad ,,, apka pyara bharosewallahbot,, meow")
#         return False

#     return True


# ================= ID =================

async def id(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user

        await update.message.reply_text(
            f"👤 User: {user.first_name}\n"
            f"🆔 ID: {user.id}"
        )
    else:
        await update.message.reply_text(
            f"🆔 Your ID: {update.effective_user.id}\n"
            f"💬 Chat ID: {update.effective_chat.id}"
        )


# ================= INFO =================

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")


    if not update.message.reply_to_message:
        await update.message.reply_text(
            "Reply to a user."
        )
        return

    user = update.message.reply_to_message.from_user

    member = await context.bot.get_chat_member(
        update.effective_chat.id,
        user.id
    )

    await update.message.reply_text(
        f"👤 Name: {user.full_name}\n"
        f"🆔 ID: {user.id}\n"
        f"📛 Username: @{user.username if user.username else 'None'}\n"
        f"⭐ Status: {member.status}"
    )


# ================= BAN =================

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")
    

    if not await admin_only(update, context):
        return

    if not update.message.reply_to_message:
        await update.message.reply_text(
            "Reply to a user."
        )
        return

    target = update.message.reply_to_message.from_user

    await context.bot.ban_chat_member(
        update.effective_chat.id,
        target.id
    )

    await update.message.reply_text(
        f"🔨 Banned: {target.full_name}"
    )


# ================= UNBAN =================

async def unban(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")


    if not await admin_only(update, context):
        return

    if len(context.args) != 1:
        await update.message.reply_text(
            "/unban USER_ID"
        )
        return

    try:
        uid = int(context.args[0])

        await context.bot.unban_chat_member(
            update.effective_chat.id,
            uid
        )

        await update.message.reply_text(
            f"✅ Unbanned: {uid}"
        )

    except:
        await update.message.reply_text(
            "Invalid ID."
        )


#  ================  fake bamm ===========

async def bam(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")


    if not await admin_only(update, context):
        return

    if not update.message.reply_to_message:
        await update.message.reply_text(
            "Reply to a user."
        )
        return

    target = update.message.reply_to_message.from_user

    await update.message.reply_text(
        f"🔨 Bammed succesfully : {target.full_name}\n\n aur ye /bam wali bkcd mat kar lala"
    )


#  =============== KICK =================

async def kick(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")


    if not await admin_only(update, context):
        return

    if not update.message.reply_to_message:
        await update.message.reply_text(
            "Reply to a user."
        )
        return

    target = update.message.reply_to_message.from_user

    await context.bot.ban_chat_member(
        update.effective_chat.id,
        target.id
    )

    await context.bot.unban_chat_member(
        update.effective_chat.id,
        target.id
    )

    await update.message.reply_text(
        f"👢 Kicked: {target.full_name}"
    )


# ================= MUTE =================

async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    if not await admin_only(update, context):
        return

    if not update.message.reply_to_message:
        await update.message.reply_text(
            "Reply to a user."
        )
        return

    target = update.message.reply_to_message.from_user

    await context.bot.restrict_chat_member(
        update.effective_chat.id,
        target.id,
        permissions=ChatPermissions(
            can_send_messages=False
        )
    )

    await update.message.reply_text(
        f"🔇 Muted: {target.full_name}"
    )


# ================= UNMUTE =================

async def unmute(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    if not await admin_only(update, context):
        return

    if not update.message.reply_to_message:
        await update.message.reply_text(
            "Reply to a user."
        )
        return

    target = update.message.reply_to_message.from_user

    await context.bot.restrict_chat_member(
        update.effective_chat.id,
        target.id,
        permissions=ChatPermissions(
            can_send_messages=True,
            can_send_audios=True,
            can_send_documents=True,
            can_send_photos=True,
            can_send_videos=True,
            can_send_video_notes=True,
            can_send_voice_notes=True,
            can_send_polls=True,
            can_add_web_page_previews=True,
            can_change_info=False,
            can_invite_users=True,
            can_pin_messages=False
        )
    )

    await update.message.reply_text(
        f"🔊 Unmuted: {target.full_name}"
    )


# ================= PROMOTE =================

async def promote(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        content = f.read()
    if str(userid) not in content:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        conten = f.read()
    if str(chatid) not in conten:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    if not await admin_only(update, context):
        return

    if not update.message.reply_to_message:
        await update.message.reply_text(
            "Reply to a user."
        )
        return

    target = update.message.reply_to_message.from_user

    await context.bot.promote_chat_member(
        update.effective_chat.id,
        target.id,
        can_delete_messages=True,
        can_restrict_members=True,
        can_invite_users=True,
        can_pin_messages=True
    )

    await update.message.reply_text(
        f"⭐ Promoted: {target.full_name}"
    )


# ================= DEMOTE =================

async def demote(update: Update, context: ContextTypes.DEFAULT_TYPE):

    userid = update.effective_user.id
    with open("data_all.txt","r") as f:
        conten = f.read()
    if str(userid) not in conten:
        with open("data_all.txt","a") as f:
            f.write(f"{userid}\n")


    chatid = update.effective_chat.id
    with open("datachat.txt","r") as f:
        content = f.read()
    if str(chatid) not in content:
        with open("datachat.txt","a") as f:
            f.write(f"{chatid}\n")

    if not await admin_only(update, context):
        return

    if not update.message.reply_to_message:
        await update.message.reply_text(
            "Reply to an admin."
        )
        return

    target = update.message.reply_to_message.from_user

    await context.bot.promote_chat_member(
        update.effective_chat.id,
        target.id,
        can_delete_messages=False,
        can_restrict_members=False,
        can_invite_users=False,
        can_pin_messages=False,
        can_manage_chat=False
    )

    await update.message.reply_text(
        f"⬇️ Demoted: {target.full_name}"
    )





app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("Start", start))
app.add_handler(CommandHandler("hi", hi))
app.add_handler(CommandHandler("say", say))
app.add_handler(CommandHandler("say100", say100))
app.add_handler(CommandHandler("save", save))
app.add_handler(CommandHandler("mynotes", mynotes))
app.add_handler(CommandHandler("delete", delete))
app.add_handler(CommandHandler("bye", bye))
app.add_handler(CommandHandler("luck", luck))
app.add_handler(CommandHandler("nude", nude))
app.add_handler(CommandHandler("sum", sum))
app.add_handler(CommandHandler("div", div))
app.add_handler(CommandHandler("mul", mul))
app.add_handler(CommandHandler("sub", sub))
app.add_handler(CommandHandler("cal", cal))
app.add_handler(CommandHandler("roll", roll))
app.add_handler(CommandHandler("prime", prime))
app.add_handler(CommandHandler("help", help))   
app.add_handler(CommandHandler("toss", toss))
app.add_handler(CommandHandler("surprise", surprise))
app.add_handler(CommandHandler("table", table))
app.add_handler(CommandHandler("flirt", flirt))
app.add_handler(CommandHandler("rps", rps))
app.add_handler(CommandHandler("numguess",numguess))
app.add_handler(CommandHandler("guess",guess))
app.add_handler(CommandHandler("broadcast",broadcast))
app.add_handler(CommandHandler("cbroadcast",cbroadcast))
app.add_handler(CommandHandler("gbroadcast",gbroadcast))
app.add_handler(CommandHandler("totalusers",totalusers))
app.add_handler(CommandHandler("menu",menu))
app.add_handler(CommandHandler("truth",truth))
app.add_handler(CommandHandler("dare",dare))
app.add_handler(CallbackQueryHandler(button))

app.add_handler(CommandHandler("id", id))
app.add_handler(CommandHandler("info", info))

app.add_handler(CommandHandler("ban", ban))
app.add_handler(CommandHandler("bam", bam))
app.add_handler(CommandHandler("unban", unban))
app.add_handler(CommandHandler("kick", kick))

app.add_handler(CommandHandler("mute", mute))
app.add_handler(CommandHandler("unmute", unmute))

app.add_handler(CommandHandler("promote", promote))
app.add_handler(CommandHandler("demote", demote))


print("Bot is running...")
import asyncio
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())
app.run_polling()
