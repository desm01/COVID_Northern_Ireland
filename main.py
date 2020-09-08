import COVID_Web
from apscheduler.schedulers.blocking import BlockingScheduler

def main():
    scr = COVID_Web.Scrapper()
    scheduler = BlockingScheduler()
    scheduler.add_job(scr.run, 'interval', minutes=1)
    scheduler.start()
    


main()
