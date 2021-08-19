import eel
from mynavi_sample import *


@eel.expose
def mynavi_search(keyword,csv):
    main(keyword,csv)




eel.init("web")


eel.start("main.html")