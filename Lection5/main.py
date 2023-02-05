# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# fruits = ['apple', 'blueberry', 'cherry', 'orange']
# counts = [40, 100, 30, 55]
# bar_labels = ['green', 'blue', '_red', 'orange']
# bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:orange']

# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

# ax.set_ylabel('fruit supply')
# ax.set_title('Fruit supply by kind and color')
# ax.legend(title='Fruit color')

# plt.show()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from spy import *

app = ApplicationBuilder().token("6089088422:AAG9t_tTWw0rtZB6UT32eDJhcXS5WIq1Ijk").build()



app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("bond", bond_command))
app.add_handler(CommandHandler("stock", stock_command))
app.add_handler(CommandHandler("Multiple", multiple_command))
app.add_handler(CommandHandler("DCF", dcf_command))


print('server start')
app.run_polling()






