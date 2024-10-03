import eel
import pyowm

# Sākam eel aplikāciju
eel.init('web')


# Python funkcija, ko sauc JS kods
@eel.expose
def get_weather(city):
    owm = pyowm.OWM("70f9e95c957112dced3aef325106a2b5")  # Tava API atslēga
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        return f"Pilsētā {city} šobrīd ir {temp} grādi!"
    except Exception as e:
        return f"Kļūda: {str(e)}"


# Startējam eel serveri
eel.start('main.html')
