import Utils
from Response.BaseClasses.OBDResponse import OBDResponse

class EvapPressureAbsolute(OBDResponse):

    def getvalue(self):
        return (int(self.byteA, 16) * 256 + int(self.byteB, 16)) / 200

    def responsecode(self):
        return '41 53'

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()