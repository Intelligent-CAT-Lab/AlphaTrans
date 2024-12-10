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

package org.apache.commons.cli.bug;

import static org.junit.Assert.assertFalse;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
import org.apache.commons.cli.PosixParser;
import org.junit.Test;

@SuppressWarnings("deprecation") // tests some deprecated classes
public class BugCLI133Test {

    @Test
    public void testOrder_test0_decomposed() throws ParseException {
        final Option optionA = Option.Option1("a", "first");
    }

    @Test
    public void testOrder_test1_decomposed() throws ParseException {
        final Option optionA = Option.Option1("a", "first");
        final Options opts = new Options();
    }

    @Test
    public void testOrder_test2_decomposed() throws ParseException {
        final Option optionA = Option.Option1("a", "first");
        final Options opts = new Options();
        opts.addOption0(optionA);
    }

    @Test
    public void testOrder_test3_decomposed() throws ParseException {
        final Option optionA = Option.Option1("a", "first");
        final Options opts = new Options();
        opts.addOption0(optionA);
        final PosixParser posixParser = new PosixParser();
    }

    @Test
    public void testOrder_test4_decomposed() throws ParseException {
        final Option optionA = Option.Option1("a", "first");
        final Options opts = new Options();
        opts.addOption0(optionA);
        final PosixParser posixParser = new PosixParser();
        final CommandLine line = posixParser.parse0(opts, null);
    }

    @Test
    public void testOrder_test5_decomposed() throws ParseException {
        final Option optionA = Option.Option1("a", "first");
        final Options opts = new Options();
        opts.addOption0(optionA);
        final PosixParser posixParser = new PosixParser();
        final CommandLine line = posixParser.parse0(opts, null);
        assertFalse(line.hasOption2((String) null));
    }
}