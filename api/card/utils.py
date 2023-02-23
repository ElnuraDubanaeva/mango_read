from datetime import datetime
import os


def path_and_rename(instance, filename):
    now = datetime.now()
    upload_to = "mango_covers"
    ext = filename.split(".")[-1]
    filename = f'{instance.mango_name}{now.strftime("d%-m%-Y% H%-M%")}.{ext}'
    return os.path.join(upload_to, filename)
