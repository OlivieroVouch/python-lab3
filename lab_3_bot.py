from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from telegram import ChatAction

task = []  # define a global list named "task" visible externally by all functions

# reading FILE from prompt
from sys import argv

script, first = argv  ## 'script' is a string storing the application name while 'first' stores the name of the external file
print("The file is called", script)  # print file name
print("The parameter is", first)  # print the parameter read --> task_list name
txt = open(first)  # open task_list text file
task = txt.readlines()  # read task_list and put it in a string 'task'
txt.close()  # close FILE
task = [line.rstrip('\n') for line in task] # read the string and clean it from newlines
# task = [task.split("\n")]  # split the list into sub-lists containing each a different task


def start(bot, update):  # function handling the start msg from Telegram
    update.message.reply_text("Hello!")  # reply with the specified string to the '/start' command


def showTasks(bot, update):  # function for handling the '/showTasks' command from Telegram
    if not task:  # if the list, put into a string, is empty
        update.message.reply_text("Nothing to do here,Sorry!")  # print this message
        print("Nothing to do here,Sorry!")
    else:  # otherwise
        update.message.reply_text(str(task))  # print the content of the string


def newTask(bot, update, args):  # take a new task as a command
    update.message.reply_text("Hey guy, it seems you'd like to add a new task!")
    update.message.reply_text("Let's insert it:")
    n_task = ' '.join(args)
    task.append(n_task)  # add the new task to the list
    update.message.reply_text("The new Task was successfully added to the list")  # print the content of the string


def removeTask(bot, update, args): # function to remove a specified task from input
    boolean = False
    update.message.reply_text("Removing task...")
    n_task = ' '.join(args)
    ## loop over the list to search for the task to be removed
    for tasks in task:
        if tasks == n_task:
            boolean = True
            task.remove(tasks)
            update.message.reply_text("The Task was successfully deleted!")

    if boolean == 0:
        update.message.reply_text("The Task you specified is not in the list") # print the content of the string



def main():
    updater = Updater("569909977:AAHc0SkWOp9WrkKSfflmaUSDPMIZD-EUcXE")  # Object creation with token from Telegram bot

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("showTasks", showTasks))
    dp.add_handler(CommandHandler("newTask", newTask, pass_args=True))
    dp.add_handler(CommandHandler("removeTask", removeTask, pass_args=True))


    updater.start_polling()

    updater.idle()


if __name__ == '__main__':  # this statement acts, in python, as a main function
    main()
