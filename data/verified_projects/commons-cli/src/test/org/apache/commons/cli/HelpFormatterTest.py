import pytest

# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.HelpFormatter import *
import unittest
import os
import io
# Imports End

class HelpFormatterTest(unittest.TestCase):

    # Class Fields Begin
    __EOL: str = os.linesep
    # Class Fields End

    # Class Methods Begin
    @pytest.mark.test
    def testAccessors(self) -> None:
        formatter = HelpFormatter()

        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")

        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")

        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")

        formatter.setLongOptPrefix("~~")
        self.assertEqual("~~", formatter.getLongOptPrefix(), "long opt prefix")

        formatter.setNewLine("\n")
        self.assertEqual("\n", formatter.getNewLine(), "new line")

        formatter.setOptPrefix("~")
        self.assertEqual("~", formatter.getOptPrefix(), "opt prefix")

        formatter.setSyntaxPrefix("-> ")
        self.assertEqual("-> ", formatter.getSyntaxPrefix(), "syntax prefix")

        formatter.setWidth(80)
        self.assertEqual(80, formatter.getWidth(), "width")


    @pytest.mark.test
    def testAutomaticUsage(self) -> None: 
        hf = HelpFormatter()
        options = None
        out = io.BytesIO()
        pw = io.TextIOWrapper(out, write_through=True)

        expected = "usage: app [-a]"
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        hf.printUsage1(pw, 60, "app", options)
        pw.flush()
        result = out.getvalue().strip().decode()
        self.assertEqual(expected, result, "simple auto usage")
        out.seek(0)
        out.truncate(0)

        expected = "usage: app [-a] [-b]"
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")\
                           .addOption1("b", False, "bbb")
        hf.printUsage1(pw, 60, "app", options)
        pw.flush()
        result = out.getvalue().strip().decode()
        self.assertEqual(expected, result, "simple auto usage")
        out.seek(0)
        out.truncate(0)


    @pytest.mark.test
    def testDefaultArgName(self) -> None:
        option = Option.builder1("f").hasArg0().required1(True).build()

        options = Options()
        options.addOption0(option)

        out = io.StringIO()

        formatter = HelpFormatter()
        formatter.setArgName("argument")
        formatter.printUsage1(out, 80, "app", options)

        expected = "usage: app -f <argument>" + HelpFormatterTest.__EOL
        result = out.getvalue()

        self.assertEqual(expected, result)

    
    @pytest.mark.test
    def testFindWrapPos(self) -> None:
        hf = HelpFormatter()

        text = "This is a test."
        self.assertEqual(7, hf.findWrapPos(text, 8, 0), "wrap position")

        self.assertEqual(-1, hf.findWrapPos(text, 8, 8), "wrap position 2")

        text = "aaaa aa"
        self.assertEqual(3, hf.findWrapPos(text, 3, 0), "wrap position 3")

        text = "aaaaaa aaaaaa"
        self.assertEqual(6, hf.findWrapPos(text, 6, 0), "wrap position 4")
        self.assertEqual(-1, hf.findWrapPos(text, 6, 7), "wrap position 4")

        text = "aaaaaa\n aaaaaa"
        self.assertEqual(7, hf.findWrapPos(text, 6, 0), "wrap position 5")
        text = "aaaaaa\t aaaaaa"
        self.assertEqual(7, hf.findWrapPos(text, 6, 0), "wrap position 6")

    
    @pytest.mark.test
    def testHeaderStartingWithLineSeparator(self) -> None:
        options = Options()
        formatter = HelpFormatter()
        header = HelpFormatterTest.__EOL + "Header"
        footer = "Footer"
        out = io.StringIO()
        formatter.printHelp3(out, 80, "foobar", header, options, 2, 2, footer, True)
        self.assertEqual(
                "usage: foobar" + \
                        HelpFormatterTest.__EOL + \
                        "" + \
                        HelpFormatterTest.__EOL + \
                        "Header" + \
                        HelpFormatterTest.__EOL + \
                        "" + \
                        HelpFormatterTest.__EOL + \
                        "Footer" + \
                        HelpFormatterTest.__EOL,
                out.getvalue())
        
    
    @pytest.mark.test
    def testHelpWithLongOptSeparator(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        options.addOption0(Option.builder1("s")\
                                 .longOpt("size")\
                                 .desc("the size")\
                                 .hasArg0()\
                                 .argName("SIZE")\
                                 .build()
        )
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build())

        formatter = HelpFormatter()
        self.assertEqual(HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator())
        formatter.setLongOptSeparator("=")
        self.assertEqual("=", formatter.getLongOptSeparator())
        out = io.StringIO()
        formatter.printHelp2(out, 80, "create", "header", options, 2, 2, "footer")
        self.assertEqual(
                "usage: create" + \
                HelpFormatterTest.__EOL + \
                "header" + \
                HelpFormatterTest.__EOL + \
                "     --age=<arg>    the age" + \
                HelpFormatterTest.__EOL + \
                "  -f <arg>          the file" + \
                HelpFormatterTest.__EOL + \
                "  -s,--size=<SIZE>  the size" + \
                HelpFormatterTest.__EOL + \
                "footer" + \
                HelpFormatterTest.__EOL,
                out.getvalue()
        )

    
    @pytest.mark.test
    def testIndentedHeaderAndFooter(self) -> None:
        options = Options()
        formatter = HelpFormatter()
        header = "  Header1\n  Header2"
        footer = "  Footer1\n  Footer2"
        out = io.StringIO()
        formatter.printHelp3(
                out, 80, "foobar", header, options, 2, 2, footer, True)
        self.assertEqual(
                "usage: foobar" + \
                HelpFormatterTest.__EOL + \
                "  Header1" + \
                HelpFormatterTest.__EOL + \
                "  Header2" + \
                HelpFormatterTest.__EOL + \
                "" + \
                HelpFormatterTest.__EOL + \
                "  Footer1" + \
                HelpFormatterTest.__EOL + \
                "  Footer2" + \
                HelpFormatterTest.__EOL,
                out.getvalue()
        )

    
    @pytest.mark.test
    def testOptionWithoutShortFormat(self) -> None:
        options = Options()
        options.addOption0(Option(0, "a", "aaa", "aaaaaaa", False, None))
        options.addOption0(Option(0, None, "bbb", "bbbbbbb", False, None))
        options.addOption0(Option(0, "c", None, "ccccccc", False, None))

        formatter = HelpFormatter()
        out = io.StringIO()
        formatter.printHelp3(out, 80, "foobar", "", options, 2, 2, "", True)
        self.assertEqual(
                "usage: foobar [-a] [--bbb] [-c]" + \
                HelpFormatterTest.__EOL + \
                "  -a,--aaa  aaaaaaa" + \
                HelpFormatterTest.__EOL + \
                "     --bbb  bbbbbbb" + \
                HelpFormatterTest.__EOL + \
                "  -c        ccccccc" + \
                HelpFormatterTest.__EOL,
                out.getvalue()
        )

    
    @pytest.mark.test
    def testOptionWithoutShortFormat2(self) -> None:
        help = Option(0, "h", "help", "print this message", False, None)
        version = Option(0, "v", "version", "print version information", False, None)
        newRun = Option(0, "n", "new", "Create NLT cache entries only for new items", False, None)
        trackerRun = Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        False,
                        None
        )

        timeLimit = Option.builder1("l")\
                          .longOpt("limit")\
                          .hasArg0()\
                          .valueSeparator0()\
                          .desc("Set time limit for execution, in mintues")\
                          .build()

        age = Option.builder1("a")\
                    .longOpt("age")\
                    .hasArg0()\
                    .valueSeparator0()\
                    .desc("Age (in days) of cache item before being recomputed")\
                    .build()

        server = Option.builder1("s")\
                       .longOpt("server")\
                       .hasArg0()\
                       .valueSeparator0()\
                       .desc("The NLT server address")\
                       .build()

        numResults = Option.builder1("r")\
                           .longOpt("results")\
                           .hasArg0()\
                           .valueSeparator0()\
                           .desc("Number of results per item")\
                           .build()

        configFile = Option.builder0()\
                           .longOpt("config")\
                           .hasArg0()\
                           .valueSeparator0()\
                           .desc("Use the specified configuration file")\
                           .build()

        mOptions = Options()
        mOptions.addOption0(help)
        mOptions.addOption0(version)
        mOptions.addOption0(newRun)
        mOptions.addOption0(trackerRun)
        mOptions.addOption0(timeLimit)
        mOptions.addOption0(age)
        mOptions.addOption0(server)
        mOptions.addOption0(numResults)
        mOptions.addOption0(configFile)

        formatter = HelpFormatter()
        eol = HelpFormatterTest.__EOL
        out = io.StringIO()
        formatter.printHelp3(out, 80, "commandline", "header", mOptions, 2, 2, "footer", True)
        self.assertEqual(
                "usage: commandline [-a <arg>] [--config <arg>] [-h] [-l <arg>] [-n] [-r <arg>]" + \
                eol + \
                "       [-s <arg>] [-t] [-v]" + \
                eol + \
                "header" + \
                eol + \
                "  -a,--age <arg>      Age (in days) of cache item before being" + \
                " recomputed" + \
                eol + \
                "     --config <arg>   Use the specified configuration file" + \
                eol + \
                "  -h,--help           print this message" + \
                eol + \
                "  -l,--limit <arg>    Set time limit for execution, in mintues" + \
                eol + \
                "  -n,--new            Create NLT cache entries only for new items" + \
                eol + \
                "  -r,--results <arg>  Number of results per item" + \
                eol + \
                "  -s,--server <arg>   The NLT server address" + \
                eol + \
                "  -t,--tracker        Create NLT cache entries only for tracker items" + \
                eol + \
                "  -v,--version        print version information" + \
                eol + \
                "footer" + \
                eol,
                out.getvalue())

    
    @pytest.mark.test
    def testPrintHelpNewlineFooter(self) -> None:
        formatter = HelpFormatter()
        out = io.BytesIO()
        pw = io.TextIOWrapper(out, write_through=True)
        options = Options()
        options.addOption2("a", "b")
        formatter.printHelp2(pw, 80, "test" + HelpFormatterTest.__EOL, "header" + HelpFormatterTest.__EOL, options, 0, 0, HelpFormatterTest.__EOL)
        expected = "usage: test" + HelpFormatterTest.__EOL + "header" + HelpFormatterTest.__EOL + "-ab" + HelpFormatterTest.__EOL + HelpFormatterTest.__EOL
        pw.flush()
        result = out.getvalue().decode()
        self.assertEqual(expected, result, "footer newline")

    
    @pytest.mark.test
    def testPrintHelpNewlineHeader(self) -> None:
        formatter = HelpFormatter()
        out = io.BytesIO()
        pw = io.TextIOWrapper(out, write_through=True)
        options = Options()
        options.addOption2("a", "b")
        formatter.printHelp2(pw, 80, "test" + HelpFormatterTest.__EOL, HelpFormatterTest.__EOL, options, 0, 0, "footer" + HelpFormatterTest.__EOL)
        expected = "usage: test" + HelpFormatterTest.__EOL + HelpFormatterTest.__EOL + "-ab" + HelpFormatterTest.__EOL + "footer" + HelpFormatterTest.__EOL
        pw.flush()
        result = out.getvalue().decode()
        self.assertEqual(expected, result, "header newline")

    
    @pytest.mark.test
    def testPrintHelpWithEmptySyntax(self) -> None:
        formatter = HelpFormatter()
        try:
                formatter.printHelp4(None, Options())
                self.fail("null command line syntax should be rejected")
        except ValueError:
                pass
        try:
                formatter.printHelp4("", Options())
                self.fail("empty command line syntax should be rejected")
        except ValueError:
                pass

    
    @pytest.mark.test
    def testPrintOptionGroupUsage(self) -> None:
        group = OptionGroup()
        group.addOption(Option.builder1("a").build())
        group.addOption(Option.builder1("b").build())
        group.addOption(Option.builder1("c").build())

        options = Options()
        options.addOptionGroup(group)

        out = io.StringIO()

        formatter = HelpFormatter()
        formatter.printUsage1(out, 80, "app", options)
        
        self.assertEqual("usage: app [-a | -b | -c]" + HelpFormatterTest.__EOL, out.getvalue())

    
    @pytest.mark.test
    def testPrintOptions(self) -> None:
        sb = ""
        hf = HelpFormatter()
        leftPad = 1
        descPad = 3
        lpad = hf.createPadding(leftPad)
        dpad = hf.createPadding(descPad)
        options = None
        expected = None


        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
        hf.renderOptions(sb, 60, options, leftPad, descPad)
        self.assertEqual(expected, str(sb), "simple non-wrapped option")

        nextLineTabStop = leftPad + descPad + len("-a")
        expected = (
                lpad + \
                "-a" + \
                dpad + \
                "aaaa aaaa aaaa" + \
                HelpFormatterTest.__EOL + \
                hf.createPadding(nextLineTabStop) + \
                "aaaa aaaa"
        )
        sb = ""
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad)
        self.assertEqual(expected, str(sb), "simple wrapped option")

        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd"
        sb = ""
        hf.renderOptions(sb, 60, options, leftPad, descPad)
        self.assertEqual(expected, str(sb), "long non-wrapped option")

        nextLineTabStop = leftPad + descPad + len("-a,--aaa")
        expected = (
                lpad + \
                "-a,--aaa" + \
                dpad + \
                "dddd dddd" + \
                HelpFormatterTest.__EOL + \
                hf.createPadding(nextLineTabStop) + \
                "dddd dddd"
        )
        sb = ""
        hf.renderOptions(sb, 25, options, leftPad, descPad)
        self.assertEqual(expected, str(sb), "long wrapped option")

        options = (
                Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")\
                         .addOption1("b", False, "feeee eeee eeee eeee")
        )
        expected = (
                lpad + \
                "-a,--aaa" + \
                dpad + \
                "dddd dddd" + \
                HelpFormatterTest.__EOL + \
                hf.createPadding(nextLineTabStop) + \
                + "dddd dddd" + \
                HelpFormatterTest.__EOL + \
                lpad + \
                "-b      " + \
                dpad + \
                "feeee eeee" + \
                HelpFormatterTest.__EOL + \
                hf.createPadding(nextLineTabStop) + \
                "eeee eeee"
        )
        sb = ""
        hf.renderOptions(sb, 25, options, leftPad, descPad)
        self.assertEqual(expected, str(sb), "multiple wrapped options")

    
    @pytest.mark.test
    def testPrintOptionWithEmptyArgNameUsage(self) -> None:
        option = Option.Option2("f", True, None)
        option.setArgName("")
        option.setRequired(True)

        options = Options()
        options.addOption0(option)

        out = io.StringIO()

        formatter = HelpFormatter()
        formatter.printUsage1(out, 80, "app", options)

        self.assertEqual("usage: app -f" + HelpFormatterTest.__EOL, out.getvalue())

    
    @pytest.mark.test
    def testPrintRequiredOptionGroupUsage(self) -> None:
        group = OptionGroup()
        group.addOption(Option.builder1("a").build())
        group.addOption(Option.builder1("b").build())
        group.addOption(Option.builder1("c").build())
        group.setRequired(True)

        options = Options()
        options.addOptionGroup(group)

        out = io.StringIO()

        formatter = HelpFormatter()
        formatter.printUsage1(out, 80, "app", options)

        self.assertEqual("usage: app -a | -b | -c" + HelpFormatterTest.__EOL, out.getvalue())


    @pytest.mark.test
    def testPrintSortedUsage(self) -> None:
        opts = Options()
        opts.addOption0(Option.Option1("a", "first"))
        opts.addOption0(Option.Option1("b", "second"))
        opts.addOption0(Option.Option1("c", "third"))

        helpFormatter = HelpFormatter()
        helpFormatter.setOptionComparator(
                lambda opt1, opt2: (opt2.getKey().lower() > opt1.getKey().lower()) - \
                        (opt1.getKey().lower() < opt1.getKey().lower())
        )
        out = io.StringIO()
        helpFormatter.printUsage1(out, 80, "app", opts)

        self.assertEqual("usage: app [-c] [-b] [-a]" + HelpFormatterTest.__EOL, out.getvalue())

    
    @pytest.mark.test
    def testPrintSortedUsageWithNullComparator(self) -> None:
        opts = Options()
        opts.addOption0(Option.Option1("c", "first"))
        opts.addOption0(Option.Option1("b", "second"))
        opts.addOption0(Option.Option1("a", "third"))

        helpFormatter = HelpFormatter()
        helpFormatter.setOptionComparator(None)

        out = io.StringIO()
        helpFormatter.printUsage1(out, 80, "app", opts)
        self.assertEqual("usage: app [-c] [-b] [-a]" + HelpFormatterTest.__EOL, out.getvalue())


    @pytest.mark.test
    def testPrintUsage(self) -> None:
        optionA = Option.Option1("a", "first")
        optionB = Option.Option1("b", "second")
        optionC = Option.Option1("c", "third")
        opts = Options()
        opts.addOption0(optionA)
        opts.addOption0(optionB)
        opts.addOption0(optionC)
        bytesOut = io.BytesIO()
        printWriter = io.TextIOWrapper(bytesOut, write_through=True)
        helpFormatter = HelpFormatter()
        try: 
                helpFormatter.printUsage1(printWriter, 80, "app", opts)
        except Exception as e:
                self.fail(f"An exception occurred: {e}")
        printWriter.flush()
        result = bytesOut.getvalue().decode()
        self.assertEqual("usage: app [-a] [-b] [-c]" + HelpFormatterTest.__EOL, result)


    @pytest.mark.test
    def testRenderWrappedTextMultiLine(self) -> None:
        width = 16
        padding = 0
        expected = "aaaa aaaa aaaa" + \
                   HelpFormatterTest.__EOL + \
                   "aaaaaa" + \
                   HelpFormatterTest.__EOL + \
                   "aaaaa"
        
        sb = ""
        hf = HelpFormatter()
        hf.renderWrappedText(sb, width, padding, expected)
        self.assertEqual(expected, str(sb), "multi line text")


    @pytest.mark.test
    def testRenderWrappedTextMultiLinePadded(self) -> None:
        width = 16
        padding = 4
        text = "aaaa aaaa aaaa" + \
               HelpFormatterTest.__EOL + \
               "aaaaaa" + \
               HelpFormatterTest.__EOL + \
               "aaaaa"
        expected = "aaaa aaaa aaaa" + \
                   HelpFormatterTest.__EOL + \
                   "    aaaaaa" + \
                   HelpFormatterTest.__EOL + \
                   "    aaaaa"
        
        sb = ""
        hf = HelpFormatter()
        hf.renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, str(sb), "multi-line padded text")


    @pytest.mark.test
    def testRenderWrappedTextSingleLine(self) -> None:
        width = 12
        padding = 0
        text = "This is a test."
        expected = "This is a" + HelpFormatterTest.__EOL + "test."
        
        sb = ""
        hf = HelpFormatter()
        hf.renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, str(sb), "single line text")


    @pytest.mark.test
    def testRenderWrappedTextSingleLinePadded(self) -> None:
        width = 12
        padding = 4
        text = "This is a test."
        expected = "This is a" + HelpFormatterTest.__EOL + "    test."

        sb = ""
        hf = HelpFormatter()
        hf.renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, str(sb), "single line padded text")


    @pytest.mark.test
    def testRenderWrappedTextSingleLinePadded2(self) -> None:
        width = 53
        padding = 24
        text = "  -p,--period <PERIOD>  PERIOD is time duration of form " + \
               "DATE[-DATE] where DATE has form YYYY[MM[DD]]"
        expected = "  -p,--period <PERIOD>  PERIOD is time duration of" + \
                   HelpFormatterTest.__EOL + \
                   "                        form DATE[-DATE] where DATE" + \
                   HelpFormatterTest.__EOL + \
                   "                        has form YYYY[MM[DD]]"
        
        sb = ""
        hf = HelpFormatter()
        hf.renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, str(sb), "single line padded text 2")


    @pytest.mark.test
    def testRenderWrappedTextWordCut(self) -> None:
        width = 7
        padding = 0
        text = "Thisisatest."
        expected = "Thisisa" + HelpFormatterTest.__EOL + "test."

        sb = ""
        hf = HelpFormatter()
        hf.renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, str(sb), "cut and wrap")
    
    
    @pytest.mark.test
    def testRtrim(self) -> None:
        formatter = HelpFormatter()

        self.assertIsNone(formatter.rtrim(None))
        self.assertEqual("", formatter.rtrim(""))
        self.assertEqual("  foo", formatter.rtrim("  foo  "))
    
    
    @pytest.mark.test
    def testUsageWithLongOptSeparator(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        options.addOption0(
                Option.builder1("s")\
                      .longOpt("size")\
                      .desc("the size")\
                      .hasArg0()\
                      .argName("SIZE")\
                      .build()
        )
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build())

        formatter = HelpFormatter()
        formatter.setLongOptSeparator("=")

        out = io.StringIO()

        formatter.printUsage1(out, 80, "create", options)
        self.assertEqual("usage: create [--age=<arg>] [-f <arg>] [-s <SIZE>]", out.getvalue().strip())

    # Class Methods End
