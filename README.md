﻿# EDMC-Triumvirate
Elite Dangerous Market Connector (EDMC) с плагином Triumvirate является мощнейшим инструментом по обработке данных, позволяет отслеживать влияние в подконтрольных фракционных системах, точечно прописывать задачи по БГС к каждой системе, собирать научные данные, координировать работу пилотов, собирать статистические данные по Таргоидам, систему запроса помощи и дозаправки, систему опознавания "свой-чужой". В дальнейшем плагин будет подготовлен для работы в оверлее игры и получит ряд улучшений, призванных упростить работу пилотов фракций на просторах Галактики.

***Конфиденциальная информация пользователя, характеристики системы и необщедоступные персональные данные принципиально не собираются, не хранятся и не обрабатываются.***

# Обратите особое внимание:

Плагин Triumvirate для EDMC категорически НЕСОВМЕСТИМ с плагинами EDMC-Canonn, EDMC-USS-Survey и с устаревшим EDMC-USS-Survey-Triumvirate-edition. EDMC-Canonn был изначально интегрирован в Triumvirate. Просьба устанавливать плагин Triumvirate "вчистую", на EDMC в котором ранее не присутствовали EDMC-Canonn, EDMC-USS-Survey, EDMC-USS-Survey-Triumvirate-edition.

## Инструкция по установке:

1) Скачать и установить последнюю версию [EDMarketConnector](https://github.com/Marginal/EDMarketConnector/blob/rel-342/README.md#installation) (если уже не установлен, обязательно проверьте EDMC на наличие обновлений)

2) Скачать последний релиз плагина [EDMC-Triumvirate](https://github.com/VAKazakov/EDMC-Triumvirate/releases/latest), нажав на кнопку Source code(zip)

3) Распаковать папку с плагином в %USERPROFILE%\AppData\Local\EDMarketConnector\plugins (это можно вставить в адресную строку проводника)

4) Запустить EDMC, если появилось окно [такого](https://cdn.discordapp.com/attachments/518418556615000074/590004329692397579/unknown.png) вида, то перейти к шагу 5, иначе вам будет необходимо проверить правильность установки  
 
5) Включить в настройках плагина Triumvirate (вкладка Triumvirate находится в настройках EDMC) автообновление

6) ***Вы Великолепны***
 
# Функции плагина:
  
## Элемент системы ориентирования

Система ориентирования используется для навигации при полетах до точек интереса и включает в себя:
 
 * Система по отслеживанию уровней влияния фракций в подконтрольных системах. Этот инструмент дает краткую информационную сводку по состоянию систем с присутствием наших фракций. Для руководителей фракций присутствует функция ручного назначения задач по конкретным системам для выдачи напрямую в плагин.
 * Дислокация  ваших судов. Инструмент, выдающий в реальном времени информацию о местонахождение ваших судов. 
 
## Элемент новостного узла

Позволяет ознакомиться с последними новостями и актуальной информацией по Галактике.

## Элемент по отчетам о перехватах Таргоидами

Позволяет собирать и анализировать информацию о времени и месте перехватов ваших судов Таргоидами. Служит для точной оценки масштабов инопланетного вторжения.

## Элемент по отчетам о NHSS

Собирает и анализирует информацию об обнаруженных инопланетных (чит. Таргоидских) сигналах.

## Элемент Кодекса

Собирает информацию записей журнала и синхронизирует ее с внешними службами, такимим как [база данных Canonn](https://api.canonn.tech/documentation).

## Элемент по анализу ликвидации Таргоидов

Собирает и обрабатывает информацию о времени, месте, типе и количестве сбитых Таргоидских кораблей. Служит для подведения итогов недели и выстраивания четкого плана по противодействию инопланетному вторжению.

## Элемент по анализу информации из журнала пилота

Собирает и обрабатывает информацию из бортового журнала. Обеспечивает обновление информации о рынках, товарах, ценах. Помогает всем пилотам получать актуальные данные. Передаёт полученную информацию на профильные сайты INARA, EDSM, EDDB. 

## Элемент по анализу отчетов FSS

Собирает и анализирует полную информацию о текущей системе.

## Элемент по принятию команд от пользователя

### Команда /sos

После того, как пилот напишет в чате игры команду "/sos" (в любом регистре), плагином будет сформирован и передан в чат дискорда фракции* (специально выделенный канал) пакет данных с местоположением, количеством топлива, местом и временем до опустошения бака. Благодаря этим данным, пилоту попавшему в опасную ситацию, можно будет своевремнно довезти топливо и произвести дозаправку.
* Если вы независимый пилот (по данным плагина) то ваш запрос о помощи будет передан в Close Encounters Corps


## Элемент системы опознавания окружающих судов

### Система опознавания "свой-чужой"

Анализ окружающего пространства на факт наличия кораблей, выдача информации о том, союзные ли это суда, либо суда противников выбранной фракции.


## Элемент STCS (Space Traffic Control System)

### Работа с союзным трафиком

Добавляет возможность выполнения диспетчерских функций при проведении масштабных фракционных мероприятий.

## Возможные перспективные элементы плагина

### Элемент вывода навигационной информации

Добавляет возможность визуальной орбитальной навигации и сопровождения судна по известным координатам на планетах, для оперативного достижения POI. 

### Элемент вывода справочной информации по POI

Добавляет возможность отображения известной информации о конкретном поселении в интерфейсе коннектора. Вывод данных по классификации, карты, если доступна, а также ссылки на дополнение данных по этому поселению.

### Элемент вывода информации оверлейно

Добавляет возможность отображения информации в теле игры.

### Элемент вывода информации о пройденном SRV расстоянии

Добавляет возможность отображения счетчика пройденного расстояния за время нахождения в SRV.
