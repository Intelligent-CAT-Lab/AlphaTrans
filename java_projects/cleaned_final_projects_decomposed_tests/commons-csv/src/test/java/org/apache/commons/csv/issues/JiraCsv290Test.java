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

package org.apache.commons.csv.issues;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.junit.jupiter.api.Test;

import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class JiraCsv290Test {

    private void testHelper(final String filename, final CSVFormat format) throws Exception {
        List<List<String>> content = new ArrayList<>();
        try (CSVParser csvParser =
                CSVParser.parse3(
                        new InputStreamReader(
                                this.getClass()
                                        .getResourceAsStream(
                                                "/org/apache/commons/csv/CSV-290/" + filename)),
                        format)) {
            content =
                    csvParser.stream()
                            .collect(Collectors.mapping(CSVRecord::toList, Collectors.toList()));
        }

        assertEquals(3, content.size());

        assertEquals("1", content.get(0).get(0));
        assertEquals("abc", content.get(0).get(1));
        assertEquals("test line 1\ntest line 2", content.get(0).get(2)); // new line
        assertEquals(null, content.get(0).get(3)); // null
        assertEquals("", content.get(0).get(4));

        assertEquals("2", content.get(1).get(0));
        assertEquals("\\b:\b \\t:\t \\n:\n \\r:\r", content.get(1).get(2)); // \b, \t, \n, \r

        assertEquals("3", content.get(2).get(0));
        assertEquals("b,c,d", content.get(2).get(2)); // value has comma
        assertEquals("\"quoted\"", content.get(2).get(3)); // quoted
    }

    @Test
    public void testPostgresqlCsv_test0_decomposed() throws Exception {
        testHelper("psql.csv", CSVFormat.POSTGRESQL_CSV);
    }

    @Test
    public void testPostgresqlText_test0_decomposed() throws Exception {
        testHelper("psql.tsv", CSVFormat.POSTGRESQL_TEXT);
    }
}