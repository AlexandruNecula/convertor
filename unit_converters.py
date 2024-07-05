class LengthConverter:
    # Dicționar pentru conversia lungimii
    length_units = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "inches": 39.3701,
        "feet": 3.28084,
        "yards": 1.09361,
    }

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit not in LengthConverter.length_units or to_unit not in LengthConverter.length_units:
            raise ValueError("Unități necunoscute pentru conversie")
        # Convertirea la metri, apoi la unitatea dorită
        return value * LengthConverter.length_units[from_unit] / LengthConverter.length_units[to_unit]

class WeightConverter:
    # Dicționar pentru conversia greutății
    weight_units = {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1e6,
        "tons": 0.001,
        "pounds": 2.20462,
        "ounces": 35.274,
    }

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit not in WeightConverter.weight_units or to_unit not in WeightConverter.weight_units:
            raise ValueError("Unități necunoscute pentru conversie")
        return value * WeightConverter.weight_units[from_unit] / WeightConverter.weight_units[to_unit]

class TemperatureConverter:
    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        elif from_unit == "celsius" and to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "celsius" and to_unit == "kelvin":
            return value + 273.15
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            return (value - 32) * 5/9
        elif from_unit == "fahrenheit" and to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "kelvin" and to_unit == "celsius":
            return value - 273.15
        elif from_unit == "kelvin" and to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            raise ValueError("Combinatie necunoscută de unități pentru conversie")
