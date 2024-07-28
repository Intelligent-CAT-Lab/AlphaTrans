from __future__ import annotations
import time
import re
import numbers
from io import BytesIO
from io import StringIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.HelpFormatter import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *


class HelpFormatterTest(unittest.TestCase):

    __EOL: str = os.linesep

    def testUsageWithLongOptSeparator(self) -> None:

        options = Options()
        options.addOption1("f", True, "the file")
        options.addOption0(
            Option.builder1("s")
            .longOpt("size")
            .desc("the size")
            .hasArg0()
            .argName("SIZE")
            .build()
        )
        options.addOption0(
            Option.builder0().longOpt("age").desc("the age").hasArg0().build()
        )

        formatter = HelpFormatter()
        formatter.setLongOptSeparator("=")

        out = io.StringIO()

        formatter.printUsage1(out, 80, "create", options)

        self.assertEqual(
            "usage: create [--age=<arg>] [-f <arg>] [-s <SIZE>]", out.getvalue().strip()
        )

    def testRtrim(self) -> None:

        formatter = HelpFormatter()

        self.assertIsNone(formatter._rtrim(None))
        self.assertEqual("", formatter._rtrim(""))
        self.assertEqual("  foo", formatter._rtrim("  foo  "))

    def testRenderWrappedTextWordCut(self) -> None:

        width = 7
        padding = 0
        text = "Thisisatest."
        expected = "Thisisa" + self.__EOL + "test."

        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, sb.getvalue(), "cut and wrap")

    def testRenderWrappedTextSingleLinePadded2(self) -> None:

        width: int = 53
        padding: int = 24
        text: str = (
            "  -p,--period <PERIOD>  PERIOD is time duration of form DATE[-DATE] where DATE has form YYYY[MM[DD]]"
        )
        expected: str = (
            "  -p,--period <PERIOD>  PERIOD is time duration of"
            + self.__EOL
            + "                        form DATE[-DATE] where DATE"
            + self.__EOL
            + "                        has form YYYY[MM[DD]]"
        )

        sb: StringIO = StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, sb.getvalue(), "single line padded text 2")

    def testRenderWrappedTextSingleLinePadded(self) -> None:

        width: int = 12
        padding: int = 4
        text: str = "This is a test."
        expected: str = "This is a" + self.__EOL + "    test."

        sb: StringIO = StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, sb.getvalue(), "single line padded text")

    def testRenderWrappedTextSingleLine(self) -> None:

        width: int = 12
        padding: int = 0
        text: str = "This is a test."
        expected: str = "This is a" + self.__EOL + "test."

        sb: StringIO = StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, sb.getvalue(), "single line text")

    def testRenderWrappedTextMultiLinePadded(self) -> None:

        width = 16
        padding = 4
        text = "aaaa aaaa aaaa" + self.__EOL + "aaaaaa" + self.__EOL + "aaaaa"
        expected = (
            "aaaa aaaa aaaa" + self.__EOL + "    aaaaaa" + self.__EOL + "    aaaaa"
        )

        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, sb.getvalue(), "multi-line padded text")

    def testRenderWrappedTextMultiLine(self) -> None:

        width: int = 16
        padding: int = 0
        expected: str = "aaaa aaaa aaaa" + self.__EOL + "aaaaaa" + self.__EOL + "aaaaa"

        sb: StringIO = StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, expected)
        self.assertEqual(expected, sb.getvalue(), "multi line text")

    def testPrintUsage(self) -> None:

        optionA = Option.Option1("a", "first")
        optionB = Option.Option1("b", "second")
        optionC = Option.Option1("c", "third")
        opts = Options()
        opts.addOption0(optionA)
        opts.addOption0(optionB)
        opts.addOption0(optionC)
        helpFormatter = HelpFormatter()
        out = StringIO()
        helpFormatter.printUsage1(out, 80, "app", opts)
        self.assertEqual(
            "usage: app [-a] [-b] [-c]" + self.__EOL, out.getvalue()
        )

    def testPrintSortedUsageWithNullComparator(self) -> None:

        opts = Options()
        opts.addOption0(Option.Option1("c", "first"))
        opts.addOption0(Option.Option1("b", "second"))
        opts.addOption0(Option.Option1("a", "third"))

        helpFormatter = HelpFormatter()
        helpFormatter.setOptionComparator(None)

        out = io.StringIO()
        helpFormatter.printUsage1(out, 80, "app", opts)

        self.assertEqual("usage: app [-c] [-b] [-a]" + self.__EOL, out.getvalue())

    def testPrintSortedUsage(self) -> None:

        opts = Options()
        opts.addOption0(Option.Option1("a", "first"))
        opts.addOption0(Option.Option1("b", "second"))
        opts.addOption0(Option.Option1("c", "third"))

        helpFormatter = HelpFormatter()
        def comparator(opt1: Option, opt2: Option) -> int:
            if opt1.getKey().casefold() > opt2.getKey().casefold():
                return -1
            if opt1.getKey().casefold() < opt2.getKey().casefold():
                return 1
            return 0
        helpFormatter.setOptionComparator(
            comparator
        )

        out = io.StringIO()
        helpFormatter.printUsage1(out, 80, "app", opts)

        self.assertEqual("usage: app [-c] [-b] [-a]" + self.__EOL, out.getvalue())

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

        self.assertEqual("usage: app -a | -b | -c" + os.linesep, out.getvalue())

    def testPrintOptionWithEmptyArgNameUsage(self) -> None:

        option = Option.Option2("f", True, None)
        option.setArgName("")
        option.setRequired(True)

        options = Options()
        options.addOption0(option)

        out = io.StringIO()

        formatter = HelpFormatter()
        formatter.printUsage1(out, 80, "app", options)

        self.assertEqual("usage: app -f" + self.__EOL, out.getvalue())

    def testPrintOptions(self) -> None:

        sb = StringIO()
        hf = HelpFormatter()
        leftPad = 1
        descPad = 3
        lpad = hf._createPadding(leftPad)
        dpad = hf._createPadding(descPad)
        EOL = os.linesep

        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, leftPad, descPad)
        assert sb.getvalue() == expected, "simple non-wrapped option"

        nextLineTabStop = leftPad + descPad + len("-a")
        expected = (
            lpad
            + "-a"
            + dpad
            + "aaaa aaaa aaaa"
            + EOL
            + hf._createPadding(nextLineTabStop)
            + "aaaa aaaa"
        )
        sb.seek(0)
        sb.truncate()
        hf._renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad)
        assert sb.getvalue() == expected, "simple wrapped option"

        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd"
        sb.seek(0)
        sb.truncate()
        hf._renderOptions(sb, 60, options, leftPad, descPad)
        assert sb.getvalue() == expected, "long non-wrapped option"

        nextLineTabStop = leftPad + descPad + len("-a,--aaa")
        expected = (
            lpad
            + "-a,--aaa"
            + dpad
            + "dddd dddd"
            + EOL
            + hf._createPadding(nextLineTabStop)
            + "dddd dddd"
        )
        sb.seek(0)
        sb.truncate()
        hf._renderOptions(sb, 25, options, leftPad, descPad)
        assert sb.getvalue() == expected, "long wrapped option"

        options = (
            Options()
            .addOption3("a", "aaa", False, "dddd dddd dddd dddd")
            .addOption1("b", False, "feeee eeee eeee eeee")
        )
        expected = (
            lpad
            + "-a,--aaa"
            + dpad
            + "dddd dddd"
            + EOL
            + hf._createPadding(nextLineTabStop)
            + "dddd dddd"
            + EOL
            + lpad
            + "-b      "
            + dpad
            + "feeee eeee"
            + EOL
            + hf._createPadding(nextLineTabStop)
            + "eeee eeee"
        )
        sb.seek(0)
        sb.truncate()
        hf._renderOptions(sb, 25, options, leftPad, descPad)
        assert sb.getvalue() == expected, "multiple wrapped options"

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

        self.assertEqual("usage: app [-a | -b | -c]" + self.__EOL, out.getvalue())

    def testPrintHelpWithEmptySyntax(self) -> None:

        formatter = HelpFormatter()
        options = Options()

        try:
            formatter.printHelp4(None, options)
            self.fail("null command line syntax should be rejected")
        except ValueError:
            pass

        try:
            formatter.printHelp4("", options)
            self.fail("empty command line syntax should be rejected")
        except ValueError:
            pass

    def testPrintHelpNewlineHeader(self) -> None:

        formatter = HelpFormatter()
        out = io.StringIO()

        options = Options()
        options.addOption2("a", "b")

        formatter.printHelp2(
            out,
            80,
            "test" + self.__EOL,
            self.__EOL,
            options,
            0,
            0,
            "footer" + self.__EOL,
        )
        expected = (
            "usage: test"
            + self.__EOL
            + self.__EOL
            + "-ab"
            + self.__EOL
            + "footer"
            + self.__EOL
        )
        out.flush()
        self.assertEqual(expected, out.getvalue(), "header newline")

    def testPrintHelpNewlineFooter(self) -> None:

        formatter = HelpFormatter()
        out = io.StringIO()

        options = Options()
        options.addOption2("a", "b")

        formatter.printHelp2(
            out,
            80,
            "test" + self.__EOL,
            "header" + self.__EOL,
            options,
            0,
            0,
            self.__EOL,
        )
        expected = (
            "usage: test"
            + self.__EOL
            + "header"
            + self.__EOL
            + "-ab"
            + self.__EOL
            + self.__EOL
        )
        out.flush()
        self.assertEqual(expected, out.getvalue(), "footer newline")

    def testOptionWithoutShortFormat2(self) -> None:

        help = Option(0, "h", "help", "print this message", False, None)
        version = Option(0, "v", "version", "print version information", False, None)
        newRun = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        trackerRun = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        timeLimit = (
            Option.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in mintues")
            .build()
        )

        age = (
            Option.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        server = (
            Option.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        numResults = (
            Option.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        configFile = (
            Option.builder0()
            .longOpt("config")
            .hasArg0()
            .valueSeparator0()
            .desc("Use the specified configuration file")
            .build()
        )

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
        eol = os.linesep
        out = io.StringIO()
        formatter.printHelp3(
            out, 80, "commandline", "header", mOptions, 2, 2, "footer", True
        )
        self.assertEqual(
            "usage: commandline [-a <arg>] [--config <arg>] [-h] [-l <arg>] [-n] [-r <arg>]"
            + eol
            + "       [-s <arg>] [-t] [-v]"
            + eol
            + "header"
            + eol
            + "  -a,--age <arg>      Age (in days) of cache item before being"
            + " recomputed"
            + eol
            + "     --config <arg>   Use the specified configuration file"
            + eol
            + "  -h,--help           print this message"
            + eol
            + "  -l,--limit <arg>    Set time limit for execution, in mintues"
            + eol
            + "  -n,--new            Create NLT cache entries only for new items"
            + eol
            + "  -r,--results <arg>  Number of results per item"
            + eol
            + "  -s,--server <arg>   The NLT server address"
            + eol
            + "  -t,--tracker        Create NLT cache entries only for tracker items"
            + eol
            + "  -v,--version        print version information"
            + eol
            + "footer"
            + eol,
            out.getvalue(),
        )

    def testOptionWithoutShortFormat(self) -> None:

        options = Options()
        options.addOption0(Option(0, "a", "aaa", "aaaaaaa", False, None))
        options.addOption0(Option(0, None, "bbb", "bbbbbbb", False, None))
        options.addOption0(Option(0, "c", None, "ccccccc", False, None))

        formatter = HelpFormatter()
        out = io.StringIO()
        formatter.printHelp3(
            out, 80, "foobar", "", options, 2, 2, "", True
        )

        self.assertEqual(
            "usage: foobar [-a] [--bbb] [-c]"
            + self.__EOL
            + "  -a,--aaa  aaaaaaa"
            + self.__EOL
            + "     --bbb  bbbbbbb"
            + self.__EOL
            + "  -c        ccccccc"
            + self.__EOL,
            out.getvalue(),
        )

    def testIndentedHeaderAndFooter(self) -> None:

        options = Options()
        formatter = HelpFormatter()
        header = "  Header1\n  Header2"
        footer = "  Footer1\n  Footer2"
        out = io.StringIO()
        formatter.printHelp3(
            out, 80, "foobar", header, options, 2, 2, footer, True
        )
        self.assertEqual(
            "usage: foobar"
            + self.__EOL
            + "  Header1"
            + self.__EOL
            + "  Header2"
            + self.__EOL
            + ""
            + self.__EOL
            + "  Footer1"
            + self.__EOL
            + "  Footer2"
            + self.__EOL,
            out.getvalue(),
        )

    def testHelpWithLongOptSeparator(self) -> None:

        options = Options()
        options.addOption1("f", True, "the file")
        options.addOption0(
            Option.builder1("s")
            .longOpt("size")
            .desc("the size")
            .hasArg0()
            .argName("SIZE")
            .build()
        )
        options.addOption0(
            Option.builder0().longOpt("age").desc("the age").hasArg0().build()
        )

        formatter = HelpFormatter()
        self.assertEqual(
            HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator()
        )
        formatter.setLongOptSeparator("=")
        self.assertEqual("=", formatter.getLongOptSeparator())

        out = io.StringIO()

        formatter.printHelp2(
            out, 80, "create", "header", options, 2, 2, "footer"
        )

        exp = ("usage: create"
            + self.__EOL
            + "header"
            + self.__EOL
            + "     --age=<arg>    the age"
            + self.__EOL
            + "  -f <arg>          the file"
            + self.__EOL
            + "  -s,--size=<SIZE>  the size"
            + self.__EOL
            + "footer"
            + self.__EOL)
        print(repr(out.getvalue()))
        print(repr(exp))
        self.assertEqual(
            exp,
            out.getvalue(),
        )

    def testHeaderStartingWithLineSeparator(self) -> None:

        options = Options()
        formatter = HelpFormatter()
        header = self.__EOL + "Header"
        footer = "Footer"
        out = io.StringIO()
        formatter.printHelp3(
            out, 80, "foobar", header, options, 2, 2, footer, True
        )
        self.assertEqual(
            "usage: foobar"
            + self.__EOL
            + ""
            + self.__EOL
            + "Header"
            + self.__EOL
            + ""
            + self.__EOL
            + "Footer"
            + self.__EOL,
            out.getvalue(),
        )

    def testFindWrapPos(self) -> None:

        hf = HelpFormatter()

        text = "This is a test."
        self.assertEqual(7, hf._findWrapPos(text, 8, 0), "wrap position")

        self.assertEqual(-1, hf._findWrapPos(text, 8, 8), "wrap position 2")

        text = "aaaa aa"
        self.assertEqual(3, hf._findWrapPos(text, 3, 0), "wrap position 3")

        text = "aaaaaa aaaaaa"
        self.assertEqual(6, hf._findWrapPos(text, 6, 0), "wrap position 4")
        self.assertEqual(-1, hf._findWrapPos(text, 6, 7), "wrap position 4")

        text = "aaaaaa\n aaaaaa"
        self.assertEqual(7, hf._findWrapPos(text, 6, 0), "wrap position 5")

        text = "aaaaaa\t aaaaaa"
        self.assertEqual(7, hf._findWrapPos(text, 6, 0), "wrap position 6")

    def testDefaultArgName(self) -> None:

        option = Option.builder1("f").hasArg0().required1(True).build()

        options = Options()
        options.addOption0(option)

        out = io.StringIO()

        formatter = HelpFormatter()
        formatter.setArgName("argument")
        formatter.printUsage1(out, 80, "app", options)

        self.assertEqual("usage: app -f <argument>" + self.__EOL, out.getvalue())

    def testAutomaticUsage(self) -> None:

        hf = HelpFormatter()
        options = Options()
        expected = "usage: app [-a]"
        out = io.StringIO()

        options.addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        hf.printUsage1(out, 60, "app", options)
        out.flush()
        self.assertEqual(expected, out.getvalue().strip(), "simple auto usage")
        out.seek(0)
        out.truncate()

        expected = "usage: app [-a] [-b]"
        options = (
            Options()
            .addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
            .addOption1("b", False, "bbb")
        )
        hf.printUsage1(out, 60, "app", options)
        out.flush()
        self.assertEqual(expected, out.getvalue().strip(), "simple auto usage")
        out.seek(0)
        out.truncate()

    def testAccessors(self) -> None:

        formatter = HelpFormatter()

        formatter.setArgName("argname")
        assert "argname" == formatter.getArgName(), "arg name"

        formatter.setDescPadding(3)
        assert 3 == formatter.getDescPadding(), "desc padding"

        formatter.setLeftPadding(7)
        assert 7 == formatter.getLeftPadding(), "left padding"

        formatter.setLongOptPrefix("~~")
        assert "~~" == formatter.getLongOptPrefix(), "long opt prefix"

        formatter.setNewLine("\n")
        assert "\n" == formatter.getNewLine(), "new line"

        formatter.setOptPrefix("~")
        assert "~" == formatter.getOptPrefix(), "opt prefix"

        formatter.setSyntaxPrefix("-> ")
        assert "-> " == formatter.getSyntaxPrefix(), "syntax prefix"

        formatter.setWidth(80)
        assert 80 == formatter.getWidth(), "width"
