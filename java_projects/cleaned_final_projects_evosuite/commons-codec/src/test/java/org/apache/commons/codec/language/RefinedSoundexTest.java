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

package org.apache.commons.codec.language;

import static org.junit.Assert.assertEquals;

import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.StringEncoderAbstractTest;
import org.junit.Test;

/** Tests RefinedSoundex. */
public class RefinedSoundexTest extends StringEncoderAbstractTest<RefinedSoundex> {

    @Override
    protected RefinedSoundex createStringEncoder() {
        return new RefinedSoundex(2, null, null);
    }

    @Test
    public void testDifference() throws EncoderException {
        assertEquals(0, this.getStringEncoder().difference(null, null));
        assertEquals(0, this.getStringEncoder().difference("", ""));
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
        assertEquals(5, this.getStringEncoder().difference("Green", "Greene"));
        assertEquals(1, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        assertEquals(8, this.getStringEncoder().difference("Smithers", "Smythers"));
        assertEquals(5, this.getStringEncoder().difference("Anothers", "Brothers"));
    }

    @Test
    public void testEncode() {
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        assertEquals("J408106", this.getStringEncoder().encode1("jumped"));
        assertEquals("O0209", this.getStringEncoder().encode1("over"));
        assertEquals("T60", this.getStringEncoder().encode1("the"));
        assertEquals("L7050", this.getStringEncoder().encode1("lazy"));
        assertEquals("D6043", this.getStringEncoder().encode1("dogs"));

        assertEquals("D6043", RefinedSoundex.US_ENGLISH.encode1("dogs"));
    }

    @Test
    public void testGetMappingCodeNonLetter() {
        final char code = this.getStringEncoder().getMappingCode('#');
        assertEquals("Code does not equals zero", 0, code);
    }

    @Test
    public void testNewInstance() {
        assertEquals("D6043", new RefinedSoundex(2, null, null).soundex("dogs"));
    }

    @Test
    public void testNewInstance2() {
        assertEquals(
                "D6043",
                new RefinedSoundex(1, null, RefinedSoundex.US_ENGLISH_MAPPING_STRING.toCharArray())
                        .soundex("dogs"));
    }

    @Test
    public void testNewInstance3() {
        assertEquals(
                "D6043",
                new RefinedSoundex(0, RefinedSoundex.US_ENGLISH_MAPPING_STRING, null)
                        .soundex("dogs"));
    }
}
