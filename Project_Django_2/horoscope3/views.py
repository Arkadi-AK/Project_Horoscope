from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import datetime
from dataclasses import dataclass

# Create your views here.


zodiac_dict = {

    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}

date_zodiac_dict = {

    'aries': [("21-03-2014", "%d-%m-%Y"), ("20-04-2014", "%d-%m-%Y")],
    'taurus': [("21-04-2014", "%d-%m-%Y"), ("21-05-2014", "%d-%m-%Y")],
    'gemini': [("22-05-2014", "%d-%m-%Y"), ("21-06-2014", "%d-%m-%Y")],
    'cancer': [("22-06-2014", "%d-%m-%Y"), ("22-07-2014", "%d-%m-%Y")],
    'leo': [("23-07-2014", "%d-%m-%Y"), ("23-08-2014", "%d-%m-%Y")],
    'virgo': [("22-08-2014", "%d-%m-%Y"), ("23-09-2014", "%d-%m-%Y")],
    'libra': [("24-09-2014", "%d-%m-%Y"), ("23-10-2014", "%d-%m-%Y")],
    'scorpio': [("24-10-2014", "%d-%m-%Y"), ("22-11-2014", "%d-%m-%Y")],
    'sagittarius': [("23-11-2014", "%d-%m-%Y"), ("21-12-2014", "%d-%m-%Y")],
    'capricorn': [("23-12-2014", "%d-%m-%Y"), ("20-01-2015", "%d-%m-%Y")],
    'aquarius': [("21-01-2015", "%d-%m-%Y"), ("19-02-2015", "%d-%m-%Y")],
    'pisces': [("20-02-2015", "%d-%m-%Y"), ("20-03-2015", "%d-%m-%Y")],

}

zodiac_types_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def get_info_types(request):
    elements = list(zodiac_types_element)
    types = ''
    for type in elements:
        # redirect_path = reverse('horoscope-types', args=[type])
        types += f"<li> <a href='{type}'> {type.title()} </a> </li>"
    main_url = reverse('horoscope-main', args=[])
    response = f"""
        <uol>
            {types}
        </ul>
        <br>
        <br>
        <b> <a f' href='{main_url}'> На главную </a></b>
        """
    return HttpResponse(response)


def index(reqest):
    zodiacs = list(zodiac_dict)
    # li_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
    context_zod = {
        'zodiacs': zodiacs
    }
    return render(reqest, 'horoscope3/index.html', context=context_zod)


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'Зовут {self.name}, возраст {self.age} лет'


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {'description_zodiac': description,
            'sign': sign_zodiac.title(),
            'my_list': [1, 2],
            'my_dict': {'name': 'Jack', 'age': 20},
            'my_class': Person('Will', 55),
            }
    return render(request, 'horoscope3/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def get_info_zodiac_types(request, zodiac_types):
    elements_type = zodiac_types_element.get(zodiac_types, None)
    type_elements1 = ''
    for type in elements_type:
        redirect_path = reverse('horoscope-name', args=[type])
        type_elements1 += f"<li> <a href='{redirect_path}'> {type.title()} </a> </li>"
    response = f"""
        <uol>
            {type_elements1}
        </ul>
        <br>
        <br>
        <b> <a href='types'> Назад на 4 Стехии </a></b>
        """
    return HttpResponse(response)


def get_info_by_date(request, month, day):
    if datetime.strptime(f"{day}-{month}", "%d-%m") < datetime.strptime("20-03", "%d-%m"):
        year = '2015'
    else:
        year = '2014'
    dt = datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y")
    ff = ''
    for i in date_zodiac_dict:
        if datetime.strptime(*date_zodiac_dict[i][0]) < dt < datetime.strptime(*date_zodiac_dict[i][1]):
            ff = f'<h2>{i.title()} </h2>'
    return HttpResponse(ff)
