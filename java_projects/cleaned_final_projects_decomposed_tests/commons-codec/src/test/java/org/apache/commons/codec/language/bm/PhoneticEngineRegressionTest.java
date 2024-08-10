/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.commons.codec.language.bm;

import static org.junit.Assert.*;

import org.junit.Test;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Map;
import java.util.TreeMap;

/**
 * Tests PhoneticEngine and Languages.LanguageSet in ways very similar to code found in solr-3.6.0.
 *
 * @since 1.7
 */
public class PhoneticEngineRegressionTest {

    

    

    

    

    /**
     * This code is similar in style to code found in Solr:
     * solr/core/src/java/org/apache/solr/analysis/BeiderMorseFilterFactory.java
     *
     * <p>Making a JUnit test out of it to protect Solr from possible future regressions in
     * Commons-Codec.
     */
    private static String encode(
            final Map<String, String> args, final boolean concat, final String input) {
        final Languages.LanguageSet languageSet;
        final PhoneticEngine engine;

        final String nameTypeArg = args.get("nameType");
        final NameType nameType =
                (nameTypeArg == null) ? NameType.GENERIC : NameType.valueOf(nameTypeArg);

        final String ruleTypeArg = args.get("ruleType");
        final RuleType ruleType =
                (ruleTypeArg == null) ? RuleType.APPROX : RuleType.valueOf(ruleTypeArg);

        engine = PhoneticEngine.PhoneticEngine0(nameType, ruleType, concat);

        final String languageSetArg = args.get("languageSet");
        if (languageSetArg == null || languageSetArg.equals("auto")) {
            languageSet = null;
        } else {
            languageSet =
                    Languages.LanguageSet.from(
                            new HashSet<>(Arrays.asList(languageSetArg.split(","))));
        }

        /*
            org/apache/lucene/analysis/phonetic/BeiderMorseFilter.java (lines 96-98) does this:

            encoded = (languages == null)
                ? engine.encode(termAtt.toString())
                : engine.encode(termAtt.toString(), languages);

            Hence our approach, below:
        */
        if (languageSet == null) {
            return engine.encode0(input);
        }
        return engine.encode1(input, languageSet);
    }

    @Test
    public void testSolrGENERIC_test0_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
    }

    @Test
    public void testSolrGENERIC_test1_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
    }

    @Test
    public void testSolrGENERIC_test2_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
    }

    @Test
    public void testSolrGENERIC_test3_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
    }

    @Test
    public void testSolrGENERIC_test4_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrGENERIC_test5_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
    }

    @Test
    public void testSolrGENERIC_test6_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
    }

    @Test
    public void testSolrGENERIC_test7_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
    }

    @Test
    public void testSolrGENERIC_test8_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
    }

    @Test
    public void testSolrGENERIC_test9_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrGENERIC_test10_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
    }

    @Test
    public void testSolrGENERIC_test11_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
    }

    @Test
    public void testSolrGENERIC_test12_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
    }

    @Test
    public void testSolrGENERIC_test13_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)");
    }

    @Test
    public void testSolrGENERIC_test14_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrGENERIC_test15_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|anzilo|ongilo|onxilo|onzilo");
        assertEquals(encode(args, true, "1234"), "");
    }

    @Test
    public void testSolrGENERIC_test16_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|anzilo|ongilo|onxilo|onzilo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
    }

    @Test
    public void testSolrGENERIC_test17_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|anzilo|ongilo|onxilo|onzilo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
    }

    @Test
    public void testSolrGENERIC_test18_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|anzilo|ongilo|onxilo|onzilo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)");
    }

    @Test
    public void testSolrGENERIC_test19_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|anzilo|ongilo|onxilo|onzilo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrGENERIC_test20_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|angelo|anhelo|anjelo|anxelo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|anzilo|ongilo|onxilo|onzilo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angilo|anxilo|anzilo|ongilo|onxilo|onzilo");
        assertEquals(encode(args, false, "1234"), "");
    }

    @Test
    public void testSolrASHKENAZI_test0_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
    }

    @Test
    public void testSolrASHKENAZI_test1_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
    }

    @Test
    public void testSolrASHKENAZI_test2_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
    }

    @Test
    public void testSolrASHKENAZI_test3_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
    }

    @Test
    public void testSolrASHKENAZI_test4_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrASHKENAZI_test5_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
    }

    @Test
    public void testSolrASHKENAZI_test6_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
    }

    @Test
    public void testSolrASHKENAZI_test7_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
    }

    @Test
    public void testSolrASHKENAZI_test8_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
    }

    @Test
    public void testSolrASHKENAZI_test9_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
    }

    @Test
    public void testSolrASHKENAZI_test10_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrASHKENAZI_test11_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
    }

    @Test
    public void testSolrASHKENAZI_test12_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
    }

    @Test
    public void testSolrASHKENAZI_test13_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
    }

    @Test
    public void testSolrASHKENAZI_test14_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
    }

    @Test
    public void testSolrASHKENAZI_test15_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
    }

    @Test
    public void testSolrASHKENAZI_test16_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrASHKENAZI_test17_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|ongilo|onxilo");
        assertEquals(encode(args, true, "1234"), "");
    }

    @Test
    public void testSolrASHKENAZI_test18_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|ongilo|onxilo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
    }

    @Test
    public void testSolrASHKENAZI_test19_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|ongilo|onxilo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
    }

    @Test
    public void testSolrASHKENAZI_test20_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|ongilo|onxilo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
    }

    @Test
    public void testSolrASHKENAZI_test21_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|ongilo|onxilo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
    }

    @Test
    public void testSolrASHKENAZI_test22_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|ongilo|onxilo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrASHKENAZI_test23_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "andZelo|angelo|anhelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "angilo|anxilo|ongilo|onxilo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "ASHKENAZI");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, false, "Angelo"),
                "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "angilo|anxilo|ongilo|onxilo");
        assertEquals(encode(args, false, "1234"), "");
    }

    @Test
    public void testSolrSEPHARDIC_test0_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
    }

    @Test
    public void testSolrSEPHARDIC_test1_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
    }

    @Test
    public void testSolrSEPHARDIC_test2_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
    }

    @Test
    public void testSolrSEPHARDIC_test3_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
    }

    @Test
    public void testSolrSEPHARDIC_test4_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrSEPHARDIC_test5_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
    }

    @Test
    public void testSolrSEPHARDIC_test6_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
    }

    @Test
    public void testSolrSEPHARDIC_test7_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
    }

    @Test
    public void testSolrSEPHARDIC_test8_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
    }

    @Test
    public void testSolrSEPHARDIC_test9_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
    }

    @Test
    public void testSolrSEPHARDIC_test10_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrSEPHARDIC_test11_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
    }

    @Test
    public void testSolrSEPHARDIC_test12_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
    }

    @Test
    public void testSolrSEPHARDIC_test13_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
    }

    @Test
    public void testSolrSEPHARDIC_test14_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
    }

    @Test
    public void testSolrSEPHARDIC_test15_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
    }

    @Test
    public void testSolrSEPHARDIC_test16_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrSEPHARDIC_test17_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(encode(args, true, "1234"), "");
    }

    @Test
    public void testSolrSEPHARDIC_test18_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
    }

    @Test
    public void testSolrSEPHARDIC_test19_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
    }

    @Test
    public void testSolrSEPHARDIC_test20_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
    }

    @Test
    public void testSolrSEPHARDIC_test21_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "danhila|danhilu|danzila|danzilu|nhila|nhilu|nzila|nzilu");
    }

    @Test
    public void testSolrSEPHARDIC_test22_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "danhila|danhilu|danzila|danzilu|nhila|nhilu|nzila|nzilu");
        args.put("languageSet", "italian,greek,spanish");
    }

    @Test
    public void testSolrSEPHARDIC_test23_decomposed()  {
        Map<String, String> args;
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, true, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, true, "D'Angelo"), "anZelo|andZelo|anxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, true, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "EXACT");
        assertEquals(encode(args, false, "Angelo"), "anZelo|andZelo|anxelo");
        assertEquals(encode(args, false, "D'Angelo"), "danZelo|dandZelo|danxelo");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(encode(args, false, "Angelo"), "andZelo|anxelo");
        assertEquals(encode(args, false, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, true, "D'Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(
                encode(args, true, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(encode(args, true, "1234"), "");
        args = new TreeMap<>();
        args.put("nameType", "SEPHARDIC");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(
                encode(args, false, "D'Angelo"),
                "danhila|danhilu|danzila|danzilu|nhila|nhilu|nzila|nzilu");
        args.put("languageSet", "italian,greek,spanish");
        assertEquals(
                encode(args, false, "Angelo"),
                "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu");
        assertEquals(encode(args, false, "1234"), "");
    }

    @Test
    public void testCompatibilityWithOriginalVersion_test0_decomposed()  {
        final Map<String, String> args = new TreeMap<>();
        args.put("nameType", "GENERIC");
    }

    @Test
    public void testCompatibilityWithOriginalVersion_test1_decomposed()  {
        final Map<String, String> args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        args.put("ruleType", "APPROX");
    }

    @Test
    public void testCompatibilityWithOriginalVersion_test2_decomposed()  {
        final Map<String, String> args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "abram"),
                "Ybram|Ybrom|abram|abran|abrom|abron|avram|avrom|obram|obran|obrom|obron|ovram|ovrom");
        assertEquals(encode(args, true, "Bendzin"), "bndzn|bntsn|bnzn|vndzn|vntsn");
    }

    @Test
    public void testCompatibilityWithOriginalVersion_test3_decomposed()  {
        final Map<String, String> args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "abram"),
                "Ybram|Ybrom|abram|abran|abrom|abron|avram|avrom|obram|obran|obrom|obron|ovram|ovrom");
        assertEquals(encode(args, true, "Bendzin"), "bndzn|bntsn|bnzn|vndzn|vntsn");
        args.put("nameType", "ASHKENAZI");
        args.put("ruleType", "APPROX");
    }

    @Test
    public void testCompatibilityWithOriginalVersion_test4_decomposed()  {
        final Map<String, String> args = new TreeMap<>();
        args.put("nameType", "GENERIC");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "abram"),
                "Ybram|Ybrom|abram|abran|abrom|abron|avram|avrom|obram|obran|obrom|obron|ovram|ovrom");
        assertEquals(encode(args, true, "Bendzin"), "bndzn|bntsn|bnzn|vndzn|vntsn");
        args.put("nameType", "ASHKENAZI");
        args.put("ruleType", "APPROX");
        assertEquals(
                encode(args, true, "abram"),
                "Ybram|Ybrom|abram|abrom|avram|avrom|imbram|imbrom|obram|obrom|ombram|ombrom|ovram|ovrom");
        assertEquals(
                encode(args, true, "Halpern"),
                "YlpYrn|Ylpirn|alpYrn|alpirn|olpYrn|olpirn|xalpirn|xolpirn");
    }
}