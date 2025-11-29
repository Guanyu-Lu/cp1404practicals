from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi object which is a specialized Taxi."""

    def __init__(self,name,fuel,fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km
        self.flagfall=4.5

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare()+self.flagfall

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

