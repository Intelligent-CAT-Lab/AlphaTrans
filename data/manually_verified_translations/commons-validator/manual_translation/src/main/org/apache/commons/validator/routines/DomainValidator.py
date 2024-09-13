from __future__ import annotations
import time
import copy
import re
import enum
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.validator.routines.RegexValidator import *


class ArrayType:

    LOCAL_MINUS = 0

    LOCAL_PLUS = 1

    LOCAL_RO = 2

    INFRASTRUCTURE_RO = 3

    COUNTRY_CODE_RO = 4

    GENERIC_RO = 5

    COUNTRY_CODE_MINUS = 6

    COUNTRY_CODE_PLUS = 7

    GENERIC_MINUS = 8

    GENERIC_PLUS = 9


class IDNBUGHOLDER:

    __IDN_TOASCII_PRESERVES_TRAILING_DOTS: bool = None

    @staticmethod
    def initialize_fields() -> None:
        IDNBUGHOLDER.__IDN_TOASCII_PRESERVES_TRAILING_DOTS: bool = (
            IDNBUGHOLDER.__keepsTrailingDot()
        )

    @staticmethod
    def __keepsTrailingDot() -> bool:

        input_ = "a."  # must be a valid name
        return input_ == input_.encode("idna").decode("utf-8")


class Item:

    def __init__(self, type_: ArrayType, values: typing.List[typing.List[str]]) -> None:
        self.type_ = type_
        self.values = values


class LazyHolder:

    __DOMAIN_VALIDATOR_WITH_LOCAL: DomainValidator = None
    __DOMAIN_VALIDATOR: DomainValidator = None

    @staticmethod
    def initialize_fields() -> None:
        LazyHolder.__DOMAIN_VALIDATOR_WITH_LOCAL: DomainValidator = DomainValidator(
            1, None, True
        )

        LazyHolder.__DOMAIN_VALIDATOR: DomainValidator = DomainValidator(1, None, False)


class DomainValidator:

    mylocalTLDsMinus: typing.List[typing.List[str]] = None

    mylocalTLDsPlus: typing.List[typing.List[str]] = None

    mygenericTLDsMinus: typing.List[typing.List[str]] = None

    mygenericTLDsPlus: typing.List[typing.List[str]] = None

    mycountryCodeTLDsPlus: typing.List[typing.List[str]] = None

    mycountryCodeTLDsMinus: typing.List[typing.List[str]] = None

    __localTLDsPlus: typing.List[str] = []
    __localTLDsMinus: typing.List[str] = []
    __genericTLDsMinus: List[str] = []
    __countryCodeTLDsMinus: typing.List[str] = []
    __genericTLDsPlus: List[str] = []
    __countryCodeTLDsPlus: typing.List[str] = []
    __inUse: bool = False
    __LOCAL_TLDS: List[str] = ["localdomain", "localhost"]
    __COUNTRY_CODE_TLDS: List[str] = [
        "ac",
        "ad",
        "ae",
        "af",
        "ag",
        "ai",
        "al",
        "am",
        "ao",
        "aq",
        "ar",
        "as",
        "at",
        "au",
        "aw",
        "ax",
        "az",
        "ba",
        "bb",
        "bd",
        "be",
        "bf",
        "bg",
        "bh",
        "bi",
        "bm",
        "bn",
        "bo",
        "br",
        "bs",
        "bt",
        "bv",
        "bw",
        "by",
        "bz",
        "ca",
        "cc",
        "cd",
        "cf",
        "cg",
        "ch",
        "ci",
        "ck",
        "cl",
        "cm",
        "cn",
        "co",
        "cr",
        "cu",
        "cv",
        "cw",
        "cx",
        "cy",
        "cz",
        "de",
        "dj",
        "dk",
        "dm",
        "do",
        "dz",
        "ec",
        "ee",
        "eg",
        "er",
        "es",
        "et",
        "eu",
        "fi",
        "fj",
        "fk",
        "fm",
        "fo",
        "fr",
        "ga",
        "gb",
        "gd",
        "ge",
        "gf",
        "gg",
        "gh",
        "gi",
        "gl",
        "gm",
        "gn",
        "gp",
        "gq",
        "gr",
        "gs",
        "gt",
        "gu",
        "gw",
        "gy",
        "hk",
        "hm",
        "hn",
        "hr",
        "ht",
        "hu",
        "id",
        "ie",
        "il",
        "im",
        "in",
        "io",
        "iq",
        "ir",
        "is",
        "it",
        "je",
        "jm",
        "jo",
        "jp",
        "ke",
        "kg",
        "kh",
        "ki",
        "km",
        "kn",
        "kp",
        "kr",
        "kw",
        "ky",
        "kz",
        "la",
        "lb",
        "lc",
        "li",
        "lk",
        "lr",
        "ls",
        "lt",
        "lu",
        "lv",
        "ly",
        "ma",
        "mc",
        "md",
        "me",
        "mg",
        "mh",
        "mk",
        "ml",
        "mm",
        "mn",
        "mo",
        "mp",
        "mq",
        "mr",
        "ms",
        "mt",
        "mu",
        "mv",
        "mw",
        "mx",
        "my",
        "mz",
        "na",
        "nc",
        "ne",
        "nf",
        "ng",
        "ni",
        "nl",
        "no",
        "np",
        "nr",
        "nu",
        "nz",
        "om",
        "pa",
        "pe",
        "pf",
        "pg",
        "ph",
        "pk",
        "pl",
        "pm",
        "pn",
        "pr",
        "ps",
        "pt",
        "pw",
        "py",
        "qa",
        "re",
        "ro",
        "rs",
        "ru",
        "rw",
        "sa",
        "sb",
        "sc",
        "sd",
        "se",
        "sg",
        "sh",
        "si",
        "sj",
        "sk",
        "sl",
        "sm",
        "sn",
        "so",
        "sr",
        "ss",
        "st",
        "su",
        "sv",
        "sx",
        "sy",
        "sz",
        "tc",
        "td",
        "tf",
        "tg",
        "th",
        "tj",
        "tk",
        "tl",
        "tm",
        "tn",
        "to",
        "tr",
        "tt",
        "tv",
        "tw",
        "tz",
        "ua",
        "ug",
        "uk",
        "us",
        "uy",
        "uz",
        "va",
        "vc",
        "ve",
        "vg",
        "vi",
        "vn",
        "vu",
        "wf",
        "ws",
        "xn--2scrj9c",
        "xn--3e0b707e",
        "xn--3hcrj9c",
        "xn--45br5cyl",
        "xn--45brj9c",
        "xn--54b7fta0cc",
        "xn--80ao21a",
        "xn--90a3ac",
        "xn--90ais",
        "xn--clchc0ea0b2g2a9gcd",
        "xn--d1alf",
        "xn--e1a4c",
        "xn--fiqs8s",
        "xn--fiqz9s",
        "xn--fpcrj9c3d",
        "xn--fzc2c9e2c",
        "xn--gecrj9c",
        "xn--h2breg3eve",
        "xn--h2brj9c",
        "xn--h2brj9c8c",
        "xn--j1amh",
        "xn--j6w193g",
        "xn--kprw13d",
        "xn--kpry57d",
        "xn--l1acc",
        "xn--lgbbat1ad8j",
        "xn--mgb9awbf",
        "xn--mgba3a4f16a",
        "xn--mgbaam7a8h",
        "xn--mgbah1a3hjkrd",
        "xn--mgbayh7gpa",
        "xn--mgbbh1a",
        "xn--mgbbh1a71e",
        "xn--mgbc0a9azcg",
        "xn--mgbcpq6gpa1a",
        "xn--mgberp4a5d4ar",
        "xn--mgbgu82a",
        "xn--mgbpl2fh",
        "xn--mgbtx2b",
        "xn--mgbx4cd0ab",
        "xn--mix891f",
        "xn--node",
        "xn--o3cw4h",
        "xn--ogbpf8fl",
        "xn--p1ai",
        "xn--pgbs0dh",
        "xn--q7ce6a",
        "xn--qxam",
        "xn--rvc1e0am3e",
        "xn--s9brj9c",
        "xn--wgbh1c",
        "xn--wgbl6a",
        "xn--xkc2al3hye2a",
        "xn--xkc2dl3a5ee0h",
        "xn--y9a3aq",
        "xn--yfro4i67o",
        "ye",
        "yt",
        "za",
        "zm",
        "zw",
    ]
    __GENERIC_TLDS: typing.List[typing.List[str]] = [
        "aaa", # aaa American Automobile Association, Inc.
        "aarp", # aarp AARP
        "abarth", # abarth Fiat Chrysler Automobiles N.V.
        "abb", # abb ABB Ltd
        "abbott", # abbott Abbott Laboratories, Inc.
        "abbvie", # abbvie AbbVie Inc.
        "abc", # abc Disney Enterprises, Inc.
        "able", # able Able Inc.
        "abogado", # abogado Top Level Domain Holdings Limited
        "abudhabi", # abudhabi Abu Dhabi Systems and Information Centre
        "academy", # academy Half Oaks, LLC
        "accenture", # accenture Accenture plc
        "accountant", # accountant dot Accountant Limited
        "accountants", # accountants Knob Town, LLC
        "aco", # aco ACO Severin Ahlmann GmbH &amp; Co. KG
        "actor", # actor United TLD Holdco Ltd.
        "adac", # adac Allgemeiner Deutscher Automobil-Club e.V. (ADAC)
        "ads", # ads Charleston Road Registry Inc.
        "adult", # adult ICM Registry AD LLC
        "aeg", # aeg Aktiebolaget Electrolux
        "aero", # aero Societe Internationale de Telecommunications Aeronautique (SITA INC
        "aetna", # aetna Aetna Life Insurance Company
        "afamilycompany", # afamilycompany Johnson Shareholdings, Inc.
        "afl", # afl Australian Football League
        "africa", # africa ZA Central Registry NPC trading as Registry.Africa
        "agakhan", # agakhan Fondation Aga Khan (Aga Khan Foundation)
        "agency", # agency Steel Falls, LLC
        "aig", # aig American International Group, Inc.
        "airbus", # airbus Airbus S.A.S.
        "airforce", # airforce United TLD Holdco Ltd.
        "airtel", # airtel Bharti Airtel Limited
        "akdn", # akdn Fondation Aga Khan (Aga Khan Foundation)
        "alfaromeo", # alfaromeo Fiat Chrysler Automobiles N.V.
        "alibaba", # alibaba Alibaba Group Holding Limited
        "alipay", # alipay Alibaba Group Holding Limited
        "allfinanz", # allfinanz Allfinanz Deutsche Vermögensberatung Aktiengesellschaft
        "allstate", # allstate Allstate Fire and Casualty Insurance Company
        "ally", # ally Ally Financial Inc.
        "alsace", # alsace REGION D ALSACE
        "alstom", # alstom ALSTOM
        "amazon", # amazon Amazon Registry Services, Inc.
        "americanexpress", # americanexpress American Express Travel Related Services
        "americanfamily", # americanfamily AmFam, Inc.
        "amex", # amex American Express Travel Related Services Company, Inc.
        "amfam", # amfam AmFam, Inc.
        "amica", # amica Amica Mutual Insurance Company
        "amsterdam", # amsterdam Gemeente Amsterdam
        "analytics", # analytics Campus IP LLC
        "android", # android Charleston Road Registry Inc.
        "anquan", # anquan QIHOO 360 TECHNOLOGY CO. LTD.
        "anz", # anz Australia and New Zealand Banking Group Limited
        "aol", # aol AOL Inc.
        "apartments", # apartments June Maple, LLC
        "app", # app Charleston Road Registry Inc.
        "apple", # apple Apple Inc.
        "aquarelle", # aquarelle Aquarelle.com
        "arab", # arab League of Arab States
        "aramco", # aramco Aramco Services Company
        "archi", # archi STARTING DOT LIMITED
        "army", # army United TLD Holdco Ltd.
        "art", # art UK Creative Ideas Limited
        "arte", # arte Association Relative à la Télévision Européenne G.E.I.E.
        "asda", # asda Wal-Mart Stores, Inc.
        "asia", # asia DotAsia Organisation Ltd.
        "associates", # associates Baxter Hill, LLC
        "athleta", # athleta The Gap, Inc.
        "attorney", # attorney United TLD Holdco, Ltd
        "auction", # auction United TLD HoldCo, Ltd.
        "audi", # audi AUDI Aktiengesellschaft
        "audible", # audible Amazon Registry Services, Inc.
        "audio", # audio Uniregistry, Corp.
        "auspost", # auspost Australian Postal Corporation
        "author", # author Amazon Registry Services, Inc.
        "auto", # auto Uniregistry, Corp.
        "autos", # autos DERAutos, LLC
        "avianca", # avianca Aerovias del Continente Americano S.A. Avianca
        "aws", # aws Amazon Registry Services, Inc.
        "axa", # axa AXA SA
        "azure", # azure Microsoft Corporation
        "baby", # baby Johnson &amp; Johnson Services, Inc.
        "baidu", # baidu Baidu, Inc.
        "banamex", # banamex Citigroup Inc.
        "bananarepublic", # bananarepublic The Gap, Inc.
        "band", # band United TLD Holdco, Ltd
        "bank", # bank fTLD Registry Services, LLC
        "bar", # bar Punto 2012 Sociedad Anonima Promotora de Inversion de Capital Variable
        "barcelona", # barcelona Municipi de Barcelona
        "barclaycard", # barclaycard Barclays Bank PLC
        "barclays", # barclays Barclays Bank PLC
        "barefoot", # barefoot Gallo Vineyards, Inc.
        "bargains", # bargains Half Hallow, LLC
        "baseball", # baseball MLB Advanced Media DH, LLC
        "basketball", # basketball Fédération Internationale de Basketball (FIBA)
        "bauhaus", # bauhaus Werkhaus GmbH
        "bayern", # bayern Bayern Connect GmbH
        "bbc", # bbc British Broadcasting Corporation
        "bbt", # bbt BB&amp;T Corporation
        "bbva", # bbva BANCO BILBAO VIZCAYA ARGENTARIA, S.A.
        "bcg", # bcg The Boston Consulting Group, Inc.
        "bcn", # bcn Municipi de Barcelona
        "beats", # beats Beats Electronics, LLC
        "beauty", # beauty L&#39;Oréal
        "beer", # beer Top Level Domain Holdings Limited
        "bentley", # bentley Bentley Motors Limited
        "berlin", # berlin dotBERLIN GmbH &amp; Co. KG
        "best", # best BestTLD Pty Ltd
        "bestbuy", # bestbuy BBY Solutions, Inc.
        "bet", # bet Afilias plc
        "bharti", # bharti Bharti Enterprises (Holding) Private Limited
        "bible", # bible American Bible Society
        "bid", # bid dot Bid Limited
        "bike", # bike Grand Hollow, LLC
        "bing", # bing Microsoft Corporation
        "bingo", # bingo Sand Cedar, LLC
        "bio", # bio STARTING DOT LIMITED
        "biz", # biz Neustar, Inc.
        "black", # black Afilias Limited
        "blackfriday", # blackfriday Uniregistry, Corp.
        "blockbuster", # blockbuster Dish DBS Corporation
        "blog", # blog Knock Knock WHOIS There, LLC
        "bloomberg", # bloomberg Bloomberg IP Holdings LLC
        "blue", # blue Afilias Limited
        "bms", # bms Bristol-Myers Squibb Company
        "bmw", # bmw Bayerische Motoren Werke Aktiengesellschaft
        "bnpparibas", # bnpparibas BNP Paribas
        "boats", # boats DERBoats, LLC
        "boehringer", # boehringer Boehringer Ingelheim International GmbH
        "bofa", # bofa NMS Services, Inc.
        "bom", # bom Núcleo de Informação e Coordenação do Ponto BR - NIC.br
        "bond", # bond Bond University Limited
        "boo", # boo Charleston Road Registry Inc.
        "book", # book Amazon Registry Services, Inc.
        "booking", # booking Booking.com B.V.
        "bosch", # bosch Robert Bosch GMBH
        "bostik", # bostik Bostik SA
        "boston", # boston Boston TLD Management, LLC
        "bot", # bot Amazon Registry Services, Inc.
        "boutique", # boutique Over Galley, LLC
        "box", # box NS1 Limited
        "bradesco", # bradesco Banco Bradesco S.A.
        "bridgestone", # bridgestone Bridgestone Corporation
        "broadway", # broadway Celebrate Broadway, Inc.
        "broker", # broker DOTBROKER REGISTRY LTD
        "brother", # brother Brother Industries, Ltd.
        "brussels", # brussels DNS.be vzw
        "budapest", # budapest Top Level Domain Holdings Limited
        "bugatti", # bugatti Bugatti International SA
        "build", # build Plan Bee LLC
        "builders", # builders Atomic Madison, LLC
        "business", # business Spring Cross, LLC
        "buy", # buy Amazon Registry Services, INC
        "buzz", # buzz DOTSTRATEGY CO.
        "bzh", # bzh Association www.bzh
        "cab", # cab Half Sunset, LLC
        "cafe", # cafe Pioneer Canyon, LLC
        "cal", # cal Charleston Road Registry Inc.
        "call", # call Amazon Registry Services, Inc.
        "calvinklein", # calvinklein PVH gTLD Holdings LLC
        "cam", # cam AC Webconnecting Holding B.V.
        "camera", # camera Atomic Maple, LLC
        "camp", # camp Delta Dynamite, LLC
        "cancerresearch", # cancerresearch Australian Cancer Research Foundation
        "canon", # canon Canon Inc.
        "capetown", # capetown ZA Central Registry NPC trading as ZA Central Registry
        "capital", # capital Delta Mill, LLC
        "capitalone", # capitalone Capital One Financial Corporation
        "car", # car Cars Registry Limited
        "caravan", # caravan Caravan International, Inc.
        "cards", # cards Foggy Hollow, LLC
        "care", # care Goose Cross, LLC
        "career", # career dotCareer LLC
        "careers", # careers Wild Corner, LLC
        "cars", # cars Uniregistry, Corp.
        "casa", # casa Top Level Domain Holdings Limited
        "case", # case CNH Industrial N.V.
        "caseih", # caseih CNH Industrial N.V.
        "cash", # cash Delta Lake, LLC
        "casino", # casino Binky Sky, LLC
        "cat", # cat Fundacio puntCAT
        "catering", # catering New Falls. LLC
        "catholic", # catholic Pontificium Consilium de Comunicationibus Socialibus (PCCS)
        "cba", # cba COMMONWEALTH BANK OF AUSTRALIA
        "cbn", # cbn The Christian Broadcasting Network, Inc.
        "cbre", # cbre CBRE, Inc.
        "cbs", # cbs CBS Domains Inc.
        "ceb", # ceb The Corporate Executive Board Company
        "center", # center Tin Mill, LLC
        "ceo", # ceo CEOTLD Pty Ltd
        "cern", # cern European Organization for Nuclear Research (&quot;CERN&quot;)
        "cfa", # cfa CFA Institute
        "cfd", # cfd DOTCFD REGISTRY LTD
        "chanel", # chanel Chanel International B.V.
        "channel", # channel Charleston Road Registry Inc.
        "charity", # charity Corn Lake, LLC
        "chase", # chase JPMorgan Chase &amp; Co.
        "chat", # chat Sand Fields, LLC
        "cheap", # cheap Sand Cover, LLC
        "chintai", # chintai CHINTAI Corporation
        "christmas", # christmas Uniregistry, Corp.
        "chrome", # chrome Charleston Road Registry Inc.
        "church", # church Holly Fileds, LLC
        "cipriani", # cipriani Hotel Cipriani Srl
        "circle", # circle Amazon Registry Services, Inc.
        "cisco", # cisco Cisco Technology, Inc.
        "citadel", # citadel Citadel Domain LLC
        "citi", # citi Citigroup Inc.
        "citic", # citic CITIC Group Corporation
        "city", # city Snow Sky, LLC
        "cityeats", # cityeats Lifestyle Domain Holdings, Inc.
        "claims", # claims Black Corner, LLC
        "cleaning", # cleaning Fox Shadow, LLC
        "click", # click Uniregistry, Corp.
        "clinic", # clinic Goose Park, LLC
        "clinique", # clinique The Estée Lauder Companies Inc.
        "clothing", # clothing Steel Lake, LLC
        "cloud", # cloud ARUBA S.p.A.
        "club", # club .CLUB DOMAINS, LLC
        "clubmed", # clubmed Club Méditerranée S.A.
        "coach", # coach Koko Island, LLC
        "codes", # codes Puff Willow, LLC
        "coffee", # coffee Trixy Cover, LLC
        "college", # college XYZ.COM LLC
        "cologne", # cologne NetCologne Gesellschaft für Telekommunikation mbH
        "com", # com VeriSign Global Registry Services
        "comcast", # comcast Comcast IP Holdings I, LLC
        "commbank", # commbank COMMONWEALTH BANK OF AUSTRALIA
        "community", # community Fox Orchard, LLC
        "company", # company Silver Avenue, LLC
        "compare", # compare iSelect Ltd
        "computer", # computer Pine Mill, LLC
        "comsec", # comsec VeriSign, Inc.
        "condos", # condos Pine House, LLC
        "construction", # construction Fox Dynamite, LLC
        "consulting", # consulting United TLD Holdco, LTD.
        "contact", # contact Top Level Spectrum, Inc.
        "contractors", # contractors Magic Woods, LLC
        "cooking", # cooking Top Level Domain Holdings Limited
        "cookingchannel", # cookingchannel Lifestyle Domain Holdings, Inc.
        "cool", # cool Koko Lake, LLC
        "coop", # coop DotCooperation LLC
        "corsica", # corsica Collectivité Territoriale de Corse
        "country", # country Top Level Domain Holdings Limited
        "coupon", # coupon Amazon Registry Services, Inc.
        "coupons", # coupons Black Island, LLC
        "courses", # courses OPEN UNIVERSITIES AUSTRALIA PTY LTD
        "cpa", # cpa American Institute of Certified Public Accountants
        "credit", # credit Snow Shadow, LLC
        "creditcard", # creditcard Binky Frostbite, LLC
        "creditunion", # creditunion CUNA Performance Resources, LLC
        "cricket", # cricket dot Cricket Limited
        "crown", # crown Crown Equipment Corporation
        "crs", # crs Federated Co-operatives Limited
        "cruise", # cruise Viking River Cruises (Bermuda) Ltd.
        "cruises", # cruises Spring Way, LLC
        "csc", # csc Alliance-One Services, Inc.
        "cuisinella", # cuisinella SALM S.A.S.
        "cymru", # cymru Nominet UK
        "cyou", # cyou Beijing Gamease Age Digital Technology Co., Ltd.
        "dabur", # dabur Dabur India Limited
        "dad", # dad Charleston Road Registry Inc.
        "dance", # dance United TLD Holdco Ltd.
        "data", # data Dish DBS Corporation
        "date", # date dot Date Limited
        "dating", # dating Pine Fest, LLC
        "datsun", # datsun NISSAN MOTOR CO., LTD.
        "day", # day Charleston Road Registry Inc.
        "dclk", # dclk Charleston Road Registry Inc.
        "dds", # dds Minds + Machines Group Limited
        "deal", # deal Amazon Registry Services, Inc.
        "dealer", # dealer Dealer Dot Com, Inc.
        "deals", # deals Sand Sunset, LLC
        "degree", # degree United TLD Holdco, Ltd
        "delivery", # delivery Steel Station, LLC
        "dell", # dell Dell Inc.
        "deloitte", # deloitte Deloitte Touche Tohmatsu
        "delta", # delta Delta Air Lines, Inc.
        "democrat", # democrat United TLD Holdco Ltd.
        "dental", # dental Tin Birch, LLC
        "dentist", # dentist United TLD Holdco, Ltd
        "desi", # desi Desi Networks LLC
        "design", # design Top Level Design, LLC
        "dev", # dev Charleston Road Registry Inc.
        "dhl", # dhl Deutsche Post AG
        "diamonds", # diamonds John Edge, LLC
        "diet", # diet Uniregistry, Corp.
        "digital", # digital Dash Park, LLC
        "direct", # direct Half Trail, LLC
        "directory", # directory Extra Madison, LLC
        "discount", # discount Holly Hill, LLC
        "discover", # discover Discover Financial Services
        "dish", # dish Dish DBS Corporation
        "diy", # diy Lifestyle Domain Holdings, Inc.
        "dnp", # dnp Dai Nippon Printing Co., Ltd.
        "docs", # docs Charleston Road Registry Inc.
        "doctor", # doctor Brice Trail, LLC
        "dog", # dog Koko Mill, LLC
        "domains", # domains Sugar Cross, LLC
        "dot", # dot Dish DBS Corporation
        "download", # download dot Support Limited
        "drive", # drive Charleston Road Registry Inc.
        "dtv", # dtv Dish DBS Corporation
        "dubai", # dubai Dubai Smart Government Department
        "duck", # duck Johnson Shareholdings, Inc.
        "dunlop", # dunlop The Goodyear Tire &amp; Rubber Company
        "dupont", # dupont E. I. du Pont de Nemours and Company
        "durban", # durban ZA Central Registry NPC trading as ZA Central Registry
        "dvag", # dvag Deutsche Vermögensberatung Aktiengesellschaft DVAG
        "dvr", # dvr Hughes Satellite Systems Corporation
        "earth", # earth Interlink Co., Ltd.
        "eat", # eat Charleston Road Registry Inc.
        "eco", # eco Big Room Inc.
        "edeka", # edeka EDEKA Verband kaufmännischer Genossenschaften e.V.
        "edu", # edu EDUCAUSE
        "education", # education Brice Way, LLC
        "email", # email Spring Madison, LLC
        "emerck", # emerck Merck KGaA
        "energy", # energy Binky Birch, LLC
        "engineer", # engineer United TLD Holdco Ltd.
        "engineering", # engineering Romeo Canyon
        "enterprises", # enterprises Snow Oaks, LLC
        "epson", # epson Seiko Epson Corporation
        "equipment", # equipment Corn Station, LLC
        "ericsson", # ericsson Telefonaktiebolaget L M Ericsson
        "erni", # erni ERNI Group Holding AG
        "esq", # esq Charleston Road Registry Inc.
        "estate", # estate Trixy Park, LLC
        "etisalat", # etisalat Emirates Telecommunic
        "eurovision", # eurovision European Broadcasting Union (EBU)
        "eus", # eus Puntueus Fundazioa
        "events", # events Pioneer Maple, LLC
        "exchange", # exchange Spring Falls, LLC
        "expert", # expert Magic Pass, LLC
        "exposed", # exposed Victor Beach, LLC
        "express", # express Sea Sunset, LLC
        "extraspace", # extraspace Extra Space Storage LLC
        "fage", # fage Fage International S.A.
        "fail", # fail Atomic Pipe, LLC
        "fairwinds", # fairwinds FairWinds Partners, LLC
        "faith", # faith dot Faith Limited
        "family", # family United TLD Holdco Ltd.
        "fan", # fan Asiamix Digital Ltd
        "fans", # fans Asiamix Digital Limited
        "farm", # farm Just Maple, LLC
        "farmers", # farmers Farmers Insurance Exchange
        "fashion", # fashion Top Level Domain Holdings Limited
        "fast", # fast Amazon Registry Services, Inc.
        "fedex", # fedex Federal Express Corporation
        "feedback", # feedback Top Level Spectrum, Inc.
        "ferrari", # ferrari Fiat Chrysler Automobiles N.V.
        "ferrero", # ferrero Ferrero Trading Lux S.A.
        "fiat", # fiat Fiat Chrysler Automobiles N.V.
        "fidelity", # fidelity Fidelity Brokerage Services LLC
        "fido", # fido Rogers Communications Canada Inc.
        "film", # film Motion Picture Domain Registry Pty Ltd
        "final", # final Núcleo de Informação e Coordenação do Ponto BR - NIC.br
        "finance", # finance Cotton Cypress, LLC
        "financial", # financial Just Cover, LLC
        "fire", # fire Amazon Registry Services, Inc.
        "firestone", # firestone Bridgestone Corporation
        "firmdale", # firmdale Firmdale Holdings Limited
        "fish", # fish Fox Woods, LLC
        "fishing", # fishing Top Level Domain Holdings Limited
        "fit", # fit Minds + Machines Group Limited
        "fitness", # fitness Brice Orchard, LLC
        "flickr", # flickr Yahoo! Domain Services Inc.
        "flights", # flights Fox Station, LLC
        "flir", # flir FLIR Systems, Inc.
        "florist", # florist Half Cypress, LLC
        "flowers", # flowers Uniregistry, Corp.
        "fly", # fly Charleston Road Registry Inc.
        "foo", # foo Charleston Road Registry Inc.
        "food", # food Lifestyle Domain Holdings, Inc.
        "foodnetwork", # foodnetwork Lifestyle Domain Holdings, Inc.
        "football", # football Foggy Farms, LLC
        "ford", # ford Ford Motor Company
        "forex", # forex DOTFOREX REGISTRY LTD
        "forsale", # forsale United TLD Holdco, LLC
        "forum", # forum Fegistry, LLC
        "foundation", # foundation John Dale, LLC
        "fox", # fox FOX Registry, LLC
        "free", # free Amazon Registry Services, Inc.
        "fresenius", # fresenius Fresenius Immobilien-Verwaltungs-GmbH
        "frl", # frl FRLregistry B.V.
        "frogans", # frogans OP3FT
        "frontdoor", # frontdoor Lifestyle Domain Holdings, Inc.
        "frontier", # frontier Frontier Communications Corporation
        "ftr", # ftr Frontier Communications Corporation
        "fujitsu", # fujitsu Fujitsu Limited
        "fujixerox", # fujixerox Xerox DNHC LLC
        "fun", # fun DotSpace, Inc.
        "fund", # fund John Castle, LLC
        "furniture", # furniture Lone Fields, LLC
        "futbol", # futbol United TLD Holdco, Ltd.
        "fyi", # fyi Silver Tigers, LLC
        "gal", # gal Asociación puntoGAL
        "gallery", # gallery Sugar House, LLC
        "gallo", # gallo Gallo Vineyards, Inc.
        "gallup", # gallup Gallup, Inc.
        "game", # game Uniregistry, Corp.
        "games", # games United TLD Holdco Ltd.
        "gap", # gap The Gap, Inc.
        "garden", # garden Top Level Domain Holdings Limited
        "gay", # gay Top Level Design, LLC
        "gbiz", # gbiz Charleston Road Registry Inc.
        "gdn", # gdn Joint Stock Company "Navigation-information systems"
        "gea", # gea GEA Group Aktiengesellschaft
        "gent", # gent COMBELL GROUP NV/SA
        "genting", # genting Resorts World Inc. Pte. Ltd.
        "george", # george Wal-Mart Stores, Inc.
        "ggee", # ggee GMO Internet, Inc.
        "gift", # gift Uniregistry, Corp.
        "gifts", # gifts Goose Sky, LLC
        "gives", # gives United TLD Holdco Ltd.
        "giving", # giving Giving Limited
        "glade", # glade Johnson Shareholdings, Inc.
        "glass", # glass Black Cover, LLC
        "gle", # gle Charleston Road Registry Inc.
        "global", # global Dot Global Domain Registry Limited
        "globo", # globo Globo Comunicação e Participações S.A
        "gmail", # gmail Charleston Road Registry Inc.
        "gmbh", # gmbh Extra Dynamite, LLC
        "gmo", # gmo GMO Internet, Inc.
        "gmx", # gmx 1&amp;1 Mail &amp; Media GmbH
        "godaddy", # godaddy Go Daddy East, LLC
        "gold", # gold June Edge, LLC
        "goldpoint", # goldpoint YODOBASHI CAMERA CO.,LTD.
        "golf", # golf Lone Falls, LLC
        "goo", # goo NTT Resonant Inc.
        "goodyear", # goodyear The Goodyear Tire &amp; Rubber Company
        "goog", # goog Charleston Road Registry Inc.
        "google", # google Charleston Road Registry Inc.
        "gop", # gop Republican State Leadership Committee, Inc.
        "got", # got Amazon Registry Services, Inc.
        "gov", # gov General Services Administration Attn: QTDC, 2E08 (.gov Domain
        "grainger", # grainger Grainger Registry Services, LLC
        "graphics", # graphics Over Madison, LLC
        "gratis", # gratis Pioneer Tigers, LLC
        "green", # green Afilias Limited
        "gripe", # gripe Corn Sunset, LLC
        "grocery", # grocery Wal-Mart Stores, Inc.
        "group", # group Romeo Town, LLC
        "guardian", # guardian The Guardian Life Insurance Company of America
        "gucci", # gucci Guccio Gucci S.p.a.
        "guge", # guge Charleston Road Registry Inc.
        "guide", # guide Snow Moon, LLC
        "guitars", # guitars Uniregistry, Corp.
        "guru", # guru Pioneer Cypress, LLC
        "hair", # hair L&#39;Oreal
        "hamburg", # hamburg Hamburg Top-Level-Domain GmbH
        "hangout", # hangout Charleston Road Registry Inc.
        "haus", # haus United TLD Holdco, LTD.
        "hbo", # hbo HBO Registry Services, Inc.
        "hdfc", # hdfc HOUSING DEVELOPMENT FINANCE CORPORATION LIMITED
        "hdfcbank", # hdfcbank HDFC Bank Limited
        "health", # health DotHealth, LLC
        "healthcare", # healthcare Silver Glen, LLC
        "help", # help Uniregistry, Corp.
        "helsinki", # helsinki City of Helsinki
        "here", # here Charleston Road Registry Inc.
        "hermes", # hermes Hermes International
        "hgtv", # hgtv Lifestyle Domain Holdings, Inc.
        "hiphop", # hiphop Uniregistry, Corp.
        "hisamitsu", # hisamitsu Hisamitsu Pharmaceutical Co.,Inc.
        "hitachi", # hitachi Hitachi, Ltd.
        "hiv", # hiv dotHIV gemeinnuetziger e.V.
        "hkt", # hkt PCCW-HKT DataCom Services Limited
        "hockey", # hockey Half Willow, LLC
        "holdings", # holdings John Madison, LLC
        "holiday", # holiday Goose Woods, LLC
        "homedepot", # homedepot Homer TLC, Inc.
        "homegoods", # homegoods The TJX Companies, Inc.
        "homes", # homes DERHomes, LLC
        "homesense", # homesense The TJX Companies, Inc.
        "honda", # honda Honda Motor Co., Ltd.
        "horse", # horse Top Level Domain Holdings Limited
        "hospital", # hospital Ruby Pike, LLC
        "host", # host DotHost Inc.
        "hosting", # hosting Uniregistry, Corp.
        "hot", # hot Amazon Registry Services, Inc.
        "hoteles", # hoteles Travel Reservations SRL
        "hotels", # hotels Booking.com B.V.
        "hotmail", # hotmail Microsoft Corporation
        "house", # house Sugar Park, LLC
        "how", # how Charleston Road Registry Inc.
        "hsbc", # hsbc HSBC Holdings PLC
        "hughes", # hughes Hughes Satellite Systems Corporation
        "hyatt", # hyatt Hyatt GTLD, L.L.C.
        "hyundai", # hyundai Hyundai Motor Company
        "ibm", # ibm International Business Machines Corporation
        "icbc", # icbc Industrial and Commercial Bank of China Limited
        "ice", # ice IntercontinentalExchange, Inc.
        "icu", # icu One.com A/S
        "ieee", # ieee IEEE Global LLC
        "ifm", # ifm ifm electronic gmbh
        "ikano", # ikano Ikano S.A.
        "imamat", # imamat Fondation Aga Khan (Aga Khan Foundation)
        "imdb", # imdb Amazon Registry Services, Inc.
        "immo", # immo Auburn Bloom, LLC
        "immobilien", # immobilien United TLD Holdco Ltd.
        "inc", # inc Intercap Holdings Inc.
        "industries", # industries Outer House, LLC
        "infiniti", # infiniti NISSAN MOTOR CO., LTD.
        "info", # info Afilias Limited
        "ing", # ing Charleston Road Registry Inc.
        "ink", # ink Top Level Design, LLC
        "institute", # institute Outer Maple, LLC
        "insurance", # insurance fTLD Registry Services LLC
        "insure", # insure Pioneer Willow, LLC
        "int", # int Internet Assigned Numbers Authority
        "intel", # intel Intel Corporation
        "international", # international Wild Way, LLC
        "intuit", # intuit Intuit Administrative Services, Inc.
        "investments", # investments Holly Glen, LLC
        "ipiranga", # ipiranga Ipiranga Produtos de Petroleo S.A.
        "irish", # irish Dot-Irish LLC
        "ismaili", # ismaili Fondation Aga Khan (Aga Khan Foundation)
        "ist", # ist Istanbul Metropolitan Municipality
        "istanbul", # istanbul Istanbul Metropolitan Municipality / Medya A.S.
        "itau", # itau Itau Unibanco Holding S.A.
        "itv", # itv ITV Services Limited
        "iveco", # iveco CNH Industrial N.V.
        "jaguar", # jaguar Jaguar Land Rover Ltd
        "java", # java Oracle Corporation
        "jcb", # jcb JCB Co., Ltd.
        "jcp", # jcp JCP Media, Inc.
        "jeep", # jeep FCA US LLC.
        "jetzt", # jetzt New TLD Company AB
        "jewelry", # jewelry Wild Bloom, LLC
        "jio", # jio Affinity Names, Inc.
        "jll", # jll Jones Lang LaSalle Incorporated
        "jmp", # jmp Matrix IP LLC
        "jnj", # jnj Johnson &amp; Johnson Services, Inc.
        "jobs", # jobs Employ Media LLC
        "joburg", # joburg ZA Central Registry NPC trading as ZA Central Registry
        "jot", # jot Amazon Registry Services, Inc.
        "joy", # joy Amazon Registry Services, Inc.
        "jpmorgan", # jpmorgan JPMorgan Chase &amp; Co.
        "jprs", # jprs Japan Registry Services Co., Ltd.
        "juegos", # juegos Uniregistry, Corp.
        "juniper", # juniper JUNIPER NETWORKS, INC.
        "kaufen", # kaufen United TLD Holdco Ltd.
        "kddi", # kddi KDDI CORPORATION
        "kerryhotels", # kerryhotels Kerry Trading Co. Limited
        "kerrylogistics", # kerrylogistics Kerry Trading Co. Limited
        "kerryproperties", # kerryproperties Kerry Trading Co. Limited
        "kfh", # kfh Kuwait Finance House
        "kia", # kia KIA MOTORS CORPORATION
        "kim", # kim Afilias Limited
        "kinder", # kinder Ferrero Trading Lux S.A.
        "kindle", # kindle Amazon Registry Services, Inc.
        "kitchen", # kitchen Just Goodbye, LLC
        "kiwi", # kiwi DOT KIWI LIMITED
        "koeln", # koeln NetCologne Gesellschaft für Telekommunikation mbH
        "komatsu", # komatsu Komatsu Ltd.
        "kosher", # kosher Kosher Marketing Assets LLC
        "kpmg", # kpmg KPMG International Cooperative (KPMG International Genossenschaft)
        "kpn", # kpn Koninklijke KPN N.V.
        "krd", # krd KRG Department of Information Technology
        "kred", # kred KredTLD Pty Ltd
        "kuokgroup", # kuokgroup Kerry Trading Co. Limited
        "kyoto", # kyoto Academic Institution: Kyoto Jyoho Gakuen
        "lacaixa", # lacaixa CAIXA D&#39;ESTALVIS I PENSIONS DE BARCELONA
        "lamborghini", # lamborghini Automobili Lamborghini S.p.A.
        "lamer", # lamer The Estée Lauder Companies Inc.
        "lancaster", # lancaster LANCASTER
        "lancia", # lancia Fiat Chrysler Automobiles N.V.
        "land", # land Pine Moon, LLC
        "landrover", # landrover Jaguar Land Rover Ltd
        "lanxess", # lanxess LANXESS Corporation
        "lasalle", # lasalle Jones Lang LaSalle Incorporated
        "lat", # lat ECOM-LAC Federación de Latinoamérica y el Caribe para Internet y el
        "latino", # latino Dish DBS Corporation
        "latrobe", # latrobe La Trobe University
        "law", # law Minds + Machines Group Limited
        "lawyer", # lawyer United TLD Holdco, Ltd
        "lds", # lds IRI Domain Management, LLC
        "lease", # lease Victor Trail, LLC
        "leclerc", # leclerc A.C.D. LEC Association des Centres Distributeurs Edouard
        "lefrak", # lefrak LeFrak Organization, Inc.
        "legal", # legal Blue Falls, LLC
        "lego", # lego LEGO Juris A/S
        "lexus", # lexus TOYOTA MOTOR CORPORATION
        "lgbt", # lgbt Afilias Limited
        "lidl", # lidl Schwarz Domains und Services GmbH &amp; Co. KG
        "life", # life Trixy Oaks, LLC
        "lifeinsurance", # lifeinsurance American Council of Life Insurers
        "lifestyle", # lifestyle Lifestyle Domain Holdings, Inc.
        "lighting", # lighting John McCook, LLC
        "like", # like Amazon Registry Services, Inc.
        "lilly", # lilly Eli Lilly and Company
        "limited", # limited Big Fest, LLC
        "limo", # limo Hidden Frostbite, LLC
        "lincoln", # lincoln Ford Motor Company
        "linde", # linde Linde Aktiengesellschaft
        "link", # link Uniregistry, Corp.
        "lipsy", # lipsy Lipsy Ltd
        "live", # live United TLD Holdco Ltd.
        "living", # living Lifestyle Domain Holdings, Inc.
        "lixil", # lixil LIXIL Group Corporation
        "llc", # llc Afilias plc
        "llp", # llp Dot Registry LLC
        "loan", # loan dot Loan Limited
        "loans", # loans June Woods, LLC
        "locker", # locker Dish DBS Corporation
        "locus", # locus Locus Analytics LLC
        "loft", # loft Annco, Inc.
        "lol", # lol Uniregistry, Corp.
        "london", # london Dot London Domains Limited
        "lotte", # lotte Lotte Holdings Co., Ltd.
        "lotto", # lotto Afilias Limited
        "love", # love Merchant Law Group LLP
        "lpl", # lpl LPL Holdings, Inc.
        "lplfinancial", # lplfinancial LPL Holdings, Inc.
        "ltd", # ltd Over Corner, LLC
        "ltda", # ltda InterNetX Corp.
        "lundbeck", # lundbeck H. Lundbeck A/S
        "lupin", # lupin LUPIN LIMITED
        "luxe", # luxe Top Level Domain Holdings Limited
        "luxury", # luxury Luxury Partners LLC
        "macys", # macys Macys, Inc.
        "madrid", # madrid Comunidad de Madrid
        "maif", # maif Mutuelle Assurance Instituteur France (MAIF)
        "maison", # maison Victor Frostbite, LLC
        "makeup", # makeup L&#39;Oréal
        "man", # man MAN SE
        "management", # management John Goodbye, LLC
        "mango", # mango PUNTO FA S.L.
        "map", # map Charleston Road Registry Inc.
        "market", # market Unitied TLD Holdco, Ltd
        "marketing", # marketing Fern Pass, LLC
        "markets", # markets DOTMARKETS REGISTRY LTD
        "marriott", # marriott Marriott Worldwide Corporation
        "marshalls", # marshalls The TJX Companies, Inc.
        "maserati", # maserati Fiat Chrysler Automobiles N.V.
        "mattel", # mattel Mattel Sites, Inc.
        "mba", # mba Lone Hollow, LLC
        "mckinsey", # mckinsey McKinsey Holdings, Inc.
        "med", # med Medistry LLC
        "media", # media Grand Glen, LLC
        "meet", # meet Afilias Limited
        "melbourne", # melbourne The Crown in right of the State of Victoria, represented
        "meme", # meme Charleston Road Registry Inc.
        "memorial", # memorial Dog Beach, LLC
        "men", # men Exclusive Registry Limited
        "menu", # menu Wedding TLD2, LLC
        "merckmsd", # merckmsd MSD Registry Holdings, Inc.
        "metlife", # metlife MetLife Services and Solutions, LLC
        "miami", # miami Top Level Domain Holdings Limited
        "microsoft", # microsoft Microsoft Corporation
        "mil", # mil DoD Network Information Center
        "mini", # mini Bayerische Motoren Werke Aktiengesellschaft
        "mint", # mint Intuit Administrative Services, Inc.
        "mit", # mit Massachusetts Institute of Technology
        "mitsubishi", # mitsubishi Mitsubishi Corporation
        "mlb", # mlb MLB Advanced Media DH, LLC
        "mls", # mls The Canadian Real Estate Association
        "mma", # mma MMA IARD
        "mobi", # mobi Afilias Technologies Limited dba dotMobi
        "mobile", # mobile Dish DBS Corporation
        "moda", # moda United TLD Holdco Ltd.
        "moe", # moe Interlink Co., Ltd.
        "moi", # moi Amazon Registry Services, Inc.
        "mom", # mom Uniregistry, Corp.
        "monash", # monash Monash University
        "money", # money Outer McCook, LLC
        "monster", # monster Monster Worldwide, Inc.
        "mormon", # mormon IRI Domain Management, LLC (&quot;Applicant&quot;)
        "mortgage", # mortgage United TLD Holdco, Ltd
        "moscow", # moscow Foundation for Assistance for Internet Technologies and
        "moto", # moto Motorola Trademark Holdings, LLC
        "motorcycles", # motorcycles DERMotorcycles, LLC
        "mov", # mov Charleston Road Registry Inc.
        "movie", # movie New Frostbite, LLC
        "msd", # msd MSD Registry Holdings, Inc.
        "mtn", # mtn MTN Dubai Limited
        "mtr", # mtr MTR Corporation Limited
        "museum", # museum Museum Domain Management Association
        "mutual", # mutual Northwestern Mutual MU TLD Registry, LLC
        "nab", # nab National Australia Bank Limited
        "nagoya", # nagoya GMO Registry, Inc.
        "name", # name VeriSign Information Services, Inc.
        "nationwide", # nationwide Nationwide Mutual Insurance Company
        "natura", # natura NATURA COSMÉTICOS S.A.
        "navy", # navy United TLD Holdco Ltd.
        "nba", # nba NBA REGISTRY, LLC
        "nec", # nec NEC Corporation
        "net", # net VeriSign Global Registry Services
        "netbank", # netbank COMMONWEALTH BANK OF AUSTRALIA
        "netflix", # netflix Netflix, Inc.
        "network", # network Trixy Manor, LLC
        "neustar", # neustar NeuStar, Inc.
        "new", # new Charleston Road Registry Inc.
        "newholland", # newholland CNH Industrial N.V.
        "news", # news United TLD Holdco Ltd.
        "next", # next Next plc
        "nextdirect", # nextdirect Next plc
        "nexus", # nexus Charleston Road Registry Inc.
        "nfl", # nfl NFL Reg Ops LLC
        "ngo", # ngo Public Interest Registry
        "nhk", # nhk Japan Broadcasting Corporation (NHK)
        "nico", # nico DWANGO Co., Ltd.
        "nike", # nike NIKE, Inc.
        "nikon", # nikon NIKON CORPORATION
        "ninja", # ninja United TLD Holdco Ltd.
        "nissan", # nissan NISSAN MOTOR CO., LTD.
        "nissay", # nissay Nippon Life Insurance Company
        "nokia", # nokia Nokia Corporation
        "northwesternmutual", # northwesternmutual Northwestern Mutual Registry, LLC
        "norton", # norton Symantec Corporation
        "now", # now Amazon Registry Services, Inc.
        "nowruz", # nowruz Asia Green IT System Bilgisayar San. ve Tic. Ltd. Sti.
        "nowtv", # nowtv Starbucks (HK) Limited
        "nra", # nra NRA Holdings Company, INC.
        "nrw", # nrw Minds + Machines GmbH
        "ntt", # ntt NIPPON TELEGRAPH AND TELEPHONE CORPORATION
        "nyc", # nyc The City of New York by and through the New York City Department of
        "obi", # obi OBI Group Holding SE &amp; Co. KGaA
        "observer", # observer Top Level Spectrum, Inc.
        "off", # off Johnson Shareholdings, Inc.
        "office", # office Microsoft Corporation
        "okinawa", # okinawa BusinessRalliart inc.
        "olayan", # olayan Crescent Holding GmbH
        "olayangroup", # olayangroup Crescent Holding GmbH
        "oldnavy", # oldnavy The Gap, Inc.
        "ollo", # ollo Dish DBS Corporation
        "omega", # omega The Swatch Group Ltd
        "one", # one One.com A/S
        "ong", # ong Public Interest Registry
        "onl", # onl I-REGISTRY Ltd., Niederlassung Deutschland
        "online", # online DotOnline Inc.
        "onyourside", # onyourside Nationwide Mutual Insurance Company
        "ooo", # ooo INFIBEAM INCORPORATION LIMITED
        "open", # open American Express Travel Related Services Company, Inc.
        "oracle", # oracle Oracle Corporation
        "orange", # orange Orange Brand Services Limited
        "org", # org Public Interest Registry (PIR)
        "organic", # organic Afilias Limited
        "origins", # origins The Estée Lauder Companies Inc.
        "osaka", # osaka Interlink Co., Ltd.
        "otsuka", # otsuka Otsuka Holdings Co., Ltd.
        "ott", # ott Dish DBS Corporation
        "ovh", # ovh OVH SAS
        "page", # page Charleston Road Registry Inc.
        "panasonic", # panasonic Panasonic Corporation
        "paris", # paris City of Paris
        "pars", # pars Asia Green IT System Bilgisayar San. ve Tic. Ltd. Sti.
        "partners", # partners Magic Glen, LLC
        "parts", # parts Sea Goodbye, LLC
        "party", # party Blue Sky Registry Limited
        "passagens", # passagens Travel Reservations SRL
        "pay", # pay Amazon Registry Services, Inc.
        "pccw", # pccw PCCW Enterprises Limited
        "pet", # pet Afilias plc
        "pfizer", # pfizer Pfizer Inc.
        "pharmacy", # pharmacy National Association of Boards of Pharmacy
        "phd", # phd Charleston Road Registry Inc.
        "philips", # philips Koninklijke Philips N.V.
        "phone", # phone Dish DBS Corporation
        "photo", # photo Uniregistry, Corp.
        "photography", # photography Sugar Glen, LLC
        "photos", # photos Sea Corner, LLC
        "physio", # physio PhysBiz Pty Ltd
        "pics", # pics Uniregistry, Corp.
        "pictet", # pictet Pictet Europe S.A.
        "pictures", # pictures Foggy Sky, LLC
        "pid", # pid Top Level Spectrum, Inc.
        "pin", # pin Amazon Registry Services, Inc.
        "ping", # ping Ping Registry Provider, Inc.
        "pink", # pink Afilias Limited
        "pioneer", # pioneer Pioneer Corporation
        "pizza", # pizza Foggy Moon, LLC
        "place", # place Snow Galley, LLC
        "play", # play Charleston Road Registry Inc.
        "playstation", # playstation Sony Computer Entertainment Inc.
        "plumbing", # plumbing Spring Tigers, LLC
        "plus", # plus Sugar Mill, LLC
        "pnc", # pnc PNC Domain Co., LLC
        "pohl", # pohl Deutsche Vermögensberatung Aktiengesellschaft DVAG
        "poker", # poker Afilias Domains No. 5 Limited
        "politie", # politie Politie Nederland
        "porn", # porn ICM Registry PN LLC
        "post", # post Universal Postal Union
        "pramerica", # pramerica Prudential Financial, Inc.
        "praxi", # praxi Praxi S.p.A.
        "press", # press DotPress Inc.
        "prime", # prime Amazon Registry Services, Inc.
        "pro", # pro Registry Services Corporation dba RegistryPro
        "prod", # prod Charleston Road Registry Inc.
        "productions", # productions Magic Birch, LLC
        "prof", # prof Charleston Road Registry Inc.
        "progressive", # progressive Progressive Casualty Insurance Company
        "promo", # promo Afilias plc
        "properties", # properties Big Pass, LLC
        "property", # property Uniregistry, Corp.
        "protection", # protection XYZ.COM LLC
        "pru", # pru Prudential Financial, Inc.
        "prudential", # prudential Prudential Financial, Inc.
        "pub", # pub United TLD Holdco Ltd.
        "pwc", # pwc PricewaterhouseCoopers LLP
        "qpon", # qpon dotCOOL, Inc.
        "quebec", # quebec PointQuébec Inc
        "quest", # quest Quest ION Limited
        "qvc", # qvc QVC, Inc.
        "racing", # racing Premier Registry Limited
        "radio", # radio European Broadcasting Union (EBU)
        "raid", # raid Johnson Shareholdings, Inc.
        "read", # read Amazon Registry Services, Inc.
        "realestate", # realestate dotRealEstate LLC
        "realtor", # realtor Real Estate Domains LLC
        "realty", # realty Fegistry, LLC
        "recipes", # recipes Grand Island, LLC
        "red", # red Afilias Limited
        "redstone", # redstone Redstone Haute Couture Co., Ltd.
        "redumbrella", # redumbrella Travelers TLD, LLC
        "rehab", # rehab United TLD Holdco Ltd.
        "reise", # reise Foggy Way, LLC
        "reisen", # reisen New Cypress, LLC
        "reit", # reit National Association of Real Estate Investment Trusts, Inc.
        "reliance", # reliance Reliance Industries Limited
        "ren", # ren Beijing Qianxiang Wangjing Technology Development Co., Ltd.
        "rent", # rent XYZ.COM LLC
        "rentals", # rentals Big Hollow,LLC
        "repair", # repair Lone Sunset, LLC
        "report", # report Binky Glen, LLC
        "republican", # republican United TLD Holdco Ltd.
        "rest", # rest Punto 2012 Sociedad Anonima Promotora de Inversion de Capital
        "restaurant", # restaurant Snow Avenue, LLC
        "review", # review dot Review Limited
        "reviews", # reviews United TLD Holdco, Ltd.
        "rexroth", # rexroth Robert Bosch GMBH
        "rich", # rich I-REGISTRY Ltd., Niederlassung Deutschland
        "richardli", # richardli Pacific Century Asset Management (HK) Limited
        "ricoh", # ricoh Ricoh Company, Ltd.
        "ril", # ril Reliance Industries Limited
        "rio", # rio Empresa Municipal de Informática SA - IPLANRIO
        "rip", # rip United TLD Holdco Ltd.
        "rmit", # rmit Royal Melbourne Institute of Technology
        "rocher", # rocher Ferrero Trading Lux S.A.
        "rocks", # rocks United TLD Holdco, LTD.
        "rodeo", # rodeo Top Level Domain Holdings Limited
        "rogers", # rogers Rogers Communications Canada Inc.
        "room", # room Amazon Registry Services, Inc.
        "rsvp", # rsvp Charleston Road Registry Inc.
        "rugby", # rugby World Rugby Strategic Developments Limited
        "ruhr", # ruhr regiodot GmbH &amp; Co. KG
        "run", # run Snow Park, LLC
        "rwe", # rwe RWE AG
        "ryukyu", # ryukyu BusinessRalliart inc.
        "saarland", # saarland dotSaarland GmbH
        "safe", # safe Amazon Registry Services, Inc.
        "safety", # safety Safety Registry Services, LLC.
        "sakura", # sakura SAKURA Internet Inc.
        "sale", # sale United TLD Holdco, Ltd
        "salon", # salon Outer Orchard, LLC
        "samsclub", # samsclub Wal-Mart Stores, Inc.
        "samsung", # samsung SAMSUNG SDS CO., LTD
        "sandvik", # sandvik Sandvik AB
        "sandvikcoromant", # sandvikcoromant Sandvik AB
        "sanofi", # sanofi Sanofi
        "sap", # sap SAP AG
        "sarl", # sarl Delta Orchard, LLC
        "sas", # sas Research IP LLC
        "save", # save Amazon Registry Services, Inc.
        "saxo", # saxo Saxo Bank A/S
        "sbi", # sbi STATE BANK OF INDIA
        "sbs", # sbs SPECIAL BROADCASTING SERVICE CORPORATION
        "sca", # sca SVENSKA CELLULOSA AKTIEBOLAGET SCA (publ)
        "scb", # scb The Siam Commercial Bank Public Company Limited (&quot;SCB&quot;)
        "schaeffler", # schaeffler Schaeffler Technologies AG &amp; Co. KG
        "schmidt", # schmidt SALM S.A.S.
        "scholarships", # scholarships Scholarships.com, LLC
        "school", # school Little Galley, LLC
        "schule", # schule Outer Moon, LLC
        "schwarz", # schwarz Schwarz Domains und Services GmbH &amp; Co. KG
        "science", # science dot Science Limited
        "scjohnson", # scjohnson Johnson Shareholdings, Inc.
        "scot", # scot Dot Scot Registry Limited
        "search", # search Charleston Road Registry Inc.
        "seat", # seat SEAT, S.A. (Sociedad Unipersonal)
        "secure", # secure Amazon Registry Services, Inc.
        "security", # security XYZ.COM LLC
        "seek", # seek Seek Limited
        "select", # select iSelect Ltd
        "sener", # sener Sener Ingeniería y Sistemas, S.A.
        "services", # services Fox Castle, LLC
        "ses", # ses SES
        "seven", # seven Seven West Media Ltd
        "sew", # sew SEW-EURODRIVE GmbH &amp; Co KG
        "sex", # sex ICM Registry SX LLC
        "sexy", # sexy Uniregistry, Corp.
        "sfr", # sfr Societe Francaise du Radiotelephone - SFR
        "shangrila", # shangrila Shangri‐La International Hotel Management Limited
        "sharp", # sharp Sharp Corporation
        "shaw", # shaw Shaw Cablesystems G.P.
        "shell", # shell Shell Information Technology International Inc
        "shia", # shia Asia Green IT System Bilgisayar San. ve Tic. Ltd. Sti.
        "shiksha", # shiksha Afilias Limited
        "shoes", # shoes Binky Galley, LLC
        "shop", # shop GMO Registry, Inc.
        "shopping", # shopping Over Keep, LLC
        "shouji", # shouji QIHOO 360 TECHNOLOGY CO. LTD.
        "show", # show Snow Beach, LLC
        "showtime", # showtime CBS Domains Inc.
        "shriram", # shriram Shriram Capital Ltd.
        "silk", # silk Amazon Registry Services, Inc.
        "sina", # sina Sina Corporation
        "singles", # singles Fern Madison, LLC
        "site", # site DotSite Inc.
        "ski", # ski STARTING DOT LIMITED
        "skin", # skin L&#39;Oréal
        "sky", # sky Sky International AG
        "skype", # skype Microsoft Corporation
        "sling", # sling Hughes Satellite Systems Corporation
        "smart", # smart Smart Communications, Inc. (SMART)
        "smile", # smile Amazon Registry Services, Inc.
        "sncf", # sncf SNCF (Société Nationale des Chemins de fer Francais)
        "soccer", # soccer Foggy Shadow, LLC
        "social", # social United TLD Holdco Ltd.
        "softbank", # softbank SoftBank Group Corp.
        "software", # software United TLD Holdco, Ltd
        "sohu", # sohu Sohu.com Limited
        "solar", # solar Ruby Town, LLC
        "solutions", # solutions Silver Cover, LLC
        "song", # song Amazon Registry Services, Inc.
        "sony", # sony Sony Corporation
        "soy", # soy Charleston Road Registry Inc.
        "space", # space DotSpace Inc.
        "sport", # sport Global Association of International Sports Federations (GAISF)
        "spot", # spot Amazon Registry Services, Inc.
        "spreadbetting", # spreadbetting DOTSPREADBETTING REGISTRY LTD
        "srl", # srl InterNetX Corp.
        "stada", # stada STADA Arzneimittel AG
        "staples", # staples Staples, Inc.
        "star", # star Star India Private Limited
        "statebank", # statebank STATE BANK OF INDIA
        "statefarm", # statefarm State Farm Mutual Automobile Insurance Company
        "stc", # stc Saudi Telecom Company
        "stcgroup", # stcgroup Saudi Telecom Company
        "stockholm", # stockholm Stockholms kommun
        "storage", # storage Self Storage Company LLC
        "store", # store DotStore Inc.
        "stream", # stream dot Stream Limited
        "studio", # studio United TLD Holdco Ltd.
        "study", # study OPEN UNIVERSITIES AUSTRALIA PTY LTD
        "style", # style Binky Moon, LLC
        "sucks", # sucks Vox Populi Registry Ltd.
        "supplies", # supplies Atomic Fields, LLC
        "supply", # supply Half Falls, LLC
        "support", # support Grand Orchard, LLC
        "surf", # surf Top Level Domain Holdings Limited
        "surgery", # surgery Tin Avenue, LLC
        "suzuki", # suzuki SUZUKI MOTOR CORPORATION
        "swatch", # swatch The Swatch Group Ltd
        "swiftcover", # swiftcover Swiftcover Insurance Services Limited
        "swiss", # swiss Swiss Confederation
        "sydney", # sydney State of New South Wales, Department of Premier and Cabinet
        "systems", # systems Dash Cypress, LLC
        "tab", # tab Tabcorp Holdings Limited
        "taipei", # taipei Taipei City Government
        "talk", # talk Amazon Registry Services, Inc.
        "taobao", # taobao Alibaba Group Holding Limited
        "target", # target Target Domain Holdings, LLC
        "tatamotors", # tatamotors Tata Motors Ltd
        "tatar", # tatar LLC "Coordination Center of Regional Domain of Tatarstan Republic"
        "tattoo", # tattoo Uniregistry, Corp.
        "tax", # tax Storm Orchard, LLC
        "taxi", # taxi Pine Falls, LLC
        "tci", # tci Asia Green IT System Bilgisayar San. ve Tic. Ltd. Sti.
        "tdk", # tdk TDK Corporation
        "team", # team Atomic Lake, LLC
        "tech", # tech Dot Tech LLC
        "technology", # technology Auburn Falls, LLC
        "tel", # tel Telnic Ltd.
        "temasek", # temasek Temasek Holdings (Private) Limited
        "tennis", # tennis Cotton Bloom, LLC
        "teva", # teva Teva Pharmaceutical Industries Limited
        "thd", # thd Homer TLC, Inc.
        "theater", # theater Blue Tigers, LLC
        "theatre", # theatre XYZ.COM LLC
        "tiaa", # tiaa Teachers Insurance and Annuity Association of America
        "tickets", # tickets Accent Media Limited
        "tienda", # tienda Victor Manor, LLC
        "tiffany", # tiffany Tiffany and Company
        "tips", # tips Corn Willow, LLC
        "tires", # tires Dog Edge, LLC
        "tirol", # tirol punkt Tirol GmbH
        "tjmaxx", # tjmaxx The TJX Companies, Inc.
        "tjx", # tjx The TJX Companies, Inc.
        "tkmaxx", # tkmaxx The TJX Companies, Inc.
        "tmall", # tmall Alibaba Group Holding Limited
        "today", # today Pearl Woods, LLC
        "tokyo", # tokyo GMO Registry, Inc.
        "tools", # tools Pioneer North, LLC
        "top", # top Jiangsu Bangning Science &amp; Technology Co.,Ltd.
        "toray", # toray Toray Industries, Inc.
        "toshiba", # toshiba TOSHIBA Corporation
        "total", # total Total SA
        "tours", # tours Sugar Station, LLC
        "town", # town Koko Moon, LLC
        "toyota", # toyota TOYOTA MOTOR CORPORATION
        "toys", # toys Pioneer Orchard, LLC
        "trade", # trade Elite Registry Limited
        "trading", # trading DOTTRADING REGISTRY LTD
        "training", # training Wild Willow, LLC
        "travel", # travel Tralliance Registry Management Company, LLC.
        "travelchannel", # travelchannel Lifestyle Domain Holdings, Inc.
        "travelers", # travelers Travelers TLD, LLC
        "travelersinsurance", # travelersinsurance Travelers TLD, LLC
        "trust", # trust Artemis Internet Inc
        "trv", # trv Travelers TLD, LLC
        "tube", # tube Latin American Telecom LLC
        "tui", # tui TUI AG
        "tunes", # tunes Amazon Registry Services, Inc.
        "tushu", # tushu Amazon Registry Services, Inc.
        "tvs", # tvs T V SUNDRAM IYENGAR  &amp; SONS PRIVATE LIMITED
        "ubank", # ubank National Australia Bank Limited
        "ubs", # ubs UBS AG
        "unicom", # unicom China United Network Communications Corporation Limited
        "university", # university Little Station, LLC
        "uno", # uno Dot Latin LLC
        "uol", # uol UBN INTERNET LTDA.
        "ups", # ups UPS Market Driver, Inc.
        "vacations", # vacations Atomic Tigers, LLC
        "vana", # vana Lifestyle Domain Holdings, Inc.
        "vanguard", # vanguard The Vanguard Group, Inc.
        "vegas", # vegas Dot Vegas, Inc.
        "ventures", # ventures Binky Lake, LLC
        "verisign", # verisign VeriSign, Inc.
        "versicherung", # versicherung dotversicherung-registry GmbH
        "vet", # vet United TLD Holdco, Ltd
        "viajes", # viajes Black Madison, LLC
        "video", # video United TLD Holdco, Ltd
        "vig", # vig VIENNA INSURANCE GROUP AG Wiener Versicherung Gruppe
        "viking", # viking Viking River Cruises (Bermuda) Ltd.
        "villas", # villas New Sky, LLC
        "vin", # vin Holly Shadow, LLC
        "vip", # vip Minds + Machines Group Limited
        "virgin", # virgin Virgin Enterprises Limited
        "visa", # visa Visa Worldwide Pte. Limited
        "vision", # vision Koko Station, LLC
        "viva", # viva Saudi Telecom Company
        "vivo", # vivo Telefonica Brasil S.A.
        "vlaanderen", # vlaanderen DNS.be vzw
        "vodka", # vodka Top Level Domain Holdings Limited
        "volkswagen", # volkswagen Volkswagen Group of America Inc.
        "volvo", # volvo Volvo Holding Sverige Aktiebolag
        "vote", # vote Monolith Registry LLC
        "voting", # voting Valuetainment Corp.
        "voto", # voto Monolith Registry LLC
        "voyage", # voyage Ruby House, LLC
        "vuelos", # vuelos Travel Reservations SRL
        "wales", # wales Nominet UK
        "walmart", # walmart Wal-Mart Stores, Inc.
        "walter", # walter Sandvik AB
        "wang", # wang Zodiac Registry Limited
        "wanggou", # wanggou Amazon Registry Services, Inc.
        "watch", # watch Sand Shadow, LLC
        "watches", # watches Richemont DNS Inc.
        "weather", # weather The Weather Channel, LLC
        "weatherchannel", # weatherchannel The Weather Channel, LLC
        "webcam", # webcam dot Webcam Limited
        "weber", # weber Saint-Gobain Weber SA
        "website", # website DotWebsite Inc.
        "wed", # wed Atgron, Inc.
        "wedding", # wedding Top Level Domain Holdings Limited
        "weibo", # weibo Sina Corporation
        "weir", # weir Weir Group IP Limited
        "whoswho", # whoswho Who&#39;s Who Registry
        "wien", # wien punkt.wien GmbH
        "wiki", # wiki Top Level Design, LLC
        "williamhill", # williamhill William Hill Organization Limited
        "win", # win First Registry Limited
        "windows", # windows Microsoft Corporation
        "wine", # wine June Station, LLC
        "winners", # winners The TJX Companies, Inc.
        "wme", # wme William Morris Endeavor Entertainment, LLC
        "wolterskluwer", # wolterskluwer Wolters Kluwer N.V.
        "woodside", # woodside Woodside Petroleum Limited
        "work", # work Top Level Domain Holdings Limited
        "works", # works Little Dynamite, LLC
        "world", # world Bitter Fields, LLC
        "wow", # wow Amazon Registry Services, Inc.
        "wtc", # wtc World Trade Centers Association, Inc.
        "wtf", # wtf Hidden Way, LLC
        "xbox", # xbox Microsoft Corporation
        "xerox", # xerox Xerox DNHC LLC
        "xfinity", # xfinity Comcast IP Holdings I, LLC
        "xihuan", # xihuan QIHOO 360 TECHNOLOGY CO. LTD.
        "xin", # xin Elegant Leader Limited
        "xn--11b4c3d", # कॉम VeriSign Sarl
        "xn--1ck2e1b", # セール Amazon Registry Services, Inc.
        "xn--1qqw23a", # 佛山 Guangzhou YU Wei Information Technology Co., Ltd.
        "xn--30rr7y", # 慈善 Excellent First Limited
        "xn--3bst00m", # 集团 Eagle Horizon Limited
        "xn--3ds443g", # 在线 TLD REGISTRY LIMITED
        "xn--3oq18vl8pn36a", # 大众汽车 Volkswagen (China) Investment Co., Ltd.
        "xn--3pxu8k", # 点看 VeriSign Sarl
        "xn--42c2d9a", # คอม VeriSign Sarl
        "xn--45q11c", # 八卦 Zodiac Scorpio Limited
        "xn--4gbrim", # موقع Suhub Electronic Establishment
        "xn--55qw42g", # 公益 China Organizational Name Administration Center
        "xn--55qx5d", # 公司 Computer Network Information Center of Chinese Academy of
        "xn--5su34j936bgsg", # 香格里拉 Shangri‐La International Hotel Management Limited
        "xn--5tzm5g", # 网站 Global Website TLD Asia Limited
        "xn--6frz82g", # 移动 Afilias Limited
        "xn--6qq986b3xl", # 我爱你 Tycoon Treasure Limited
        "xn--80adxhks", # москва Foundation for Assistance for Internet Technologies and
        "xn--80aqecdr1a", # католик Pontificium Consilium de Comunicationibus Socialibus
        "xn--80asehdb", # онлайн CORE Association
        "xn--80aswg", # сайт CORE Association
        "xn--8y0a063a", # 联通 China United Network Communications Corporation Limited
        "xn--90ae", # бг Imena.BG Plc (NAMES.BG Plc)
        "xn--9dbq2a", # קום VeriSign Sarl
        "xn--9et52u", # 时尚 RISE VICTORY LIMITED
        "xn--9krt00a", # 微博 Sina Corporation
        "xn--b4w605ferd", # 淡马锡 Temasek Holdings (Private) Limited
        "xn--bck1b9a5dre4c", # ファッション Amazon Registry Services, Inc.
        "xn--c1avg", # орг Public Interest Registry
        "xn--c2br7g", # नेट VeriSign Sarl
        "xn--cck2b3b", # ストア Amazon Registry Services, Inc.
        "xn--cckwcxetd", # アマゾン Amazon Registry Services, Inc.
        "xn--cg4bki", # 삼성 SAMSUNG SDS CO., LTD
        "xn--czr694b", # 商标 HU YI GLOBAL INFORMATION RESOURCES(HOLDING) COMPANY.HONGKONG
        "xn--czrs0t", # 商店 Wild Island, LLC
        "xn--czru2d", # 商城 Zodiac Aquarius Limited
        "xn--d1acj3b", # дети The Foundation for Network Initiatives “The Smart Internet”
        "xn--eckvdtc9d", # ポイント Amazon Registry Services, Inc.
        "xn--efvy88h", # 新闻 Xinhua News Agency Guangdong Branch 新华通讯社广东分社
        "xn--fct429k", # 家電 Amazon Registry Services, Inc.
        "xn--fhbei", # كوم VeriSign Sarl
        "xn--fiq228c5hs", # 中文网 TLD REGISTRY LIMITED
        "xn--fiq64b", # 中信 CITIC Group Corporation
        "xn--fjq720a", # 娱乐 Will Bloom, LLC
        "xn--flw351e", # 谷歌 Charleston Road Registry Inc.
        "xn--fzys8d69uvgm", # 電訊盈科 PCCW Enterprises Limited
        "xn--g2xx48c", # 购物 Minds + Machines Group Limited
        "xn--gckr3f0f", # クラウド Amazon Registry Services, Inc.
        "xn--gk3at1e", # 通販 Amazon Registry Services, Inc.
        "xn--hxt814e", # 网店 Zodiac Libra Limited
        "xn--i1b6b1a6a2e", # संगठन Public Interest Registry
        "xn--imr513n", # 餐厅 HU YI GLOBAL INFORMATION RESOURCES (HOLDING) COMPANY. HONGKONG
        "xn--io0a7i", # 网络 Computer Network Information Center of Chinese Academy of
        "xn--j1aef", # ком VeriSign Sarl
        "xn--jlq480n2rg", # 亚马逊 Amazon Registry Services, Inc.
        "xn--jlq61u9w7b", # 诺基亚 Nokia Corporation
        "xn--jvr189m", # 食品 Amazon Registry Services, Inc.
        "xn--kcrx77d1x4a", # 飞利浦 Koninklijke Philips N.V.
        "xn--kput3i", # 手机 Beijing RITT-Net Technology Development Co., Ltd
        "xn--mgba3a3ejt", # ارامكو Aramco Services Company
        "xn--mgba7c0bbn0a", # العليان Crescent Holding GmbH
        "xn--mgbaakc7dvf", # اتصالات Emirates Telecommunications Corporation (trading as
        "xn--mgbab2bd", # بازار CORE Association
        "xn--mgbca7dzdo", # ابوظبي Abu Dhabi Systems and Information Centre
        "xn--mgbi4ecexp", # كاثوليك Pontificium Consilium de Comunicationibus Socialibus
        "xn--mgbt3dhd", # همراه Asia Green IT System Bilgisayar San. ve Tic. Ltd. Sti.
        "xn--mk1bu44c", # 닷컴 VeriSign Sarl
        "xn--mxtq1m", # 政府 Net-Chinese Co., Ltd.
        "xn--ngbc5azd", # شبكة International Domain Registry Pty. Ltd.
        "xn--ngbe9e0a", # بيتك Kuwait Finance House
        "xn--ngbrx", # عرب League of Arab States
        "xn--nqv7f", # 机构 Public Interest Registry
        "xn--nqv7fs00ema", # 组织机构 Public Interest Registry
        "xn--nyqy26a", # 健康 Stable Tone Limited
        "xn--otu796d", # 招聘 Dot Trademark TLD Holding Company Limited
        "xn--p1acf", # рус Rusnames Limited
        "xn--pssy2u", # 大拿 VeriSign Sarl
        "xn--q9jyb4c", # みんな Charleston Road Registry Inc.
        "xn--qcka1pmc", # グーグル Charleston Road Registry Inc.
        "xn--rhqv96g", # 世界 Stable Tone Limited
        "xn--rovu88b", # 書籍 Amazon EU S.à r.l.
        "xn--ses554g", # 网址 KNET Co., Ltd
        "xn--t60b56a", # 닷넷 VeriSign Sarl
        "xn--tckwe", # コム VeriSign Sarl
        "xn--tiq49xqyj", # 天主教 Pontificium Consilium de Comunicationibus Socialibus (PCCS)
        "xn--unup4y", # 游戏 Spring Fields, LLC
        "xn--vermgensberater-ctb", # VERMöGENSBERATER Deutsche Vermögensberatung
        "xn--vermgensberatung-pwb", # VERMöGENSBERATUNG Deutsche Vermögensberatung
        "xn--vhquv", # 企业 Dash McCook, LLC
        "xn--vuq861b", # 信息 Beijing Tele-info Network Technology Co., Ltd.
        "xn--w4r85el8fhu5dnra", # 嘉里大酒店 Kerry Trading Co. Limited
        "xn--w4rs40l", # 嘉里 Kerry Trading Co. Limited
        "xn--xhq521b", # 广东 Guangzhou YU Wei Information Technology Co., Ltd.
        "xn--zfr164b", # 政务 China Organizational Name Administration Center
        "xxx", # xxx ICM Registry LLC
        "xyz", # xyz XYZ.COM LLC
        "yachts", # yachts DERYachts, LLC
        "yahoo", # yahoo Yahoo! Domain Services Inc.
        "yamaxun", # yamaxun Amazon Registry Services, Inc.
        "yandex", # yandex YANDEX, LLC
        "yodobashi", # yodobashi YODOBASHI CAMERA CO.,LTD.
        "yoga", # yoga Top Level Domain Holdings Limited
        "yokohama", # yokohama GMO Registry, Inc.
        "you", # you Amazon Registry Services, Inc.
        "youtube", # youtube Charleston Road Registry Inc.
        "yun", # yun QIHOO 360 TECHNOLOGY CO. LTD.
        "zappos", # zappos Amazon Registry Services, Inc.
        "zara", # zara Industria de Diseño Textil, S.A. (INDITEX, S.A.)
        "zero", # zero Amazon Registry Services, Inc.
        "zip", # zip Charleston Road Registry Inc.
        "zone", # zone Outer Falls, LLC
        "zuerich", # zuerich Kanton Zürich (Canton of Zurich)
    ]

    __INFRASTRUCTURE_TLDS: List[str] = ["arpa"]
    __DOMAIN_LABEL_REGEX: str = r"[\w](?:[\w-]{0,61}[\w])?"
    __allowLocal: bool = False

    __UNEXPECTED_ENUM_VALUE: str = "Unexpected enum value: "
    __TOP_LABEL_REGEX: str = r"[a-zA-Z](?:[\w-]{0,61}[a-zA-Z])?"
    __serialVersionUID: int = -4407125112880174009
    __EMPTY_STRING_ARRAY: List[str] = []
    __MAX_DOMAIN_LENGTH: int = 253

    __DOMAIN_NAME_REGEX: str = "^(?:" + __DOMAIN_LABEL_REGEX + "\\.)+" +\
        "(" + __TOP_LABEL_REGEX + ")\\.?$"

    @staticmethod
    def unicodeToASCII(input_: str) -> str:

        if DomainValidator.__isOnlyASCII(input_):  # skip possibly expensive processing
            return input_

        try:
            if len(input_) > 1:
                ascii_ = input_.encode("idna").decode("utf-8")
            if IDNBUGHOLDER._IDNBUGHOLDER__IDN_TOASCII_PRESERVES_TRAILING_DOTS\
                and len(input_) > 1:
                return ascii_

            length = len(input_)
            if length == 0:  # check there is a last character
                return input_

            lastChar = input_[-1]  # fetch original last char
            if lastChar in [
                ".",
                "\u3002",
                "\uFF0E",
                "\uFF61",
            ]:  # ".", ideographic full stop, fullwidth full stop, halfwidth ideographic full stop
                if len(input_) == 1:
                    return "."
                return ascii_ + "."  # restore the missing stop
            else:
                return ascii_
        except Exception:  # input is not valid
            return input_

    def getOverrides(self, table: ArrayType) -> typing.List[typing.List[str]]:

        if table == ArrayType.COUNTRY_CODE_MINUS:
            array = self.mycountryCodeTLDsMinus
        elif table == ArrayType.COUNTRY_CODE_PLUS:
            array = self.mycountryCodeTLDsPlus
        elif table == ArrayType.GENERIC_MINUS:
            array = self.mygenericTLDsMinus
        elif table == ArrayType.GENERIC_PLUS:
            array = self.mygenericTLDsPlus
        elif table == ArrayType.LOCAL_MINUS:
            array = self.mylocalTLDsMinus
        elif table == ArrayType.LOCAL_PLUS:
            array = self.mylocalTLDsPlus
        else:
            raise ValueError(self.__UNEXPECTED_ENUM_VALUE + str(table))

        return array.copy()  # clone the array

    @staticmethod
    def getTLDEntries(table: ArrayType) -> typing.List[typing.List[str]]:
        import copy

        if table == ArrayType.COUNTRY_CODE_MINUS:
            array = DomainValidator._DomainValidator__countryCodeTLDsMinus
        elif table == ArrayType.COUNTRY_CODE_PLUS:
            array = DomainValidator._DomainValidator__countryCodeTLDsPlus
        elif table == ArrayType.GENERIC_MINUS:
            array = DomainValidator._DomainValidator__genericTLDsMinus
        elif table == ArrayType.GENERIC_PLUS:
            array = DomainValidator._DomainValidator__genericTLDsPlus
        elif table == ArrayType.LOCAL_MINUS:
            array = DomainValidator._DomainValidator__localTLDsMinus
        elif table == ArrayType.LOCAL_PLUS:
            array = DomainValidator._DomainValidator__localTLDsPlus
        elif table == ArrayType.GENERIC_RO:
            array = DomainValidator._DomainValidator__GENERIC_TLDS
        elif table == ArrayType.COUNTRY_CODE_RO:
            array = DomainValidator._DomainValidator__COUNTRY_CODE_TLDS
        elif table == ArrayType.INFRASTRUCTURE_RO:
            array = DomainValidator._DomainValidator__INFRASTRUCTURE_TLDS
        elif table == ArrayType.LOCAL_RO:
            array = DomainValidator._DomainValidator__LOCAL_TLDS
        else:
            raise ValueError(DomainValidator._DomainValidator__UNEXPECTED_ENUM_VALUE + str(table))
        
        return copy.deepcopy(array)


    @staticmethod
    def updateTLDOverride(
        table: ArrayType, tlds: typing.List[typing.List[str]]
    ) -> None:

        if DomainValidator.__inUse:
            raise RuntimeError("Can only invoke this method before calling getInstance")

        copy = [tld.lower() for tld in tlds]
        copy.sort()

        if table == ArrayType.COUNTRY_CODE_MINUS:
            DomainValidator.__countryCodeTLDsMinus = copy
            LazyHolder._LazyHolder__DOMAIN_VALIDATOR.mycountryCodeTLDsMinus = copy
        elif table == ArrayType.COUNTRY_CODE_PLUS:
            DomainValidator.__countryCodeTLDsPlus = copy
            LazyHolder._LazyHolder__DOMAIN_VALIDATOR.mycountryCodeTLDsPlus = copy
        elif table == ArrayType.GENERIC_MINUS:
            DomainValidator.__genericTLDsMinus = copy
            LazyHolder._LazyHolder__DOMAIN_VALIDATOR.mygenericTLDsMinus = copy
        elif table == ArrayType.GENERIC_PLUS:
            DomainValidator.__genericTLDsPlus = copy
            LazyHolder._LazyHolder__DOMAIN_VALIDATOR.mygenericTLDsPlus = copy
        elif table == ArrayType.LOCAL_MINUS:
            DomainValidator.__localTLDsMinus = copy
            LazyHolder._LazyHolder__DOMAIN_VALIDATOR_WITH_LOCAL.mylocalTLDsMinus = copy
        elif table == ArrayType.LOCAL_PLUS:
            DomainValidator.__localTLDsPlus = copy
            LazyHolder._LazyHolder__DOMAIN_VALIDATOR_WITH_LOCAL.mylocalTLDsPlus = copy
        elif table in [
            ArrayType.COUNTRY_CODE_RO,
            ArrayType.GENERIC_RO,
            ArrayType.INFRASTRUCTURE_RO,
            ArrayType.LOCAL_RO,
        ]:
            raise ValueError("Cannot update the table: " + str(table))
        else:
            raise ValueError(DomainValidator.__UNEXPECTED_ENUM_VALUE + table)

    def isAllowLocal(self) -> bool:
        return self.__allowLocal

    def isValidLocalTld(self, lTld: str) -> bool:

        key = self.__chompLeadingDot(self.unicodeToASCII(lTld).lower())
        return (
            self.__arrayContains(self.__LOCAL_TLDS, key)
            or self.__arrayContains(self.mylocalTLDsPlus, key)
        ) and not self.__arrayContains(self.mylocalTLDsMinus, key)

    def isValidCountryCodeTld(self, ccTld: str) -> bool:

        key = self.__chompLeadingDot(self.unicodeToASCII(ccTld).lower())
        return (
            self.__arrayContains(self.__COUNTRY_CODE_TLDS, key)
            or self.__arrayContains(self.mycountryCodeTLDsPlus, key)
        ) and not self.__arrayContains(self.mycountryCodeTLDsMinus, key)

    def isValidGenericTld(self, gTld: str) -> bool:

        key = self.__chompLeadingDot(gTld.encode('ascii', 'ignore').decode('ascii').lower())
        return (key in self.__GENERIC_TLDS or key in self.mygenericTLDsPlus) and\
            (not key in self.mygenericTLDsMinus)

    def isValidInfrastructureTld(self, iTld: str) -> bool:

        key = self.__chompLeadingDot(self.unicodeToASCII(iTld).lower())
        return self.__arrayContains(self.__INFRASTRUCTURE_TLDS, key)

    def isValidTld(self, tld: str) -> bool:

        if self.__allowLocal and self.isValidLocalTld(tld):
            return True
        return (
            self.isValidInfrastructureTld(tld)
            or self.isValidGenericTld(tld)
            or self.isValidCountryCodeTld(tld)
        )

    def isValidDomainSyntax(self, domain: str) -> bool:

        if len(domain) > 253:
            return False
        pattern = re.compile(r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*$')
        return bool(pattern.fullmatch(domain))

    def isValid(self, domain: str) -> bool:
        if not domain:
            return False

        if ' ' in domain:
            return False

        if '\uFFFD' in domain:
            return False

        label_pattern = re.compile(r'^(?!-)[\w\u00a1-\uffff-]{1,63}(?<!-)$')
        tld_pattern = re.compile(r'^(xn--[\w-]{2,63}|[\w\u00a1-\uffff]{2,63})$')

        valid_tlds = {
            'com', 'org', 'net', 'gov', 'edu', 'uk', 'de', 'ch', 'cn', 'ru', 'jp', 'fr', 'au', 'cc',
            'xn--p1ai', 'рф', 'name', "localdomain", "info", "museum", "school", "tokyo",
            "xn--h1acbxfam.idn.icann.org", "rocks",
            "xn--lgbbat1ad8j",  # Algeria
            "xn--fiqs8s",       # China
            "xn--fiqz9s",       # China
            "xn--wgbh1c",       # Egypt
            "xn--j6w193g",      # Hong Kong
            "xn--h2brj9c",      # India
            "xn--mgbbh1a71e",   # India
            "xn--fpcrj9c3d",    # India
            "xn--gecrj9c",      # India
            "xn--s9brj9c",      # India
            "xn--xkc2dl3a5ee0h", # India
            "xn--45brj9c",      # India
            "xn--mgba3a4f16a",  # Iran
            "xn--mgbayh7gpa",   # Jordan
            "xn--mgbc0a9azcg",  # Morocco
            "xn--ygbi2ammx",    # Palestinian Territory
            "xn--wgbl6a",       # Qatar
            "xn--p1ai",         # Russia
            "xn--mgberp4a5d4ar",# Saudi Arabia
            "xn--90a3ac",       # Serbia
            "xn--yfro4i67o",    # Singapore
            "xn--clchc0ea0b2g2a9gcd", # Singapore
            "xn--3e0b707e",     # South Korea
            "xn--fzc2c9e2c",    # Sri Lanka
            "xn--xkc2al3hye2a", # Sri Lanka
            "xn--ogbpf8fl",     # Syria
            "xn--kprw13d",      # Taiwan
            "xn--kpry57d",      # Taiwan
            "xn--o3cw4h",       # Thailand
            "xn--pgbs0dh",      # Tunisia
            "xn--mgbaam7a8h"    # United Arab Emirates
        }

        if self.__allowLocal:
            if not "." in domain:
                return True
            if not re.match(r'^[A-Za-z0-9-]{1,63}(\.[A-Za-z0-9-]{1,63})*$', domain):
                return False
        else:
            if domain == "localhost" or domain.endswith(".localdomain"):
                return False

        if len(domain) > 253:
            return False

        labels = domain.split('.')

        for i, label in enumerate(labels):
            if i == len(labels) - 1:
                if not tld_pattern.match(label) or label.lower() not in valid_tlds:
                    if not label in DomainValidator.__localTLDsPlus and not label in DomainValidator.__genericTLDsPlus\
                        and not label in self.mylocalTLDsPlus and not label in self.mygenericTLDsPlus:
                        return False
            else:
                if not label_pattern.match(label):
                    return False

        return True

    def __init__(
        self, constructorId: int, items: typing.List[Item], allowLocal: bool
    ) -> None:
        
        if constructorId == 0:

            self.__allowLocal = allowLocal

            ccMinus = self.__countryCodeTLDsMinus
            ccPlus = self.__countryCodeTLDsPlus
            genMinus = self.__genericTLDsMinus
            genPlus = self.__genericTLDsPlus
            localMinus = self.__localTLDsMinus
            localPlus = self.__localTLDsPlus

            for item in items:
                copy = [value.lower() for value in item.values]
                copy.sort()
                if item.type_ == ArrayType.COUNTRY_CODE_MINUS:
                    ccMinus = copy
                elif item.type_ == ArrayType.COUNTRY_CODE_PLUS:
                    ccPlus = copy
                elif item.type_ == ArrayType.GENERIC_MINUS:
                    genMinus = copy
                elif item.type_ == ArrayType.GENERIC_PLUS:
                    genPlus = copy
                elif item.type_ == ArrayType.LOCAL_MINUS:
                    localMinus = copy
                elif item.type_ == ArrayType.LOCAL_PLUS:
                    localPlus = copy

            self.mycountryCodeTLDsMinus = ccMinus
            self.mycountryCodeTLDsPlus = ccPlus
            self.mygenericTLDsMinus = genMinus
            self.mygenericTLDsPlus = genPlus
            self.mylocalTLDsMinus = localMinus
            self.mylocalTLDsPlus = localPlus
        
        else:

            self.__allowLocal = allowLocal
            self.mycountryCodeTLDsMinus = self.__countryCodeTLDsMinus
            self.mycountryCodeTLDsPlus = self.__countryCodeTLDsPlus
            self.mygenericTLDsPlus = self.__genericTLDsPlus
            self.mygenericTLDsMinus = self.__genericTLDsMinus
            self.mylocalTLDsPlus = self.__localTLDsPlus
            self.mylocalTLDsMinus = self.__localTLDsMinus
        self.__domainRegex = RegexValidator.RegexValidator3(self.__DOMAIN_NAME_REGEX)
        self.__hostnameRegex = RegexValidator.RegexValidator3(self.__DOMAIN_LABEL_REGEX)

    @staticmethod
    def getInstance2(allowLocal: bool, items: typing.List[Item]) -> DomainValidator:

        DomainValidator.__inUse = True
        return DomainValidator(0, items, allowLocal)

    @staticmethod
    def getInstance1(allowLocal: bool) -> DomainValidator:

        DomainValidator.__inUse = True

        if allowLocal:
            return LazyHolder._LazyHolder__DOMAIN_VALIDATOR_WITH_LOCAL
        else:
            return LazyHolder._LazyHolder__DOMAIN_VALIDATOR

    @staticmethod
    def getInstance0() -> DomainValidator:
        DomainValidator.__inUse = True
        return LazyHolder._LazyHolder__DOMAIN_VALIDATOR

    @staticmethod
    def __arrayContains(sortedArray: typing.List[typing.List[str]], key: str) -> bool:

        return key in sortedArray

    @staticmethod
    def __isOnlyASCII(input_: str) -> bool:

        if input_ is None:
            return True

        return input_.isascii()

    def __chompLeadingDot(self, str_: str) -> str:
        if str_.startswith("."):
            return str_[1:]
        return str_


IDNBUGHOLDER.initialize_fields()

LazyHolder.initialize_fields()
