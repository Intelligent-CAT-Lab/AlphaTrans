from __future__ import annotations
import time
import locale
import re
import logging
import sys
import os
import numbers
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.GnuParser import *
from src.main.org.apache.commons.cli.HelpFormatter import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.PosixParser import *


class ApplicationTest(unittest.TestCase):

    def testNLT(self) -> None:

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
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        age = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        server = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        numResults = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        configFile = (
            OptionBuilder.withLongOpt("file")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Use the specified configuration file")
            .create0()
        )

        options = Options()
        options.addOption0(help)
        options.addOption0(version)
        options.addOption0(newRun)
        options.addOption0(trackerRun)
        options.addOption0(timeLimit)
        options.addOption0(age)
        options.addOption0(server)
        options.addOption0(numResults)
        options.addOption0(configFile)

        parser = PosixParser()

        args = ["-v", "-l", "10", "-age", "5", "-file", "filename"]

        line = parser.parse0(options, args)
        self.assertTrue(line.hasOption2("v"))
        self.assertEqual(line.getOptionValue4("l"), "10")
        self.assertEqual(line.getOptionValue4("limit"), "10")
        self.assertEqual(line.getOptionValue4("a"), "5")
        self.assertEqual(line.getOptionValue4("age"), "5")
        self.assertEqual(line.getOptionValue4("file"), "filename")

    def testMan(self) -> None:

        cmdLine = "man [-c|-f|-k|-w|-tZT device] [-adlhu7V] [-Mpath] [-Ppager] [-Slist] [-msystem] [-pstring] [-Llocale] [-eextension] [section] page ..."
        options = (
            Options()
            .addOption3("a", "all", False, "find all matching manual pages.")
            .addOption3("d", "debug", False, "emit debugging messages.")
            .addOption3(
                "e", "extension", False, "limit search to extension type 'extension'."
            )
            .addOption3("f", "whatis", False, "equivalent to whatis.")
            .addOption3("k", "apropos", False, "equivalent to apropos.")
            .addOption3(
                "w", "location", False, "print physical location of man page(s)."
            )
            .addOption3(
                "l",
                "local-file",
                False,
                "interpret 'page' argument(s) as local filename(s)",
            )
            .addOption3("u", "update", False, "force a cache consistency check.")
            .addOption3("r", "prompt", True, "provide 'less' pager with prompt.")
            .addOption3(
                "c",
                "catman",
                False,
                "used by catman to reformat out of date cat pages.",
            )
            .addOption3(
                "7",
                "ascii",
                False,
                "display ASCII translation or certain latin1 chars.",
            )
            .addOption3("t", "troff", False, "use troff format pages.")
            .addOption3("T", "troff-device", True, "use groff with selected device.")
            .addOption3("Z", "ditroff", False, "use groff with selected device.")
            .addOption3(
                "D", "default", False, "reset all options to their default values."
            )
            .addOption3(
                "M", "manpath", True, "set search path for manual pages to 'path'."
            )
            .addOption3("P", "pager", True, "use program 'pager' to display output.")
            .addOption3("S", "sections", True, "use colon separated section list.")
            .addOption3(
                "m", "systems", True, "search for man pages from other unix system(s)."
            )
            .addOption3(
                "L", "locale", True, "define the locale for this particular man search."
            )
            .addOption3(
                "p",
                "preprocessor",
                True,
                "string indicates which preprocessor to run.\n e - [n]eqn  p - pic     t - tbl\n g - grap    r - refer   v - vgrind",
            )
            .addOption3("V", "version", False, "show version.")
            .addOption3("h", "help", False, "show this usage message.")
        )

        hf = HelpFormatter()
        eol = "\n"
        out = io.StringIO()
        hf.printHelp3(
            out,
            60,
            cmdLine,
            None,
            options,
            HelpFormatter.DEFAULT_LEFT_PAD,
            HelpFormatter.DEFAULT_DESC_PAD,
            None,
            False,
        )
        self.assertEqual(
            "usage: man [-c|-f|-k|-w|-tZT device] [-adlhu7V] [-Mpath] [-Ppager] [-Slist] [-msystem] [-pstring] [-Llocale] [-eextension] [section] page ...\n"
            + eol
            + " -7,--ascii                display ASCII translation or certain latin1 chars.\n"
            + " -a,--all                  find all matching manual pages.\n"
            + " -c,--catman               used by catman to reformat out of date cat pages.\n"
            + " -d,--debug                emit debugging messages.\n"
            + " -D,--default              reset all options to their default values.\n"
            + " -e,--extension            limit search to extension type 'extension'.\n"
            + " -f,--whatis               equivalent to whatis.\n"
            + " -h,--help                 show this usage message.\n"
            + " -k,--apropos              equivalent to apropos.\n"
            + " -l,--local-file           interpret 'page' argument(s) as local filename(s)\n"
            + " -L,--locale <arg>         define the locale for this particular man search.\n"
            + " -M,--manpath <arg>        set search path for manual pages to 'path'.\n"
            + " -m,--systems <arg>        search for man pages from other unix system(s).\n"
            + " -P,--pager <arg>          use program 'pager' to display output.\n"
            + " -p,--preprocessor <arg>   string indicates which preprocessor to run.\n"
            + "                           e - [n]eqn  p - pic     t - tbl\n"
            + "                           g - grap    r - refer   v - vgrind\n"
            + " -r,--prompt <arg>         provide 'less' pager with prompt.\n"
            + " -S,--sections <arg>       use colon separated section list.\n"
            + " -t,--troff                use troff format pages.\n"
            + " -T,--troff-device <arg>   use groff with selected device.\n"
            + " -u,--update               force a cache consistency check.\n"
            + " -V,--version              show version.\n"
            + " -w,--location             print physical location of man page(s).\n"
            + " -Z,--ditroff              use groff with selected device.\n",
            out.getvalue(),
        )

    def testLs(self) -> None:

        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )
        options.addOption0(
            OptionBuilder.withLongOpt("block-size")
            .withDescription("use SIZE-byte blocks")
            .hasArg0()
            .withArgName("SIZE")
            .create0()
        )
        options.addOption3(
            "B", "ignore-backups", False, "do not list implied entried ending with ~"
        )
        options.addOption1(
            "c",
            False,
            "with -lt: sort by, and show, ctime (time of last modification of file status"
            + " information) with -l:show ctime and sort by name otherwise: sort by ctime",
        )
        options.addOption1("C", False, "list entries by columns")

        args = ["--block-size=10"]

        line = parser.parse0(options, args)
        self.assertTrue(line.hasOption2("block-size"))
        self.assertEqual(line.getOptionValue4("block-size"), "10")

    def testGroovy(self) -> None:

        options = Options()

        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g."
                + " '.bak')"
            )
            .create1("i")
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )
        options.addOption0(
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )
        options.addOption0(
            OptionBuilder.withArgName("splitPattern")
            .hasOptionalArg()
            .withDescription(
                "split lines using splitPattern (default '\\s') using implicit"
                + " 'split' variable"
            )
            .withLongOpt("autosplit")
            .create1("a")
        )

        parser = PosixParser()
        line = parser.parse1(options, ["-e", "println 'hello'"], True)

        self.assertTrue(line.hasOption0("e"))
        self.assertEqual("println 'hello'", line.getOptionValue0("e"))

    def testAnt(self) -> None:

        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        options.addOption0(
            OptionBuilder.withDescription("use value for given property")
            .hasArgs0()
            .withValueSeparator0()
            .create1("D")
        )
        options.addOption1(
            "find",
            True,
            "search for buildfile towards the root of the filesystem and use it",
        )

        args = [
            "-buildfile",
            "mybuild.xml",
            "-Dproperty=value",
            "-Dproperty1=value1",
            "-projecthelp",
        ]

        line = parser.parse0(options, args)

        opts = line.getOptionValues2("D")
        self.assertEqual("property", opts[0])
        self.assertEqual("value", opts[1])
        self.assertEqual("property1", opts[2])
        self.assertEqual("value1", opts[3])

        self.assertEqual(line.getOptionValue4("buildfile"), "mybuild.xml")

        self.assertTrue(line.hasOption2("projecthelp"))
