![Latest Release](https://img.shields.io/github/release/VAKazakov/EDMC-Triumvirate.svg)

# EDMC-Triumvirate
Плагин Triumvirate для EDMC, разработанный фракцией Close Encounters Corps, является важной частью общей экосистемы "сервер-сайт-плагин-дискорд", выступает универсальным инструментом по сбору и обработке игровых данных, позволяет отслеживать влияние в подконтрольных фракционных системах, точечно выводить пользователю задачи по БГС непосредственно к каждой системе, координировать работу пилотов, оповещать коллег о нештатных ситуациях в дальних перелетах. В дальнейшем, этот плагин получит ряд улучшений, призванных еще сильнее упростить работу пилотов на просторах Галактики.

***Конфиденциальная информация пользователя, характеристики системы и необщедоступные персональные данные принципиально не собираются, не хранятся и не обрабатываются.***

# Обратите особое внимание:

Плагин для EDMC Triumvirate категорически НЕСОВМЕСТИМ с плагином EDMC-Canonn, EDMC-USS-Survey и с устаревшим EDMC-USS-Survey-Triumvirate-edition. Плагин EDMC-Canonn был изначально интегрирован в Triumvirate, также нами была интегрирована поддержка Discord Presence, FCMC и передача собранных научных данных не только на сервера Canonn, но и по адресам ATEL-IGAU, работает система выдачи и учета выполненных миссий в рамка деятельности против Клуба.

# Функции плагина (будет обновляться по мере внесения улучшений)

## Элемент по принятию команд от пользователя


### Команда /sos

После того, как пилот напишет в чате игры команду "/sos" (в любом регистре), плагином будет сформирован и передан в чат дискорда фракции* (в специально выделенный канал) пакет данных с местоположением, количеством топлива, местом и временем до опустошения бака. Благодаря этим данным, пилоту, попавшему в опасную ситуацию, можно будет своевременно довезти топливо и произвести дозаправку.

\*Если вы независимый пилот (по данным плагина) то ваш запрос о помощи будет передан в Close Encounters Corps

* Прорабатывается добавление функции отображения пройденного расстояния на ТРП.

## Элемент системы ориентирования (aka Патруль)

Система ориентирования используется для навигации при полетах до точек интереса и включает в себя:

* Прорабатывается автоматизация и передача всех функций системы по отслеживанию уровней влияния фракций в подконтрольных системах для анализа и обработки на сервера фракции. Этот инструмент дает краткую информационную сводку по состоянию систем с присутствием наших фракций. Для руководителей фракций присутствует функция ручного назначения задач по конкретным системам для выдачи напрямую в плагин и возможность полуавтоматической выдачи задач по купированию негативных статусов.
* Дислокация ваших судов. Инструмент, выдающий в реальном времени информацию о местонахождение ваших судов. Прорабатывается добавление функции подобной компасу/GPS для наглядного полета к точкам интереса.
* Прорабатывается добавление функции орбитальной навигации и следованию по заданным координатам с выдачей справочной информации о известных точках маршрута.
* Прорабатывается добавление функции отправки данных о кораблях командира на сервер и сайт для выдачи информации о местоположении на интерактивной карте в реальном/псевдореальном времени.
* Прорабатывается добавление функции выдачи информации о дислокации вашего корабля-носителя, перечне его характеристик и заполнении топливных баков.
* Прорабатывается добавление функции системы опознания “свой-чужой” для определения того, кто находится перед вами – сопартиец, союзник или противник/нейтрал.

## Элемент новостного узла

Позволяет ознакомиться с последними новостями и актуальной информацией по Галактике.

## Элемент по отчетам о перехватах Таргоидами

Позволяет собирать и анализировать информацию о времени и месте перехватов ваших судов Таргоидами. Служит для точной оценки масштабов инопланетного вторжения.

## Элемент по отчетам о NHSS

Собирает и анализирует информацию об обнаруженных инопланетных сигналах.

## Элемент по отчетам FSS

Собирает и анализирует полную информацию о текущей системе.

## Элемент Кодекса

Собирает информацию записей журнала и в режиме добровольного обмена информацией синхронизирует ее с внешними научными службами, такимим как [база данных Canonn](https://api.canonn.tech/documentation) и [база данных ATEL-IGAU](https://github.com/Elite-IGAU/ATEL-EDMC).

## Элемент по анализу ликвидации Таргоидов

Собирает и обрабатывает информацию о времени, месте, типе и количестве сбитых Таргоидских кораблей. Служит для подведения итогов недели и выстраивания четкого плана по противодействию инопланетному вторжению.

* Прорабатывается добавление функции передачи всей собранной информации на сервера фракции для обработки и передачи в интерактивные таблицы на сайте фракции.

## Элемент по анализу информации из журнала пилота

Собирает и обрабатывает информацию из бортового журнала. Обеспечивает обновление информации о рынках, товарах, ценах. Помогает всем пилотам получать актуальные данные. Передаёт полученную информацию в профильные системы INARA, EDSM, EDDB и тому подобные.

## Элемент сбора информации о кораблях-носителях

Собирает и обрабатывает информацию о корабле-носителе конкретного пилота. Обеспечивает обновление информации на сайте FCMC, позволяет отображать, практически в реальном времени, корабли-носители пилотов фракции на интерактивной карте на сайте фракции. Помогает всем пилотам получать актуальные данные. Передаёт полученную информацию в профильные системы INARA, EDSM, EDDB и тому подобные.

## Элемент по изменению интерфейса в зависимости от фракции

* Прорабатывается добавление функции изменения стиля оформления окна плагина под стиль конкретной фракции игрока.

## Инструкция по установке:

1) Скачать и установить последнюю версию[EDMarketConnector] (https://github.com/Marginal/EDMarketConnector/blob/rel-342/README.md#installation) (если он уже установлен, обязательно проверьте EDMC на наличие обновлений)

2) Скачать самый свежий релиз плагина[EDMC-Triumvirate] (https://github.com/VAKazakov/EDMC-Triumvirate/releases/latest), нажав на кнопку Source code(zip)

3) Распаковать папку с плагином в %USERPROFILE%\AppData\Local\EDMarketConnector\plugins (это можно вставить в адресную строку проводника)

4) Запустить EDMC, если появилось окно [такого](https://cdn.discordapp.com/attachments/518418556615000074/590004329692397579/unknown.png) вида, то перейти к шагу 5, иначе вам будет необходимо проверить правильность установки

5) ***Вы великолепны!***

## Разработка
На текущий момент плагин, как и EDMC в целом, работает на Python 3.7., но, возможен дальнейший переход и на более свежие версии Python.
Как подготовить окружение для разработки:
```bash
pip2 install -r requirements-dev.txt
pre-commit install
```

## Disclaimer
EDMC-Triumvirate was created using assets and imagery from Elite Dangerous, with the permission of Frontier Developments plc, for non-commercial purposes. It is not endorsed by nor reflects the views or opinions of Frontier Developments and no employee of Frontier Developments was involved in the making of it.

EDMC-Triumvirate use data from [Canonn API V2](https://docs.canonn.tech), [ED Star Map (EDSM)](https://www.edsm.net/), [Elite BGS](https://elitebgs.app/), with permision of their owners.

EDMC-Triumvirate based on [EDMC-Canonn](https://github.com/canonn-science/EDMC-Canonn), with permission of initial developers.

All Contents Copyright ©️ 2016-2020 Close Encounters Corps, Triumvirate. KAZAK0V, AntonyVern, Osmium. All Rights Reserved.

Logo - Антон Верницкий aka AntonyVern/Automatic system.
