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
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;

import org.junit.Test;

import java.util.Properties;

@SuppressWarnings("deprecation") // tests some deprecated classes
public class CommandLineTest {

    @Test
    public void testBuilder_test0_decomposed()  {
        final CommandLine.Builder builder = new CommandLine.Builder();
    }

    @Test
    public void testBuilder_test1_decomposed()  {
        final CommandLine.Builder builder = new CommandLine.Builder();
        builder.addArg("foo").addArg("bar");
    }

    @Test
    public void testBuilder_test2_decomposed()  {
        final CommandLine.Builder builder = new CommandLine.Builder();
        builder.addArg("foo").addArg("bar");
        Option.builder1("T");
    }

    @Test
    public void testBuilder_test3_decomposed()  {
        final CommandLine.Builder builder = new CommandLine.Builder();
        builder.addArg("foo").addArg("bar");
        Option.builder1("T");
        Option.builder1("T").build();
    }

    @Test
    public void testBuilder_test4_decomposed()  {
        final CommandLine.Builder builder = new CommandLine.Builder();
        builder.addArg("foo").addArg("bar");
        Option.builder1("T");
        Option.builder1("T").build();
        builder.addOption(Option.builder1("T").build());
    }

    @Test
    public void testBuilder_test5_decomposed()  {
        final CommandLine.Builder builder = new CommandLine.Builder();
        builder.addArg("foo").addArg("bar");
        Option.builder1("T");
        Option.builder1("T").build();
        builder.addOption(Option.builder1("T").build());
        final CommandLine cmd = builder.build();
    }

    @Test
    public void testBuilder_test6_decomposed()  {
        final CommandLine.Builder builder = new CommandLine.Builder();
        builder.addArg("foo").addArg("bar");
        Option.builder1("T");
        Option.builder1("T").build();
        builder.addOption(Option.builder1("T").build());
        final CommandLine cmd = builder.build();
        assertEquals("foo", cmd.getArgs()[0]);
    }

    @Test
    public void testBuilder_test7_decomposed()  {
        final CommandLine.Builder builder = new CommandLine.Builder();
        builder.addArg("foo").addArg("bar");
        Option.builder1("T");
        Option.builder1("T").build();
        builder.addOption(Option.builder1("T").build());
        final CommandLine cmd = builder.build();
        assertEquals("foo", cmd.getArgs()[0]);
        assertEquals("bar", cmd.getArgList().get(1));
    }

    @Test
    public void testBuilder_test8_decomposed()  {
        final CommandLine.Builder builder = new CommandLine.Builder();
        builder.addArg("foo").addArg("bar");
        Option.builder1("T");
        Option.builder1("T").build();
        builder.addOption(Option.builder1("T").build());
        final CommandLine cmd = builder.build();
        assertEquals("foo", cmd.getArgs()[0]);
        assertEquals("bar", cmd.getArgList().get(1));
        cmd.getOptions();
    }

    @Test
    public void testBuilder_test9_decomposed()  {
        final CommandLine.Builder builder = new CommandLine.Builder();
        builder.addArg("foo").addArg("bar");
        Option.builder1("T");
        Option.builder1("T").build();
        builder.addOption(Option.builder1("T").build());
        final CommandLine cmd = builder.build();
        assertEquals("foo", cmd.getArgs()[0]);
        assertEquals("bar", cmd.getArgList().get(1));
        cmd.getOptions();
        assertEquals("T", cmd.getOptions()[0].getOpt());
    }

    @Test
    public void testGetOptionProperties_test0_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
    }

    @Test
    public void testGetOptionProperties_test1_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
    }

    @Test
    public void testGetOptionProperties_test2_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
    }

    @Test
    public void testGetOptionProperties_test3_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
    }

    @Test
    public void testGetOptionProperties_test4_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
    }

    @Test
    public void testGetOptionProperties_test5_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
    }

    @Test
    public void testGetOptionProperties_test6_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
    }

    @Test
    public void testGetOptionProperties_test7_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
    }

    @Test
    public void testGetOptionProperties_test8_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
    }

    @Test
    public void testGetOptionProperties_test9_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0());
    }

    @Test
    public void testGetOptionProperties_test10_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0());
        final Parser parser = new GnuParser();
    }

    @Test
    public void testGetOptionProperties_test11_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0());
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testGetOptionProperties_test12_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0());
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
        final Properties props = cl.getOptionProperties1("D");
    }

    @Test
    public void testGetOptionProperties_test13_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0());
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
        final Properties props = cl.getOptionProperties1("D");
        assertNotNull("null properties", props);
        assertEquals("number of properties in " + props, 4, props.size());
    }

    @Test
    public void testGetOptionProperties_test14_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0());
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
        final Properties props = cl.getOptionProperties1("D");
        assertNotNull("null properties", props);
        assertEquals("number of properties in " + props, 4, props.size());
        assertEquals("property 1", "value1", props.getProperty("param1"));
        assertEquals("property 2", "value2", props.getProperty("param2"));
    }

    @Test
    public void testGetOptionProperties_test15_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0());
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
        final Properties props = cl.getOptionProperties1("D");
        assertNotNull("null properties", props);
        assertEquals("number of properties in " + props, 4, props.size());
        assertEquals("property 1", "value1", props.getProperty("param1"));
        assertEquals("property 2", "value2", props.getProperty("param2"));
        assertEquals("property 3", "true", props.getProperty("param3"));
        assertEquals("property 4", "value4", props.getProperty("param4"));
    }

    @Test
    public void testGetOptionProperties_test16_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0());
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
        final Properties props = cl.getOptionProperties1("D");
        assertNotNull("null properties", props);
        assertEquals("number of properties in " + props, 4, props.size());
        assertEquals("property 1", "value1", props.getProperty("param1"));
        assertEquals("property 2", "value2", props.getProperty("param2"));
        assertEquals("property 3", "true", props.getProperty("param3"));
        assertEquals("property 4", "value4", props.getProperty("param4"));
        assertEquals(
                "property with long format",
                "bar",
                cl.getOptionProperties1("property").getProperty("foo"));
    }

    @Test
    public void testGetOptionPropertiesWithOption_test0_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
    }

    @Test
    public void testGetOptionPropertiesWithOption_test1_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
    }

    @Test
    public void testGetOptionPropertiesWithOption_test2_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
    }

    @Test
    public void testGetOptionPropertiesWithOption_test3_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
    }

    @Test
    public void testGetOptionPropertiesWithOption_test4_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
    }

    @Test
    public void testGetOptionPropertiesWithOption_test5_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
    }

    @Test
    public void testGetOptionPropertiesWithOption_test6_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
    }

    @Test
    public void testGetOptionPropertiesWithOption_test7_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        final Option optionProperty =
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
    }

    @Test
    public void testGetOptionPropertiesWithOption_test8_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        final Option optionProperty =
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(optionD);
        options.addOption0(optionProperty);
    }

    @Test
    public void testGetOptionPropertiesWithOption_test9_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        final Option optionProperty =
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(optionD);
        options.addOption0(optionProperty);
        final Parser parser = new GnuParser();
    }

    @Test
    public void testGetOptionPropertiesWithOption_test10_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        final Option optionProperty =
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(optionD);
        options.addOption0(optionProperty);
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testGetOptionPropertiesWithOption_test11_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        final Option optionProperty =
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(optionD);
        options.addOption0(optionProperty);
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
        final Properties props = cl.getOptionProperties0(optionD);
    }

    @Test
    public void testGetOptionPropertiesWithOption_test12_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        final Option optionProperty =
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(optionD);
        options.addOption0(optionProperty);
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
        final Properties props = cl.getOptionProperties0(optionD);
        assertNotNull("null properties", props);
        assertEquals("number of properties in " + props, 4, props.size());
    }

    @Test
    public void testGetOptionPropertiesWithOption_test13_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        final Option optionProperty =
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(optionD);
        options.addOption0(optionProperty);
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
        final Properties props = cl.getOptionProperties0(optionD);
        assertNotNull("null properties", props);
        assertEquals("number of properties in " + props, 4, props.size());
        assertEquals("property 1", "value1", props.getProperty("param1"));
        assertEquals("property 2", "value2", props.getProperty("param2"));
    }

    @Test
    public void testGetOptionPropertiesWithOption_test14_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        final Option optionProperty =
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(optionD);
        options.addOption0(optionProperty);
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
        final Properties props = cl.getOptionProperties0(optionD);
        assertNotNull("null properties", props);
        assertEquals("number of properties in " + props, 4, props.size());
        assertEquals("property 1", "value1", props.getProperty("param1"));
        assertEquals("property 2", "value2", props.getProperty("param2"));
        assertEquals("property 3", "true", props.getProperty("param3"));
        assertEquals("property 4", "value4", props.getProperty("param4"));
    }

    @Test
    public void testGetOptionPropertiesWithOption_test15_decomposed() throws Exception {
        final String[] args = {
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar"
        };
        final Options options = new Options();
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2);
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
        OptionBuilder.withValueSeparator0();
        OptionBuilder.withValueSeparator0().hasArgs1(2);
        OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property");
        final Option optionProperty =
                OptionBuilder.withValueSeparator0().hasArgs1(2).withLongOpt("property").create0();
        options.addOption0(optionD);
        options.addOption0(optionProperty);
        final Parser parser = new GnuParser();
        final CommandLine cl = parser.parse0(options, args);
        final Properties props = cl.getOptionProperties0(optionD);
        assertNotNull("null properties", props);
        assertEquals("number of properties in " + props, 4, props.size());
        assertEquals("property 1", "value1", props.getProperty("param1"));
        assertEquals("property 2", "value2", props.getProperty("param2"));
        assertEquals("property 3", "true", props.getProperty("param3"));
        assertEquals("property 4", "value4", props.getProperty("param4"));
        assertEquals(
                "property with long format",
                "bar",
                cl.getOptionProperties0(optionProperty).getProperty("foo"));
    }

    @Test
    public void testGetOptions_test0_decomposed()  {
        final CommandLine cmd = new CommandLine();
    }

    @Test
    public void testGetOptions_test1_decomposed()  {
        final CommandLine cmd = new CommandLine();
        assertNotNull(cmd.getOptions());
        assertEquals(0, cmd.getOptions().length);
    }

    @Test
    public void testGetOptions_test2_decomposed()  {
        final CommandLine cmd = new CommandLine();
        assertNotNull(cmd.getOptions());
        assertEquals(0, cmd.getOptions().length);
        Option.Option1("a",null);
    }

    @Test
    public void testGetOptions_test3_decomposed()  {
        final CommandLine cmd = new CommandLine();
        assertNotNull(cmd.getOptions());
        assertEquals(0, cmd.getOptions().length);
        Option.Option1("a",null);
        cmd.addOption(Option.Option1("a", null));
    }

    @Test
    public void testGetOptions_test4_decomposed()  {
        final CommandLine cmd = new CommandLine();
        assertNotNull(cmd.getOptions());
        assertEquals(0, cmd.getOptions().length);
        Option.Option1("a",null);
        cmd.addOption(Option.Option1("a", null));
        Option.Option1("b",null);
    }

    @Test
    public void testGetOptions_test5_decomposed()  {
        final CommandLine cmd = new CommandLine();
        assertNotNull(cmd.getOptions());
        assertEquals(0, cmd.getOptions().length);
        Option.Option1("a",null);
        cmd.addOption(Option.Option1("a", null));
        Option.Option1("b",null);
        cmd.addOption(Option.Option1("b", null));
    }

    @Test
    public void testGetOptions_test6_decomposed()  {
        final CommandLine cmd = new CommandLine();
        assertNotNull(cmd.getOptions());
        assertEquals(0, cmd.getOptions().length);
        Option.Option1("a",null);
        cmd.addOption(Option.Option1("a", null));
        Option.Option1("b",null);
        cmd.addOption(Option.Option1("b", null));
        Option.Option1("c",null);
    }

    @Test
    public void testGetOptions_test7_decomposed()  {
        final CommandLine cmd = new CommandLine();
        assertNotNull(cmd.getOptions());
        assertEquals(0, cmd.getOptions().length);
        Option.Option1("a",null);
        cmd.addOption(Option.Option1("a", null));
        Option.Option1("b",null);
        cmd.addOption(Option.Option1("b", null));
        Option.Option1("c",null);
        cmd.addOption(Option.Option1("c", null));
    }

    @Test
    public void testGetOptions_test8_decomposed()  {
        final CommandLine cmd = new CommandLine();
        assertNotNull(cmd.getOptions());
        assertEquals(0, cmd.getOptions().length);
        Option.Option1("a",null);
        cmd.addOption(Option.Option1("a", null));
        Option.Option1("b",null);
        cmd.addOption(Option.Option1("b", null));
        Option.Option1("c",null);
        cmd.addOption(Option.Option1("c", null));
        assertEquals(3, cmd.getOptions().length);
    }

    @Test
    public void testGetParsedOptionValue_test0_decomposed() throws Exception {
        final Options options = new Options();
    }

    @Test
    public void testGetParsedOptionValue_test1_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.hasArg0();
    }

    @Test
    public void testGetParsedOptionValue_test2_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().withType0(Number.class);
    }

    @Test
    public void testGetParsedOptionValue_test3_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().withType0(Number.class);
        OptionBuilder.hasArg0().withType0(Number.class).create2("i");
    }

    @Test
    public void testGetParsedOptionValue_test4_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().withType0(Number.class);
        OptionBuilder.hasArg0().withType0(Number.class).create2("i");
        options.addOption0(OptionBuilder.hasArg0().withType0(Number.class).create2("i"));
    }

    @Test
    public void testGetParsedOptionValue_test5_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().withType0(Number.class);
        OptionBuilder.hasArg0().withType0(Number.class).create2("i");
        options.addOption0(OptionBuilder.hasArg0().withType0(Number.class).create2("i"));
        OptionBuilder.hasArg0();
    }

    @Test
    public void testGetParsedOptionValue_test6_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().withType0(Number.class);
        OptionBuilder.hasArg0().withType0(Number.class).create2("i");
        options.addOption0(OptionBuilder.hasArg0().withType0(Number.class).create2("i"));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create2("f");
    }

    @Test
    public void testGetParsedOptionValue_test7_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().withType0(Number.class);
        OptionBuilder.hasArg0().withType0(Number.class).create2("i");
        options.addOption0(OptionBuilder.hasArg0().withType0(Number.class).create2("i"));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create2("f");
        options.addOption0(OptionBuilder.hasArg0().create2("f"));
    }

    @Test
    public void testGetParsedOptionValue_test8_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().withType0(Number.class);
        OptionBuilder.hasArg0().withType0(Number.class).create2("i");
        options.addOption0(OptionBuilder.hasArg0().withType0(Number.class).create2("i"));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create2("f");
        options.addOption0(OptionBuilder.hasArg0().create2("f"));
        final CommandLineParser parser = new DefaultParser(2, false, null);
    }

    @Test
    public void testGetParsedOptionValue_test9_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().withType0(Number.class);
        OptionBuilder.hasArg0().withType0(Number.class).create2("i");
        options.addOption0(OptionBuilder.hasArg0().withType0(Number.class).create2("i"));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create2("f");
        options.addOption0(OptionBuilder.hasArg0().create2("f"));
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});
    }

    @Test
    public void testGetParsedOptionValue_test10_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().withType0(Number.class);
        OptionBuilder.hasArg0().withType0(Number.class).create2("i");
        options.addOption0(OptionBuilder.hasArg0().withType0(Number.class).create2("i"));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create2("f");
        options.addOption0(OptionBuilder.hasArg0().create2("f"));
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});
        assertEquals(123, ((Number) cmd.getParsedOptionValue2("i")).intValue());
        assertEquals("foo", cmd.getParsedOptionValue2("f"));
    }

    @Test
    public void testGetParsedOptionValueWithChar_test0_decomposed() throws Exception {
        final Options options = new Options();
    }

    @Test
    public void testGetParsedOptionValueWithChar_test1_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
    }

    @Test
    public void testGetParsedOptionValueWithChar_test2_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
    }

    @Test
    public void testGetParsedOptionValueWithChar_test3_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
    }

    @Test
    public void testGetParsedOptionValueWithChar_test4_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        Option.builder1("i").hasArg0().type(Number.class).build();
    }

    @Test
    public void testGetParsedOptionValueWithChar_test5_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        Option.builder1("i").hasArg0().type(Number.class).build();
        options.addOption0(Option.builder1("i").hasArg0().type(Number.class).build());
    }

    @Test
    public void testGetParsedOptionValueWithChar_test6_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        Option.builder1("i").hasArg0().type(Number.class).build();
        options.addOption0(Option.builder1("i").hasArg0().type(Number.class).build());
        Option.builder1("f");
    }

    @Test
    public void testGetParsedOptionValueWithChar_test7_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        Option.builder1("i").hasArg0().type(Number.class).build();
        options.addOption0(Option.builder1("i").hasArg0().type(Number.class).build());
        Option.builder1("f");
        Option.builder1("f").hasArg0();
    }

    @Test
    public void testGetParsedOptionValueWithChar_test8_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        Option.builder1("i").hasArg0().type(Number.class).build();
        options.addOption0(Option.builder1("i").hasArg0().type(Number.class).build());
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().build();
    }

    @Test
    public void testGetParsedOptionValueWithChar_test9_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        Option.builder1("i").hasArg0().type(Number.class).build();
        options.addOption0(Option.builder1("i").hasArg0().type(Number.class).build());
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().build();
        options.addOption0(Option.builder1("f").hasArg0().build());
    }

    @Test
    public void testGetParsedOptionValueWithChar_test10_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        Option.builder1("i").hasArg0().type(Number.class).build();
        options.addOption0(Option.builder1("i").hasArg0().type(Number.class).build());
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().build();
        options.addOption0(Option.builder1("f").hasArg0().build());
        final CommandLineParser parser = new DefaultParser(2, false, null);
    }

    @Test
    public void testGetParsedOptionValueWithChar_test11_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        Option.builder1("i").hasArg0().type(Number.class).build();
        options.addOption0(Option.builder1("i").hasArg0().type(Number.class).build());
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().build();
        options.addOption0(Option.builder1("f").hasArg0().build());
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});
    }

    @Test
    public void testGetParsedOptionValueWithChar_test12_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        Option.builder1("i").hasArg0().type(Number.class).build();
        options.addOption0(Option.builder1("i").hasArg0().type(Number.class).build());
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().build();
        options.addOption0(Option.builder1("f").hasArg0().build());
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});
        assertEquals(123, ((Number) cmd.getParsedOptionValue0('i')).intValue());
        assertEquals("foo", cmd.getParsedOptionValue0('f'));
    }

    @Test
    public void testGetParsedOptionValueWithOption_test0_decomposed() throws Exception {
        final Options options = new Options();
    }

    @Test
    public void testGetParsedOptionValueWithOption_test1_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
    }

    @Test
    public void testGetParsedOptionValueWithOption_test2_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
    }

    @Test
    public void testGetParsedOptionValueWithOption_test3_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
    }

    @Test
    public void testGetParsedOptionValueWithOption_test4_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
    }

    @Test
    public void testGetParsedOptionValueWithOption_test5_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
    }

    @Test
    public void testGetParsedOptionValueWithOption_test6_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
    }

    @Test
    public void testGetParsedOptionValueWithOption_test7_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        final Option optF = Option.builder1("f").hasArg0().build();
    }

    @Test
    public void testGetParsedOptionValueWithOption_test8_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        final Option optF = Option.builder1("f").hasArg0().build();
        options.addOption0(optI);
        options.addOption0(optF);
    }

    @Test
    public void testGetParsedOptionValueWithOption_test9_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        final Option optF = Option.builder1("f").hasArg0().build();
        options.addOption0(optI);
        options.addOption0(optF);
        final CommandLineParser parser = new DefaultParser(2, false, null);
    }

    @Test
    public void testGetParsedOptionValueWithOption_test10_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        final Option optF = Option.builder1("f").hasArg0().build();
        options.addOption0(optI);
        options.addOption0(optF);
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});
    }

    @Test
    public void testGetParsedOptionValueWithOption_test11_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        final Option optF = Option.builder1("f").hasArg0().build();
        options.addOption0(optI);
        options.addOption0(optF);
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});
        assertEquals(123, ((Number) cmd.getParsedOptionValue1(optI)).intValue());
        assertEquals("foo", cmd.getParsedOptionValue1(optF));
    }

    @Test
    public void testNullhOption_test0_decomposed() throws Exception {
        final Options options = new Options();
    }

    @Test
    public void testNullhOption_test1_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
    }

    @Test
    public void testNullhOption_test2_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
    }

    @Test
    public void testNullhOption_test3_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
    }

    @Test
    public void testNullhOption_test4_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
    }

    @Test
    public void testNullhOption_test5_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
    }

    @Test
    public void testNullhOption_test6_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
    }

    @Test
    public void testNullhOption_test7_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        final Option optF = Option.builder1("f").hasArg0().build();
    }

    @Test
    public void testNullhOption_test8_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        final Option optF = Option.builder1("f").hasArg0().build();
        options.addOption0(optI);
        options.addOption0(optF);
    }

    @Test
    public void testNullhOption_test9_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        final Option optF = Option.builder1("f").hasArg0().build();
        options.addOption0(optI);
        options.addOption0(optF);
        final CommandLineParser parser = new DefaultParser(2, false, null);
    }

    @Test
    public void testNullhOption_test10_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        final Option optF = Option.builder1("f").hasArg0().build();
        options.addOption0(optI);
        options.addOption0(optF);
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});
    }

    @Test
    public void testNullhOption_test11_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        final Option optF = Option.builder1("f").hasArg0().build();
        options.addOption0(optI);
        options.addOption0(optF);
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});
        assertNull(cmd.getOptionValue2((Option) null));
    }

    @Test
    public void testNullhOption_test12_decomposed() throws Exception {
        final Options options = new Options();
        Option.builder1("i");
        Option.builder1("i").hasArg0();
        Option.builder1("i").hasArg0().type(Number.class);
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        final Option optF = Option.builder1("f").hasArg0().build();
        options.addOption0(optI);
        options.addOption0(optF);
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});
        assertNull(cmd.getOptionValue2((Option) null));
        assertNull(cmd.getParsedOptionValue1((Option) null));
    }
}