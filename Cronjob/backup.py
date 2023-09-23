from Utils.utils import backup_panel
from AdminBot.bot import bot
from config import ADMINS_ID

# Send backup file to admins
def cron_backup():
    file_name = backup_panel()
    if file_name:
        for admin_id in ADMINS_ID:
            bot.send_document(admin_id, open(file_name, 'rb'))
