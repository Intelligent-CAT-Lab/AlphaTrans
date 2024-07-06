from __future__ import annotations
import copy
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.digest.MurmurHash3 import *


class MurmurHash3Test(unittest.TestCase):

    __RANDOM_BYTES: typing.List[int] = None

    __RANDOM_INTS: typing.List[int] = [
        46,
        246,
        249,
        184,
        247,
        84,
        99,
        144,
        62,
        77,
        195,
        220,
        92,
        20,
        150,
        159,
        38,
        40,
        124,
        252,
        185,
        28,
        63,
        13,
        213,
        172,
        85,
        198,
        118,
        74,
        109,
        157,
        132,
        216,
        76,
        177,
        173,
        23,
        140,
        86,
        146,
        95,
        54,
        176,
        114,
        179,
        234,
        174,
        183,
        141,
        122,
        12,
        60,
        116,
        200,
        142,
        6,
        167,
        59,
        240,
        33,
        29,
        165,
        111,
        243,
        30,
        219,
        110,
        255,
        53,
        32,
        35,
        64,
        225,
        96,
        152,
        70,
        41,
        133,
        80,
        244,
        127,
        57,
        199,
        5,
        164,
        151,
        49,
        26,
        180,
        203,
        83,
        108,
        39,
        126,
        208,
        42,
        206,
        178,
        19,
        69,
        223,
        71,
        231,
        250,
        125,
        211,
        232,
        189,
        55,
        44,
        82,
        48,
        221,
        43,
        192,
        241,
        103,
        155,
        27,
        51,
        163,
        21,
        169,
        91,
        94,
        217,
        191,
        78,
        72,
        93,
        102,
        104,
        105,
        8,
        113,
        100,
        143,
        89,
        245,
        227,
        120,
        160,
        251,
        153,
        145,
        45,
        218,
        168,
        233,
        229,
        253,
        67,
        22,
        182,
        98,
        137,
        128,
        135,
        11,
        214,
        66,
        73,
        171,
        188,
        170,
        131,
        207,
        79,
        106,
        24,
        75,
        237,
        194,
        7,
        129,
        215,
        81,
        248,
        242,
        16,
        25,
        136,
        147,
        156,
        97,
        52,
        10,
        181,
        17,
        205,
        58,
        101,
        68,
        230,
        1,
        37,
        0,
        222,
        88,
        130,
        148,
        224,
        47,
        50,
        197,
        34,
        212,
        196,
        209,
        14,
        36,
        139,
        228,
        154,
        31,
        175,
        202,
        236,
        161,
        3,
        162,
        190,
        254,
        134,
        119,
        4,
        61,
        65,
        117,
        186,
        107,
        204,
        9,
        187,
        201,
        90,
        149,
        226,
        56,
        239,
        238,
        235,
        112,
        87,
        18,
        121,
        115,
        138,
        123,
        210,
        2,
        193,
        166,
        158,
        15,
    ]
    __TEST_HASH64: str = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
    )

    @staticmethod
    def run_static_init():
        MurmurHash3Test.__RANDOM_BYTES = [0] * len(MurmurHash3Test.__RANDOM_INTS)
        for i in range(len(MurmurHash3Test.__RANDOM_BYTES)):
            MurmurHash3Test.__RANDOM_BYTES[i] = MurmurHash3Test.__RANDOM_INTS[i] & 0xFF

    def testIncrementalHashWithUnprocessedBytesAndHugeLengthArray(self) -> None:

        pass  # LLM could not translate this method

    def testIncrementalHash32x86(self) -> None:
        bytes = [0] * 1023
        ThreadLocalRandom.current().nextBytes(bytes)
        for seed in [-567, 0, 6787990]:
            self.__assertIncrementalHash32x86(bytes, seed, [0, 0])
            self.__assertIncrementalHash32x86(bytes, seed, [1, 1, 1, 1, 1, 1, 1, 1])
            self.__assertIncrementalHash32x86(bytes, seed, [1, 4])
            self.__assertIncrementalHash32x86(bytes, seed, [2, 4])
            self.__assertIncrementalHash32x86(bytes, seed, [3, 4])
            self.__assertIncrementalHash32x86(bytes, seed, [4, 1])
            self.__assertIncrementalHash32x86(bytes, seed, [4, 2])
            self.__assertIncrementalHash32x86(bytes, seed, [4, 3])
            self.__assertIncrementalHash32x86(bytes, seed, [4, 16, 64])
            for i in range(10):
                self.__assertIncrementalHash32x86(
                    bytes, seed, self.__createRandomBlocks(len(bytes))
                )

    def testIncrementalHash32(self) -> None:
        bytes = [0] * 1023
        ThreadLocalRandom.current().nextBytes(bytes)
        for seed in [-567, 0, 6787990]:
            self.__assertIncrementalHash32(bytes, seed, [0, 0])
            self.__assertIncrementalHash32(bytes, seed, [1, 1, 1, 1, 1, 1, 1, 1])
            self.__assertIncrementalHash32(bytes, seed, [1, 4])
            self.__assertIncrementalHash32(bytes, seed, [2, 4])
            self.__assertIncrementalHash32(bytes, seed, [3, 4])
            self.__assertIncrementalHash32(bytes, seed, [4, 1])
            self.__assertIncrementalHash32(bytes, seed, [4, 2])
            self.__assertIncrementalHash32(bytes, seed, [4, 3])
            self.__assertIncrementalHash32(bytes, seed, [4, 16, 64])
            for i in range(10):
                self.__assertIncrementalHash32x86(
                    bytes, seed, self.__createRandomBlocks(len(bytes))
                )

    def testHash128x64WithOffsetLengthAndNegativeSeed(self) -> None:
        seed: int = -42
        offset: int = 13

        answers: typing.List[typing.List[int]] = [
            [7182599573337898253, -6490979146667806054],
            [-461284136738605467, 7073284964362976233],
            [-3090354666589400212, 2978755180788824810],
            [5052807367580803906, -4497188744879598335],
            [5003711854877353474, -6616808651483337088],
            [2043501804923817748, -760668448196918637],
            [6813003268375229932, -1818545210475363684],
            [4488070015393027916, 8520186429078977003],
            [4709278711722456062, -2262080641289046033],
            [-5944514262756048380, 5968714500873552518],
            [-2304397529301122510, 6451500469518446488],
            [-1054078041081348909, -915114408909600132],
            [1300471646869277217, -399493387666437046],
            [-2821780479886030222, -9061571187511294733],
            [8005764841242557505, 4135287855434326053],
            [318307346637037498, -5355856739901286522],
            [3380719536119187025, 1890890833937151467],
            [2691044185935730001, 7963546423617895734],
            [-5277462388534000227, 3613853764390780573],
            [8504421722476165699, 2058020162708103700],
            [-6578421288092422241, 3311200163790829579],
            [-5915037218487974215, -7385137075895184179],
            [659642911937398022, 854071824595671049],
            [-7007237968866727198, 1372258010932080058],
            [622891376282772539, -4140783491297489868],
            [8357110718969014985, -4737117827581590306],
            [2208857857926305405, -8360240839768465042],
            [858120048221036376, -5822288789703639119],
            [-1988334009458340679, 1262479472434068698],
            [-8580307083590783934, 3634449965473715778],
            [6705664584730187559, 5192304951463791556],
            [-6426410954037604142, -1579122709247558101],
        ]
        for i in range(len(answers)):
            self.assertListEqual(
                "Length: " + str(i),
                answers[i],
                MurmurHash3.hash128x64(self.__RANDOM_BYTES, offset, i, seed),
            )

    def testHash128x64WithOffsetLengthAndSeed(self) -> None:
        seed: int = 42
        offset: int = 13
        answers: typing.List[typing.List[int]] = [
            [-1140915396076141277, -3386313222241793095],
            [2745805417334040752, -3045882272665292331],
            [6807939080212835946, -1975749467247671127],
            [-7924884987449335214, -4468571497642087939],
            [3005389733967167773, -5809440073240597398],
            [8032745196600164727, 4545709434702374224],
            [2095398623732573832, 1778447136435513908],
            [4492723708121417255, -7411125500882394867],
            [8467397417110552178, -1503802302645548949],
            [4189760269121918355, -8004336343217265057],
            [4939298084211301953, -8419135013628844658],
            [5497136916151148085, -394028342910298191],
            [3405983294878231737, -3216533807498089078],
            [5833223403351466775, -1792451370239813325],
            [7730583391236194819, 5356157313842354092],
            [3111977482488580945, -3119414725698132191],
            [3314524606404365027, -1923219843083192742],
            [7299569240140613949, 4176392429810027494],
            [6398084683727166117, 7703960505857395788],
            [-8594572031068184774, 4394224719145783692],
            [-7589785442804461713, 4110439243215224554],
            [-5343610105946840628, -4423992782020122809],
            [-522490326525787270, 289136460641968781],
            [-5320637070354802556, -7845553044730489027],
            [1344456408744313334, 3803048032054968586],
            [1131205296221907191, -6256656049039287019],
            [8583339267101027117, 8934225022848628726],
            [-6379552869905441749, 8973517768420051734],
            [5076646564516328801, 8561479196844000567],
            [-4610341636137642517, -6694266039505142069],
            [-758896383254029789, 4050360662271552727],
            [-6123628195475753507, 4283875822581966645],
        ]
        for i in range(len(answers)):
            self.assertListEqual(
                answers[i],
                MurmurHash3.hash128x641(
                    MurmurHash3Test.__RANDOM_BYTES, offset, i, seed
                ),
            )

    def testHash128x64(self) -> None:
        self.assertListEqual(
            [1972113670104592209, 5171809317673151911],
            MurmurHash3.hash128x640(self.__RANDOM_BYTES),
        )
        answers: typing.List[typing.List[int]] = [
            [0, 0],
            [-2808653841080383123, -2531784594030660343],
            [-1284575471001240306, -8226941173794461820],
            [1645529003294647142, 4109127559758330427],
            [-4117979116203940765, -8362902660322042742],
            [2559943399590596158, 4738005461125350075],
            [-1651760031591552651, -5386079254924224461],
            [-6208043960690815609, 7862371518025305074],
            [-5150023478423646337, 8346305334874564507],
            [7658274117911906792, -4962914659382404165],
            [1309458104226302269, 570003296096149119],
            [7440169453173347487, -3489345781066813740],
            [-5698784298612201352, 3595618450161835420],
            [-3822574792738072442, 6878153771369862041],
            [3705084673301918328, 3202155281274291907],
            [-6797166743928506931, -4447271093653551597],
            [5240533565589385084, -5575481185288758327],
            [-8467620131382649428, -6450630367251114468],
            [3632866961828686471, -5957695976089313500],
            [-6450283648077271139, -7908632714374518059],
            [226350826556351719, 8225586794606475685],
            [-2382996224496980401, 2188369078123678011],
            [-1337544762358780825, 7004253486151757299],
            [2889033453638709716, -4099509333153901374],
            [-8644950936809596954, -5144522919639618331],
            [-5628571865255520773, -839021001655132087],
            [-5226774667293212446, -505255961194269502],
            [1337107025517938142, 3260952073019398505],
            [9149852874328582511, 1880188360994521535],
            [-4035957988359881846, -7709057850766490780],
            [-3842593823306330815, 3805147088291453755],
            [4030161393619149616, -2813603781312455238],
        ]
        for i in range(len(answers)):
            bytes: typing.List[int] = self.__RANDOM_BYTES[0:i]
            self.assertListEqual(answers[i], MurmurHash3.hash128x640(bytes))

    def testHash128String(self) -> None:
        seed: int = 104729
        minSize: int = 1
        maxSize: int = 11
        codePoints: int = 112956
        chars: typing.List[int] = [0] * ((maxSize - minSize) * 2)
        for i in range(1000):
            pos: int = 0
            size: int = ThreadLocalRandom.current().nextInt(minSize, maxSize)
            for j in range(size):
                codePoint: int = ThreadLocalRandom.current().nextInt(codePoints)
                pos += Character.toChars(codePoint, chars, pos)
            text: str = String.copyValueOf(chars, 0, pos)
            bytes: typing.List[int] = StringUtils.getBytesUtf8(text)
            h1: typing.List[int] = MurmurHash3.hash1282(bytes, 0, len(bytes), seed)
            h2: typing.List[int] = MurmurHash3.hash1281(text)
            Assert.assertArrayEquals(h1, h2)

    def testHash128WithOffsetLengthAndNegativeSeed(self) -> None:
        seed: int = -42
        offset: int = 13
        answers: typing.List[typing.List[int]] = [
            [5954234972212089025, 3342108296337967352],
            [8501094764898402923, 7873951092908129427],
            [-3334322685492296196, -2842715922956549478],
            [-2177918982459519644, -1612349961980368636],
            [4172870320608886992, -4177375712254136503],
            [7546965006884307324, -5222114032564054641],
            [-2885083166621537267, -2069868899915344482],
            [-2397098497873118851, 4990578036999888806],
            [-706479374719025018, 7531201699171849870],
            [6487943141157228609, 3576221902299447884],
            [6671331646806999453, -3428049860825046360],
            [-8700221138601237020, -2748450904559980545],
            [-9028762509863648063, 6130259301750313402],
            [729958512305702590, -36367317333638988],
            [-3803232241584178983, -4257744207892929651],
            [5734013720237474696, -760784490666078990],
            [-6097477411153026656, 625288777006549065],
            [1320365359996757504, -2251971390373072541],
            [5551441703887653022, -3516892619809375941],
            [698875391638415033, 3456972931370496131],
            [5874956830271303805, -6074126509360777023],
            [-7030758398537734781, -3174643657101295554],
            [6835789852786226556, 7245353136839389595],
            [-7755767580598793204, -6680491060945077989],
            [-3099789923710523185, -2751080516924952518],
            [-7772046549951435453, 5263206145535830491],
            [7458715941971015543, 5470582752171544854],
            [-7753394773760064468, -2330157750295630617],
            [-5899278942232791979, 6235686401271389982],
            [4881732293467626532, 2617335658565007304],
            [-5722863941703478257, -5424475653939430258],
            [-3703319768293496315, -2124426428486426443],
        ]
        for i in range(len(answers)):
            self.assertListEqual(
                answers[i], MurmurHash3.hash1282(self.__RANDOM_BYTES, offset, i, seed)
            )

    def testHash128WithOffsetLengthAndSeed(self) -> None:
        seed: int = 42
        offset: int = 13
        answers: typing.List[typing.List[int]] = [
            [-1140915396076141277, -3386313222241793095],
            [2745805417334040752, -3045882272665292331],
            [6807939080212835946, -1975749467247671127],
            [-7924884987449335214, -4468571497642087939],
            [3005389733967167773, -5809440073240597398],
            [8032745196600164727, 4545709434702374224],
            [2095398623732573832, 1778447136435513908],
            [4492723708121417255, -7411125500882394867],
            [8467397417110552178, -1503802302645548949],
            [4189760269121918355, -8004336343217265057],
            [4939298084211301953, -8419135013628844658],
            [5497136916151148085, -394028342910298191],
            [3405983294878231737, -3216533807498089078],
            [5833223403351466775, -1792451370239813325],
            [7730583391236194819, 5356157313842354092],
            [3111977482488580945, -3119414725698132191],
            [3314524606404365027, -1923219843083192742],
            [7299569240140613949, 4176392429810027494],
            [6398084683727166117, 7703960505857395788],
            [-8594572031068184774, 4394224719145783692],
            [-7589785442804461713, 4110439243215224554],
            [-5343610105946840628, -4423992782020122809],
            [-522490326525787270, 289136460641968781],
            [-5320637070354802556, -7845553044730489027],
            [1344456408744313334, 3803048032054968586],
            [1131205296221907191, -6256656049039287019],
            [8583339267101027117, 8934225022848628726],
            [-6379552869905441749, 8973517768420051734],
            [5076646564516328801, 8561479196844000567],
            [-4610341636137642517, -6694266039505142069],
            [-758896383254029789, 4050360662271552727],
            [-6123628195475753507, 4283875822581966645],
        ]
        for i in range(len(answers)):
            self.assertListEqual(
                answers[i],
                MurmurHash3.hash1282(MurmurHash3Test.__RANDOM_BYTES, offset, i, seed),
            )

    def testHash128(self) -> None:

        pass  # LLM could not translate this method

    def testHash64InNotEqualToHash128(self) -> None:
        for i in range(32):
            bytes = self.__RANDOM_BYTES[:i]
            h1 = MurmurHash3.hash643(bytes)
            hash = MurmurHash3.hash1280(bytes)
            self.assertNotEqual(
                "Did not expect hash64 to match upper bits of hash128", hash[0], h1
            )
            self.assertNotEqual(
                "Did not expect hash64 to match lower bits of hash128", hash[1], h1
            )

    def testHash64WithPrimitives(self) -> None:

        pass  # LLM could not translate this method

    def testHash64WithOffsetAndLength(self) -> None:
        origin: typing.List[int] = StringUtils.getBytesUtf8(self.__TEST_HASH64)
        originOffset: typing.List[int] = [123] * (len(origin) + 150)
        originOffset[150 : 150 + len(origin)] = origin
        hash: int = MurmurHash3.hash644(originOffset, 150, len(origin))
        self.assertEqual(5785358552565094607, hash)

    def testHash64(self) -> None:
        origin: typing.List[int] = StringUtils.getBytesUtf8(self.__TEST_HASH64)
        hash: int = MurmurHash3.hash643(origin)
        self.assertEqual(5785358552565094607, hash)

    def testHash32x86WithTrailingNegativeSignedBytes(self) -> None:
        self.assertEqual(-43192051, MurmurHash3.hash32x861([0xFF], 0, 1, 0))
        self.assertEqual(-582037868, MurmurHash3.hash32x861([0x00, 0xFF], 0, 2, 0))
        self.assertEqual(922088087, MurmurHash3.hash32x861([0x00, 0x00, 0xFF], 0, 3, 0))
        self.assertEqual(-1309567588, MurmurHash3.hash32x861([0xFF, 0x00], 0, 2, 0))
        self.assertEqual(
            -363779670, MurmurHash3.hash32x861([0xFF, 0x00, 0x00], 0, 3, 0)
        )
        self.assertEqual(
            -225068062, MurmurHash3.hash32x861([0x00, 0xFF, 0x00], 0, 3, 0)
        )

    def testHash32x86WithOffsetLengthAndSeed(self) -> None:
        seed: int = -42
        offset: int = 13
        answers: typing.List[int] = [
            192929823,
            -27171978,
            -1282326280,
            -816314453,
            -1176217753,
            -1904531247,
            1962794233,
            -1302316624,
            -1151850323,
            -1464386748,
            -369299427,
            972232488,
            1747314487,
            2137398916,
            690986564,
            -1985866226,
            -678669121,
            -2123325690,
            -253319081,
            46181235,
            656058278,
            1401175653,
            1750113912,
            -1567219725,
            2032742772,
            -2024269989,
            -305340794,
            1161737942,
            -661265418,
            172838872,
            -650122718,
            -1934812417,
        ]
        for i in range(answers.__len__()):
            self.assertEqual(
                answers[i],
                MurmurHash3.hash32x861(MurmurHash3Test.__RANDOM_BYTES, offset, i, seed),
            )

    def testhash32x86(self) -> None:
        self.assertEqual(1546271276, MurmurHash3.hash32x860(self.__RANDOM_BYTES))

        answers = [
            0,
            -1353253853,
            915381745,
            -734983419,
            1271125654,
            -1042265893,
            -1204521619,
            735845843,
            138310876,
            -1918938664,
            1399647898,
            -1126342309,
            2067593280,
            1220975287,
            1941281084,
            -1289513180,
            942412060,
            -618173583,
            -269546647,
            -1645631262,
            1162379906,
            -1960125577,
            -1856773195,
            1980513522,
            1174612855,
            905810751,
            1044578220,
            -1758486689,
            -491393913,
            839836946,
            -435014415,
            2044851178,
        ]
        for i in range(len(answers)):
            bytes = self.__RANDOM_BYTES[:i]
            self.assertEqual(answers[i], MurmurHash3.hash32x860(bytes))

    def testHash32WithTrailingNegativeSignedBytesIsInvalid(self) -> None:
        self.assertNotEqual(-43192051, MurmurHash3.hash328([-1], 0, 1, 0))
        self.assertNotEqual(-582037868, MurmurHash3.hash328([0, -1], 0, 2, 0))
        self.assertNotEqual(922088087, MurmurHash3.hash328([0, 0, -1], 0, 3, 0))
        self.assertNotEqual(-1309567588, MurmurHash3.hash328([-1, 0], 0, 2, 0))
        self.assertNotEqual(-363779670, MurmurHash3.hash328([-1, 0, 0], 0, 3, 0))
        self.assertNotEqual(-225068062, MurmurHash3.hash328([0, -1, 0], 0, 3, 0))

    def testHash32String(self) -> None:
        seed: int = 104729
        minSize: int = 1
        maxSize: int = 11
        codePoints: int = 112956
        chars: typing.List[int] = [0] * ((maxSize - minSize) * 2)
        for i in range(1000):
            pos: int = 0
            size: int = ThreadLocalRandom.current().nextInt(minSize, maxSize)
            for j in range(size):
                codePoint: int = ThreadLocalRandom.current().nextInt(codePoints)
                pos += Character.toChars(codePoint, chars, pos)
            text: str = String.copyValueOf(chars, 0, pos)
            bytes: typing.List[int] = StringUtils.getBytesUtf8(text)
            h1: int = MurmurHash3.hash328(bytes, 0, len(bytes), seed)
            h2: int = MurmurHash3.hash325(text)
            Assert.assertEquals(h1, h2)

    def testHash32WithOffsetLengthAndSeed(self) -> None:
        seed: int = -42
        offset: int = 13
        answers: typing.List[int] = [
            192929823,
            -27171978,
            -1282326280,
            -816314453,
            -1176217753,
            -1904531247,
            1962794233,
            -1302316624,
            -1151850323,
            -1464386748,
            -369299427,
            972232488,
            1747314487,
            2137398916,
            690986564,
            -1985866226,
            -678669121,
            -2123325690,
            -253319081,
            46181235,
            656058278,
            1401175653,
            1750113912,
            -1567219725,
            2032742772,
            -2024269989,
            -305340794,
            1161737942,
            -661265418,
            172838872,
            -650122718,
            -1934812417,
        ]
        for i in range(answers.__len__()):
            if i % 4 == 0 or not self.__negativeBytes(
                self.__RANDOM_BYTES, offset + (i // 4) * 4, i % 4
            ):
                self.assertEqual(
                    answers[i],
                    MurmurHash3.hash328(self.__RANDOM_BYTES, offset, i, seed),
                )
            else:
                self.assertNotEqual(
                    answers[i],
                    MurmurHash3.hash328(self.__RANDOM_BYTES, offset, i, seed),
                )

    def testHash32WithLengthAndSeed(self) -> None:
        seed: int = -42
        self.assertEqual(
            1693958011,
            MurmurHash3.hash327(
                MurmurHash3Test.__RANDOM_BYTES,
                len(MurmurHash3Test.__RANDOM_BYTES),
                seed,
            ),
        )

        answers: typing.List[int] = [
            192929823,
            7537536,
            -99368911,
            -1261039957,
            -1719251056,
            -399594848,
            372285930,
            -80756529,
            1770924588,
            -1071759082,
            1832217706,
            1921413466,
            1701676113,
            675584253,
            1620634486,
            427719405,
            -973727623,
            533209078,
            136016960,
            1947798330,
            428635832,
            -1125743884,
            793211715,
            -2068889169,
            -136818786,
            -720841364,
            -891446378,
            1990860976,
            -710528065,
            -1602505694,
            -1493714677,
            1911121524,
        ]
        for i in range(len(answers)):
            if i % 4 == 0 or not MurmurHash3Test.__negativeBytes(
                MurmurHash3Test.__RANDOM_BYTES, (i // 4) * 4, i % 4
            ):
                self.assertEqual(
                    answers[i],
                    MurmurHash3.hash327(MurmurHash3Test.__RANDOM_BYTES, i, seed),
                )
            else:
                self.assertNotEqual(
                    answers[i],
                    MurmurHash3.hash327(MurmurHash3Test.__RANDOM_BYTES, i, seed),
                )

    def testHash32WithLength(self) -> None:
        self.assertEqual(
            1905657630,
            MurmurHash3.hash326(self.__RANDOM_BYTES, len(self.__RANDOM_BYTES)),
        )

        answers = [
            -965378730,
            418246248,
            1175981702,
            -616767012,
            -12304673,
            1697005142,
            -1212417875,
            -420043393,
            -826068069,
            -1721451528,
            -544986914,
            892942691,
            27535194,
            974863697,
            1835661694,
            -894915836,
            1826914566,
            -677571679,
            1218764493,
            -375719050,
            -1320048170,
            -503583763,
            1321750696,
            -175065786,
            -496878386,
            -12065683,
            512351473,
            716560510,
            -1944803590,
            10253199,
            1105638211,
            525704533,
        ]
        for i in range(len(answers)):
            if i % 4 == 0 or not self.__negativeBytes(
                self.__RANDOM_BYTES, (i // 4) * 4, i % 4
            ):
                self.assertEqual(
                    answers[i], MurmurHash3.hash326(self.__RANDOM_BYTES, i)
                )
            else:
                self.assertNotEqual(
                    answers[i], MurmurHash3.hash326(self.__RANDOM_BYTES, i)
                )

    def testHash32(self) -> None:
        self.assertEqual(1905657630, MurmurHash3.hash324(self.__RANDOM_BYTES))

        answers = [
            -965378730,
            418246248,
            1175981702,
            -616767012,
            -12304673,
            1697005142,
            -1212417875,
            -420043393,
            -826068069,
            -1721451528,
            -544986914,
            892942691,
            27535194,
            974863697,
            1835661694,
            -894915836,
            1826914566,
            -677571679,
            1218764493,
            -375719050,
            -1320048170,
            -503583763,
            1321750696,
            -175065786,
            -496878386,
            -12065683,
            512351473,
            716560510,
            -1944803590,
            10253199,
            1105638211,
            525704533,
        ]
        for i in range(len(answers)):
            bytes = self.__RANDOM_BYTES[:i]
            if i % 4 == 0 or not self.__negativeBytes(bytes, (i // 4) * 4, i % 4):
                self.assertEqual(answers[i], MurmurHash3.hash324(bytes))
            else:
                self.assertNotEqual(answers[i], MurmurHash3.hash324(bytes))

    def testHash32LongSeed(self) -> None:
        offset: int = 0
        seed: int = 104729

        length: int = MurmurHash3.LONG_BYTES
        buffer: ByteBuffer = ByteBuffer.allocate(length)
        bytes: typing.List[int] = buffer.array()
        data: typing.List[int] = self.__createLongTestData()
        for i in data:
            buffer.putLong(0, i)
            self.assertEqual(
                MurmurHash3.hash32x861(bytes, offset, length, seed),
                MurmurHash3.hash323(i, seed),
            )

    def testHash32Long(self) -> None:
        offset: int = 0
        seed: int = 104729

        length: int = MurmurHash3.LONG_BYTES
        buffer: ByteBuffer = ByteBuffer.allocate(length)
        bytes: typing.List[int] = buffer.array()
        data: typing.List[int] = self.__createLongTestData()
        for i in data:
            buffer.putLong(0, i)
            self.assertEqual(
                MurmurHash3.hash32x861(bytes, offset, length, seed),
                MurmurHash3.hash322(i),
            )

    def testHash32LongLongSeed(self) -> None:
        offset: int = 0
        seed: int = 104729

        length: int = MurmurHash3.LONG_BYTES * 2
        buffer: ByteBuffer = ByteBuffer.allocate(length)
        bytes: typing.List[int] = buffer.array()
        data: typing.List[int] = self.__createLongTestData()
        for i in data:
            for j in data:
                buffer.putLong(0, i)
                buffer.putLong(MurmurHash3.LONG_BYTES, j)
                self.assertEqual(
                    MurmurHash3.hash32x861(bytes, offset, length, seed),
                    MurmurHash3.hash321(i, j, seed),
                )

    def testHash32LongLong(self) -> None:
        offset: int = 0
        seed: int = 104729

        length: int = MurmurHash3.LONG_BYTES * 2
        buffer: ByteBuffer = ByteBuffer.allocate(length)
        bytes: typing.List[int] = buffer.array()
        data: typing.List[int] = self.__createLongTestData()
        for i in data:
            for j in data:
                buffer.putLong(0, i)
                buffer.putLong(MurmurHash3.LONG_BYTES, j)
                self.assertEqual(
                    MurmurHash3.hash32x861(bytes, offset, length, seed),
                    MurmurHash3.hash320(i, j),
                )

    @staticmethod
    def __createRandomBlocks(maxLength: int) -> typing.List[int]:
        blocks = [0] * 20
        count = 0
        length = 0
        while count < len(blocks) and length < maxLength:
            size = ThreadLocalRandom.current().nextInt(1, 9)
            blocks[count] = size
            count += 1
            length += size
        return blocks[:count]

    @staticmethod
    def __assertIncrementalHash32x86(
        bytes: typing.List[int], seed: int, blocks: typing.List[int]
    ) -> None:
        offset = 0
        total = 0
        inc = IncrementalHash32x86()
        inc.start(seed)
        for block in blocks:
            total += block
            h1 = MurmurHash3.hash32x861(bytes, 0, total, seed)
            inc.add(bytes, offset, block)
            offset += block
            h2 = inc.end()
            assert h1 == h2, "Hashes differ"
            assert h1 == inc.end(), "Hashes differ after no additional data"

    @staticmethod
    def __assertIncrementalHash32(
        bytes: typing.List[int], seed: int, blocks: typing.List[int]
    ) -> None:
        offset = 0
        total = 0
        inc = IncrementalHash32x86()
        inc.start(seed)
        for block in blocks:
            total += block
            h1 = MurmurHash3.hash328(bytes, 0, total, seed)
            inc.add(bytes, offset, block)
            offset += block
            h2 = inc.end()
            assert h1 == h2, "Hashes differ"
            assert h1 == inc.end(), "Hashes differ after no additional data"

    @staticmethod
    def __negativeBytes(bytes: typing.List[int], start: int, length: int) -> bool:

        pass  # LLM could not translate this method

    @staticmethod
    def __createLongTestData() -> typing.List[int]:
        data: typing.List[int] = [0] * 100
        data[0] = 0
        data[1] = -9223372036854775808
        data[2] = 9223372036854775807
        data[3] = -1
        for i in range(4, len(data)):
            data[i] = ThreadLocalRandom.current().nextLong()
        return data


MurmurHash3Test.run_static_init()
