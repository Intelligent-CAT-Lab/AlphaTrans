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
    public void testTest_test0_decomposed() throws Exception {
        assertFalse(test("foo"));
        assertTrue(test("@|foo|"));
        assertTrue(test("@|foo"));
    }

    @Test
    public void testRender_test0_decomposed() {
        String str = render0("@|bold foo|@");
    }

    @Test
    public void testRender_test1_decomposed() {
        String str = render0("@|bold foo|@");
        System.out.println(str);
        ansi0();
    }

    @Test
    public void testRender_test2_decomposed() {
        String str = render0("@|bold foo|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
    }

    @Test
    public void testRender_test3_decomposed() {
        String str = render0("@|bold foo|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).a1("foo");
    }

    @Test
    public void testRender_test4_decomposed() {
        String str = render0("@|bold foo|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).a1("foo");
        ansi0().a0(INTENSITY_BOLD).a1("foo").reset();
    }

    @Test
    public void testRender_test5_decomposed() {
        String str = render0("@|bold foo|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).a1("foo");
        ansi0().a0(INTENSITY_BOLD).a1("foo").reset();
        assertEquals(ansi0().a0(INTENSITY_BOLD).a1("foo").reset().toString(), str);
    }

    @Test
    public void testRender_test6_decomposed() {
        String str = render0("@|bold foo|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).a1("foo");
        ansi0().a0(INTENSITY_BOLD).a1("foo").reset();
        assertEquals(ansi0().a0(INTENSITY_BOLD).a1("foo").reset().toString(), str);
        ansi0();
    }

    @Test
    public void testRender_test7_decomposed() {
        String str = render0("@|bold foo|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).a1("foo");
        ansi0().a0(INTENSITY_BOLD).a1("foo").reset();
        assertEquals(ansi0().a0(INTENSITY_BOLD).a1("foo").reset().toString(), str);
        ansi0();
        ansi0().bold();
    }

    @Test
    public void testRender_test8_decomposed() {
        String str = render0("@|bold foo|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).a1("foo");
        ansi0().a0(INTENSITY_BOLD).a1("foo").reset();
        assertEquals(ansi0().a0(INTENSITY_BOLD).a1("foo").reset().toString(), str);
        ansi0();
        ansi0().bold();
        ansi0().bold().a1("foo");
    }

    @Test
    public void testRender_test9_decomposed() {
        String str = render0("@|bold foo|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).a1("foo");
        ansi0().a0(INTENSITY_BOLD).a1("foo").reset();
        assertEquals(ansi0().a0(INTENSITY_BOLD).a1("foo").reset().toString(), str);
        ansi0();
        ansi0().bold();
        ansi0().bold().a1("foo");
        ansi0().bold().a1("foo").reset();
    }

    @Test
    public void testRender_test10_decomposed() {
        String str = render0("@|bold foo|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).a1("foo");
        ansi0().a0(INTENSITY_BOLD).a1("foo").reset();
        assertEquals(ansi0().a0(INTENSITY_BOLD).a1("foo").reset().toString(), str);
        ansi0();
        ansi0().bold();
        ansi0().bold().a1("foo");
        ansi0().bold().a1("foo").reset();
        assertEquals(ansi0().bold().a1("foo").reset().toString(), str);
    }

    @Test
    public void testRenderCodes_test0_decomposed() {
        String str = renderCodes1("bold red");
    }

    @Test
    public void testRenderCodes_test1_decomposed() {
        String str = renderCodes1("bold red");
        System.out.println(str);
        ansi0();
    }

    @Test
    public void testRenderCodes_test2_decomposed() {
        String str = renderCodes1("bold red");
        System.out.println(str);
        ansi0();
        ansi0().bold();
    }

    @Test
    public void testRenderCodes_test3_decomposed() {
        String str = renderCodes1("bold red");
        System.out.println(str);
        ansi0();
        ansi0().bold();
        ansi0().bold().fg0(Color.RED);
    }

    @Test
    public void testRenderCodes_test4_decomposed() {
        String str = renderCodes1("bold red");
        System.out.println(str);
        ansi0();
        ansi0().bold();
        ansi0().bold().fg0(Color.RED);
        assertEquals(ansi0().bold().fg0(Color.RED).toString(), str);
    }

    @Test
    public void testRender2_test0_decomposed() {
        String str = render0("@|bold,red foo|@");
    }

    @Test
    public void testRender2_test1_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
    }

    @Test
    public void testRender2_test2_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
        Ansi.ansi0().a0(INTENSITY_BOLD);
    }

    @Test
    public void testRender2_test3_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
        Ansi.ansi0().a0(INTENSITY_BOLD);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED);
    }

    @Test
    public void testRender2_test4_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
        Ansi.ansi0().a0(INTENSITY_BOLD);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo");
    }

    @Test
    public void testRender2_test5_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
        Ansi.ansi0().a0(INTENSITY_BOLD);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo");
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset();
    }

    @Test
    public void testRender2_test6_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
        Ansi.ansi0().a0(INTENSITY_BOLD);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo");
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset();
        assertEquals(Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset().toString(), str);
    }

    @Test
    public void testRender2_test7_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
        Ansi.ansi0().a0(INTENSITY_BOLD);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo");
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset();
        assertEquals(Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset().toString(), str);
        Ansi.ansi0();
    }

    @Test
    public void testRender2_test8_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
        Ansi.ansi0().a0(INTENSITY_BOLD);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo");
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset();
        assertEquals(Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset().toString(), str);
        Ansi.ansi0();
        Ansi.ansi0().bold();
    }

    @Test
    public void testRender2_test9_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
        Ansi.ansi0().a0(INTENSITY_BOLD);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo");
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset();
        assertEquals(Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset().toString(), str);
        Ansi.ansi0();
        Ansi.ansi0().bold();
        Ansi.ansi0().bold().fgRed();
    }

    @Test
    public void testRender2_test10_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
        Ansi.ansi0().a0(INTENSITY_BOLD);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo");
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset();
        assertEquals(Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset().toString(), str);
        Ansi.ansi0();
        Ansi.ansi0().bold();
        Ansi.ansi0().bold().fgRed();
        Ansi.ansi0().bold().fgRed().a1("foo");
    }

    @Test
    public void testRender2_test11_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
        Ansi.ansi0().a0(INTENSITY_BOLD);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo");
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset();
        assertEquals(Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset().toString(), str);
        Ansi.ansi0();
        Ansi.ansi0().bold();
        Ansi.ansi0().bold().fgRed();
        Ansi.ansi0().bold().fgRed().a1("foo");
        Ansi.ansi0().bold().fgRed().a1("foo").reset();
    }

    @Test
    public void testRender2_test12_decomposed() {
        String str = render0("@|bold,red foo|@");
        System.out.println(str);
        Ansi.ansi0();
        Ansi.ansi0().a0(INTENSITY_BOLD);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED);
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo");
        Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset();
        assertEquals(Ansi.ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo").reset().toString(), str);
        Ansi.ansi0();
        Ansi.ansi0().bold();
        Ansi.ansi0().bold().fgRed();
        Ansi.ansi0().bold().fgRed().a1("foo");
        Ansi.ansi0().bold().fgRed().a1("foo").reset();
        assertEquals(Ansi.ansi0().bold().fgRed().a1("foo").reset().toString(), str);
    }

    @Test
    public void testRender3_test0_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
    }

    @Test
    public void testRender3_test1_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
    }

    @Test
    public void testRender3_test2_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
    }

    @Test
    public void testRender3_test3_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
    }

    @Test
    public void testRender3_test4_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
    }

    @Test
    public void testRender3_test5_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset();
    }

    @Test
    public void testRender3_test6_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset();
        assertEquals(
                ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset().toString(), str);
    }

    @Test
    public void testRender3_test7_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset();
        assertEquals(
                ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset().toString(), str);
        ansi0();
    }

    @Test
    public void testRender3_test8_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset();
        assertEquals(
                ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset().toString(), str);
        ansi0();
        ansi0().bold();
    }

    @Test
    public void testRender3_test9_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset();
        assertEquals(
                ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset().toString(), str);
        ansi0();
        ansi0().bold();
        ansi0().bold().fgRed();
    }

    @Test
    public void testRender3_test10_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset();
        assertEquals(
                ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset().toString(), str);
        ansi0();
        ansi0().bold();
        ansi0().bold().fgRed();
        ansi0().bold().fgRed().a1("foo bar baz");
    }

    @Test
    public void testRender3_test11_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset();
        assertEquals(
                ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset().toString(), str);
        ansi0();
        ansi0().bold();
        ansi0().bold().fgRed();
        ansi0().bold().fgRed().a1("foo bar baz");
        ansi0().bold().fgRed().a1("foo bar baz").reset();
    }

    @Test
    public void testRender3_test12_decomposed() {
        String str = render0("@|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset();
        assertEquals(
                ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset().toString(), str);
        ansi0();
        ansi0().bold();
        ansi0().bold().fgRed();
        ansi0().bold().fgRed().a1("foo bar baz");
        ansi0().bold().fgRed().a1("foo bar baz").reset();
        assertEquals(ansi0().bold().fgRed().a1("foo bar baz").reset().toString(), str);
    }

    @Test
    public void testRender4_test0_decomposed() {
        String str = render0("@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@");
    }

    @Test
    public void testRender4_test1_decomposed() {
        String str = render0("@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
    }

    @Test
    public void testRender4_test2_decomposed() {
        String str = render0("@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
    }

    @Test
    public void testRender4_test3_decomposed() {
        String str = render0("@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
    }

    @Test
    public void testRender4_test4_decomposed() {
        String str = render0("@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
    }

    @Test
    public void testRender4_test5_decomposed() {
        String str = render0("@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset();
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset().a1(" ick ");
        ansi0().a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz")
                .reset()
                .a1(" ick ")
                .a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz")
                .reset()
                .a1(" ick ")
                .a0(INTENSITY_BOLD)
                .fg0(RED);
        ansi0().a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz")
                .reset()
                .a1(" ick ")
                .a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz")
                .reset()
                .a1(" ick ")
                .a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz")
                .reset();
    }

    @Test
    public void testRender4_test6_decomposed() {
        String str = render0("@|bold,red foo bar baz|@ ick @|bold,red foo bar baz|@");
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).fg0(RED);
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset();
        ansi0().a0(INTENSITY_BOLD).fg0(RED).a1("foo bar baz").reset().a1(" ick ");
        ansi0().a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz")
                .reset()
                .a1(" ick ")
                .a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz")
                .reset()
                .a1(" ick ")
                .a0(INTENSITY_BOLD)
                .fg0(RED);
        ansi0().a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz")
                .reset()
                .a1(" ick ")
                .a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz");
        ansi0().a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz")
                .reset()
                .a1(" ick ")
                .a0(INTENSITY_BOLD)
                .fg0(RED)
                .a1("foo bar baz")
                .reset();
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
    public void testRender5_test0_decomposed() {
        ansi0();
    }

    @Test
    public void testRender5_test1_decomposed() {
        ansi0();
        ansi0().render0("@|bold Hello|@");
    }

    @Test
    public void testRender5_test2_decomposed() {
        ansi0();
        ansi0().render0("@|bold Hello|@");
        String str = ansi0().render0("@|bold Hello|@").toString();
    }

    @Test
    public void testRender5_test3_decomposed() {
        ansi0();
        ansi0().render0("@|bold Hello|@");
        String str = ansi0().render0("@|bold Hello|@").toString();
        System.out.println(str);
        ansi0();
    }

    @Test
    public void testRender5_test4_decomposed() {
        ansi0();
        ansi0().render0("@|bold Hello|@");
        String str = ansi0().render0("@|bold Hello|@").toString();
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
    }

    @Test
    public void testRender5_test5_decomposed() {
        ansi0();
        ansi0().render0("@|bold Hello|@");
        String str = ansi0().render0("@|bold Hello|@").toString();
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).a1("Hello");
    }

    @Test
    public void testRender5_test6_decomposed() {
        ansi0();
        ansi0().render0("@|bold Hello|@");
        String str = ansi0().render0("@|bold Hello|@").toString();
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).a1("Hello");
        ansi0().a0(INTENSITY_BOLD).a1("Hello").reset();
    }

    @Test
    public void testRender5_test7_decomposed() {
        ansi0();
        ansi0().render0("@|bold Hello|@");
        String str = ansi0().render0("@|bold Hello|@").toString();
        System.out.println(str);
        ansi0();
        ansi0().a0(INTENSITY_BOLD);
        ansi0().a0(INTENSITY_BOLD).a1("Hello");
        ansi0().a0(INTENSITY_BOLD).a1("Hello").reset();
        assertEquals(ansi0().a0(INTENSITY_BOLD).a1("Hello").reset().toString(), str);
    }

    @Test
    public void testRenderNothing_test0_decomposed() {
        assertEquals("foo", render0("foo"));
    }

    @Test
    public void testRenderInvalidMissingEnd_test0_decomposed() {
        String str = render0("@|bold foo");
    }

    @Test
    public void testRenderInvalidMissingEnd_test1_decomposed() {
        String str = render0("@|bold foo");
        assertEquals("@|bold foo", str);
    }

    @Test
    public void testRenderInvalidEndBeforeStart_test0_decomposed() {
        assertThrows(IllegalArgumentException.class, () -> render0("@|@"));
    }

    @Test
    public void testRenderInvalidMissingText_test0_decomposed() {
        String str = render0("@|bold|@");
    }

    @Test
    public void testRenderInvalidMissingText_test1_decomposed() {
        String str = render0("@|bold|@");
        assertEquals("@|bold|@", str);
    }
}
