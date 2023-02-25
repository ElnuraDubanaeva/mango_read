from django.utils.translation import gettext as _
from rest_framework.serializers import ValidationError
import re


class UppercaseValidator(object):
    """The password must contain at least 1 uppercase letter, A-Z."""

    def validate(self, password, user=None):
        if not re.findall("[A-Z]", password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code="password_no_upper",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 uppercase letter, A-Z.")


class SpecialCharValidator(object):
    """The password must contain at least 1 special character @#$%!^&*"""

    def validate(self, password, user=None):
        if not re.findall("[@#$%!^&*]", password):
            raise ValidationError(
                _(
                    "The password must contain at least 1 special character: "
                    + "@#$%!^&*"
                ),
                code="password_no_symbol",
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 special character: " + "@#$%!^&*"
        )


class IsIncludeOneDigit(object):
    def validate(self, password, user=None):
        if not re.findall(r"(?:[0-9])", password):
            raise ValidationError(
                _(f"Password must include at least one digit"),
                code=f"password_no_digit",
            )

    def get_help_text(self):
        return _("Password must include at least one digit")


class IsIncludeOnlyLatn(object):
    def validate(self, password, user=None):
        if re.findall(r"(?:[а-яА-ЯёЁ])", password):
            raise ValidationError(
                _("Password must include only latn letters"),
                code="password should contain only latn letters",
            )

    def get_help_text(self):
        return _("Password must include only latyn letters")
