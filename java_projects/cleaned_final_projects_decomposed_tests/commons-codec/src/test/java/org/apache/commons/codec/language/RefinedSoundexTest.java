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
    public void testDifference_test0_decomposed() throws EncoderException {
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test1_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
    }

    @Test
    public void testDifference_test2_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test3_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
    }

    @Test
    public void testDifference_test4_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test5_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
    }

    @Test
    public void testDifference_test6_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test7_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
    }

    @Test
    public void testDifference_test8_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test9_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
    }

    @Test
    public void testDifference_test10_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test11_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
    }

    @Test
    public void testDifference_test12_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test13_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
    }

    @Test
    public void testDifference_test14_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test15_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().difference("Green", "Greene"));
    }

    @Test
    public void testDifference_test16_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test17_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
    }

    @Test
    public void testDifference_test18_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test19_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
    }

    @Test
    public void testDifference_test20_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test21_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(8, this.getStringEncoder().difference("Smithers", "Smythers"));
    }

    @Test
    public void testDifference_test22_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(8, this.getStringEncoder().difference("Smithers", "Smythers"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test23_decomposed() throws EncoderException {
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
        assertEquals(6, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        assertEquals(8, this.getStringEncoder().difference("Smithers", "Smythers"));
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().difference("Anothers", "Brothers"));
    }

    @Test
    public void testEncode_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testEncode_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
    }

    @Test
    public void testEncode_test2_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
    }

    @Test
    public void testEncode_test3_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
    }

    @Test
    public void testEncode_test4_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
    }

    @Test
    public void testEncode_test5_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
    }

    @Test
    public void testEncode_test6_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
    }

    @Test
    public void testEncode_test7_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
    }

    @Test
    public void testEncode_test8_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
    }

    @Test
    public void testEncode_test9_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
    }

    @Test
    public void testEncode_test10_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
    }

    @Test
    public void testEncode_test11_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
    }

    @Test
    public void testEncode_test12_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
    }

    @Test
    public void testEncode_test13_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        assertEquals("J408106", this.getStringEncoder().encode1("jumped"));
    }

    @Test
    public void testEncode_test14_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        assertEquals("J408106", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
    }

    @Test
    public void testEncode_test15_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        assertEquals("J408106", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        assertEquals("O0209", this.getStringEncoder().encode1("over"));
    }

    @Test
    public void testEncode_test16_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        assertEquals("J408106", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        assertEquals("O0209", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
    }

    @Test
    public void testEncode_test17_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        assertEquals("J408106", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        assertEquals("O0209", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("the"));
    }

    @Test
    public void testEncode_test18_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        assertEquals("J408106", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        assertEquals("O0209", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("the"));
        this.getStringEncoder();
    }

    @Test
    public void testEncode_test19_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        assertEquals("J408106", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        assertEquals("O0209", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("the"));
        this.getStringEncoder();
        assertEquals("L7050", this.getStringEncoder().encode1("lazy"));
    }

    @Test
    public void testEncode_test20_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        assertEquals("J408106", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        assertEquals("O0209", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("the"));
        this.getStringEncoder();
        assertEquals("L7050", this.getStringEncoder().encode1("lazy"));
        this.getStringEncoder();
    }

    @Test
    public void testEncode_test21_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        assertEquals("J408106", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        assertEquals("O0209", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("the"));
        this.getStringEncoder();
        assertEquals("L7050", this.getStringEncoder().encode1("lazy"));
        this.getStringEncoder();
        assertEquals("D6043", this.getStringEncoder().encode1("dogs"));
    }

    @Test
    public void testEncode_test22_decomposed()  {
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        assertEquals("T6036084", this.getStringEncoder().encode1("TESTING"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        assertEquals("Q503", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        assertEquals("B1908", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        assertEquals("F205", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        assertEquals("J408106", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        assertEquals("O0209", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
        assertEquals("T60", this.getStringEncoder().encode1("the"));
        this.getStringEncoder();
        assertEquals("L7050", this.getStringEncoder().encode1("lazy"));
        this.getStringEncoder();
        assertEquals("D6043", this.getStringEncoder().encode1("dogs"));
        assertEquals("D6043", RefinedSoundex.US_ENGLISH.encode1("dogs"));
    }

    @Test
    public void testGetMappingCodeNonLetter_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetMappingCodeNonLetter_test1_decomposed()  {
        this.getStringEncoder();
        final char code = this.getStringEncoder().getMappingCode('#');
    }

    @Test
    public void testGetMappingCodeNonLetter_test2_decomposed()  {
        this.getStringEncoder();
        final char code = this.getStringEncoder().getMappingCode('#');
        assertEquals("Code does not equals zero", 0, code);
    }

    @Test
    public void testNewInstance_test0_decomposed()  {
        assertEquals("D6043", new RefinedSoundex(2, null, null).soundex("dogs"));
    }

    @Test
    public void testNewInstance2_test0_decomposed()  {
        assertEquals(
                "D6043",
                new RefinedSoundex(1, null, RefinedSoundex.US_ENGLISH_MAPPING_STRING.toCharArray())
                        .soundex("dogs"));
    }

    @Test
    public void testNewInstance3_test0_decomposed()  {
        assertEquals(
                "D6043",
                new RefinedSoundex(0, RefinedSoundex.US_ENGLISH_MAPPING_STRING, null)
                        .soundex("dogs"));
    }
}