
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */


package org.apache.commons.cli;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

import java.io.PrintWriter;
import java.io.StringWriter;

/**
 * This is a collection of tests that test real world applications command lines.
 *
 * <p>The following applications are tested:
 *
 * <ul>
 *   <li>ls
 *   <li>Ant
 *   <li>Groovy
 *   <li>man
 * </ul>
 */
@SuppressWarnings("deprecation") // tests some deprecated classes
public class ApplicationTest {
    /** Ant test */
    @Test
    public void testAnt() throws Exception {
        final CommandLineParser parser = new GnuParser();
        final Options options = new Options();
        options.addOption1("help", false, "print this message");
        options.addOption1("projecthelp", false, "print project help information");
        options.addOption1("version", false, "print the version information and exit");
        options.addOption1("quiet", false, "be extra quiet");
        options.addOption1("verbose", false, "be extra verbose");
        options.addOption1("debug", false, "print debug information");
        options.addOption1("logfile", true, "use given file for log");
        options.addOption1("logger", true, "the class which is to perform the logging");
        options.addOption1("listener", true, "add an instance of a class as a project listener");
        options.addOption1("buildfile", true, "use given buildfile");
        options.addOption0(
                OptionBuilder.withDescription("use value for given property")
                        .hasArgs0()
                        .withValueSeparator0()
                        .create1('D'));
        options.addOption1(
                "find", true, "search for buildfile towards the root of the filesystem and use it");

        final String[] args = {
            "-buildfile", "mybuild.xml", "-Dproperty=value", "-Dproperty1=value1", "-projecthelp"
        };

        final CommandLine line = parser.parse0(options, args);

        final String[] opts = line.getOptionValues2("D");
        assertEquals("property", opts[0]);
        assertEquals("value", opts[1]);
        assertEquals("property1", opts[2]);
        assertEquals("value1", opts[3]);

        assertEquals(line.getOptionValue4("buildfile"), "mybuild.xml");

        assertTrue(line.hasOption2("projecthelp"));
    }

    @Test
    public void testGroovy() throws Exception {
        final Options options = new Options();

        options.addOption0(
                OptionBuilder.withLongOpt("define")
                        .withDescription("define a system property")
                        .hasArg1(true)
                        .withArgName("name=value")
                        .create1('D'));
        options.addOption0(
                OptionBuilder.hasArg1(false)
                        .withDescription("usage information")
                        .withLongOpt("help")
                        .create1('h'));
        options.addOption0(
                OptionBuilder.hasArg1(false)
                        .withDescription("debug mode will print out full stack traces")
                        .withLongOpt("debug")
                        .create1('d'));
        options.addOption0(
                OptionBuilder.hasArg1(false)
                        .withDescription("display the Groovy and JVM versions")
                        .withLongOpt("version")
                        .create1('v'));
        options.addOption0(
                OptionBuilder.withArgName("charset")
                        .hasArg0()
                        .withDescription("specify the encoding of the files")
                        .withLongOpt("encoding")
                        .create1('c'));
        options.addOption0(
                OptionBuilder.withArgName("script")
                        .hasArg0()
                        .withDescription("specify a command line script")
                        .create1('e'));
        options.addOption0(
                OptionBuilder.withArgName("extension")
                        .hasOptionalArg()
                        .withDescription(
                                "modify files in place; create backup if extension is given (e.g."
                                        + " \'.bak\')")
                        .create1('i'));
        options.addOption0(
                OptionBuilder.hasArg1(false)
                        .withDescription(
                                "process files line by line using implicit 'line' variable")
                        .create1('n'));
        options.addOption0(
                OptionBuilder.hasArg1(false)
                        .withDescription(
                                "process files line by line and print result (see also -n)")
                        .create1('p'));
        options.addOption0(
                OptionBuilder.withArgName("port")
                        .hasOptionalArg()
                        .withDescription("listen on a port and process inbound lines")
                        .create1('l'));
        options.addOption0(
                OptionBuilder.withArgName("splitPattern")
                        .hasOptionalArg()
                        .withDescription(
                                "split lines using splitPattern (default '\\s') using implicit"
                                        + " 'split' variable")
                        .withLongOpt("autosplit")
                        .create1('a'));

        final Parser parser = new PosixParser();
        final CommandLine line =
                parser.parse1(options, new String[] {"-e", "println 'hello'"}, true);

        assertTrue(line.hasOption0('e'));
        assertEquals("println 'hello'", line.getOptionValue0('e'));
    }

    @Test
    public void testLs() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final Options options = new Options();
        options.addOption3("a", "all", false, "do not hide entries starting with .");
        options.addOption3("A", "almost-all", false, "do not list implied . and ..");
        options.addOption3("b", "escape", false, "print octal escapes for nongraphic characters");
        options.addOption0(
                OptionBuilder.withLongOpt("block-size")
                        .withDescription("use SIZE-byte blocks")
                        .hasArg0()
                        .withArgName("SIZE")
                        .create0());
        options.addOption3(
                "B", "ignore-backups", false, "do not list implied entried ending with ~");
        options.addOption1(
                "c",
                false,
                "with -lt: sort by, and show, ctime (time of last modification of file status"
                    + " information) with -l:show ctime and sort by name otherwise: sort by ctime");
        options.addOption1("C", false, "list entries by columns");

        final String[] args = {"--block-size=10"};

        final CommandLine line = parser.parse0(options, args);
        assertTrue(line.hasOption2("block-size"));
        assertEquals(line.getOptionValue4("block-size"), "10");
    }

    /** author Slawek Zachcial */
    @Test
    public void testMan() {
        final String cmdLine =
                "man [-c|-f|-k|-w|-tZT device] [-adlhu7V] [-Mpath] [-Ppager] [-Slist] [-msystem]"
                        + " [-pstring] [-Llocale] [-eextension] [section] page ...";
        final Options options =
                new Options()
                        .addOption3("a", "all", false, "find all matching manual pages.")
                        .addOption3("d", "debug", false, "emit debugging messages.")
                        .addOption3(
                                "e",
                                "extension",
                                false,
                                "limit search to extension type 'extension'.")
                        .addOption3("f", "whatis", false, "equivalent to whatis.")
                        .addOption3("k", "apropos", false, "equivalent to apropos.")
                        .addOption3(
                                "w", "location", false, "print physical location of man page(s).")
                        .addOption3(
                                "l",
                                "local-file",
                                false,
                                "interpret 'page' argument(s) as local filename(s)")
                        .addOption3("u", "update", false, "force a cache consistency check.")
                        .addOption3("r", "prompt", true, "provide 'less' pager with prompt.")
                        .addOption3(
                                "c",
                                "catman",
                                false,
                                "used by catman to reformat out of date cat pages.")
                        .addOption3(
                                "7",
                                "ascii",
                                false,
                                "display ASCII translation or certain latin1 chars.")
                        .addOption3("t", "troff", false, "use troff format pages.")
                        .addOption3("T", "troff-device", true, "use groff with selected device.")
                        .addOption3("Z", "ditroff", false, "use groff with selected device.")
                        .addOption3(
                                "D", "default", false, "reset all options to their default values.")
                        .addOption3(
                                "M", "manpath", true, "set search path for manual pages to 'path'.")
                        .addOption3("P", "pager", true, "use program 'pager' to display output.")
                        .addOption3("S", "sections", true, "use colon separated section list.")
                        .addOption3(
                                "m",
                                "systems",
                                true,
                                "search for man pages from other unix system(s).")
                        .addOption3(
                                "L",
                                "locale",
                                true,
                                "define the locale for this particular man search.")
                        .addOption3(
                                "p",
                                "preprocessor",
                                true,
                                "string indicates which preprocessor to run.\n"
                                        + " e - [n]eqn  p - pic     t - tbl\n"
                                        + " g - grap    r - refer   v - vgrind")
                        .addOption3("V", "version", false, "show version.")
                        .addOption3("h", "help", false, "show this usage message.");

        final HelpFormatter hf = new HelpFormatter();
        final String eol = System.getProperty("line.separator");
        final StringWriter out = new StringWriter();
        hf.printHelp3(
                new PrintWriter(out),
                60,
                cmdLine,
                null,
                options,
                HelpFormatter.DEFAULT_LEFT_PAD,
                HelpFormatter.DEFAULT_DESC_PAD,
                null,
                false);
        assertEquals(
                "usage: man [-c|-f|-k|-w|-tZT device] [-adlhu7V] [-Mpath]"
                        + eol
                        + "           [-Ppager] [-Slist] [-msystem] [-pstring]"
                        + eol
                        + "           [-Llocale] [-eextension] [section] page ..."
                        + eol
                        + " -7,--ascii                display ASCII translation or"
                        + eol
                        + "                           certain latin1 chars."
                        + eol
                        + " -a,--all                  find all matching manual pages."
                        + eol
                        + " -c,--catman               used by catman to reformat out of"
                        + eol
                        + "                           date cat pages."
                        + eol
                        + " -d,--debug                emit debugging messages."
                        + eol
                        + " -D,--default              reset all options to their"
                        + eol
                        + "                           default values."
                        + eol
                        + " -e,--extension            limit search to extension type"
                        + eol
                        + "                           'extension'."
                        + eol
                        + " -f,--whatis               equivalent to whatis."
                        + eol
                        + " -h,--help                 show this usage message."
                        + eol
                        + " -k,--apropos              equivalent to apropos."
                        + eol
                        + " -l,--local-file           interpret 'page' argument(s) as"
                        + eol
                        + "                           local filename(s)"
                        + eol
                        + " -L,--locale <arg>         define the locale for this"
                        + eol
                        + "                           particular man search."
                        + eol
                        + " -M,--manpath <arg>        set search path for manual pages"
                        + eol
                        + "                           to 'path'."
                        + eol
                        + " -m,--systems <arg>        search for man pages from other"
                        + eol
                        + "                           unix system(s)."
                        + eol
                        + " -P,--pager <arg>          use program 'pager' to display"
                        + eol
                        + "                           output."
                        + eol
                        + " -p,--preprocessor <arg>   string indicates which"
                        + eol
                        + "                           preprocessor to run."
                        + eol
                        + "                           e - [n]eqn  p - pic     t - tbl"
                        + eol
                        + "                           g - grap    r - refer   v -"
                        + eol
                        + "                           vgrind"
                        + eol
                        + " -r,--prompt <arg>         provide 'less' pager with prompt."
                        + eol
                        + " -S,--sections <arg>       use colon separated section list."
                        + eol
                        + " -t,--troff                use troff format pages."
                        + eol
                        + " -T,--troff-device <arg>   use groff with selected device."
                        + eol
                        + " -u,--update               force a cache consistency check."
                        + eol
                        + " -V,--version              show version."
                        + eol
                        + " -w,--location             print physical location of man"
                        + eol
                        + "                           page(s)."
                        + eol
                        + " -Z,--ditroff              use groff with selected device."
                        + eol,
                out.toString());
    }

    /** Real world test with long and short options. */
    @Test
    public void testNLT() throws Exception {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);

        final Option timeLimit =
                OptionBuilder.withLongOpt("limit")
                        .hasArg0()
                        .withValueSeparator0()
                        .withDescription("Set time limit for execution, in minutes")
                        .create2("l");

        final Option age =
                OptionBuilder.withLongOpt("age")
                        .hasArg0()
                        .withValueSeparator0()
                        .withDescription("Age (in days) of cache item before being recomputed")
                        .create2("a");

        final Option server =
                OptionBuilder.withLongOpt("server")
                        .hasArg0()
                        .withValueSeparator0()
                        .withDescription("The NLT server address")
                        .create2("s");

        final Option numResults =
                OptionBuilder.withLongOpt("results")
                        .hasArg0()
                        .withValueSeparator0()
                        .withDescription("Number of results per item")
                        .create2("r");

        final Option configFile =
                OptionBuilder.withLongOpt("file")
                        .hasArg0()
                        .withValueSeparator0()
                        .withDescription("Use the specified configuration file")
                        .create0();

        final Options options = new Options();
        options.addOption0(help);
        options.addOption0(version);
        options.addOption0(newRun);
        options.addOption0(trackerRun);
        options.addOption0(timeLimit);
        options.addOption0(age);
        options.addOption0(server);
        options.addOption0(numResults);
        options.addOption0(configFile);

        final CommandLineParser parser = new PosixParser();

        final String[] args = {"-v", "-l", "10", "-age", "5", "-file", "filename"};

        final CommandLine line = parser.parse0(options, args);
        assertTrue(line.hasOption2("v"));
        assertEquals(line.getOptionValue4("l"), "10");
        assertEquals(line.getOptionValue4("limit"), "10");
        assertEquals(line.getOptionValue4("a"), "5");
        assertEquals(line.getOptionValue4("age"), "5");
        assertEquals(line.getOptionValue4("file"), "filename");
    }
}
