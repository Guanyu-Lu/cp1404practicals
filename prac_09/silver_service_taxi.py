from prac_09.taxi import Taxi
class SilverServiceTaxi(Taxi):

    def __init__(self,name,fuel,fanciness):
        super().__init__(name, fuel)
        self.price_per_km=fanciness*1.23
        self.current_fare_distance=0
        self.flagfall=4.5

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare()+self.flagfall
    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()},plus flagfall of ${self.flagfall:.2f}"

