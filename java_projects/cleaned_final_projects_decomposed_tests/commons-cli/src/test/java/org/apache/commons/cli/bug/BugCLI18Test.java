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

import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.junit.Test;

import java.io.PrintWriter;
import java.io.StringWriter;

/** https://issues.apache.org/jira/browse/CLI-18 */
public class BugCLI18Test {

    @Test
    public void testCLI18_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testCLI18_test1_decomposed()  {
        final Options options = new Options();
        options.addOption0(new Option(0, "a", "aaa", "aaaaaaa", false, null));
    }

    @Test
    public void testCLI18_test2_decomposed()  {
        final Options options = new Options();
        options.addOption0(new Option(0, "a", "aaa", "aaaaaaa", false, null));
        options.addOption0(
                new Option(
                        0,
                        null,
                        "bbb",
                        "bbbbbbb dksh fkshd fkhs dkfhsdk fhskd hksdks dhfowehfsdhfkjshf skfhkshf sf"
                                + " jkshfk sfh skfh skf f",
                        false,
                        null));
    }

    @Test
    public void testCLI18_test3_decomposed()  {
        final Options options = new Options();
        options.addOption0(new Option(0, "a", "aaa", "aaaaaaa", false, null));
        options.addOption0(
                new Option(
                        0,
                        null,
                        "bbb",
                        "bbbbbbb dksh fkshd fkhs dkfhsdk fhskd hksdks dhfowehfsdhfkjshf skfhkshf sf"
                                + " jkshfk sfh skfh skf f",
                        false,
                        null));
        options.addOption0(new Option(0, "c", null, "ccccccc", false, null));
    }

    @Test
    public void testCLI18_test4_decomposed()  {
        final Options options = new Options();
        options.addOption0(new Option(0, "a", "aaa", "aaaaaaa", false, null));
        options.addOption0(
                new Option(
                        0,
                        null,
                        "bbb",
                        "bbbbbbb dksh fkshd fkhs dkfhsdk fhskd hksdks dhfowehfsdhfkjshf skfhkshf sf"
                                + " jkshfk sfh skfh skf f",
                        false,
                        null));
        options.addOption0(new Option(0, "c", null, "ccccccc", false, null));
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testCLI18_test5_decomposed()  {
        final Options options = new Options();
        options.addOption0(new Option(0, "a", "aaa", "aaaaaaa", false, null));
        options.addOption0(
                new Option(
                        0,
                        null,
                        "bbb",
                        "bbbbbbb dksh fkshd fkhs dkfhsdk fhskd hksdks dhfowehfsdhfkjshf skfhkshf sf"
                                + " jkshfk sfh skfh skf f",
                        false,
                        null));
        options.addOption0(new Option(0, "c", null, "ccccccc", false, null));
        final HelpFormatter formatter = new HelpFormatter();
        final StringWriter out = new StringWriter();
        formatter.printHelp3(
                new PrintWriter(out),
                80,
                "foobar",
                "dsfkfsh kdh hsd hsdh fkshdf ksdh fskdh fsdh fkshfk sfdkjhskjh fkjh fkjsh khsdkj"
                        + " hfskdhf skjdfh ksf khf s",
                options,
                2,
                2,
                "blort j jgj j jg jhghjghjgjhgjhg jgjhgj jhg jhg hjg jgjhghjg jhg hjg jhgjg"
                        + " jgjhghjg jg jgjhgjgjg jhg jhgjh"
                        + '\r'
                        + '\n'
                        + "rarrr",
                true);
    }
}