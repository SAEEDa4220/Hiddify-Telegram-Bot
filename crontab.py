# Crontab
from Cronjob.backup import cron_backup
from Cronjob.reminder import cron_reminder
import argparse

# use argparse to get the arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--backup", action="store_true", help="Backup the panel")
    parser.add_argument("--reminder", action="store_true", help="Send reminder to users")
    args = parser.parse_args()

    # run the functions based on the arguments
    if args.backup:
        cron_backup()
    elif args.reminder:
        cron_reminder()

# To run this file, use this command:
# python3 crontab.py --backup
# python3 crontab.py --reminder
