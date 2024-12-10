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

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 */
public class AnsiStringTest {

    @Test
    public void testCursorPosition_test0_decomposed() {
        Ansi.ansi0();
    }

    @Test
    public void testCursorPosition_test1_decomposed() {
        Ansi.ansi0();
        Ansi.ansi0().cursor(3, 6);
    }

    @Test
    public void testCursorPosition_test2_decomposed() {
        Ansi.ansi0();
        Ansi.ansi0().cursor(3, 6);
        Ansi ansi = Ansi.ansi0().cursor(3, 6).reset();
    }

    @Test
    public void testCursorPosition_test3_decomposed() {
        Ansi.ansi0();
        Ansi.ansi0().cursor(3, 6);
        Ansi ansi = Ansi.ansi0().cursor(3, 6).reset();
        assertEquals("\u001B[3;6H\u001B[m", ansi.toString());
    }
}
