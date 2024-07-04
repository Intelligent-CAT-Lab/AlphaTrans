from __future__ import annotations
import re
from abc import ABC
import unittest
import pytest
import io


class Base64TestData:

    ENCODED_76_CHARS_PER_LINE: str = (
        "9IPNKwUvdLiIAp6ctz12SiQmOGstWyYvSPeevufDhrzaws65voykKjbIj33YWTa9xA7c/FHypWcl\n"
        + "rZhQ7onfc3JE93BJ5fT4R9zAEdjbjy1hv4ZYNnET4WJeXMLJ/5p+qBpTsPpepW8DNVYy1c02/1wy\n"
        + "C+kgA6CvRUd9cSr/lt88AEdsTV4GMCn1+EwuAiYdivxuzn+cLM8q2jewqlI52tP9J7Cs8vqG71s6\n"
        + "+WAELKvm/UovvyaOi+OdMUfjQ0JLiLkHu6p9OwUgvQqiDKzEv/Augo0dTPZzYGEyCP5GVrle3QQd\n"
        + "gciIHnpdd4VUTPGRUbXeKbh++U3fbJIng/sQXM3IYByMZ7xt9HWS1LUcRdQ7Prwn/IlQWxOMeq+K\n"
        + "ZJSoAviWtdserXyHbIEa//hmr4p/j80k0g9q35hq1ayGM9984ALTSaZ8WeyFbZx1CxC/Qoqf92UH\n"
        + "/ylBRnSJNn4sS0oa3uUbNvOnpkB4D9V7Ut9atinCJrw+wiJcMl+9kp251IUxBGA4cUxh0eaxk3OD\n"
        + "WnwI95EktmWOKwCSP0xjWwIMxDjygwAG5R8fk9H9bVi1thMavm4nDc4vaNoSE1RnZNYwbiUVlVPM\n"
        + "9EclvJWTWd6igWeA0MxHAA8iOM5Vnmqp/WGM7UDq59rBIdNQCoeTJaAkEtAuLL5zogOa5e+MzVjv\n"
        + "B5MYQlOlaaTtQrRApXa5Z4VfEanu9UK2fi1T8jJPFC2PmXebxp0bnO+VW+bgyEdIIkIQCaZq1MKWC3\n"
        + "KuiOS9BJ1t7O0A2JKJKvoE4UNulzV2TGCC+KAnmjRqQBqXlJmgjHQAoHNZKOma/uIQOsvfDnqicYdD\n"
        + "mfyCYuV89HjA1H8tiDJ85VfsrFHdcbPAoNCpi65awJSHfdPO1NDONOK++S7Y0VXUgoYYrBV4Y7YbC8\n"
        + "wg/nqcimr3lm3tRyp+QsgKzdREbfNRk0F5PLyLfsUElepjs1QdV3fEV1LJtiywA3ubVNQJRxhbYxa/\n"
        + "C/Xy2qxpm6vvdL92l3q1ccev35IcaOiSx7Im+/GxV2lVKdaOvYVGDD1zBRe6Y2CwQb9p088l3/93q\n"
        + "GR5593NCiuPPWcsDWwUShM1EyW0FNX1F8bnzHnYijoyE/jf4s/l9bBd7yJdRWRCyih2WcypAiOIEkBs\n"
        + "H+dCTgalu8sRDoMh4ZIBBdgHfoZUycLqReQFLZZ4Sl4zSmzt5vQxQFhEKb9+ff/4rb1KAo6wifengxVf\n"
        + "Isa2b5ljXzAqXs7JkPvmC6fa7X4ZZndRokaxYlu3cg8OV+uG/6YAHZilo8at0OpkkNdNFuhwuGlkBqrZ\n"
        + "KNUj/gSiYYc06gF/r/z6iWAjpXJRW1qq3CLZXdZFZ/VrqXeVjtOAu2A=\n"
    )
    ENCODED_64_CHARS_PER_LINE: str = (
        "9IPNKwUvdLiIAp6ctz12SiQmOGstWyYvSPeevufDhrzaws65voykKjbIj33YWTa9\n"
        + "xA7c/FHypWclrZhQ7onfc3JE93BJ5fT4R9zAEdjbjy1hv4ZYNnET4WJeXMLJ/5p+qBpTsPpepW8D\n"
        + "NVYy1c02/1wyC+kgA6CvRUd9cSr/lt88AEdsTV4GMCn1+EwuAiYdivxuzn+cLM8q2jewqlI52tP9J7\n"
        + "Cs8vqG71s6+WAELKvm/UovvyaOi+OdMUfjQ0JLiLkHu6p9OwUgvQqiDKzEv/Augo0dTPZzYGEyCP5\n"
        + "GVrle3QQdgciIHnpdd4VUTPGRUbXeKbh++U3fbJIng/sQXM3IYByMZ7xt9HWS1LUcRdQ7Prwn/IlQW\n"
        + "xOMeq+KZJSoAviWtdserXyHbIEa//hmr4p/j80k0g9q35hq1ayGM9984ALTSaZ8WeyFbZx1CxC/Qoqf9\n"
        + "2UH/ylBRnSJNn4sS0oa3uUbNvOnpkB4D9V7Ut9atinCJrw+wiJcMl+9kp251IUxBGA4cUxh0eaxk3OD\n"
        + "WnwI95EktmWOKwCSP0xjWwIMxDjygwAG5R8fk9H9bVi1thMavm4nDc4vaNoSE1RnZNYwbiUVlVPM9Ecl\n"
        + "vJWTWd6igWeA0MxHAA8iOM5Vnmqp/WGM7UDq59rBIdNQCoeTJaAkEtAuLL5zogOa5e+MzVjvB5MYQlO\n"
        + "laaTtQrRApXa5Z4VfEanu9UK2fi1T8jJPFC2PmXebxp0bnO+VW+bgyEdIIkIQCaZq1MKWC3KuiOS9BJ1\n"
        + "t7O0A2JKJKvoE4UNulzV2TGCC+KAnmjRqQBqXlJmgjHQAoHNZKOma/uIQOsvfDnqicYdDmfyCYuV89HjA\n"
        + "1H8tiDJ85VfsrFHdcbPAoNCpi65awJSHfdPO1NDONOK++S7Y0VXUgoYYrBV4Y7YbC8wg/nqcimr3lm3tR\n"
        + "yp+QsgKzdREbfNRk0F5PLyLfsUElepjs1QdV3fEV1LJtiywA3ubVNQJRxhbYxa/C/Xy2qxpm6vvdL92l3\n"
        + "q1ccev35IcaOiSx7Im+/GxV2lVKdaOvYVGDD1zBRe6Y2CwQb9p088l3/93qGR5593NCiuPPWcsDWwUShM1\n"
        + "EyW0FNX1F8bnzHnYijoyE/jf4s/l9bBd7yJdRWRCyih2WcypAiOIEkBsH+dCTgalu8sRDoMh4ZIBBdgHfo\n"
        + "ZUycLqReQFLZZ4Sl4zSmzt5vQxQFhEKb9+ff/4rb1KAo6wifengxVfIsa2b5ljXzAqXs7JkPvmC6fa7X4ZZ\n"
        + "ndRokaxYlu3cg8OV+uG/6YAHZilo8at0OpkkNdNFuhwuGlkBqrZKNUj/gSiYYc06gF/r/z6iWAjpXJRW1qq\n"
        + "3CLZXdZFZ/VrqXeVjtOAu2A=\n"
    )
    CODEC_98_NPE_DECODED: str = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123"
    )
    CODEC_98_NPE: str = (
        "YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM="
    )
    CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3: str = "124"
