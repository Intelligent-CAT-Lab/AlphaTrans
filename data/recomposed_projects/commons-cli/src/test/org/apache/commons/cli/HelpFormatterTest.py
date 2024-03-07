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
            options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build())
            formatter = HelpFormatter()
            formatter.setLongOptSeparator("=")
            out = StringWriter()
            formatter.printUsage1(PrintWriter(out), 80, "create", options)
            self.assertEqual("usage: create [--age=<arg>] [-f <arg>] [-s <SIZE>]", out.toString().strip())

    def testRtrim(self) -> None:

            formatter = HelpFormatter()
            self.assertIsNone(formatter.rtrim(None))
            self.assertEqual("", formatter.rtrim(""))
            self.assertEqual("  foo", formatter.rtrim("  foo  "))

    def testRenderWrappedTextWordCut(self) -> None:

            width = 7
            padding = 0
            text = "Thisisatest."
            expected = "Thisisa" + self.__EOL + "test."
            sb = StringBuffer()
            self._renderWrappedText(sb, width, padding, text)
            self.assertEqual("cut and wrap", expected, sb.toString())

    def testRenderWrappedTextSingleLinePadded2(self) -> None:

            width = 53
            padding = 24
            text = (
                "  -p,--period <PERIOD>  PERIOD is time duration of form "
                "DATE[-DATE] where DATE has form YYYY[MM[DD]]"
            )
            expected = (
                "  -p,--period <PERIOD>  PERIOD is time duration of"
                f"{self.__EOL}                        form DATE[-DATE] where DATE"
                f"{self.__EOL}                        has form YYYY[MM[DD]]"
            )
            sb = StringIO()
            self._renderWrappedText(sb, width, padding, text)
            self.assertEqual("single line padded text 2", expected, sb.getvalue())

    def testRenderWrappedTextSingleLinePadded(self) -> None:

            width = 12
            padding = 4
            text = "This is a test."
            expected = "This is a" + self.__EOL + "    test."
            sb = StringBuffer()
            self._renderWrappedText(sb, width, padding, text)
            self.assertEqual("single line padded text", expected, sb.toString())

    def testRenderWrappedTextSingleLine(self) -> None:

            width = 12
            padding = 0
            text = "This is a test."
            expected = "This is a" + self.__EOL + "test."
            sb = StringIO()
            self._renderWrappedText(sb, width, padding, text)
            self.assertEqual("single line text", expected, sb.getvalue())

    def testRenderWrappedTextMultiLinePadded(self) -> None:

            width = 16
            padding = 4
            text = "aaaa aaaa aaaa\n" + "aaaaaa\n" + "aaaaa"
            expected = "aaaa aaaa aaaa\n" + "    aaaaaa\n" + "    aaaaa"
            sb = StringBuffer()
            self._renderWrappedText(sb, width, padding, text)
            self.assertEqual("multi-line padded text", expected, sb.toString())

    def testRenderWrappedTextMultiLine(self) -> None:

            width = 16
            padding = 0
            expected = "aaaa aaaa aaaa\n" + "aaaaaa\n" + "aaaaa"
            sb = StringBuffer()
            self._renderWrappedText(sb, width, padding, expected)
            self.assertEqual("multi line text", expected, sb.toString())

    def testPrintUsage(self) -> None:


        pass # LLM could not translate method body

    def testPrintSortedUsageWithNullComparator(self) -> None:

            opts = Options()
            opts.addOption0(Option.Option1("c", "first"))
            opts.addOption0(Option.Option1("b", "second"))
            opts.addOption0(Option.Option1("a", "third"))
            helpFormatter = HelpFormatter()
            helpFormatter.setOptionComparator(None)
            out = StringWriter()
            helpFormatter.printUsage1(PrintWriter(out), 80, "app", opts)
            self.assertEqual("usage: app [-c] [-b] [-a]" + EOL, out.toString())

    def testPrintSortedUsage(self) -> None:

            opts = Options()
            opts.addOption0(Option.Option1("a", "first"))
            opts.addOption0(Option.Option1("b", "second"))
            opts.addOption0(Option.Option1("c", "third"))
            helpFormatter = HelpFormatter()
            helpFormatter.setOptionComparator(
                    lambda opt1, opt2: opt2.getKey().compareToIgnoreCase(opt1.getKey()))
            out = StringWriter()
            helpFormatter.printUsage1(PrintWriter(out), 80, "app", opts)
            self.assertEqual("usage: app [-c] [-b] [-a]" + EOL, out.toString())

    def testPrintRequiredOptionGroupUsage(self) -> None:

            group = OptionGroup()
            group.addOption(Option.builder1("a").build())
            group.addOption(Option.builder1("b").build())
            group.addOption(Option.builder1("c").build())
            group.setRequired(True)
            options = Options()
            options.addOptionGroup(group)
            out = StringWriter()
            formatter = HelpFormatter()
            formatter.printUsage1(PrintWriter(out), 80, "app", options)
            self.assertEqual("usage: app -a | -b | -c" + EOL, out.toString())

    def testPrintOptionWithEmptyArgNameUsage(self) -> None:

            option = self.Option2("f", True, None)
            option.setArgName("")
            option.setRequired(True)
            options = Options()
            options.addOption0(option)
            out = StringWriter()
            formatter = HelpFormatter()
            formatter.printUsage1(PrintWriter(out), 80, "app", options)
            self.assertEqual("usage: app -f" + self.__EOL, out.toString())

    def testPrintOptions(self) -> None:

            sb = StringBuffer()
            hf = HelpFormatter()
            leftPad = 1
            descPad = 3
            lpad = hf.createPadding(leftPad)
            dpad = hf.createPadding(descPad)
            options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
            expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
            hf.renderOptions(sb, 60, options, leftPad, descPad)
            self.assertEqual("simple non-wrapped option", expected, sb.toString())
            nextLineTabStop = leftPad + descPad + "-a".length()
            expected = (
                lpad
                + "-a"
                + dpad
                + "aaaa aaaa aaaa"
                + EOL
                + hf.createPadding(nextLineTabStop)
                + "aaaa aaaa"
            )
            sb.setLength(0)
            hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad)
            self.assertEqual("simple wrapped option", expected, sb.toString())
            options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
            expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd"
            sb.setLength(0)
            hf.renderOptions(sb, 60, options, leftPad, descPad)
            self.assertEqual("long non-wrapped option", expected, sb.toString())
            nextLineTabStop = leftPad + descPad + "-a,--aaa".length()
            expected = (
                lpad
                + "-a,--aaa"
                + dpad
                + "dddd dddd"
                + EOL
                + hf.createPadding(nextLineTabStop)
                + "dddd dddd"
            )
            sb.setLength(0)
            hf.renderOptions(sb, 25, options, leftPad, descPad)
            self.assertEqual("long wrapped option", expected, sb.toString())
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
                + hf.createPadding(nextLineTabStop)
                + "dddd dddd"
                + EOL
                + lpad
                + "-b      "
                + dpad
                + "feeee eeee"
                + EOL
                + hf.createPadding(nextLineTabStop)
                + "eeee eeee"
            )
            sb.setLength(0)
            hf.renderOptions(sb, 25, options, leftPad, descPad)
            self.assertEqual("multiple wrapped options", expected, sb.toString())

    def testPrintOptionGroupUsage(self) -> None:

            group = OptionGroup()
            group.addOption(Option.builder1("a").build())
            group.addOption(Option.builder1("b").build())
            group.addOption(Option.builder1("c").build())
            options = Options()
            options.addOptionGroup(group)
            out = StringIO()
            formatter = HelpFormatter()
            formatter.printUsage1(PrintWriter(out), 80, "app", options)
            self.assertEqual("usage: app [-a | -b | -c]" + EOL, out.getvalue())

    def testPrintHelpWithEmptySyntax(self) -> None:

            formatter = HelpFormatter()
            try:
                formatter.printHelp4(None, Options())
                self.fail("null command line syntax should be rejected")
            except IllegalArgumentException:
                pass
            try:
                formatter.printHelp4("", Options())
                self.fail("empty command line syntax should be rejected")
            except IllegalArgumentException:
                pass

    def testPrintHelpNewlineHeader(self) -> None:

            formatter = HelpFormatter()
            out = io.BytesIO()
            pw = io.TextIOWrapper(out, newline="")
            options = Options()
            options.addOption2("a", "b")
            formatter.printHelp2(pw, 80, "test\n", "\n", options, 0, 0, "footer\n")
            expected = "usage: test\n\n-ab\nfooter\n"
            pw.flush()
            self.assertEqual("header newline", expected, out.getvalue())

    def testPrintHelpNewlineFooter(self) -> None:

            formatter = HelpFormatter()
            out = io.StringIO()
            pw = io.TextIOWrapper(out, newline="")
            options = Options()
            options.addOption2("a", "b")
            formatter.printHelp2(pw, 80, "test" + self.__EOL, "header" + self.__EOL, options, 0, 0, self.__EOL)
            expected = "usage: test" + self.__EOL + "header" + self.__EOL + "-ab" + self.__EOL + self.__EOL
            pw.flush()
            self.assertEqual("footer newline", expected, out.getvalue())

    def testOptionWithoutShortFormat2(self) -> None:


        pass # LLM could not translate method body

    def testOptionWithoutShortFormat(self) -> None:

            options = Options()
            options.addOption0(Option(0, "a", "aaa", "aaaaaaa", False, None))
            options.addOption0(Option(0, None, "bbb", "bbbbbbb", False, None))
            options.addOption0(Option(0, "c", None, "ccccccc", False, None))
            formatter = HelpFormatter()
            out = StringWriter()
            formatter.printHelp3(PrintWriter(out), 80, "foobar", "", options, 2, 2, "", True)
            self.assertEqual(
                    "usage: foobar [-a] [--bbb] [-c]"
                            + EOL
                            + "  -a,--aaa  aaaaaaa"
                            + EOL
                            + "     --bbb  bbbbbbb"
                            + EOL
                            + "  -c        ccccccc"
                            + EOL,
                    out.toString())

    def testIndentedHeaderAndFooter(self) -> None:

            options = Options()
            formatter = HelpFormatter()
            header = "  Header1\n  Header2"
            footer = "  Footer1\n  Footer2"
            out = StringWriter()
            formatter.printHelp3(
                    PrintWriter(out), 80, "foobar", header, options, 2, 2, footer, True)
            self.assertEqual(
                    "usage: foobar"
                            + EOL
                            + "  Header1"
                            + EOL
                            + "  Header2"
                            + EOL
                            + ""
                            + EOL
                            + "  Footer1"
                            + EOL
                            + "  Footer2"
                            + EOL,
                    out.toString())

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
            options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build())
            formatter = HelpFormatter()
            self.assertEqual(HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator())
            formatter.setLongOptSeparator("=")
            self.assertEqual("=", formatter.getLongOptSeparator())
            out = StringWriter()
            formatter.printHelp2(PrintWriter(out), 80, "create", "header", options, 2, 2, "footer")
            self.assertEqual(
                "usage: create"
                + EOL
                + "header"
                + EOL
                + "     --age=<arg>    the age"
                + EOL
                + "  -f <arg>          the file"
                + EOL
                + "  -s,--size=<SIZE>  the size"
                + EOL
                + "footer"
                + EOL,
                out.toString()
            )

    def testHeaderStartingWithLineSeparator(self) -> None:

            options = Options()
            formatter = HelpFormatter()
            header = EOL + "Header"
            footer = "Footer"
            out = StringWriter()
            formatter.printHelp3(
                    PrintWriter(out), 80, "foobar", header, options, 2, 2, footer, True)
            self.assertEqual(
                    "usage: foobar" + EOL + "" + EOL + "Header" + EOL + "" + EOL + "Footer" + EOL,
                    out.toString())

    def testFindWrapPos(self) -> None:

            hf = HelpFormatter()
            text = "This is a test."
            assert hf.findWrapPos(text, 8, 0) == 7
            assert hf.findWrapPos(text, 8, 8) == -1
            text = "aaaa aa"
            assert hf.findWrapPos(text, 3, 0) == 3
            text = "aaaaaa aaaaaa"
            assert hf.findWrapPos(text, 6, 0) == 6
            assert hf.findWrapPos(text, 6, 7) == -1
            text = "aaaaaa\n aaaaaa"
            assert hf.findWrapPos(text, 6, 0) == 7
            text = "aaaaaa\t aaaaaa"
            assert hf.findWrapPos(text, 6, 0) == 7

    def testDefaultArgName(self) -> None:

            option = Option.builder1("f").hasArg0().required1(True).build()
            options = Options()
            options.addOption0(option)
            out = StringWriter()
            formatter = HelpFormatter()
            formatter.setArgName("argument")
            formatter.printUsage1(PrintWriter(out), 80, "app", options)
            self.assertEqual("usage: app -f <argument>" + EOL, out.toString())

    def testAutomaticUsage(self) -> None:


        pass # LLM could not translate method body

    def testAccessors(self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


class new Comparator<Option>(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def compare(self, opt1: Option, opt2: Option) -> int:

            return opt2.getKey().lower().compareTo(opt1.getKey().lower())

    def (self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


