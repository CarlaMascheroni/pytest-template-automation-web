from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By

def inputSearchId():
    return UIElement(By.XPATH, "//input[@class='gLFyf gsfi']")

def searchXpath2():
    return UIElement(By.XPATH, "//ul/li[1]/div/div[2]/div[1]")

def searchXpath():
    return UIElement(By.XPATH, "//div[3]/center/input[1]")

def STATS_ID():
    return UIElement(By.ID, "rcnt")