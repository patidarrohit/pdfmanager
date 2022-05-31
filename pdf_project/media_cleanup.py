from apscheduler.schedulers.background import BackgroundScheduler
from pathlib import Path
import os

scheduler = BackgroundScheduler()
BASE_DIR = Path(__file__).resolve(strict=True).parent
work_dir = os.path.join(BASE_DIR, 'media/temp')
src_dir_list = ['pdf_merge', 'pdf_rotate', 'pdf_split', 'pdf_extract', 'pdf_watermark', 'pdf_info']

@scheduler.scheduled_job('interval', minutes=10)
def clean_old_files():
    for i in src_dir_list:
        tgt_dir = os.path.join(work_dir, i)
        if os.path.isdir(tgt_dir):
            res = os.popen(f"find {tgt_dir} -maxdepth 1 -type d -mmin +5 -print").read()
            res = res.split("\n")[:-1]
            if len(res) > 0 and res[0] == tgt_dir:
                res = res[1:]
            for j in res:
                os.system(f"rm -rf {j}")
                print(f"Directory {j} has been deleted.")


scheduler.start()