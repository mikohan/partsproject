from django.utils.translation import gettext as _


MAIN_PAGE_CHOICES = (
    (1, _("Легковые запчасти")),
    (2, _("Новые поступления")),
    (3, _("Запчасти к спецтехнике")),
    (5, _("Разные запчасти")),
    (6, _("Фичуред продукт")),
    (7, _("Часто просматриваемые")),
    (8, _("Бестселлер"))
)
RELEVANCE_CHOICES = (
    (1, _("Unread")),
    (2, _("Read"))
)