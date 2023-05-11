from Tyre.tyre import Tyre


class Carrigan(Tyre):
    def __init__(self, tyre_array):
        self.tyre_array = tyre_array
        

    def needs_service(self,tyre_array):
        for i in  tyre_array :
            if i>=3:
                return True