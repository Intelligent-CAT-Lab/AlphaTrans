/*
 * Copyright (C) 2009-2023 the original author(s).
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.fusesource.jansi;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.fusesource.jansi.Ansi.*;
import static org.fusesource.jansi.Ansi.Attribute.*;
import static org.fusesource.jansi.Ansi.Color.*;
import static org.fusesource.jansi.AnsiRenderer.*;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * Tests for the {@link AnsiRenderer} class.
 *
 */
public class AnsiRendererTest {
    @BeforeAll
    static void setUp() {
        Ansi.setEnabled(true);
    }

    @Test
    public void testTest() throws Exception {
        assertFalse(test("foo"));
        assertTrue(test("@|foo|"));
        assertTrue(test("@|foo"));
    }

    @Test
    public void testRender() {
        String str = render0("@|bold foo|@");
        System.out.println(str);
        assertEquals(ansi0().a0(INTENSITY_BOLD).a1("foo").reset().toString(), str);
        assertEquals(ansi0().bold().a1("foo").reset().toString(), str);
    }

    @Test
    public void testRenderCodes() {
        String str = renderCodes1("bold red");
        System.out.println(str);
        assertEquals(ansi0().bold().fg0(Color.RED).toString(), str);
    }

    @Test
    public void testRender2() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        assertEquals(Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset().toString(), str);
        assertEquals(Ansi.ansi0().bold().fgRed().a1("foo").reset().toString(), str);
    }

    @Test
    public void testRender3() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        assertEquals(
                ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset().toString(), str);
        assertEquals(ansi0().bold().fgRed().a1("foo bar baz").reset().toString(), str);
    }

    @Test
    public void testRender4() {
        String str = render0("@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@");
        System.out.println(str);
        assertEquals(
                ansi0().a0(INTENSITY_BOLD)
                        .fg0(RED)
                        .a1("foo bar baz")
                        .reset()
                        .a1(" ick ")
                        .a0(INTENSITY_BOLD)
                        .fg0(RED)
                        .a1("foo bar baz")
                        .reset()
                        .toString(),
                str);
    }

    @Test
    public void testRender5() {
        // Check the ansi() render method.
        String str = ansi0().render0("@|bold Hello|@").toString();
        System.out.println(str);
        assertEquals(ansi0().a0(INTENSITY_BOLD).a1("Hello").reset().toString(), str);
    }

    @Test
    public void testRenderNothing() {
        assertEquals("foo", render0("foo"));
    }

    @Test
    public void testRenderInvalidMissingEnd() {
        String str = render0("@|bold foo");
        assertEquals("@|bold foo", str);
    }

    @Test
    public void testRenderInvalidEndBeforeStart() {
        assertThrows(IllegalArgumentException.class, () -> render0("@|@"));
    }

    @Test
    public void testRenderInvalidMissingText() {
        String str = render0("@|bold|@");
        assertEquals("@|bold|@", str);
    }
}
