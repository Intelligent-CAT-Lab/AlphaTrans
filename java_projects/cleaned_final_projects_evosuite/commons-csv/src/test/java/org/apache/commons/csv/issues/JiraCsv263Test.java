
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


package org.apache.commons.csv.issues;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.QuoteMode;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.io.Reader;
import java.io.StringReader;

/** Tests [CSV-263] Print from Reader with embedded quotes generates incorrect output. */
public class JiraCsv263Test {

    @Test
    public void testPrintFromReaderWithQuotes() throws IOException {
        final CSVFormat format =
                CSVFormat.RFC4180
                        .builder()
                        .setDelimiter0(',')
                        .setQuote0('"')
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NON_NUMERIC)
                        .build();
        final StringBuilder out = new StringBuilder();

        final Reader atStartOnly = new StringReader("\"a,b,c\r\nx,y,z");
        format.print2(atStartOnly, out, true);
        assertEquals("\"\"\"a,b,c\r\nx,y,z\"", out.toString());

        final Reader atEndOnly = new StringReader("a,b,c\r\nx,y,z\"");
        out.setLength(0);
        format.print2(atEndOnly, out, true);
        assertEquals("\"a,b,c\r\nx,y,z\"\"\"", out.toString());

        final Reader atBeginEnd = new StringReader("\"a,b,c\r\nx,y,z\"");
        out.setLength(0);
        format.print2(atBeginEnd, out, true);
        assertEquals("\"\"\"a,b,c\r\nx,y,z\"\"\"", out.toString());

        final Reader embeddedBeginMiddle = new StringReader("\"a\",b,c\r\nx,\"y\",z");
        out.setLength(0);
        format.print2(embeddedBeginMiddle, out, true);
        assertEquals("\"\"\"a\"\",b,c\r\nx,\"\"y\"\",z\"", out.toString());

        final Reader embeddedMiddleEnd = new StringReader("a,\"b\",c\r\nx,y,\"z\"");
        out.setLength(0);
        format.print2(embeddedMiddleEnd, out, true);
        assertEquals("\"a,\"\"b\"\",c\r\nx,y,\"\"z\"\"\"", out.toString());

        final Reader nested = new StringReader("a,\"b \"and\" c\",d");
        out.setLength(0);
        format.print2(nested, out, true);
        assertEquals("\"a,\"\"b \"\"and\"\" c\"\",d\"", out.toString());
    }
}
