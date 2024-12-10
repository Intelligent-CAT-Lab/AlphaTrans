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

package org.apache.commons.csv;

import org.junit.jupiter.params.provider.Arguments;

import java.util.Arrays;
import java.util.stream.Stream;

/**
 * Tests parsing of duplicate column names in a CSV header. The test verifies that headers are
 * consistently handled by CSVFormat and CSVParser.
 */
public class CSVDuplicateHeaderTest {

    /**
     * Return test cases for duplicate header data for use in CSVFormat.
     *
     * <p>This filters the parsing test data to all cases where the allow missing column names flag
     * is true and ignore header case is false: these flags are exclusively for parsing. CSVFormat
     * validation applies to both parsing and writing and thus validation is less strict and behaves
     * as if the allow missing column names constraint and the ignore header case behavior are
     * absent. The filtered data is then returned with the parser flags set to both true and false
     * for each test case.
     *
     * @return the stream of arguments
     */
    static Stream<Arguments> duplicateHeaderAllowsMissingColumnsNamesData() {
        return duplicateHeaderData()
                .filter(
                        arg ->
                                Boolean.TRUE.equals(arg.get()[1])
                                        && Boolean.FALSE.equals(arg.get()[2]))
                .flatMap(
                        arg -> {
                            final Object[][] data = new Object[4][];
                            final Boolean[] flags = {Boolean.TRUE, Boolean.FALSE};
                            int i = 0;
                            for (final Boolean a : flags) {
                                for (final Boolean b : flags) {
                                    data[i] = arg.get().clone();
                                    data[i][1] = a;
                                    data[i][2] = b;
                                    i++;
                                }
                            }
                            return Arrays.stream(data).map(Arguments::of);
                        });
    }

    /**
     * Return test cases for duplicate header data for use in parsing (CSVParser). Uses the order:
     *
     * <pre>
     * DuplicateHeaderMode duplicateHeaderMode
     * boolean allowMissingColumnNames
     * String[] headers
     * boolean valid
     * </pre>
     *
     * @return the stream of arguments
     */
    static Stream<Arguments> duplicateHeaderData() {
        return Stream.of(
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, false, false, new String[] {"A", "B"}, true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", "B"},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, false, false, new String[] {"A", "B"}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, true, false, new String[] {"A", "B"}, true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"A", "B"},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, true, false, new String[] {"A", "B"}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, false, false, new String[] {"A", ""}, false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, false, false, new String[] {"A", ""}, false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, true, false, new String[] {"A", ""}, true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY, true, false, new String[] {"A", ""}, true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, true, false, new String[] {"A", ""}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, false, false, new String[] {"A", " "}, false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {"A", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, true, false, new String[] {"A", " "}, true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"A", " "},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, true, false, new String[] {"A", " "}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {"A", null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {"A", null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, true, false, new String[] {"A", null}, true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"A", null},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, true, false, new String[] {"A", null}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, false, false, new String[] {"A", "A"}, false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", "A"},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, false, false, new String[] {"A", "A"}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, true, false, new String[] {"A", "A"}, false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"A", "A"},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, true, false, new String[] {"A", "A"}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, false, false, new String[] {"", ""}, false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, false, false, new String[] {"", ""}, false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, true, false, new String[] {"", ""}, false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY, true, false, new String[] {"", ""}, true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, true, false, new String[] {"", ""}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, false, false, new String[] {" ", " "}, false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {" ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {" ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, true, false, new String[] {" ", " "}, false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {" ", " "},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, true, false, new String[] {" ", " "}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {"   ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"   ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {"   ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        false,
                        new String[] {"   ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"   ", "   "},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        false,
                        new String[] {"   ", "   "},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        false,
                        new String[] {null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {null, null},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        false,
                        new String[] {null, null},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {" ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {" ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {" ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        false,
                        new String[] {" ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {" ", "   "},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        false,
                        new String[] {" ", "   "},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {" ", null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {" ", null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {" ", null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, true, false, new String[] {" ", null}, false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {" ", null},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, true, false, new String[] {" ", null}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {"A", "A", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", "A", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {"A", "A", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        false,
                        new String[] {"A", "A", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"A", "A", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        false,
                        new String[] {"A", "A", "", ""},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {"A", "B", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", "B", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {"A", "B", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        false,
                        new String[] {"A", "B", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"A", "B", "", ""},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        false,
                        new String[] {"A", "B", "", ""},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {"A", "A", " ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", "A", " ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {"A", "A", " ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        false,
                        new String[] {"A", "A", " ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"A", "A", " ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        false,
                        new String[] {"A", "A", " ", " "},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {"A", "A", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", "A", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {"A", "A", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        false,
                        new String[] {"A", "A", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"A", "A", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        false,
                        new String[] {"A", "A", null, null},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {"A", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {"A", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        false,
                        new String[] {"A", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"A", "", ""},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        false,
                        new String[] {"A", "", ""},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {"A", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {"A", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        false,
                        new String[] {"A", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"A", null, null},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        false,
                        new String[] {"A", null, null},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        false,
                        new String[] {"A", " ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        false,
                        new String[] {"A", " ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        false,
                        new String[] {"A", " ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        false,
                        new String[] {"A", " ", "   "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        false,
                        new String[] {"A", " ", "   "},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        false,
                        new String[] {"A", " ", "   "},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, false, true, new String[] {"A", "a"}, false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        true,
                        new String[] {"A", "a"},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, false, true, new String[] {"A", "a"}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW, true, true, new String[] {"A", "a"}, false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        true,
                        new String[] {"A", "a"},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL, true, true, new String[] {"A", "a"}, true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        true,
                        new String[] {"A", "a", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        true,
                        new String[] {"A", "a", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        true,
                        new String[] {"A", "a", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        true,
                        new String[] {"A", "a", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        true,
                        new String[] {"A", "a", "", ""},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        true,
                        new String[] {"A", "a", "", ""},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        true,
                        new String[] {"A", "a", " ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        true,
                        new String[] {"A", "a", " ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        true,
                        new String[] {"A", "a", " ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        true,
                        new String[] {"A", "a", " ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        true,
                        new String[] {"A", "a", " ", " "},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        true,
                        new String[] {"A", "a", " ", " "},
                        true),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        false,
                        true,
                        new String[] {"A", "a", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        false,
                        true,
                        new String[] {"A", "a", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        false,
                        true,
                        new String[] {"A", "a", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.DISALLOW,
                        true,
                        true,
                        new String[] {"A", "a", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_EMPTY,
                        true,
                        true,
                        new String[] {"A", "a", null, null},
                        false),
                Arguments.of(
                        DuplicateHeaderMode.ALLOW_ALL,
                        true,
                        true,
                        new String[] {"A", "a", null, null},
                        true));
    }

    /**
     * Tests duplicate headers with the CSVFormat.
     *
     * @param duplicateHeaderMode the duplicate header mode
     * @param allowMissingColumnNames the allow missing column names flag (only used for parsing)
     * @param ignoreHeaderCase the ignore header case flag (only used for parsing)
     * @param headers the headers
     * @param valid true if the settings are expected to be valid, otherwise expect a
     *     IllegalArgumentException
     */

    /**
     * Tests duplicate headers with the CSVParser.
     *
     * @param duplicateHeaderMode the duplicate header mode
     * @param allowMissingColumnNames the allow missing column names flag (only used for parsing)
     * @param ignoreHeaderCase the ignore header case flag (only used for parsing)
     * @param headers the headers (joined with the CSVFormat delimiter to create a string input)
     * @param valid true if the settings are expected to be valid, otherwise expect a
     *     IllegalArgumentException
     * @throws IOException Signals that an I/O exception has occurred.
     */

    
}
