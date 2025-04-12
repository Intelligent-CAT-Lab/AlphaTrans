
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


package org.apache.commons.codec.language.bm;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

/**
 * Tests Rule.
 *
 * @since 1.6
 */
public class RuleTest {

    private Rule.Phoneme[][] makePhonemes() {
        final String[][] words = {
            {"rinD", "rinDlt", "rina", "rinalt", "rino", "rinolt", "rinu", "rinult"},
            {"dortlaj", "dortlej", "ortlaj", "ortlej", "ortlej-dortlaj"}
        };
        final Rule.Phoneme[][] phonemes = new Rule.Phoneme[words.length][];

        for (int i = 0; i < words.length; i++) {
            final String[] words_i = words[i];
            final Rule.Phoneme[] phonemes_i = phonemes[i] = new Rule.Phoneme[words_i.length];
            for (int j = 0; j < words_i.length; j++) {
                phonemes_i[j] = new Rule.Phoneme(2, words_i[j], Languages.NO_LANGUAGES, null);
            }
        }

        return phonemes;
    }

    @Test
    public void testPhonemeComparedToSelfIsZero() {
        for (final Rule.Phoneme[] phs : makePhonemes()) {
            for (final Rule.Phoneme ph : phs) {
                assertEquals(
                        "Phoneme compared to itself should be zero: " + ph.getPhonemeText(),
                        0,
                        Rule.Phoneme.COMPARATOR.compare(ph, ph));
            }
        }
    }

    @Test
    public void testSubSequenceWorks() {

        final Rule.Phoneme a = new Rule.Phoneme(2, "a", null, null);
        final Rule.Phoneme b = new Rule.Phoneme(2, "b", null, null);
        final Rule.Phoneme cd = new Rule.Phoneme(2, "cd", null, null);
        final Rule.Phoneme ef = new Rule.Phoneme(2, "ef", null, null);
        final Rule.Phoneme ghi = new Rule.Phoneme(2, "ghi", null, null);
        final Rule.Phoneme jkl = new Rule.Phoneme(2, "jkl", null, null);

        assertEquals('a', a.getPhonemeText().charAt(0));
        assertEquals('b', b.getPhonemeText().charAt(0));
        assertEquals('c', cd.getPhonemeText().charAt(0));
        assertEquals('d', cd.getPhonemeText().charAt(1));
        assertEquals('e', ef.getPhonemeText().charAt(0));
        assertEquals('f', ef.getPhonemeText().charAt(1));
        assertEquals('g', ghi.getPhonemeText().charAt(0));
        assertEquals('h', ghi.getPhonemeText().charAt(1));
        assertEquals('i', ghi.getPhonemeText().charAt(2));
        assertEquals('j', jkl.getPhonemeText().charAt(0));
        assertEquals('k', jkl.getPhonemeText().charAt(1));
        assertEquals('l', jkl.getPhonemeText().charAt(2));

        System.out.println("a: " + a.getPhonemeText());
        System.out.println("b: " + b.getPhonemeText());

        final Rule.Phoneme a_b = Rule.Phoneme.Phoneme0(a, b);
        assertEquals('a', a_b.getPhonemeText().charAt(0));
        assertEquals('b', a_b.getPhonemeText().charAt(1));
        assertEquals("ab", a_b.getPhonemeText().subSequence(0, 2).toString());
        assertEquals("a", a_b.getPhonemeText().subSequence(0, 1).toString());
        assertEquals("b", a_b.getPhonemeText().subSequence(1, 2).toString());

        final Rule.Phoneme cd_ef = Rule.Phoneme.Phoneme0(cd, ef);
        assertEquals('c', cd_ef.getPhonemeText().charAt(0));
        assertEquals('d', cd_ef.getPhonemeText().charAt(1));
        assertEquals('e', cd_ef.getPhonemeText().charAt(2));
        assertEquals('f', cd_ef.getPhonemeText().charAt(3));
        assertEquals("c", cd_ef.getPhonemeText().subSequence(0, 1).toString());
        assertEquals("d", cd_ef.getPhonemeText().subSequence(1, 2).toString());
        assertEquals("e", cd_ef.getPhonemeText().subSequence(2, 3).toString());
        assertEquals("f", cd_ef.getPhonemeText().subSequence(3, 4).toString());
        assertEquals("cd", cd_ef.getPhonemeText().subSequence(0, 2).toString());
        assertEquals("de", cd_ef.getPhonemeText().subSequence(1, 3).toString());
        assertEquals("ef", cd_ef.getPhonemeText().subSequence(2, 4).toString());
        assertEquals("cde", cd_ef.getPhonemeText().subSequence(0, 3).toString());
        assertEquals("def", cd_ef.getPhonemeText().subSequence(1, 4).toString());
        assertEquals("cdef", cd_ef.getPhonemeText().subSequence(0, 4).toString());

        final Rule.Phoneme a_b_cd = Rule.Phoneme.Phoneme0(Rule.Phoneme.Phoneme0(a, b), cd);
        assertEquals('a', a_b_cd.getPhonemeText().charAt(0));
        assertEquals('b', a_b_cd.getPhonemeText().charAt(1));
        assertEquals('c', a_b_cd.getPhonemeText().charAt(2));
        assertEquals('d', a_b_cd.getPhonemeText().charAt(3));
        assertEquals("a", a_b_cd.getPhonemeText().subSequence(0, 1).toString());
        assertEquals("b", a_b_cd.getPhonemeText().subSequence(1, 2).toString());
        assertEquals("c", a_b_cd.getPhonemeText().subSequence(2, 3).toString());
        assertEquals("d", a_b_cd.getPhonemeText().subSequence(3, 4).toString());
        assertEquals("ab", a_b_cd.getPhonemeText().subSequence(0, 2).toString());
        assertEquals("bc", a_b_cd.getPhonemeText().subSequence(1, 3).toString());
        assertEquals("cd", a_b_cd.getPhonemeText().subSequence(2, 4).toString());
        assertEquals("abc", a_b_cd.getPhonemeText().subSequence(0, 3).toString());
        assertEquals("bcd", a_b_cd.getPhonemeText().subSequence(1, 4).toString());
        assertEquals("abcd", a_b_cd.getPhonemeText().subSequence(0, 4).toString());
    }
}
