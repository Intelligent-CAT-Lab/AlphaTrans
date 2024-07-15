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
    public void testBuilder() {
        final CommandLine.Builder builder = new CommandLine.Builder();
        builder.addArg("foo").addArg("bar");
        builder.addOption(Option.builder1("T").build());
        final CommandLine cmd = builder.build();

        assertEquals("foo", cmd.getArgs()[0]);
        assertEquals("bar", cmd.getArgList().get(1));
        assertEquals("T", cmd.getOptions()[0].getOpt());
    }

    @Test
    public void testGetOptionProperties() throws Exception {
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
        options.addOption0(OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D'));
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
    public void testGetOptionPropertiesWithOption() throws Exception {
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
        final Option optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D');
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
    public void testGetOptions() {
        final CommandLine cmd = new CommandLine();
        assertNotNull(cmd.getOptions());
        assertEquals(0, cmd.getOptions().length);

        cmd.addOption(Option.Option1("a", null));
        cmd.addOption(Option.Option1("b", null));
        cmd.addOption(Option.Option1("c", null));

        assertEquals(3, cmd.getOptions().length);
    }

    @Test
    public void testGetParsedOptionValue() throws Exception {
        final Options options = new Options();
        options.addOption0(OptionBuilder.hasArg0().withType0(Number.class).create2("i"));
        options.addOption0(OptionBuilder.hasArg0().create2("f"));

        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});

        assertEquals(123, ((Number) cmd.getParsedOptionValue2("i")).intValue());
        assertEquals("foo", cmd.getParsedOptionValue2("f"));
    }

    @Test
    public void testGetParsedOptionValueWithChar() throws Exception {
        final Options options = new Options();
        options.addOption0(Option.builder1("i").hasArg0().type(Number.class).build());
        options.addOption0(Option.builder1("f").hasArg0().build());

        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});

        assertEquals(123, ((Number) cmd.getParsedOptionValue0('i')).intValue());
        assertEquals("foo", cmd.getParsedOptionValue0('f'));
    }

    @Test
    public void testGetParsedOptionValueWithOption() throws Exception {
        final Options options = new Options();
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        final Option optF = Option.builder1("f").hasArg0().build();
        options.addOption0(optI);
        options.addOption0(optF);

        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});

        assertEquals(123, ((Number) cmd.getParsedOptionValue1(optI)).intValue());
        assertEquals("foo", cmd.getParsedOptionValue1(optF));
    }

    @Test
    public void testNullhOption() throws Exception {
        final Options options = new Options();
        final Option optI = Option.builder1("i").hasArg0().type(Number.class).build();
        final Option optF = Option.builder1("f").hasArg0().build();
        options.addOption0(optI);
        options.addOption0(optF);
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final CommandLine cmd = parser.parse0(options, new String[] {"-i", "123", "-f", "foo"});
        assertNull(cmd.getOptionValue2((Option) null));
        assertNull(cmd.getParsedOptionValue1((Option) null));
    }
}
