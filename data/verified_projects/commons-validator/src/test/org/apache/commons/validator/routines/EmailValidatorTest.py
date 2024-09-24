import pytest

import unittest
from src.main.org.apache.commons.validator.routines.EmailValidator import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.test.org.apache.commons.validator.ResultPair import ResultPair
import sys

class EmailValidatorTest(unittest.TestCase):

    _FORM_KEY = "emailForm"
    _ACTION = "email"

    __testEmailFromPerl = [
        ResultPair("abigail@example.com", True),
        ResultPair("abigail@example.com ", True),
        ResultPair(" abigail@example.com", True),
        ResultPair("abigail @example.com ", True),
        ResultPair("*@example.net", True),
        ResultPair("\"\\\"\"@foo.bar", True),
        ResultPair("fred&barny@example.com", True),
        ResultPair("---@example.com", True),
        ResultPair("foo-bar@example.net", True),
        ResultPair("\"127.0.0.1\"@[127.0.0.1]", True),
        ResultPair("Abigail <abigail@example.com>", True),
        ResultPair("Abigail<abigail@example.com>", True),
        ResultPair("Abigail<@a,@b,@c:abigail@example.com>", True),
        ResultPair("\"This is a phrase\"<abigail@example.com>", True),
        ResultPair("\"Abigail \"<abigail@example.com>", True),
        ResultPair("\"Joe & J. Harvey\" <example @Org>", True),
        ResultPair("Abigail <abigail @ example.com>", True),
        ResultPair("Abigail made this <  abigail   @   example  .    com    >", True),
        ResultPair("Abigail(the bitch)@example.com", True),
        ResultPair("Abigail <abigail @ example . (bar) com >", True),
        ResultPair(
            "Abigail < (one)  abigail (two) @(three)example . (bar) com (quz) >",
            True
        ),
        ResultPair(
            "Abigail (foo) (((baz)(nested) (comment)) ! ) < (one)  abigail (two)" +\
                " @(three)example . (bar) com (quz) >",
            True
        ),
        ResultPair("Abigail <abigail(fo\\(o)@example.com>", True),
        ResultPair("Abigail <abigail(fo\\)o)@example.com> ", True),
        ResultPair("(foo) abigail@example.com", True),
        ResultPair("abigail@example.com (foo)", True),
        ResultPair("\"Abi\\\"gail\" <abigail@example.com>", True),
        ResultPair("abigail@[example.com]", True),
        ResultPair("abigail@[exa\\[ple.com]", True),
        ResultPair("abigail@[exa\\]ple.com]", True),
        ResultPair("\":sysmail\"@  Some-Group. Some-Org", True),
        ResultPair("Muhammed.(I am  the greatest) Ali @(the)Vegas.WBA", True),
        ResultPair("mailbox.sub1.sub2@this-domain", True),
        ResultPair("sub-net.mailbox@sub-domain.domain", True),
        ResultPair("name:;", True),
        ResultPair("':;", True),
        ResultPair("name:   ;", True),
        ResultPair("Alfred Neuman <Neuman@BBN-TENEXA>", True),
        ResultPair("Neuman@BBN-TENEXA", True),
        ResultPair("\"George, Ted\" <Shared@Group.Arpanet>", True),
        ResultPair("Wilt . (the  Stilt) Chamberlain@NBA.US", True),
        ResultPair("Cruisers:  Port@Portugal, Jones@SEA;", True),
        ResultPair("$@[]", True),
        ResultPair("*()@[]", True),
        ResultPair("\"quoted ( brackets\" ( a comment )@example.com", True),
        ResultPair("\"Joe & J. Harvey\"\\x0D\\x0A     <ddd\\@ Org>", True),
        ResultPair("\"Joe &\\x0D\\x0A J. Harvey\" <ddd \\@ Org>", True),
        ResultPair(
            "Gourmets:  Pompous Person <WhoZiWhatZit\\@Cordon-Bleu>,\\x0D\\x0A" +\
                "        Childs\\@WGBH.Boston, \"Galloping Gourmet\"\\@\\x0D\\x0A" +\
                "        ANT.Down-Under (Australian National Television),\\x0D\\x0A" + \
                "        Cheapie\\@Discount-Liquors;",
            True
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
        ResultPair("\"Abi\"gail\" <abigail@example.com>", False),
        ResultPair("abigail@[exa]ple.com]", False),
        ResultPair("abigail@[exa[ple.com]", False),
        ResultPair("abigail@[exaple].com]", False),
        ResultPair("abigail@", False),
        ResultPair("@example.com", False),
        ResultPair("phrase: abigail@example.com abigail@example.com ;", False),
        ResultPair("invalid�char@example.com", False)
    ]

    __validator = None

    
    def setUp(self) -> None:
        self.__validator = EmailValidator.getInstance0()
        self.__validator._EmailValidator__domainValidator.mygenericTLDsPlus = []
        self.__validator._EmailValidator__domainValidator.mylocalLDsPlus = []
        DomainValidator._DomainValidator__genericTLDsPlus = []
        DomainValidator._DomainValidator__localTLDsPlus = []

    
    @pytest.mark.test
    def testEmail(self) -> None:
        self.assertTrue(self.__validator.isValid("jsmith@apache.org"))

    
    @pytest.mark.test
    def testEmailWithNumericAddress(self) -> None:
        self.assertTrue(self.__validator.isValid("someone@[216.109.118.76]"))
        self.assertTrue(self.__validator.isValid("someone@yahoo.com"))

    
    @pytest.mark.test
    def testEmailExtension(self) -> None:
        self.assertTrue(self.__validator.isValid("jsmith@apache.org"))

        self.assertTrue(self.__validator.isValid("jsmith@apache.com"))

        self.assertTrue(self.__validator.isValid("jsmith@apache.net"))

        self.assertTrue(self.__validator.isValid("jsmith@apache.info"))

        self.assertFalse(self.__validator.isValid("jsmith@apache."))

        self.assertFalse(self.__validator.isValid("jsmith@apache.c"))

        self.assertTrue(self.__validator.isValid("someone@yahoo.museum"))

        self.assertFalse(self.__validator.isValid("someone@yahoo.mu-seum"))

    
    @pytest.mark.test
    def testEmailWithDash(self) -> None:
        self.assertTrue(self.__validator.isValid("andy.noble@data-workshop.com"))

        self.assertFalse(self.__validator.isValid("andy-noble@data-workshop.-com"))

        self.assertFalse(self.__validator.isValid("andy-noble@data-workshop.c-om"))

        self.assertFalse(self.__validator.isValid("andy-noble@data-workshop.co-m"))

    
    @pytest.mark.test
    def testEmailWithDotEnd(self) -> None:
        self.assertFalse(self.__validator.isValid("andy.noble@data-workshop.com."))

    
    @pytest.mark.test
    def testEmailWithBogusCharacter(self) -> None:
        self.assertFalse(self.__validator.isValid("andy.noble@\u008fdata-workshop.com"))

        self.assertTrue(self.__validator.isValid("andy.o'reilly@data-workshop.com"))

        self.assertFalse(self.__validator.isValid("andy@o'reilly.data-workshop.com"))

        self.assertTrue(self.__validator.isValid("foo+bar@i.am.not.in.us.example.com"))

        self.assertFalse(self.__validator.isValid("foo+bar@example+3.com"))

        self.assertFalse(self.__validator.isValid("test@%*.com"))
        self.assertFalse(self.__validator.isValid("test@^&#.com"))

    
    @pytest.mark.test
    def testVALIDATOR_315(self) -> None:
        self.assertFalse(self.__validator.isValid("me@at&t.net"))
        self.assertTrue(self.__validator.isValid("me@att.net"))

    
    @pytest.mark.test
    def testVALIDATOR_278(self) -> None:
        self.assertFalse(self.__validator.isValid("someone@-test.com"))
        self.assertFalse(self.__validator.isValid("someone@test-.com"))

    
    @pytest.mark.test
    def testValidator235(self) -> None:
        version = sys.version_info
        if version < (2, 6): 
            #Python 2.6 is the latest version available at the birth of Java 1.6
            print("Cannot run Unicode IDN tests")
            return
        self.assertTrue(
            self.__validator.isValid("someone@xn--d1abbgf6aiiy.xn--p1ai"),
            "xn--d1abbgf6aiiy.xn--p1ai should validate"
        )
        self.assertTrue(
            self.__validator.isValid("someone@президент.рф"),
            "президент.рф should validate"
        )
        self.assertTrue(
            self.__validator.isValid("someone@www.bücher.ch"),
            "www.bücher.ch should validate"
        )
        self.assertFalse(
            self.__validator.isValid("someone@www.�.ch"),
            "www.�.ch FFFD should fail"
        )
        self.assertTrue(
            self.__validator.isValid("someone@www.bücher.ch"),
            "www.bücher.ch should validate"
        )
        self.assertFalse(
            self.__validator.isValid("someone@www.�.ch"),
            "www.�.ch FFFD should fail"
        )

    
    @pytest.mark.test
    def testEmailWithCommas(self) -> None:
        self.assertFalse(self.__validator.isValid("joeblow@apa,che.org"))

        self.assertFalse(self.__validator.isValid("joeblow@apache.o,rg"))

        self.assertFalse(self.__validator.isValid("joeblow@apache,org"))

    
    @pytest.mark.test
    def testEmailWithSpaces(self) -> None:
        self.assertFalse(self.__validator.isValid("joeblow @apache.org"))

        self.assertFalse(self.__validator.isValid("joeblow@ apache.org"))

        self.assertFalse(self.__validator.isValid(" joeblow@apache.org"))

        self.assertFalse(self.__validator.isValid("joeblow@apache.org "))

        self.assertFalse(self.__validator.isValid("joe blow@apache.org "))

        self.assertFalse(self.__validator.isValid("joeblow@apa che.org "))

        self.assertTrue(self.__validator.isValid("\"joeblow \"@apache.org"))

        self.assertTrue(self.__validator.isValid("\" joeblow\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\" joe blow \"@apache.org"))

    
    @pytest.mark.test
    def testEmailWithControlChars(self) -> None:
        for c in range(32):
            self.assertFalse(
                self.__validator.isValid(f"foo{chr(c)}bar@domain.com"),
                f"Test control char {c}"
            )
        self.assertFalse(
            self.__validator.isValid(f"foo{chr(127)}bar@domain.com"),
            "Test control char 127"
        )

    
    @pytest.mark.test
    def testEmailLocalhost(self) -> None:
        noLocal = EmailValidator.getInstance2(False)
        allowLocal = EmailValidator.getInstance2(True)
        self.assertEqual(self.__validator, noLocal)

        self.assertTrue(
            allowLocal.isValid("joe@localhost.localdomain"),
            "@localhost.localdomain should be accepted but wasn't"
        )
        self.assertTrue(
            allowLocal.isValid("joe@localhost"),
            "@localhost should be accepted but wasn't"
        )

        self.assertFalse(
            noLocal.isValid("joe@localhost.localdomain"),
            "@localhost.localdomain should not be accepted but was"
        )
        self.assertFalse(
            noLocal.isValid("joe@localhost"),
            "@localhost should not be accepted but was"
        )

    
    @pytest.mark.test
    def testEmailWithSlashes(self) -> None:
        self.assertTrue(
            self.__validator.isValid("joe!/blow@apache.org"),
            "/ and ! valid in username"
        )
        self.assertFalse(
            self.__validator.isValid("joe@ap/ache.org"),
            "/ not valid in domain"
        )
        self.assertFalse(
            self.__validator.isValid("joe@apac!he.org"),
            "! not valid in domain"
        )
    

    @pytest.mark.test
    def testEmailUserName(self) -> None:
        
        self.assertTrue(self.__validator.isValid("joe1blow@apache.org"))

        self.assertTrue(self.__validator.isValid("joe$blow@apache.org"))

        self.assertTrue(self.__validator.isValid("joe-@apache.org"))

        self.assertTrue(self.__validator.isValid("joe_@apache.org"))

        self.assertTrue(self.__validator.isValid("joe+@apache.org"))  # + is valid unquoted

        self.assertTrue(self.__validator.isValid("joe!@apache.org"))  # ! is valid unquoted

        self.assertTrue(self.__validator.isValid("joe*@apache.org"))  # * is valid unquoted

        self.assertTrue(self.__validator.isValid("joe'@apache.org"))  # ' is valid unquoted

        self.assertTrue(self.__validator.isValid("joe%45@apache.org"))  # % is valid unquoted

        self.assertTrue(self.__validator.isValid("joe?@apache.org"))  # ? is valid unquoted

        self.assertTrue(self.__validator.isValid("joe&@apache.org"))  # & ditto

        self.assertTrue(self.__validator.isValid("joe=@apache.org"))  # = ditto

        self.assertTrue(self.__validator.isValid("+joe@apache.org"))  # + is valid unquoted

        self.assertTrue(self.__validator.isValid("!joe@apache.org"))  # ! is valid unquoted

        self.assertTrue(self.__validator.isValid("*joe@apache.org"))  # * is valid unquoted

        self.assertTrue(self.__validator.isValid("'joe@apache.org"))  # ' is valid unquoted

        self.assertTrue(self.__validator.isValid("%joe45@apache.org"))  # % is valid unquoted

        self.assertTrue(self.__validator.isValid("?joe@apache.org"))  # ? is valid unquoted

        self.assertTrue(self.__validator.isValid("&joe@apache.org"))  # & ditto

        self.assertTrue(self.__validator.isValid("=joe@apache.org"))  # = ditto

        self.assertTrue(self.__validator.isValid("+@apache.org"))  # + is valid unquoted

        self.assertTrue(self.__validator.isValid("!@apache.org"))  # ! is valid unquoted

        self.assertTrue(self.__validator.isValid("*@apache.org"))  # * is valid unquoted

        self.assertTrue(self.__validator.isValid("'@apache.org"))  # ' is valid unquoted

        self.assertTrue(self.__validator.isValid("%@apache.org"))  # % is valid unquoted

        self.assertTrue(self.__validator.isValid("?@apache.org"))  # ? is valid unquoted

        self.assertTrue(self.__validator.isValid("&@apache.org"))  # & ditto

        self.assertTrue(self.__validator.isValid("=@apache.org"))  # = ditto

        self.assertFalse(
            self.__validator.isValid("joe.@apache.org")
        )  # . not allowed at end of local part

        self.assertFalse(
            self.__validator.isValid(".joe@apache.org")
        )  # . not allowed at start of local part

        self.assertFalse(self.__validator.isValid(".@apache.org"))  # . not allowed alone

        self.assertTrue(self.__validator.isValid("joe.ok@apache.org"))  # . allowed embedded

        self.assertFalse(
            self.__validator.isValid("joe..ok@apache.org")
        )  # .. not allowed embedded

        self.assertFalse(self.__validator.isValid("..@apache.org"))  # .. not allowed alone

        self.assertFalse(self.__validator.isValid("joe(@apache.org"))

        self.assertFalse(self.__validator.isValid("joe)@apache.org"))

        self.assertFalse(self.__validator.isValid("joe,@apache.org"))

        self.assertFalse(self.__validator.isValid("joe;@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe.\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\".joe\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe+\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe@\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe!\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe*\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe'\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe(\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe)\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe,\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe%45\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe;\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe?\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe&\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"joe=\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"..\"@apache.org"))

        self.assertTrue(self.__validator.isValid("\"john\\\"doe\"@apache.org"))

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
            self.__validator.isValid(
                "\\>escape\\\\special\\^characters\\<@example.com"
            )
        )

        self.assertTrue(self.__validator.isValid("Abc\\@def@example.com"))

        self.assertFalse(self.__validator.isValid("Abc@def@example.com"))

        self.assertTrue(self.__validator.isValid("space\\ monkey@example.com"))


    @unittest.skip("VALIDATOR-267")
    @pytest.mark.test
    def testEmailFromPerl(self) -> None:
        errors = 0
        for index in range(len(self.__testEmailFromPerl)):
            item = self.__testEmailFromPerl[index].item
            exp = self.__testEmailFromPerl[index].valid
            act = self.__validator.isValid(item)
            if not act == exp:
                print(f"{item.email}: expected {exp} actual {act}", file=sys.stderr)
                errors += 1
        
        self.assertEqual(0, errors, "Expected 0 errors")

    
    @pytest.mark.test
    def testValidator293(self) -> None:
        self.assertTrue(self.__validator.isValid("abc-@abc.com"))
        self.assertTrue(self.__validator.isValid("abc_@abc.com"))
        self.assertTrue(self.__validator.isValid("abc-def@abc.com"))
        self.assertTrue(self.__validator.isValid("abc_def@abc.com"))
        self.assertFalse(self.__validator.isValid("abc@abc_def.com"))

    
    @pytest.mark.test
    def testValidator365(self) -> None:
        self.assertFalse(
            self.__validator.isValid(
                "Loremipsumdolorsitametconsecteturadipiscingelit.Nullavi" +\
                "taeligulamattisrhoncusnuncegestasmattisleo.Donecnonsap" +\
                "ieninmagnatristiquedictumaacturpis.Fusceorciduifacilis" +\
                "isutsapieneuconsequatpharetralectus.Quisqueenimestpulv" +\
                "inarutquamvitaeportamattisex.Nullamquismaurisplaceratc" +\
                "onvallisjustoquisportamauris.Innullalacusconvalliseufr" +\
                "ingillautvenenatissitametdiam.Maecenasluctusligulascele" +\
                "risquepulvinarfeugiat.Sedmolestienullaaliquetorciluctus" +\
                "idpharetranislfinibus.Suspendissemalesuadatinciduntduis" +\
                "itametportaarcusollicitudinnec.Donecetmassamagna.Curabi" +\
                "tururnadiampretiumveldignissimporttitorfringillaeuneque" +\
                ".Duisantetelluspharetraidtinciduntinterdummolestiesitam" +\
                "etfelis.Utquisquamsitametantesagittisdapibusacnonodio.N" +\
                "amrutrummolestiediamidmattis.Cumsociisnatoquepenatibus" +\
                "etmagnisdisparturientmontesnasceturridiculusmus.Morbipo" +\
                "sueresedmetusacconsectetur.Etiamquisipsumvitaejustotemp" +\
                "usmaximus.Sedultriciesplaceratvolutpat.Integerlacuslect" +\
                "usmaximusacornarequissagittissitametjusto.Cumsociisnato" +\
                "quepenatibusetmagnisdisparturientmontesnasceturridicul" +\
                "usmus.Maecenasindictumpurussedrutrumex.Nullafacilisi.In" +\
                "tegerfinibusfinibusmietpharetranislfaucibusvel.Maecenas" +\
                "egetdolorlacinialobortisjustovelullamcorpersem.Vivamusa" +\
                "liquetpurusidvariusornaresapienrisusrutrumnisitincidun" +\
                "tmollissemnequeidmetus.Etiamquiseleifendpurus.Nuncfeli" +\
                "snuncscelerisqueiddignissimnecfinibusalibero.Nuncsempe" +\
                "renimnequesitamethendreritpurusfacilisisac.Maurisdapib" +\
                "ussemperfelisdignissimgravida.Aeneanultricesblanditneq" +\
                "uealiquamfinibusodioscelerisqueac.Aliquamnecmassaeumaur" +\
                "isfaucibusfringilla.Etiamconsequatligulanisisitametali" +\
                "quamnibhtemporquis.Nuncinterdumdignissimnullaatsodales" +\
                "arcusagittiseu.Proinpharetrametusneclacuspulvinarsedvol" +\
                "utpatliberoornare.Sedligulanislpulvinarnonlectuseublan" +\
                "ditfacilisisante.Sedmollisnislalacusauctorsuscipit.Inh" +\
                "achabitasseplateadictumst.Phasellussitametvelittemporv" +\
                "enenatisfeliseuegestasrisus.Aliquameteratsitametnibhco" +\
                "mmodofinibus.Morbiefficiturodiovelpulvinariaculis.Aenea" +\
                "ntemporipsummassaaconsecteturturpisfaucibusultrices.Pra" +\
                "esentsodalesmaurisquisportafermentum.Etiamnisinislvenen" +\
                "atisvelauctorutullamcorperinjusto.Proinvelligulaerat.Pha" +\
                "sellusvestibulumgravidamassanonfeugiat.Maecenaspharetr" +\
                "aeuismodmetusegetefficitur.Suspendisseamet@gmail.com"
            )
        )

    
    @pytest.mark.test
    def testEmailAtTLD(self) -> None:
        val = EmailValidator.getInstance1(False, True)
        self.assertTrue(val.isValid("test@com"))

    
    @pytest.mark.test
    def testValidator359(self) -> None:
        val = EmailValidator.getInstance1(False, True)
        self.assertFalse(val.isValid("test@.com"))

    
    @pytest.mark.test
    def testValidator374(self) -> None:
        self.assertTrue(self.__validator.isValid("abc@school.school"))

    
    @pytest.mark.test
    def testValidator473_1(self) -> None:
        with self.assertRaises(ValueError):
            EmailValidator(0, False, False, None)

    
    @pytest.mark.test
    def testValidator473_2(self) -> None:
        with self.assertRaises(ValueError):
            items = []
            EmailValidator(0, False, False, DomainValidator.getInstance2(True, items))

    
    @pytest.mark.test
    def testValidator473_3(self) -> None:
        with self.assertRaises(ValueError):
            items = []
            EmailValidator(0, True, False, DomainValidator.getInstance2(False, items))

    
    @pytest.mark.test
    def testValidator473_4(self) -> None:
        try:    
            self.assertFalse(self.__validator.isValidDomain("test.local"))
        except AttributeError:
            self.assertFalse(self.__validator._isValidDomain("test.local"))

        try:
            gp = DomainValidator.ArrayType.GENERIC_PLUS
        except AttributeError:
            gp = ArrayType.GENERIC_PLUS
        try:
            items = [DomainValidator.Item(gp, ["local"])]
        except AttributeError:
            items = [Item(gp, ["local"])]
        val = EmailValidator(0, True, False, DomainValidator.getInstance2(True, items))
        
        try:
            self.assertTrue(val.isValidDomain("test.local"))
        except AttributeError:
            self.assertTrue(val._isValidDomain("test.local"))

    
    @staticmethod
    def main(args) -> None:
        validator = self.__validator.getInstance0()
        for arg in args:
            print(f"{arg}: {validator.isValid(arg)}")
