# -*- coding: utf-8 -*-
import sys

users_base_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTXE8HCavThmJt1Wshy3GyF2ZJ-264SbNRVucsPUe2rbEgpm-e3tqsX-8K2mwsG4ozBj6qUyOOd4RMe/pub?gid=1832580214&single=true&output=tsv"
news_url = "https://docs.google.com/spreadsheets/d/1UnrH5ULSycKzySonUDA79aPBqxUbvNOEOSlW85NY1a0/export?&format=csv"
canonn_patrols_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSMFJL2u0TbLMAQQ5zYixzgjjsNtGunZ9-PPZFheB4xzrjwR0JPPMcdMwqLm8ioVMp3MP4-k-JsIVzO/pub?gid=282559555&single=true&output=csv"
bgs_tasks_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQQZFJ4O0nb3L1WJk5oMEPJrr1w5quBSnPRwSbz66XCYx0Lq6aAexm9s1t8N8iRxpdbUOtrhKqQMayY/pub?gid=0&single=true&output=csv"
edsm_poi_url = "https://www.edsm.net/en/galactic-mapping/json"

ships = {
    "adder": " Adder",
    "typex_3": " Alliance Challenger",
    "typex": " Alliance Chieftain",
    "typex_2": " Alliance Crusader",
    "anaconda": "а Anaconda",
    "asp explorer": " Asp Explorer",
    "asp": " Asp Explorer",
    "asp scout": " Asp Scout",
    "asp_scout": " Asp Scout",
    "beluga liner": "а Beluga Liner",
    "belugaliner": "а Beluga Liner",
    "cobra mk. iii": "а Cobra MkIII",
    "cobramkiii": "а Cobra MkIII",
    "cobra mk. iv": "а Cobra MkIV",
    "cobramkiv": "а Cobra MkIV",
    "diamondback explorer": " Diamondback Explorer",
    "diamondbackxl": " Diamondback Explorer",
    "diamondback scout": " Diamondback Scout",
    "diamondback": " Diamondback Scout",
    "dolphin": " Dolphin",
    "eagle": " Eagle",
    "federal assault ship": " Federal Assault Ship",
    "federation_dropship_mkii": " Federal Assault Ship",
    "federal corvette": " Federal Corvette",
    "federation_corvette": " Federal Corvette",
    "federal dropship": " Federal Dropship",
    "federation_dropship": " Federal Dropship",
    "federal gunship": " Federal Gunship",
    "federation_gunship": " Federal Gunship",
    "fer-de-lance": " Fer-de-Lance",
    "ferdelance": " Fer-de-Lance",
    "hauler": " Hauler",
    "imperial clipper": " Imperial Clipper",
    "empire_trader": " Imperial Clipper",
    "imperial courier": " Imperial Courier",
    "empire_courier": " Imperial Courier",
    "imperial cutter": " Imperial Cutter",
    "cutter": " Imperial Cutter",
    "imperial eagle": " Imperial Eagle",
    "empire_eagle": " Imperial Eagle",
    "keelback": " Keelback",
    "independant_trader": " Keelback",  # ???
    "krait_mkii": " Krait MkII",
    "krait_light": " Krait Phantom",
    "mamba": "а Mamba",
    "orca": "а Orca",
    "python": " Python",
    "sidewinder": " Sidewinder",
    "type 6 transporter": " Type-6 Transporter",
    "type6": " Type-6 Transporter",
    "type 7 transporter": " Type-7 Transporter",
    "type7": " Type-7 Transporter",
    "type 9 heavy": " Type-9 Heavy",
    "type9": " Type-9 Heavy",
    "type 10 defender": " Type-10 Defender",
    "type9_military": " Type-10 Defender",
    "viper mk. iii": " Viper MkIII",
    "viper": " Viper MkIII",
    "viper mk. iv": " Viper MkIV",
    "viper_mkiv": " Viper MkIV",
    "vulture": "а Vulture",
}

states = {
    "civilliberty": "Гражданские свободы",
    "none": "",
    "boom": "Бум",
    "bust": "Спад",
    "civilunrest": "Гражданские беспорядки",
    "civilwar": "Гражданская война",
    "election": "Выборы",
    "expansion": "Экспансия",
    "famine": "Голод",
    "investment": "Инвестиции",
    "lockdown": "Изоляция",
    "outbreak": "Эпдемия",
    "retreat": "Отступление",
    "war": "Война",
}

support_message = """В случае возникновения проблем с плагином
или в случае, если Вы поставили неправильное сообщество в гугл-форме,
пишите в канал CEC #triumvirate_tech_support или в личку Казаков#4700"""
