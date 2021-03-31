# Suhu Counter.., wait...why i type like this
# OK This is My Learning Proses or Maybe Not Really cuz i Fork it from Someone else
# And little Bit Modification but you get the point

class TemperatureCounter:
    def __init__(self, heat):
        self.heatNumber = heat

    def celcius(self):
        cel = self.heatNumber
        fahren = ((cel / 5) * 9) + 32
        kelvin = cel + 273.15
        reamur = (cel / 5) * 4
        return fahren, kelvin, reamur

    def fahrenheit(self):
        fahren = self.heatNumber
        cel = ((fahren - 32) * 5) / 9
        kelvin = (((fahren - 32) * 5) / 9) + 273
        reamur = ((fahren - 32) * 4) / 9
        return cel, kelvin, reamur

    def kelvin(self):
        kelvin = self.heatNumber
        cel = kelvin - 273.15
        fahren = (((kelvin - 273) * 9) / 5) - 32
        reamur = ((kelvin - 273) * 5) / 9
        return cel, fahren, reamur

    def reamur(self):
        reamur = self.heatNumber
        cel = (reamur * 5) / 4
        fahren = cel + 273
        kelvin = ((reamur * 9) / 4) + 32
        return cel, fahren, kelvin

# I Call it The End of the Day
