from django.utils.translation import gettext_lazy as _
from . import constants

MINIMAL_QUANTITY = _(f"Минимальное кол-во для заказа {constants.MINIMAL_QUANTITY} шт")
CHOICE_REQUIRED = _("Выберите один из пунктов списка")
REQUIRED_FIELD = _("Заполните это поле")
REQUIRED = _("Поле обязательно для заполнения")
TAG_INVALID = _(f"Тэг должен быть больше {constants.TAG_MIN_LENGTH} символов")
DESCRIPTION_INVALID = _(f"Описание должно быть длинной больше {constants.RESTAURANT_DESCRIPTION_MIN_LENGTH} символов")
# TITLE_INVALID = _(f"Название должно быть длинной не менее {constants.TITLE_MIN_LENGTH} символов")
TITLE_INVALID = _(f"Это поле обязательное")
PASSOWRD_INVALID = _(f"Пароль должен быть больше {constants.PASSWORD_MIN_LENGTH} символов")
LOGIN_INVALID = _(f"Логин должен быть больше {constants.LOGIN_MIN_LENGTH} символов")
REASON_INVALID = _(f"Причина должна быть больше {constants.REASON_FOR_CHANGE_MIN_LENGTH} символов")

FIRST_SYMBOL_VALIDATION = _("Первый символ должен быть маленькой буквой английского алфавита, "
                            "а тэг состоять из английского алфавита, чисел и нижнего прочерка '_'")
VALUE_CONTAIN_RULE = _("Тэг должен содержать только буквы английского алфавита и числа")
PASSWORD_NOT_EQUAL = _("Пароли не совпадают")

MANAGER_VALIDATE = _("Какой-то текст чтобы провалидироваться")
WRONG_PARAM = _("Не верно переданный параметр")
MANAGER_SETTINGS_ALREADY_EXIST = _("Настройки менеджера уже добавлены")
MANAGER_SETTINGS_DOESNT_EXIST = _("Настройки менеджера еще не добавлены")
MENU_NOT_FOUND = _("ID такого меню нет")
MENU_DIDNT_GET = _("ID меню не получено")
SUBMENU_NOT_FOUND = _("ID такого подменю нет")
DISH_NOT_FOUND = _("ID такого блюда нет")
THIS_SUBMENU_ALREADY_EXIST = _("Такая категория в этом меню уже есть")
RESTAURANT_ALREADY_EXIST = _("Ресторан уже добавлен")
RESTAURANT_DOESNT_EXIST = _("Ресторан еще не добавлен")
RESTAURANT_IS_NOT_FULL = _("Ресторан заполнен не до конца")
IN_FIRST_CREATE_RESTAURANT = _("Сначала заполните информацию о заведении и загрузите логотип и фон")
WRONG_RESTAURANT_ID = _("Неверно переданный ID ресторана")
ADDRESS_ALREADY_EXIST = _("Адрес уже добавлен")
ADDRESS_DOESNT_EXIST = _("Адрес еще не добавлен")
SERVICE_ALREADY_EXIST = _("Услуги уже добавлены")
SERVICE_DOESNT_EXIST = _("Услуги еще не добавлены")
CONTACTS_ALREADY_EXIST = _("Контакты уже добавлены")
CONTACTS_DOESNT_EXIST = _("Контакты еще не добавлены")

TAG_ALREADY_EXIST = _("Такой тэг уже есть")
TAG_DOESNT_EXIST = _("Такого тэга нет")
TAGS_CANNOT_BE_EQUAL = _("Тэги не могут быть одинаковыми")
OLD_TAG_DOESNT_PASS = _("Старый тэг не подходит")

EMAIL_ALREADY_EXISTS = _("Пользователь с таким email уже существует в базе")
EMAIL_DOESNT_EXIST = _("Пользователя с таким email в системе не существует")
EMAILS_CANNOT_BE_EQUAL = _("Email адреса не могут быть одинаковыми")
EMAILS_RESET_SUCCESSFULLY = _("Email изменен успешно")
EMAIL_IS_NOT_UNIQUE = _("Данный email есть у нескольких ресторанов")
LOGIN_ALREADY_EXISTS = _("Пользователь с таким логином уже существует в базе")
LOGIN_DOESNT_EXIST = _("Пользователя с таким логином в системе не существует")
PHONE_ALREADY_EXISTS = _("Пользователь с таким телефоном уже существует в базе")
WRONG_LOGIN_OR_PASSWORD = _("имя или пароль введены неправильно")
PHONE_INCORRECT = _("Вы ввели неправилный формат телефона")
PASSWORD_RESET_SUCCESSFULLY = _("Пароль изменен успешно")
FORBIDDEN = _("Доступ запрещен")

MENU_COPIED_SUCCESS = _("Меню успешно скопировано")
MENU_COPIED_ERROR = _("Не удалось скопировать, у другого ресторана есть меню")

EXCEL_INCORRECT = _("Excel шаблон заполнен не верно")
MENU_IS_NOT_SELECTED = _("Вы не выбрали меню для подменю")
SUBMENU_EQUAL_TITLES = _("Такое название подменю уже есть")