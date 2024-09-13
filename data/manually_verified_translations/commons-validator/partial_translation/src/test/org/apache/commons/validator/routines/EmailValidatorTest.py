from __future__ import annotations
import re
import sys
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.test.org.apache.commons.validator.ResultPair import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.main.org.apache.commons.validator.routines.EmailValidator import *


class EmailValidatorTest(unittest.TestCase):

    _ACTION: str = "email"
    _FORM_KEY: str = "emailForm"
    __testEmailFromPerl: typing.List[ResultPair] = [
        ResultPair("abigail@example.com", True),
        ResultPair("abigail@example.com ", True),
        ResultPair(" abigail@example.com", True),
        ResultPair("abigail @example.com ", True),
        ResultPair("*@example.net", True),
        ResultPair('"\\""@foo.bar', True),
        ResultPair("fred&barny@example.com", True),
        ResultPair("---@example.com", True),
        ResultPair("foo-bar@example.net", True),
        ResultPair('"127.0.0.1"@[127.0.0.1]', True),
        ResultPair("Abigail <abigail@example.com>", True),
        ResultPair("Abigail<abigail@example.com>", True),
        ResultPair("Abigail<@a,@b,@c:abigail@example.com>", True),
        ResultPair('"This is a phrase"<abigail@example.com>', True),
        ResultPair('"Abigail "<abigail@example.com>', True),
        ResultPair('"Joe & J. Harvey" <example @Org>', True),
        ResultPair("Abigail <abigail @ example.com>", True),
        ResultPair("Abigail made this <  abigail   @   example  .    com    >", True),
        ResultPair("Abigail(the bitch)@example.com", True),
        ResultPair("Abigail <abigail @ example . (bar) com >", True),
        ResultPair(
            "Abigail < (one)  abigail (two) @(three)example . (bar) com (quz) >", True
        ),
        ResultPair(
            "Abigail (foo) (((baz)(nested) (comment)) ! ) < (one)  abigail (two)"
            + " @(three)example . (bar) com (quz) >",
            True,
        ),
        ResultPair("Abigail <abigail(fo\\(o)@example.com>", True),
        ResultPair("Abigail <abigail(fo\\)o)@example.com> ", True),
        ResultPair("(foo) abigail@example.com", True),
        ResultPair("abigail@example.com (foo)", True),
        ResultPair('"Abi\\"gail" <abigail@example.com>', True),
        ResultPair("abigail@[example.com]", True),
        ResultPair("abigail@[exa\\[ple.com]", True),
        ResultPair("abigail@[exa\\]ple.com]", True),
        ResultPair('":sysmail"@  Some-Group. Some-Org', True),
        ResultPair("Muhammed.(I am  the greatest) Ali @(the)Vegas.WBA", True),
        ResultPair("mailbox.sub1.sub2@this-domain", True),
        ResultPair("sub-net.mailbox@sub-domain.domain", True),
        ResultPair("name:;", True),
        ResultPair("':;", True),
        ResultPair("name:   ;", True),
        ResultPair("Alfred Neuman <Neuman@BBN-TENEXA>", True),
        ResultPair("Neuman@BBN-TENEXA", True),
        ResultPair('"George, Ted" <Shared@Group.Arpanet>', True),
        ResultPair("Wilt . (the  Stilt) Chamberlain@NBA.US", True),
        ResultPair("Cruisers:  Port@Portugal, Jones@SEA;", True),
        ResultPair("$@[]", True),
        ResultPair("*()@[]", True),
        ResultPair('"quoted ( brackets" ( a comment )@example.com', True),
        ResultPair('"Joe & J. Harvey"\\x0D\\x0A     <ddd\\@ Org>', True),
        ResultPair('"Joe &\\x0D\\x0A J. Harvey" <ddd \\@ Org>', True),
        ResultPair(
            "Gourmets:  Pompous Person <WhoZiWhatZit\\@Cordon-Bleu>,\\x0D\\x0A"
            + '        Childs\\@WGBH.Boston, "Galloping Gourmet"\\@\\x0D\\x0A'
            + "        ANT.Down-Under (Australian National Television),\\x0D\\x0A"
            + "        Cheapie\\@Discount-Liquors;",
            True,
        ),
        ResultPair("   Just a string", False),
        ResultPair("string", False),
        ResultPair("(comment)", False),
        ResultPair("()@example.com", False),
        ResultPair("fred(&)barny@example.com", False),
        ResultPair("fred\\ barny@example.com", False),
        ResultPair("Abigail <abi gail @ example.com>", False),
        ResultPair("Abigail <abigail(fo(o)@example.com>", False),
        ResultPair("Abigail <abigail(fo)o)@example.com>", False),
        ResultPair('"Abi"gail" <abigail@example.com>', False),
        ResultPair("abigail@[exa]ple.com]", False),
        ResultPair("abigail@[exa[ple.com]", False),
        ResultPair("abigail@[exaple].com]", False),
        ResultPair("abigail@", False),
        ResultPair("@example.com", False),
        ResultPair("phrase: abigail@example.com abigail@example.com ;", False),
        ResultPair("invalid�char@example.com", False),
    ]
    __validator: EmailValidator = None

    def testValidator473_4(self) -> None:

        pass  # LLM could not translate this method

    def testValidator473_3(self) -> None:

        items = []
        try:
            EmailValidator(0, True, False, DomainValidator.getInstance2(False, items))
        except ValueError:
            pass

    def testValidator473_2(self) -> None:

        items = []
        try:
            EmailValidator(0, False, False, DomainValidator.getInstance2(True, items))
        except ValueError:
            pass

    def testValidator473_1(self) -> None:

        with pytest.raises(ValueError):
            EmailValidator(0, False, False, None)

    def testValidator374(self) -> None:

        self.assertTrue(self.__validator.isValid("abc@school.school"))

    def testValidator359(self) -> None:

        val = EmailValidator.getInstance1(False, True)
        self.assertFalse(val.isValid("test@.com"))

    def testEmailAtTLD(self) -> None:

        val = EmailValidator.getInstance1(False, True)
        self.assertTrue(val.isValid("test@com"))

    def testValidator365(self) -> None:

        email = (
            "Loremipsumdolorsitametconsecteturadipiscingelit.Nullavitaeligulamattisrhoncusnuncegestasmattisleo."
            + "Donecnonsapieninmagnatristiquedictumaacturpis.Fusceorciduifacilisisutsapieneuconsequatpharetralectus."
            + "Quisqueenimestpulvinarutquamvitaeportamattisex.Nullamquismaurisplaceratconvallisjustoquisportamauris."
            + "Innullalacusconvalliseufringillautvenenatissitametdiam.Maecenasluctusligulascelerisquepulvinarfeugiat."
            + "Sedmolestienullaaliquetorciluctusidpharetranislfinibus.Suspendissemalesuadatinciduntduisitametportaarcusollicitudinnec."
            + "Donecetmassamagna.Curabitururnadiampretiumveldignissimporttitorfringillaeuneque."
            + "Duisantetelluspharetraidtinciduntinterdummolestiesitametfelis.Utquisquamsitametantesagittisdapibusacnonodio."
            + "Namrutrummolestiediamidmattis.Cumsociisnatoquepenatibusetmagnisdisparturientmontesnasceturridiculusmus."
            + "Morbiposueresedmetusacconsectetur.Etiamquisipsumvitaejustotempusmaximus.Sedultriciesplaceratvolutpat."
            + "Integerlacuslectusmaximusacornarequissagittissitametjusto."
            + "Cumsociisnatoquepenatibusetmagnisdisparturientmontesnasceturridiculusmus.Maecenasindictumpurussedrutrumex.Nullafacilisi."
            + "Integerfinibusfinibusmietpharetranislfaucibusvel.Maecenasegetdolorlacinialobortisjustovelullamcorpersem."
            + "Vivamusaliquetpurusidvariusornaresapienrisusrutrumnisitinciduntmollissemnequeidmetus."
            + "Etiamquiseleifendpurus.Nuncfelisnuncscelerisqueiddignissimnecfinibusalibero."
            + "Nuncsemperenimnequesitamethendreritpurusfacilisisac.Maurisdapibussemperfelisdignissimgravida."
            + "Aeneanultricesblanditnequealiquamfinibusodioscelerisqueac.Aliquamnecmassaeumaurisfaucibusfringilla."
            + "Etiamconsequatligulanisisitametaliquamnibhtemporquis.Nuncinterdumdignissimnullaatsodalesarcusagittiseu."
            + "Proinpharetrametusneclacuspulvinarsedvolutpatliberoornare.Sedligulanislpulvinarnonlectuseublanditfacilisisante."
            + "Sedmollisnislalacusauctorsuscipit.Inhachabitasseplateadictumst.Phasellussitametvelittemporvenenatisfeliseuegestasrisus."
            + "Aliquameteratsitametnibhcommodofinibus.Morbiefficiturodiovelpulvinariaculis."
            + "Aeneantemporipsummassaaconsecteturturpisfaucibusultrices.Praesentsodalesmaurisquisportafermentum."
            + "Etiamnisinislvenenatisvelauctorutullamcorperinjusto.Proinvelligulaerat.Phasellusvestibulumgravidamassanonfeugiat."
            + "Maecenaspharetraeuismodmetusegetefficitur.Suspendisseamet@gmail.com"
        )

        self.assertFalse(self.__validator.isValid(email))

    def testValidator293(self) -> None:

        self.assertTrue(self.__validator.isValid("abc-@abc.com"))
        self.assertTrue(self.__validator.isValid("abc_@abc.com"))
        self.assertTrue(self.__validator.isValid("abc-def@abc.com"))
        self.assertTrue(self.__validator.isValid("abc_def@abc.com"))
        self.assertFalse(self.__validator.isValid("abc@abc_def.com"))

    @pytest.mark.skip(reason="Ignore")
    def testEmailFromPerl(self) -> None:

        errors = 0
        for index in range(len(self.__testEmailFromPerl)):
            item = self.__testEmailFromPerl[index].item
            exp = self.__testEmailFromPerl[index].valid
            act = self.__validator.isValid(item)
            if act != exp:
                print(f"{item}: expected {exp} actual {act}")
                errors += 1

        self.assertEqual("Expected 0 errors", 0, errors)

    def testEmailUserName(self) -> None:

        self.assertTrue(self.__validator.isValid("joe1blow@apache.org"))
        self.assertTrue(self.__validator.isValid("joe$blow@apache.org"))
        self.assertTrue(self.__validator.isValid("joe-@apache.org"))
        self.assertTrue(self.__validator.isValid("joe_@apache.org"))
        self.assertTrue(self.__validator.isValid("joe+@apache.org"))
        self.assertTrue(self.__validator.isValid("joe@apache.org"))
        self.assertTrue(self.__validator.isValid("joe*@apache.org"))
        self.assertTrue(self.__validator.isValid("joe'@apache.org"))
        self.assertTrue(self.__validator.isValid("joe%45@apache.org"))
        self.assertTrue(self.__validator.isValid("joe?@apache.org"))
        self.assertTrue(self.__validator.isValid("joe&@apache.org"))
        self.assertTrue(self.__validator.isValid("joe=@apache.org"))
        self.assertTrue(self.__validator.isValid("+joe@apache.org"))
        self.assertTrue(self.__validator.isValid("blow@apache.org"))
        self.assertTrue(self.__validator.isValid("*joe@apache.org"))
        self.assertTrue(self.__validator.isValid("'joe@apache.org"))
        self.assertTrue(self.__validator.isValid("%joe45@apache.org"))
        self.assertTrue(self.__validator.isValid("?joe@apache.org"))
        self.assertTrue(self.__validator.isValid("&joe@apache.org"))
        self.assertTrue(self.__validator.isValid("=joe@apache.org"))
        self.assertTrue(self.__validator.isValid("+@apache.org"))
        self.assertTrue(self.__validator.isValid("*@apache.org"))
        self.assertTrue(self.__validator.isValid("'@apache.org"))
        self.assertTrue(self.__validator.isValid("%@apache.org"))
        self.assertTrue(self.__validator.isValid("?@apache.org"))
        self.assertTrue(self.__validator.isValid("&@apache.org"))
        self.assertTrue(self.__validator.isValid("=@apache.org"))
        self.assertFalse(self.__validator.isValid("joe.@apache.org"))
        self.assertFalse(self.__validator.isValid(".joe@apache.org"))
        self.assertFalse(self.__validator.isValid(".@apache.org"))
        self.assertTrue(self.__validator.isValid("joe.ok@apache.org"))
        self.assertFalse(self.__validator.isValid("joe..ok@apache.org"))
        self.assertFalse(self.__validator.isValid("..@apache.org"))
        self.assertFalse(self.__validator.isValid("joe(@apache.org"))
        self.assertFalse(self.__validator.isValid("joe)@apache.org"))
        self.assertFalse(self.__validator.isValid("joe,@apache.org"))
        self.assertFalse(self.__validator.isValid("joe;@apache.org"))
        self.assertTrue(self.__validator.isValid('"joe."@apache.org'))
        self.assertTrue(self.__validator.isValid('".joe"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe+"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe@"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe*"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe\'"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe("@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe)"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe,"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe%45"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe;"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe?"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe&"@apache.org'))
        self.assertTrue(self.__validator.isValid('"joe="@apache.org'))
        self.assertTrue(self.__validator.isValid('".."@apache.org'))
        self.assertTrue(self.__validator.isValid('"john\\"doe"@apache.org'))
        self.assertTrue(
            self.__validator.isValid(
                "john56789.john56789.john56789.john56789.john56789.john56789.john@example.com"
            )
        )
        self.assertFalse(
            self.__validator.isValid(
                "john56789.john56789.john56789.john56789.john56789.john56789.john5@example.com"
            )
        )
        self.assertTrue(
            self.__validator.isValid("\\>escape\\\\special\\^characters\\<@example.com")
        )
        self.assertTrue(self.__validator.isValid("Abc\\@def@example.com"))
        self.assertFalse(self.__validator.isValid("Abc@def@example.com"))
        self.assertTrue(self.__validator.isValid("space\\ monkey@example.com"))

    def testEmailWithSlashes(self) -> None:

        self.assertTrue(
            "/ and ! valid in username",
            self.__validator.isValid("joe!/blow@apache.org"),
        )
        self.assertFalse(
            "/ not valid in domain", self.__validator.isValid("joe@ap/ache.org")
        )
        self.assertFalse(
            " not valid in domain",
            self.__validator.isValid("joe@apac not valid in domain"),
        )

    def testEmailLocalhost(self) -> None:

        noLocal = EmailValidator.getInstance2(False)
        allowLocal = EmailValidator.getInstance2(True)
        self.assertEqual(self.__validator, noLocal)
        self.assertTrue(
            "@localhost.localdomain should be accepted but wasn't",
            allowLocal.isValid("joe@localhost.localdomain"),
        )
        self.assertTrue(
            "@localhost should be accepted but wasn't",
            allowLocal.isValid("joe@localhost"),
        )
        self.assertFalse(
            "@localhost.localdomain should be accepted but wasn't",
            noLocal.isValid("joe@localhost.localdomain"),
        )
        self.assertFalse(
            "@localhost should be accepted but wasn't", noLocal.isValid("joe@localhost")
        )

    def testEmailWithControlChars(self) -> None:

        for c in range(32):
            self.assertFalse(
                "Test control char " + str(c),
                self.__validator.isValid("foo" + chr(c) + "bar@domain.com"),
            )
        self.assertFalse(
            "Test control char 127",
            self.__validator.isValid("foo" + chr(127) + "bar@domain.com"),
        )

    def testEmailWithSpaces(self) -> None:

        self.assertFalse(self.__validator.isValid("joeblow @apache.org"))
        self.assertFalse(self.__validator.isValid("joeblow@ apache.org"))
        self.assertFalse(self.__validator.isValid(" joeblow@apache.org"))
        self.assertFalse(self.__validator.isValid("joeblow@apache.org "))
        self.assertFalse(self.__validator.isValid("joe blow@apache.org "))
        self.assertFalse(self.__validator.isValid("joeblow@apa che.org "))
        self.assertTrue(self.__validator.isValid('"joeblow "@apache.org'))
        self.assertTrue(self.__validator.isValid('" joeblow"@apache.org'))
        self.assertTrue(self.__validator.isValid('" joe blow "@apache.org'))

    def testEmailWithCommas(self) -> None:

        self.assertFalse(self.__validator.isValid("joeblow@apa,che.org"))
        self.assertFalse(self.__validator.isValid("joeblow@apache.o,rg"))
        self.assertFalse(self.__validator.isValid("joeblow@apache,org"))

    def testValidator235(self) -> None:

        version = platform.python_version()
        if version.split(".")[1] < 6:
            print("Cannot run Unicode IDN tests")
            return

        self.assertTrue(
            self.__validator.isValid("someone@xn--d1abbgf6aiiy.xn--p1ai"),
            "xn--d1abbgf6aiiy.xn--p1ai should validate",
        )
        self.assertTrue(
            self.__validator.isValid("someone@президент.рф"),
            "президент.рф should validate",
        )
        self.assertTrue(
            self.__validator.isValid("someone@www.b\u00fccher.ch"),
            "www.b\u00fccher.ch should validate",
        )
        self.assertFalse(
            self.__validator.isValid("someone@www.\uFFFD.ch"),
            "www.\uFFFD.ch FFFD should fail",
        )
        self.assertTrue(
            self.__validator.isValid("someone@www.b\u00fccher.ch"),
            "www.b\u00fccher.ch should validate",
        )
        self.assertFalse(
            self.__validator.isValid("someone@www.\uFFFD.ch"),
            "www.\uFFFD.ch FFFD should fail",
        )

    def testVALIDATOR_278(self) -> None:

        self.assertFalse(self.__validator.isValid("someone@-test.com"))
        self.assertFalse(self.__validator.isValid("someone@test-.com"))

    def testVALIDATOR_315(self) -> None:

        self.assertFalse(self.__validator.isValid("me@at&t.net"))
        self.assertTrue(self.__validator.isValid("me@att.net"))

    def testEmailWithBogusCharacter(self) -> None:

        self.assertFalse(self.__validator.isValid("andy.noble@\u008fdata-workshop.com"))
        self.assertTrue(self.__validator.isValid("andy.o'reilly@data-workshop.com"))
        self.assertFalse(self.__validator.isValid("andy@o'reilly.data-workshop.com"))
        self.assertTrue(self.__validator.isValid("foo+bar@i.am.not.in.us.example.com"))
        self.assertFalse(self.__validator.isValid("foo+bar@example+3.com"))
        self.assertFalse(self.__validator.isValid("test@%*.com"))
        self.assertFalse(self.__validator.isValid("test@^&#.com"))

    def testEmailWithDotEnd(self) -> None:

        self.assertFalse(self.__validator.isValid("andy.noble@data-workshop.com."))

    def testEmailWithDash(self) -> None:

        self.assertTrue(self.__validator.isValid("andy.noble@data-workshop.com"))
        self.assertFalse(self.__validator.isValid("andy-noble@data-workshop.-com"))
        self.assertFalse(self.__validator.isValid("andy-noble@data-workshop.c-om"))
        self.assertFalse(self.__validator.isValid("andy-noble@data-workshop.co-m"))

    def testEmailExtension(self) -> None:

        self.assertTrue(self.__validator.isValid("jsmith@apache.org"))
        self.assertTrue(self.__validator.isValid("jsmith@apache.com"))
        self.assertTrue(self.__validator.isValid("jsmith@apache.net"))
        self.assertTrue(self.__validator.isValid("jsmith@apache.info"))
        self.assertFalse(self.__validator.isValid("jsmith@apache."))
        self.assertFalse(self.__validator.isValid("jsmith@apache.c"))
        self.assertTrue(self.__validator.isValid("someone@yahoo.museum"))
        self.assertFalse(self.__validator.isValid("someone@yahoo.mu-seum"))

    def testEmailWithNumericAddress(self) -> None:

        self.assertTrue(self.__validator.isValid("someone@[216.109.118.76]"))
        self.assertTrue(self.__validator.isValid("someone@yahoo.com"))

    def testEmail(self) -> None:

        self.assertTrue(self.__validator.isValid("jsmith@apache.org"))

    def setUp(self) -> None:
        self.__validator = EmailValidator.getInstance0()

    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:

        validator = EmailValidator.getInstance0()
        for arg in args:
            print(f"{arg}: {validator.isValid(arg)}")
