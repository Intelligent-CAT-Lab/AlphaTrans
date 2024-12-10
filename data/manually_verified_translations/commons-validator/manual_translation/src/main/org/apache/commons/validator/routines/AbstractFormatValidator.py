from __future__ import annotations
import locale
import re
from decimal import Decimal
from io import StringIO
from abc import ABC
import datetime
import typing
import zoneinfo
from typing import *
from decimal import InvalidOperation


class AbstractFormatValidator(ABC):

    __strict: bool = False

    __serialVersionUID: int = -4690687565200568258

    CUSTOM_NUMBER_FORMATTER_SUFFIX = "NUMBER"
    CUSTOM_DATE_FORMATTER_SUFFIX = "DATE"

    def is_before(self, s: str, char1: str, char2: str) -> bool:
        index1 = s.find(char1)
        index2 = s.find(char2)
        
        if index1 == -1 or index2 == -1:
            return False
        
        return index1 < index2
    
    def java_to_python_format(self, java_format: str) -> str:
        java_to_python_map = {
            'yyyy': '%Y',
            'yy': '%y',
            'MMMM': '%B',
            'MMM': '%b',
            'MM': '%m',
            'dd': '%d',
            'HH': '%H',
            'mm': '%M',
            'ss': '%S',
            'a': '%p',
            'z': '%z',
            'EEEE': '%A',
            'E': '%a',
        }
        pattern = re.compile('|'.join(re.escape(key) for key in java_to_python_map.keys()))
        python_format = pattern.sub(lambda x: java_to_python_map[x.group(0)], java_format)

        return python_format
    
    def construct_datetime(self, format_str: str, value: str, tz: datetime.timezone):
        cur_locale = locale.getlocale()
        if cur_locale and 'en_US' in cur_locale:
            known_formats = [
                "%m/%d/%y", "%m/%d/%Y",
                "%m/%d/%y %H:%M",
                "%m/%d/%y %I:%M %p",
                "%Y-%m-%d",
                "%y-%m-%d",
                "%Y-%m-%d",
                "%y-%m-%d",
                "%H:%M",
                "%I:%M %p"
            ] 
        else:
            known_formats = [
                "%m/%d/%y", "%d.%m.%Y", "%d/%m/%Y",
                "%m/%d/%y %H:%M",
                "%m/%d/%y %I:%M %p",
                "%d/%m/%y %H:%M",
                "%d/%m/%y %I:%M %p",
                "%Y-%m-%d",
                "%y-%m-%d",
                "%Y-%m-%d",
                "%y-%m-%d",
                "%H:%M",
                "%I:%M %p"
            ] 

        if format_str is None:
            try:
                if not cur_locale or (cur_locale and not 'en_US' in cur_locale):
                    dt = datetime.datetime.strptime(value, "%x")
                    if tz:
                        dt = dt.replace(tzinfo=tz)
                    return dt
                else:
                    raise ValueError("Intentionally raised to avoid parsing months into dates")
            except ValueError:
                for known_format in known_formats:
                    try:
                        dt = datetime.datetime.strptime(value, known_format)
                        if tz:
                            dt = dt.replace(tzinfo=tz)
                        return dt
                    except ValueError:
                        continue
                raise ValueError(f"Could not parse date: {value}")
        elif (format_str.count('-') == 2 and value.count('-') == 2):
            format_map = {
                "yyyy": "%Y",
                "dd": "%d",
                "MMMM": "%B",
                "MMM": "%b", 
                "MM": "%m",
                "HH": "%H",
                "mm": "%M",
                "hh": "%I",
                "ss": "%S",
                "a": "%p",
                "AM/PM": "%p",
                "yy": "%y"
            }
            known_formats = [
                "%Y-%m-%d",
                "%y-%m-%d",
                "%Y-%m-%d",
                "%y-%m-%d",
                "%H-%M-%S"
            ]
            py_format_str = format_str
            for java_fmt, py_fmt in format_map.items():
                py_format_str = py_format_str.replace(java_fmt, py_fmt)
            if "%H" in py_format_str:
                known_formats = [py_format_str]
            for known_format in known_formats:
                try:
                    dt = datetime.datetime.strptime(value, known_format)
                    if tz:
                        dt = dt.replace(tzinfo=tz)
                    return dt
                except ValueError:
                    continue
            raise ValueError(f"Could not parse date: {value}")
        elif format_str in [f"%x %X", "%X"] or format_str.count(":") > 1:
            try:
                if not cur_locale or (cur_locale and not 'en_US' in cur_locale):
                    dt = datetime.datetime.strptime(value, "%X")
                    if tz:
                        dt = dt.replace(tzinfo=tz)
                    return dt
                else:
                    raise ValueError("Intentionally raised to avoid parsing months into dates")
            except ValueError:
                for known_format in known_formats:
                    try:
                        dt = datetime.datetime.strptime(value, known_format)
                        if tz:
                            dt = dt.replace(tzinfo=tz)
                        return dt
                    except ValueError:
                        continue
                raise ValueError(f"Could not parse date: {value}")
        
        format_map = {
            "yyyy": "%Y",
            "dd": "%d",
            "MMMM": "%B",
            "MMM": "%b", 
            "MM": "%m",
            "HH": "%H",
            "mm": "%M",
            "hh": "%I",
            "ss": "%S",
            "a": "%p",
            "AM/PM": "%p",
            "yy": "%y"
        }
        
        for java_fmt, py_fmt in format_map.items():
            format_str = format_str.replace(java_fmt, py_fmt)

        try:
            dt = datetime.datetime.strptime(value, format_str)
            if tz:
                dt = dt.replace(tzinfo=tz)
            return dt
        except ValueError as e:
            raise ValueError(f"Error parsing date: {e}")
    
    
    def truncate_to_two_chars_after_last_dot(self, s: str) -> str:
        last_dot_index = s.rfind('.')
        
        if last_dot_index == -1:
            return s
        
        before_dot = s[:last_dot_index + 1]
        after_dot = s[last_dot_index + 1:]
        
        if len(after_dot) > 2:
            after_dot = after_dot[:2]
        
        return before_dot + after_dot
    
    def _parse(self, value: str, formatter: typing.Any) -> typing.Any:

        pos = 0

        currency_symbols = [
            "$",    # United States Dollar
            "€",    # Euro
            "¥",    # Japanese Yen
            "£",    # British Pound Sterling
            "A$",   # Australian Dollar
            "C$",   # Canadian Dollar
            "CHF",  # Swiss Franc
            "¥",    # Chinese Yuan
            "kr",   # Swedish Krona
            "NZ$",  # New Zealand Dollar
            "$",    # Mexican Peso
            "S$",   # Singapore Dollar
            "HK$",  # Hong Kong Dollar
            "kr",   # Norwegian Krone
            "₩",    # South Korean Won
            "₺",    # Turkish Lira
            "₹",    # Indian Rupee
            "₽",    # Russian Ruble
            "R",    # South African Rand
            "R$",   # Brazilian Real
            "kr",   # Danish Krone
            "zł",   # Polish Zloty
            "฿",    # Thai Baht
            "Rp",   # Indonesian Rupiah
            "Ft",   # Hungarian Forint
            "Kč",   # Czech Koruna
            "₪",    # Israeli New Shekel
            "$",    # Chilean Peso
            "₱",    # Philippine Peso
            "د.إ",  # United Arab Emirates Dirham
            "$",    # Colombian Peso
            "ر.س",  # Saudi Riyal
            "RM",   # Malaysian Ringgit
        ]

        if (isinstance(formatter, str) and (not "{:,.0f}" in formatter) and\
            formatter.endswith("DISALLOW FRACTION")) or\
            (isinstance(formatter, str) and formatter.endswith("DISALLOW FRACTION") and\
            any(c in value for c in currency_symbols)):
            formatter = formatter[:-len("DISALLOW FRACTION")]
            conv = locale.localeconv()
            decimalPoint = conv['decimal_point']
            if decimalPoint in value:
                locale.setlocale(locale.LC_ALL, "")
                return None

    
        if "en_GB" in locale.getlocale():
            left = "["
            right = "]"
        else:
            left = "("
            right = ")"
        for currency_symbol in currency_symbols:
            if value.startswith(currency_symbol) or (value.startswith("-") and\
                value[1:].startswith(currency_symbol)) or (value.startswith(left) and\
                value.endswith(right) and value[1:].startswith(currency_symbol)) or\
                (value.startswith(left) and value.endswith(right)\
                and value[1] == "-" and value[2:].startswith(currency_symbol)) or\
                "\u00A4" in formatter:
                if ("£" in value or "[" in value) and "\u00A4" in formatter:
                    locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
                    left = "["
                if ("$" in value or "(" in value) and "\u00A4" in formatter:
                    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
                elif "en_US" in locale.getlocale() and value[0] == "-":
                    return None
                locale_specific_currency_symbol = locale.currency(
                    0, symbol=True, grouping=False
                )[0]
                if value and locale_specific_currency_symbol in value:
                    value = value.replace(
                        locale_specific_currency_symbol,
                        ""
                    )
                conv = locale.localeconv()
                decimalPoint = conv['decimal_point']
                thousandsSep = conv['thousands_sep']
                if not thousandsSep:
                    if decimalPoint == ",":
                        thousandsSep = "."
                    elif decimalPoint == ".":
                        thousandsSep = ","
                if value.startswith(left):
                    value = value[0] + "-" + value[1:]
                if decimalPoint == ",":
                    value = value.replace(decimalPoint, ".")
                value = value.replace(thousandsSep, "").replace("(", "")\
                    .replace(")", "").replace("[", "").replace("]", "")
                try:
                    if not "##0.000" in formatter:
                        value = self.truncate_to_two_chars_after_last_dot(value)
                    locale.setlocale(locale.LC_ALL, "")
                    return Decimal(value)
                except Exception:
                    locale.setlocale(locale.LC_ALL, "")
                    return None


        try:
            parsedValue = None
            if isinstance(formatter, list):
                formatter, tz = formatter
            else:
                tz = None
            if "{:.0f}" in formatter or "{:,.0f}" in formatter or "{:,}" in formatter:
                conv = locale.localeconv()
                decimalPoint = conv['decimal_point']
                thousandsSep = conv['thousands_sep']
                if not thousandsSep:
                    if decimalPoint == ",":
                        thousandsSep = "."
                    elif decimalPoint == ".":
                        thousandsSep = ","
                if not self.__strict:
                    valueCopy = re.sub(r'[^\d]+$', '', value)
                else:
                    valueCopy = value
                if self.is_before(valueCopy, decimalPoint, thousandsSep):
                    raise ValueError("Thousand separator appear after decimal points")
                parsedValue = Decimal(
                    valueCopy.replace(decimalPoint, "__temp__")\
                        .replace(thousandsSep, "")\
                        .replace("__temp__", ".")
                )
            elif formatter == "{:.0%}":
                parsedValue = Decimal(value.replace('%', '')) / 100
            elif formatter.endswith(AbstractFormatValidator.CUSTOM_NUMBER_FORMATTER_SUFFIX):
                formatter = formatter[
                    :-len(AbstractFormatValidator.CUSTOM_NUMBER_FORMATTER_SUFFIX)
                ]
                decimalPoint = locale.localeconv()['decimal_point']
                thousandsSep = locale.localeconv()['thousands_sep']
                if not thousandsSep:
                    if decimalPoint == ",":
                        thousandsSep = "."
                    elif decimalPoint == ".":
                        thousandsSep = ","
                temp_string = formatter.replace(decimalPoint, '__temp__').replace(thousandsSep, ',')
                formatter = temp_string.replace('__temp__', '.')
                separator = re.search(r'[^\d]', formatter)
                if separator:
                    separator = separator.group(0)
                else:
                    separator = ''
                if not self.__strict:
                    valueCopy = re.sub(r'[^\d]+$', '', value)
                else:
                    valueCopy = value
                if self.is_before(valueCopy, decimalPoint, thousandsSep):
                    raise ValueError("Thousand separator appear after decimal points")
                parsedValue = Decimal(
                    valueCopy.replace(separator, '').replace(thousandsSep, '')
                )
            elif formatter == "%x":
                parsedValue = self.construct_datetime(None, value, tz)
            elif formatter == f"%x %X" or formatter == "%X":
                parsedValue = self.construct_datetime(formatter, value, tz)
            elif formatter.endswith(AbstractFormatValidator.CUSTOM_DATE_FORMATTER_SUFFIX):
                formatter = formatter[
                    :-len(AbstractFormatValidator.CUSTOM_DATE_FORMATTER_SUFFIX)
                ]
                parsedValue = self.construct_datetime(formatter, value, tz)
            else:
                decimalPoint = locale.localeconv()['decimal_point']
                thousandsSep = locale.localeconv()['thousands_sep']
                if not thousandsSep:
                    if decimalPoint == ",":
                        thousandsSep = "."
                    elif decimalPoint == ".":
                        thousandsSep = ","
                locale.setlocale(locale.LC_ALL, "")
                return Decimal(value.replace(thousandsSep, ""))
            pos = len(value)
        except ((ValueError, InvalidOperation)) as e:
            locale.setlocale(locale.LC_ALL, "")
            return None

        if self.isStrict() and pos < len(value):
            locale.setlocale(locale.LC_ALL, "")
            return None

        if parsedValue is not None:
            parsedValue = self._processParsedValue(parsedValue, formatter)

        locale.setlocale(locale.LC_ALL, "")
        return parsedValue

    def indian_format(self, number: Decimal):
        number_str = "{:.2f}".format(number)
        
        integer_part, decimal_part = number_str.split('.')
        
        reversed_integer = integer_part[::-1]
        
        grouped = re.sub(r'(\d{2})(?=\d)', r'\1,', reversed_integer, count=1)
        grouped = re.sub(r'(\d{2})(?=\d)', r'\1,', grouped)
        
        formatted_integer = grouped[::-1]
        
        return f"{formatted_integer}.{decimal_part}"
    
    def format_decimal(self, value: Decimal, format_string: str) -> str:
        if format_string == "#,#0.00":
            return self.indian_format(value)
        float_value = float(value)
        formatted_value = f"{float_value:,.2f}"
        if ',' in format_string:
            thousands_sep = format_string.split(',')[1]
            formatted_value = formatted_value.replace(',', thousands_sep)
        if '.' in format_string:
            decimal_places = format_string.split('.')[1]
            formatted_value = f"{float_value:,.{len(decimal_places)}f}"
        return formatted_value

    
    def _format4(self, value: typing.Any, formatter: typing.Any, pattern: str) -> str:
        if formatter == "{:,.0f}":   # Java `setParseIntegerOnly()` only influences `parse()`
            formatter = "{:,}"
            if pattern:
                formatter = pattern + AbstractFormatValidator.CUSTOM_NUMBER_FORMATTER_SUFFIX
        if formatter.endswith(AbstractFormatValidator.CUSTOM_NUMBER_FORMATTER_SUFFIX):
            formatter = formatter[
                :-len(AbstractFormatValidator.CUSTOM_NUMBER_FORMATTER_SUFFIX)
            ]
            result = self.format_decimal(value, formatter)
        else:
            result = formatter.format(value)
        decimalPoint = locale.localeconv()['decimal_point']
        thousandsSep = locale.localeconv()['thousands_sep']
        if not thousandsSep:
            if decimalPoint == ",":
                thousandsSep = "."
            elif decimalPoint == ".":
                thousandsSep = ","
        if thousandsSep == ".":
            result = result.replace(decimalPoint, "__temp__")\
                .replace(thousandsSep, decimalPoint)\
                .replace("__temp__", thousandsSep)
        locale.setlocale(locale.LC_ALL, "")
        return result

    def format3(self, value: typing.Any, pattern: str, locale: typing.Any) -> str:
        formatter = self._getFormat(pattern, locale)
        return self._format4(value, formatter, pattern)

    def _format2(self, value: typing.Any, locale: typing.Any) -> str:
        return self.format3(value, None, locale)

    def _format1(self, value: typing.Any, pattern: str) -> str:
        return self.format3(value, pattern, None)

    def _format0(self, value: typing.Any) -> str:
        return self.format3(value, None, None)

    def isValid2(self, value: str, locale: typing.Any) -> bool:
        return self.isValid3(value, None, locale)

    def isValid1(self, value: str, pattern: str) -> bool:
        if pattern:
            pattern = pattern.replace("\u00A4","")
        return self.isValid3(value, pattern, None)

    def isValid0(self, value: str) -> bool:
        return self.isValid3(value, None, None)

    def isStrict(self) -> bool:
        return self.__strict

    def __init__(self, strict: bool) -> None:
        self.__strict = strict

    def _getFormat(self, pattern: str, locale: typing.Any) -> typing.Any:
        pass

    def _processParsedValue(self, value: typing.Any, formatter: typing.Any) -> typing.Any:
        pass

    def isValid3(self, value: str, pattern: str, locale: typing.Any) -> bool:
        pass
