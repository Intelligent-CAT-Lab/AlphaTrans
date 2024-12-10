from __future__ import annotations
import time
import re
import sys
import os
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.GnuParser import *
from src.main.org.apache.commons.cli.HelpFormatter import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.PosixParser import *


class BugsTest(unittest.TestCase):

    def test31148(self) -> None:

        multi_arg_option = PosixParser.Option1("o", "option with multiple args")
        multi_arg_option.setArgs(1)

        options = Options()
        options.addOption0(multi_arg_option)

        parser = PosixParser()
        args = []
        props = {}
        props["o"] = "ovalue"
        cl = parser.parse2(options, args, props)

        self.assertTrue(cl.hasOption0("o"))
        self.assertEqual("ovalue", cl.getOptionValue0("o"))

    def test15648(self) -> None:

        parser = PosixParser()
        args = ["-m", '"Two Words"']
        m = OptionBuilder.hasArgs0().create2("m")
        options = Options()
        options.addOption0(m)
        line = parser.parse0(options, args)
        self.assertEqual("Two Words", line.getOptionValue4("m"))

    def test15046(self) -> None:

        parser = PosixParser()
        cli_args = ["-z", "c"]

        options = Options()
        options.addOption0(Option(0, "z", "timezone", "affected option", True, None))

        parser.parse0(options, cli_args)

        options.addOption3("c", "conflict", True, "conflict option")
        line = parser.parse0(options, cli_args)
        self.assertEqual(line.getOptionValue0("z"), "c")
        self.assertFalse(line.hasOption2("c"))

    def test14786(self) -> None:

        o = OptionBuilder.isRequired0().withDescription("test").create2("test")
        opts = Options()
        opts.addOption0(o)
        opts.addOption0(o)

        parser = GnuParser()

        args = ["-test"]

        line = parser.parse0(opts, args)
        self.assertTrue(line.hasOption2("test"))

    def test13935(self) -> None:

        directions = OptionGroup()

        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)

        directions.addOption(left)
        directions.addOption(right)
        directions.setRequired(True)

        opts = Options()
        opts.addOptionGroup(directions)
        opts.addOption0(straight)

        parser = PosixParser()

        args = []
        try:
            parser.parse0(opts, args)
            self.fail("Expected ParseException")
        except ParseException:
            pass

        args = ["-s"]
        try:
            parser.parse0(opts, args)
            self.fail("Expected ParseException")
        except ParseException:
            pass

        args = ["-s", "-l"]
        line = parser.parse0(opts, args)
        self.assertIsNotNone(line)

        opts.addOption0(forward)
        args = ["-s", "-l", "-f"]
        line = parser.parse0(opts, args)
        self.assertIsNotNone(line)

    def test13666(self) -> None:

        options = Options()
        dir = OptionBuilder.withDescription("dir").hasArg0().create1("d")
        options.addOption0(dir)

        oldSystemOut = sys.stdout
        try:
            bytes = io.BytesIO()
            print = io.TextIOWrapper(
                bytes,
                sys.stdout.encoding,
                "strict",
                lineterminator="\n",
                write_through=True,
            )

            print.write("\n")
            eol = bytes.getvalue().decode(sys.stdout.encoding)
            bytes.truncate(0)
            bytes.seek(0)

            sys.stdout = print

            formatter = HelpFormatter()
            formatter.printHelp4("dir", options)

            self.assertEqual(
                "usage: dir" + eol + " -d <arg>   dir" + eol,
                bytes.getvalue().decode(sys.stdout.encoding),
            )
        finally:
            sys.stdout = oldSystemOut

    def test13425(self) -> None:

        options = Options()
        oldpass = (
            OptionBuilder.withLongOpt("old-password")
            .withDescription("Use this option to specify the old password")
            .hasArg0()
            .create1("o")
        )
        newpass = (
            OptionBuilder.withLongOpt("new-password")
            .withDescription("Use this option to specify the new password")
            .hasArg0()
            .create1("n")
        )

        args = ["-o", "-n", "newpassword"]

        options.addOption0(oldpass)
        options.addOption0(newpass)

        parser = PosixParser()

        try:
            parser.parse0(options, args)
            self.fail("MissingArgumentException not caught.")
        except MissingArgumentException:
            pass

    def test12210(self) -> None:

        mainOptions = Options()

        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()

        grp.addOption(Option.Option2("exec", False, "description for this option"))

        grp.addOption(Option.Option2("rep", False, "description for this option"))

        mainOptions.addOptionGroup(grp)

        execOptions = Options()
        execOptions.addOption1("exec_opt1", False, " desc")
        execOptions.addOption1("exec_opt2", False, " desc")

        repOptions = Options()
        repOptions.addOption1("repopto", False, "desc")
        repOptions.addOption1("repoptt", False, "desc")

        parser = GnuParser()

        cmd = parser.parse1(mainOptions, argv, True)
        argv = cmd.getArgs()

        if cmd.hasOption2("exec"):
            cmd = parser.parse1(execOptions, argv, False)
            assert cmd.hasOption2("exec_opt1")
            assert cmd.hasOption2("exec_opt2")
        elif cmd.hasOption2("rep"):
            cmd = parser.parse1(repOptions, argv, False)
        else:
            self.fail("exec option not found")

    def test11680(self) -> None:

        options = Options()
        options.addOption1("f", True, "foobar")
        options.addOption1("m", True, "missing")
        args = ["-f", "foo"]

        parser = PosixParser()

        cmd = parser.parse0(options, args)

        cmd.getOptionValue5("f", "default f")
        cmd.getOptionValue5("m", "default m")

    def test11458(self) -> None:

        options = Options()
        options.addOption0(
            OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        )
        options.addOption0(
            OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")
        )
        args = ["-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"]

        parser = PosixParser()

        cmd = parser.parse0(options, args)

        values = cmd.getOptionValues0("D")

        self.assertEqual(values[0], "JAVA_HOME")
        self.assertEqual(values[1], "/opt/java")

        values = cmd.getOptionValues0("p")

        self.assertEqual(values[0], "file1")
        self.assertEqual(values[1], "file2")
        self.assertEqual(values[2], "file3")

        iter = cmd.iterator()
        while iter.hasNext():
            opt = iter.next()
            if opt.getId() == "D":
                self.assertEqual(opt.getValue1(0), "JAVA_HOME")
                self.assertEqual(opt.getValue1(1), "/opt/java")
            elif opt.getId() == "p":
                self.assertEqual(opt.getValue1(0), "file1")
                self.assertEqual(opt.getValue1(1), "file2")
                self.assertEqual(opt.getValue1(2), "file3")
            else:
                self.fail("-D option not found")

    def test11457(self) -> None:

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())
        args = ["--verbose"]

        parser = PosixParser()

        cmd = parser.parse0(options, args)
        self.assertTrue(cmd.hasOption2("verbose"))

    def test11456(self) -> None:

        options = Options()
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        options.addOption0(OptionBuilder.hasArg0().create1("b"))
        args = ["-a", "-bvalue"]

        parser = PosixParser()

        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")

        options = Options()
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        options.addOption0(OptionBuilder.hasArg0().create1("b"))
        args = ["-a", "-b", "value"]

        parser = GnuParser()

        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")
