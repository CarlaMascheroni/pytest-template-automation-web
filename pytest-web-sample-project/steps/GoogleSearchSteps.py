from pages import GoogleSearchPage as page
from core.steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion

class GoogleSearchSteps(BaseStep):

    def enterSearchCriteria(self, text):
        driverElem = page.inputSearchId()
        driverElem.setText(text)
        return self


    def clickSearchButton(self):
        driverElem = page.searchXpath()
        driverElem.click()
        return self



    def verifyResult(self):
        driverElem = page.STATS_ID()
        Assertion.assertFalse("Resultados no encontrados", driverElem.getText().isEmpty())
        return self
