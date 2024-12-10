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

import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.nio.file.Path;
import java.nio.file.Paths;

import org.fusesource.jansi.Ansi.Color;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.condition.EnabledOnOs;
import org.junit.jupiter.api.condition.OS;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * Tests for the {@link Ansi} class.
 *
 */
public class AnsiTest {

    @ParameterizedTest
    @CsvSource({
        "-2147483648,ESC[2147483647T", "2147483647,ESC[2147483647S",
        "-100000,ESC[100000T", "100000,ESC[100000S"
    })
    public void testScrollUp(int x, String expected) {
        assertAnsi(expected, Ansi.ansi0().scrollUp(x));
    }

    @ParameterizedTest
    @CsvSource({
        "-2147483648,ESC[2147483647S", "2147483647,ESC[2147483647T",
        "-100000,ESC[100000S", "100000,ESC[100000T"
    })
    public void testScrollDown(int x, String expected) {
        assertAnsi(expected, Ansi.ansi0().scrollDown(x));
    }

    @ParameterizedTest
    @CsvSource({
        "-1,-1,ESC[1;1H", "-1,0,ESC[1;1H", "-1,1,ESC[1;1H", "-1,2,ESC[1;2H",
        "0,-1,ESC[1;1H", "0,0,ESC[1;1H", "0,1,ESC[1;1H", "0,2,ESC[1;2H",
        "1,-1,ESC[1;1H", "1,0,ESC[1;1H", "1,1,ESC[1;1H", "1,2,ESC[1;2H",
        "2,-1,ESC[2;1H", "2,0,ESC[2;1H", "2,1,ESC[2;1H", "2,2,ESC[2;2H"
    })
    public void testCursor(int x, int y, String expected) {
        assertAnsi(expected, Ansi.Ansi0().cursor(x, y));
    }

    @ParameterizedTest
    @CsvSource({"-1,ESC[1G", "0,ESC[1G", "1,ESC[1G", "2,ESC[2G"})
    public void testCursorToColumn(int x, String expected) {
        assertAnsi(expected, Ansi.Ansi0().cursorToColumn(x));
    }

    @ParameterizedTest
    @CsvSource({"-2,ESC[2B", "-1,ESC[1B", "0,''", "1,ESC[1A", "2,ESC[2A"})
    public void testCursorUp(int y, String expected) {
        assertAnsi(expected, Ansi.Ansi0().cursorUp(y));
    }

    @ParameterizedTest
    @CsvSource({"-2,ESC[2A", "-1,ESC[1A", "0,''", "1,ESC[1B", "2,ESC[2B"})
    public void testCursorDown(int y, String expected) {
        assertAnsi(expected, Ansi.Ansi0().cursorDown(y));
    }

    @ParameterizedTest
    @CsvSource({"-2,ESC[2D", "-1,ESC[1D", "0,''", "1,ESC[1C", "2,ESC[2C"})
    public void testCursorRight(int x, String expected) {
        assertAnsi(expected, Ansi.Ansi0().cursorRight(x));
    }

    @ParameterizedTest
    @CsvSource({"-2,ESC[2C", "-1,ESC[1C", "0,''", "1,ESC[1D", "2,ESC[2D"})
    public void testCursorLeft(int x, String expected) {
        assertAnsi(expected, Ansi.Ansi0().cursorLeft(x));
    }

    @ParameterizedTest
    @CsvSource({
        "-2,-2,ESC[2DESC[2A", "-2,-1,ESC[2DESC[1A", "-2,0,ESC[2D", "-2,1,ESC[2DESC[1B", "-2,2,ESC[2DESC[2B",
        "-1,-2,ESC[1DESC[2A", "-1,-1,ESC[1DESC[1A", "-1,0,ESC[1D", "-1,1,ESC[1DESC[1B", "-1,2,ESC[1DESC[2B",
        "0,-2,ESC[2A", "0,-1,ESC[1A", "0,0,''", "0,1,ESC[1B", "0,2,ESC[2B",
        "1,-2,ESC[1CESC[2A", "1,-1,ESC[1CESC[1A", "1,0,ESC[1C", "1,1,ESC[1CESC[1B", "1,2,ESC[1CESC[2B",
        "2,-2,ESC[2CESC[2A", "2,-1,ESC[2CESC[1A", "2,0,ESC[2C", "2,1,ESC[2CESC[1B", "2,2,ESC[2CESC[2B"
    })
    public void testCursorMove(int x, int y, String expected) {
        assertAnsi(expected, Ansi.Ansi0().cursorMove(x, y));
    }

    @ParameterizedTest
    @CsvSource({"-2,ESC[2F", "-1,ESC[1F", "0,ESC[0E", "1,ESC[1E", "2,ESC[2E"})
    public void testCursorDownLine1(int n, String expected) {
        assertAnsi(expected, Ansi.Ansi0().cursorDownLine1(n));
    }

    @ParameterizedTest
    @CsvSource({"-2,ESC[2E", "-1,ESC[1E", "0,ESC[0F", "1,ESC[1F", "2,ESC[2F"})
    public void testCursorUpLine1(int n, String expected) {
        assertAnsi(expected, Ansi.Ansi0().cursorUpLine1(n));
    }

    @Test
    @EnabledOnOs(OS.WINDOWS)
    @Disabled("Does not really fail: launch `javaw -jar jansi-xxx.jar` directly instead")
    public void testAnsiMainWithNoConsole() throws Exception {
        Path javaHome = Paths.get(System.getProperty("java.home"));
        Path java = javaHome.resolve("bin\\javaw.exe");
        String cp = System.getProperty("java.class.path");

        Process process = new ProcessBuilder()
                .command(java.toString(), "-cp", cp, AnsiMain.class.getName())
                .start();

        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        try (InputStream in = process.getInputStream()) {
            byte[] buffer = new byte[8192];
            while (true) {
                int nb = in.read(buffer);
                if (nb > 0) {
                    baos.write(buffer, 0, nb);
                } else {
                    break;
                }
            }
        }

        assertTrue(baos.toString().contains("test on System.out"), baos.toString());
    }

    private static void assertAnsi(String expected, Ansi actual) {
        assertEquals(expected.replace("ESC", "\033"), actual.toString());
    }

    @Test
    public void testSetEnabled_test0_decomposed() throws Exception {
        Ansi.setEnabled(false);
    }

    @Test
    public void testSetEnabled_test1_decomposed() throws Exception {
        Ansi.setEnabled(false);
        Ansi.isEnabled();
    }

    @Test
    public void testSetEnabled_test2_decomposed() throws Exception {
        Ansi.setEnabled(false);
        Ansi.isEnabled();
        new Thread(() -> assertFalse(Ansi.isEnabled())).run();
    }

    @Test
    public void testSetEnabled_test3_decomposed() throws Exception {
        Ansi.setEnabled(false);
        Ansi.isEnabled();
        new Thread(() -> assertFalse(Ansi.isEnabled())).run();
        Ansi.setEnabled(true);
    }

    @Test
    public void testSetEnabled_test4_decomposed() throws Exception {
        Ansi.setEnabled(false);
        Ansi.isEnabled();
        new Thread(() -> assertFalse(Ansi.isEnabled())).run();
        Ansi.setEnabled(true);
        Ansi.isEnabled();
    }

    @Test
    public void testSetEnabled_test5_decomposed() throws Exception {
        Ansi.setEnabled(false);
        Ansi.isEnabled();
        new Thread(() -> assertFalse(Ansi.isEnabled())).run();
        Ansi.setEnabled(true);
        Ansi.isEnabled();
        new Thread(() -> assertTrue(Ansi.isEnabled())).run();
    }

    @Test
    public void testClone_test0_decomposed() throws CloneNotSupportedException {
        Ansi.ansi0();
    }

    @Test
    public void testClone_test1_decomposed() throws CloneNotSupportedException {
        Ansi.ansi0();
        Ansi.ansi0().a1("Some text");
    }

    @Test
    public void testClone_test2_decomposed() throws CloneNotSupportedException {
        Ansi.ansi0();
        Ansi.ansi0().a1("Some text");
        Ansi.ansi0().a1("Some text").bg0(Color.BLACK);
    }

    @Test
    public void testClone_test3_decomposed() throws CloneNotSupportedException {
        Ansi.ansi0();
        Ansi.ansi0().a1("Some text");
        Ansi.ansi0().a1("Some text").bg0(Color.BLACK);
        Ansi ansi = Ansi.ansi0().a1("Some text").bg0(Color.BLACK).fg0(Color.WHITE);
    }

    @Test
    public void testClone_test4_decomposed() throws CloneNotSupportedException {
        Ansi.ansi0();
        Ansi.ansi0().a1("Some text");
        Ansi.ansi0().a1("Some text").bg0(Color.BLACK);
        Ansi ansi = Ansi.ansi0().a1("Some text").bg0(Color.BLACK).fg0(Color.WHITE);
        Ansi clone = Ansi.Ansi1(ansi);
    }

    @Test
    public void testClone_test5_decomposed() throws CloneNotSupportedException {
        Ansi.ansi0();
        Ansi.ansi0().a1("Some text");
        Ansi.ansi0().a1("Some text").bg0(Color.BLACK);
        Ansi ansi = Ansi.ansi0().a1("Some text").bg0(Color.BLACK).fg0(Color.WHITE);
        Ansi clone = Ansi.Ansi1(ansi);
        ansi.a1("test");
        clone.a1("test");
    }

    @Test
    public void testClone_test6_decomposed() throws CloneNotSupportedException {
        Ansi.ansi0();
        Ansi.ansi0().a1("Some text");
        Ansi.ansi0().a1("Some text").bg0(Color.BLACK);
        Ansi ansi = Ansi.ansi0().a1("Some text").bg0(Color.BLACK).fg0(Color.WHITE);
        Ansi clone = Ansi.Ansi1(ansi);
        ansi.a1("test");
        clone.a1("test");
        ansi.a1("test").reset();
        clone.a1("test").reset();
    }

    @Test
    public void testClone() throws CloneNotSupportedException {
        Ansi ansi = Ansi.ansi0().a1("Some text").bg0(Color.BLACK).fg0(Color.WHITE);
        Ansi clone = Ansi.Ansi1(ansi);

        assertEquals(
                ansi.a1("test").reset().toString(), clone.a1("test").reset().toString());
    }

    @Test
    public void testApply_test0_decomposed() {
        Ansi.ansi0();
    }

    @Test
    public void testApply_test1_decomposed() {
        Ansi.ansi0();
        Ansi.ansi0().apply(ansi -> ansi.a1("test"));
    }

    @Test
    public void testApply_test2_decomposed() {
        Ansi.ansi0();
        Ansi.ansi0().apply(ansi -> ansi.a1("test"));
        assertEquals("test", Ansi.ansi0().apply(ansi -> ansi.a1("test")).toString());
    }

    @Test
    public void testCursorDownLine0_test0_decomposed() {
        Ansi.Ansi0();
    }

    @Test
    public void testCursorDownLine0_test1_decomposed() {
        Ansi.Ansi0();
        assertAnsi("ESC[E", Ansi.Ansi0().cursorDownLine0());
    }

    @Test
    public void testCursorUpLine0_test0_decomposed() {
        Ansi.Ansi0();
    }

    @Test
    public void testCursorUpLine0_test1_decomposed() {
        Ansi.Ansi0();
        assertAnsi("ESC[F", Ansi.Ansi0().cursorUpLine0());
    }

    @Test
    public void testColorDisabled_test0_decomposed() {
        Ansi.setEnabled(false);
    }

    @Test
    public void testColorDisabled_test1_decomposed() {
        Ansi.setEnabled(false);
        try {
            assertEquals(
                    "test",
                    Ansi.ansi0()
                            .fg1(32)
                            .a1("t")
                            .fgRgb0(0)
                            .a1("e")
                            .bg1(24)
                            .a1("s")
                            .bgRgb0(100)
                            .a1("t")
                            .toString());
        } finally {
            Ansi.setEnabled(true);
        }
    }
}
