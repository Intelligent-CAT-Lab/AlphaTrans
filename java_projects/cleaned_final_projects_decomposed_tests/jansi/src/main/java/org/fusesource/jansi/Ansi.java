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

import java.util.ArrayList;
import java.util.concurrent.Callable;

import org.fusesource.jansi.Ansi.Erase;

/**
 * Provides a fluent API for generating
 * <a href="https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences">ANSI escape sequences</a>.
 *
 * @since 1.0
 */
public class Ansi implements Appendable {

    private static final char FIRST_ESC_CHAR = 27;
    private static final char SECOND_ESC_CHAR = '[';

    /**
     * <a href="https://en.wikipedia.org/wiki/ANSI_escape_code#Colors">ANSI 8 colors</a> for fluent API
     */
    public enum Color {
        BLACK(0, "BLACK"),
        RED(1, "RED"),
        GREEN(2, "GREEN"),
        YELLOW(3, "YELLOW"),
        BLUE(4, "BLUE"),
        MAGENTA(5, "MAGENTA"),
        CYAN(6, "CYAN"),
        WHITE(7, "WHITE"),
        DEFAULT(9, "DEFAULT");

        private final int value;
        private final String name;

        Color(int index, String name) {
            this.value = index;
            this.name = name;
        }

        @Override
        public String toString() {
            return name;
        }

        public int value() {
            return value;
        }

        public int fg() {
            return value + 30;
        }

        public int bg() {
            return value + 40;
        }

        public int fgBright() {
            return value + 90;
        }

        public int bgBright() {
            return value + 100;
        }
    }

    /**
     * Display attributes, also know as
     * <a href="https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters">SGR
     * (Select Graphic Rendition) parameters</a>.
     */
    public enum Attribute {
        RESET(0, "RESET"),
        INTENSITY_BOLD(1, "INTENSITY_BOLD"),
        INTENSITY_FAINT(2, "INTENSITY_FAINT"),
        ITALIC(3, "ITALIC_ON"),
        UNDERLINE(4, "UNDERLINE_ON"),
        BLINK_SLOW(5, "BLINK_SLOW"),
        BLINK_FAST(6, "BLINK_FAST"),
        NEGATIVE_ON(7, "NEGATIVE_ON"),
        CONCEAL_ON(8, "CONCEAL_ON"),
        STRIKETHROUGH_ON(9, "STRIKETHROUGH_ON"),
        UNDERLINE_DOUBLE(21, "UNDERLINE_DOUBLE"),
        INTENSITY_BOLD_OFF(22, "INTENSITY_BOLD_OFF"),
        ITALIC_OFF(23, "ITALIC_OFF"),
        UNDERLINE_OFF(24, "UNDERLINE_OFF"),
        BLINK_OFF(25, "BLINK_OFF"),
        NEGATIVE_OFF(27, "NEGATIVE_OFF"),
        CONCEAL_OFF(28, "CONCEAL_OFF"),
        STRIKETHROUGH_OFF(29, "STRIKETHROUGH_OFF");

        private final int value;
        private final String name;

        Attribute(int index, String name) {
            this.value = index;
            this.name = name;
        }

        @Override
        public String toString() {
            return name;
        }

        public int value() {
            return value;
        }
    }

    /**
     * ED (Erase in Display) / EL (Erase in Line) parameter (see
     * <a href="https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences">CSI sequence J and K</a>)
     * @see Ansi#eraseScreen(Erase)
     * @see Ansi#eraseLine(Erase)
     */
    public enum Erase {
        FORWARD(0, "FORWARD"),
        BACKWARD(1, "BACKWARD"),
        ALL(2, "ALL");

        private final int value;
        private final String name;

        Erase(int index, String name) {
            this.value = index;
            this.name = name;
        }

        @Override
        public String toString() {
            return name;
        }

        public int value() {
            return value;
        }
    }

    @FunctionalInterface
    public interface Consumer {
        void apply(Ansi ansi);
    }

    public static final String DISABLE = Ansi.class.getName() + ".disable";

    private static Callable<Boolean> detector = () -> !Boolean.getBoolean(DISABLE);

    public static void setDetector(final Callable<Boolean> detector) {
        if (detector == null) throw new IllegalArgumentException();
        Ansi.detector = detector;
    }

    public static boolean isDetected() {
        try {
            return detector.call();
        } catch (Exception e) {
            return true;
        }
    }

    private static final InheritableThreadLocal<Boolean> holder = new InheritableThreadLocal<Boolean>() {
        @Override
        protected Boolean initialValue() {
            return isDetected();
        }
    };

    public static void setEnabled(final boolean flag) {
        holder.set(flag);
    }

    public static boolean isEnabled() {
        return holder.get();
    }

    public static Ansi ansi0() {
        if (isEnabled()) {
            return Ansi.Ansi0();
        } else {
            return new NoAnsi(null);
        }
    }

    public static Ansi ansi1(StringBuilder builder) {
        if (isEnabled()) {
            return new Ansi(0, builder, null);
        } else {
            return new NoAnsi(builder);
        }
    }

    public static Ansi ansi2(int size) {
        if (isEnabled()) {
            return Ansi.Ansi2(size);
        } else {
            return new NoAnsi(size);
        }
    }

    private static class NoAnsi extends Ansi {

        public NoAnsi(Object args) {
            super(0, determineStringBuilder(args), null);
        }

        private static StringBuilder determineStringBuilder(Object args) {
            if (args == null) {
                return new StringBuilder(80);
            } else if (args instanceof Integer) {
                return new StringBuilder((Integer) args);
            } else if (args instanceof StringBuilder) {
                return (StringBuilder) args;
            } else {
                throw new IllegalArgumentException("Invalid argument type");
            }
        }

        // @Override
        public Ansi fg0(Color color) {
            return this;
        }

        // @Override
        public Ansi bg0(Color color) {
            return this;
        }

        @Override
        public Ansi fgBright(Color color) {
            return this;
        }

        @Override
        public Ansi bgBright(Color color) {
            return this;
        }

        // @Override
        public Ansi fg1(int color) {
            return this;
        }

        @Override
        public Ansi fgRgb1(int r, int g, int b) {
            return this;
        }

        // @Override
        public Ansi bg1(int color) {
            return this;
        }

        @Override
        public Ansi bgRgb1(int r, int g, int b) {
            return this;
        }

        @Override
        public Ansi a0(Attribute attribute) {
            return this;
        }

        @Override
        public Ansi cursor(int row, int column) {
            return this;
        }

        @Override
        public Ansi cursorToColumn(int x) {
            return this;
        }

        @Override
        public Ansi cursorUp(int y) {
            return this;
        }

        @Override
        public Ansi cursorRight(int x) {
            return this;
        }

        @Override
        public Ansi cursorDown(int y) {
            return this;
        }

        @Override
        public Ansi cursorLeft(int x) {
            return this;
        }

        // @Override
        public Ansi cursorDownLine0() {
            return this;
        }

        // @Override
        public Ansi cursorDownLine1(final int n) {
            return this;
        }

        // @Override
        public Ansi cursorUpLine0() {
            return this;
        }

        // @Override
        public Ansi cursorUpLine1(final int n) {
            return this;
        }

        // @Override
        public Ansi eraseScreen0() {
            return this;
        }

        // @Override
        public Ansi eraseScreen1(Erase kind) {
            return this;
        }

        // @Override
        public Ansi eraseLine0() {
            return this;
        }

        // @Override
        public Ansi eraseLine1(Erase kind) {
            return this;
        }

        @Override
        public Ansi scrollUp(int rows) {
            return this;
        }

        @Override
        public Ansi scrollDown(int rows) {
            return this;
        }

        @Override
        public Ansi saveCursorPosition() {
            return this;
        }

        @Override
        @Deprecated
        public Ansi restorCursorPosition() {
            return this;
        }

        @Override
        public Ansi restoreCursorPosition() {
            return this;
        }

        @Override
        public Ansi reset() {
            return this;
        }
    }

    private final StringBuilder builder;
    private final ArrayList<Integer> attributeOptions = new ArrayList<>(5);

    public static Ansi Ansi0() {
        return new Ansi(0, new StringBuilder(80), null);
    }

    public static Ansi Ansi1(Ansi parent) {
        return new Ansi(1, new StringBuilder(parent.builder), parent);
    }

    public static Ansi Ansi2(int size) {
        return new Ansi(0, new StringBuilder(size), null);
    }

    public Ansi(int constructorId, StringBuilder builder, Ansi parent) {

        this.builder = builder;

        if (constructorId == 1) {
            attributeOptions.addAll(parent.attributeOptions);
        }
    }

    public Ansi fg0(Color color) {
        attributeOptions.add(color.fg());
        return this;
    }

    public Ansi fg1(int color) {
        attributeOptions.add(38);
        attributeOptions.add(5);
        attributeOptions.add(color & 0xff);
        return this;
    }

    public Ansi fgRgb0(int color) {
        return fgRgb1(color >> 16, color >> 8, color);
    }

    public Ansi fgRgb1(int r, int g, int b) {
        attributeOptions.add(38);
        attributeOptions.add(2);
        attributeOptions.add(r & 0xff);
        attributeOptions.add(g & 0xff);
        attributeOptions.add(b & 0xff);
        return this;
    }

    public Ansi fgBlack() {
        return this.fg0(Color.BLACK);
    }

    public Ansi fgBlue() {
        return this.fg0(Color.BLUE);
    }

    public Ansi fgCyan() {
        return this.fg0(Color.CYAN);
    }

    public Ansi fgDefault() {
        return this.fg0(Color.DEFAULT);
    }

    public Ansi fgGreen() {
        return this.fg0(Color.GREEN);
    }

    public Ansi fgMagenta() {
        return this.fg0(Color.MAGENTA);
    }

    public Ansi fgRed() {
        return this.fg0(Color.RED);
    }

    public Ansi fgYellow() {
        return this.fg0(Color.YELLOW);
    }

    public Ansi bg0(Color color) {
        attributeOptions.add(color.bg());
        return this;
    }

    public Ansi bg1(int color) {
        attributeOptions.add(48);
        attributeOptions.add(5);
        attributeOptions.add(color & 0xff);
        return this;
    }

    public Ansi bgRgb0(int color) {
        return bgRgb1(color >> 16, color >> 8, color);
    }

    public Ansi bgRgb1(int r, int g, int b) {
        attributeOptions.add(48);
        attributeOptions.add(2);
        attributeOptions.add(r & 0xff);
        attributeOptions.add(g & 0xff);
        attributeOptions.add(b & 0xff);
        return this;
    }

    public Ansi bgCyan() {
        return this.bg0(Color.CYAN);
    }

    public Ansi bgDefault() {
        return this.bg0(Color.DEFAULT);
    }

    public Ansi bgGreen() {
        return this.bg0(Color.GREEN);
    }

    public Ansi bgMagenta() {
        return this.bg0(Color.MAGENTA);
    }

    public Ansi bgRed() {
        return this.bg0(Color.RED);
    }

    public Ansi bgYellow() {
        return this.bg0(Color.YELLOW);
    }

    public Ansi fgBright(Color color) {
        attributeOptions.add(color.fgBright());
        return this;
    }

    public Ansi fgBrightBlack() {
        return this.fgBright(Color.BLACK);
    }

    public Ansi fgBrightBlue() {
        return this.fgBright(Color.BLUE);
    }

    public Ansi fgBrightCyan() {
        return this.fgBright(Color.CYAN);
    }

    public Ansi fgBrightDefault() {
        return this.fgBright(Color.DEFAULT);
    }

    public Ansi fgBrightGreen() {
        return this.fgBright(Color.GREEN);
    }

    public Ansi fgBrightMagenta() {
        return this.fgBright(Color.MAGENTA);
    }

    public Ansi fgBrightRed() {
        return this.fgBright(Color.RED);
    }

    public Ansi fgBrightYellow() {
        return this.fgBright(Color.YELLOW);
    }

    public Ansi bgBright(Color color) {
        attributeOptions.add(color.bgBright());
        return this;
    }

    public Ansi bgBrightCyan() {
        return this.bgBright(Color.CYAN);
    }

    public Ansi bgBrightDefault() {
        return this.bgBright(Color.DEFAULT);
    }

    public Ansi bgBrightGreen() {
        return this.bgBright(Color.GREEN);
    }

    public Ansi bgBrightMagenta() {
        return this.bgBright(Color.MAGENTA);
    }

    public Ansi bgBrightRed() {
        return this.bgBright(Color.RED);
    }

    public Ansi bgBrightYellow() {
        return this.bgBright(Color.YELLOW);
    }

    public Ansi a0(Attribute attribute) {
        attributeOptions.add(attribute.value());
        return this;
    }

    /**
     * Moves the cursor to row n, column m. The values are 1-based.
     * Any values less than 1 are mapped to 1.
     *
     * @param row    row (1-based) from top
     * @param column column (1 based) from left
     * @return this Ansi instance
     */
    public Ansi cursor(final int row, final int column) {
        return appendEscapeSequence2('H', Math.max(1, row), Math.max(1, column));
    }

    /**
     * Moves the cursor to column n. The parameter n is 1-based.
     * If n is less than 1 it is moved to the first column.
     *
     * @param x the index (1-based) of the column to move to
     * @return this Ansi instance
     */
    public Ansi cursorToColumn(final int x) {
        return appendEscapeSequence1('G', Math.max(1, x));
    }

    /**
     * Moves the cursor up. If the parameter y is negative it moves the cursor down.
     *
     * @param y the number of lines to move up
     * @return this Ansi instance
     */
    public Ansi cursorUp(final int y) {
        return y > 0 ? appendEscapeSequence1('A', y) : y < 0 ? cursorDown(-y) : this;
    }

    /**
     * Moves the cursor down. If the parameter y is negative it moves the cursor up.
     *
     * @param y the number of lines to move down
     * @return this Ansi instance
     */
    public Ansi cursorDown(final int y) {
        return y > 0 ? appendEscapeSequence1('B', y) : y < 0 ? cursorUp(-y) : this;
    }

    /**
     * Moves the cursor right. If the parameter x is negative it moves the cursor left.
     *
     * @param x the number of characters to move right
     * @return this Ansi instance
     */
    public Ansi cursorRight(final int x) {
        return x > 0 ? appendEscapeSequence1('C', x) : x < 0 ? cursorLeft(-x) : this;
    }

    /**
     * Moves the cursor left. If the parameter x is negative it moves the cursor right.
     *
     * @param x the number of characters to move left
     * @return this Ansi instance
     */
    public Ansi cursorLeft(final int x) {
        return x > 0 ? appendEscapeSequence1('D', x) : x < 0 ? cursorRight(-x) : this;
    }

    /**
     * Moves the cursor relative to the current position. The cursor is moved right if x is
     * positive, left if negative and down if y is positive and up if negative.
     *
     * @param x the number of characters to move horizontally
     * @param y the number of lines to move vertically
     * @return this Ansi instance
     * @since 2.2
     */
    public Ansi cursorMove(final int x, final int y) {
        return cursorRight(x).cursorDown(y);
    }

    /**
     * Moves the cursor to the beginning of the line below.
     *
     * @return this Ansi instance
     */
    public Ansi cursorDownLine0() {
        return appendEscapeSequence0('E');
    }

    /**
     * Moves the cursor to the beginning of the n-th line below. If the parameter n is negative it
     * moves the cursor to the beginning of the n-th line above.
     *
     * @param n the number of lines to move the cursor
     * @return this Ansi instance
     */
    public Ansi cursorDownLine1(final int n) {
        return n < 0 ? cursorUpLine1(-n) : appendEscapeSequence1('E', n);
    }

    /**
     * Moves the cursor to the beginning of the line above.
     *
     * @return this Ansi instance
     */
    public Ansi cursorUpLine0() {
        return appendEscapeSequence0('F');
    }

    /**
     * Moves the cursor to the beginning of the n-th line above. If the parameter n is negative it
     * moves the cursor to the beginning of the n-th line below.
     *
     * @param n the number of lines to move the cursor
     * @return this Ansi instance
     */
    public Ansi cursorUpLine1(final int n) {
        return n < 0 ? cursorDownLine1(-n) : appendEscapeSequence1('F', n);
    }

    public Ansi eraseScreen0() {
        return appendEscapeSequence1('J', Erase.ALL.value());
    }

    public Ansi eraseScreen1(final Erase kind) {
        return appendEscapeSequence1('J', kind.value());
    }

    public Ansi eraseLine0() {
        return appendEscapeSequence0('K');
    }

    public Ansi eraseLine1(final Erase kind) {
        return appendEscapeSequence1('K', kind.value());
    }

    public Ansi scrollUp(final int rows) {
        if (rows == Integer.MIN_VALUE) {
            return scrollDown(Integer.MAX_VALUE);
        }
        return rows > 0 ? appendEscapeSequence1('S', rows) : rows < 0 ? scrollDown(-rows) : this;
    }

    public Ansi scrollDown(final int rows) {
        if (rows == Integer.MIN_VALUE) {
            return scrollUp(Integer.MAX_VALUE);
        }
        return rows > 0 ? appendEscapeSequence1('T', rows) : rows < 0 ? scrollUp(-rows) : this;
    }

    @Deprecated
    public Ansi restorCursorPosition() {
        return restoreCursorPosition();
    }

    public Ansi saveCursorPosition() {
        saveCursorPositionSCO();
        return saveCursorPositionDEC();
    }

    // SCO command
    public Ansi saveCursorPositionSCO() {
        return appendEscapeSequence0('s');
    }

    // DEC command
    public Ansi saveCursorPositionDEC() {
        builder.append(FIRST_ESC_CHAR);
        builder.append('7');
        return this;
    }

    public Ansi restoreCursorPosition() {
        restoreCursorPositionSCO();
        return restoreCursorPositionDEC();
    }

    // SCO command
    public Ansi restoreCursorPositionSCO() {
        return appendEscapeSequence0('u');
    }

    // DEC command
    public Ansi restoreCursorPositionDEC() {
        builder.append(FIRST_ESC_CHAR);
        builder.append('8');
        return this;
    }

    public Ansi reset() {
        return a0(Attribute.RESET);
    }

    public Ansi bold() {
        return a0(Attribute.INTENSITY_BOLD);
    }

    public Ansi boldOff() {
        return a0(Attribute.INTENSITY_BOLD_OFF);
    }

    public Ansi a1(String value) {
        flushAttributes();
        builder.append(value);
        return this;
    }

    public Ansi a2(boolean value) {
        flushAttributes();
        builder.append(value);
        return this;
    }

    public Ansi a3(char value) {
        flushAttributes();
        builder.append(value);
        return this;
    }

    public Ansi a4(char[] value, int offset, int len) {
        flushAttributes();
        builder.append(value, offset, len);
        return this;
    }

    public Ansi a5(char[] value) {
        flushAttributes();
        builder.append(value);
        return this;
    }

    public Ansi a6(CharSequence value, int start, int end) {
        flushAttributes();
        builder.append(value, start, end);
        return this;
    }

    public Ansi a7(CharSequence value) {
        flushAttributes();
        builder.append(value);
        return this;
    }

    public Ansi a8(double value) {
        flushAttributes();
        builder.append(value);
        return this;
    }

    public Ansi a9(float value) {
        flushAttributes();
        builder.append(value);
        return this;
    }

    public Ansi a10(int value) {
        flushAttributes();
        builder.append(value);
        return this;
    }

    public Ansi a11(long value) {
        flushAttributes();
        builder.append(value);
        return this;
    }

    public Ansi a12(Object value) {
        flushAttributes();
        builder.append(value);
        return this;
    }

    public Ansi a13(StringBuffer value) {
        flushAttributes();
        builder.append(value);
        return this;
    }

    public Ansi newline() {
        flushAttributes();
        builder.append(System.getProperty("line.separator"));
        return this;
    }

    public Ansi format(String pattern, Object... args) {
        flushAttributes();
        builder.append(String.format(pattern, args));
        return this;
    }

    /**
     * Applies another function to this Ansi instance.
     *
     * @param fun the function to apply
     * @return this Ansi instance
     * @since 2.2
     */
    public Ansi apply(Consumer fun) {
        fun.apply(this);
        return this;
    }

    /**
     * Uses the {@link AnsiRenderer}
     * to generate the ANSI escape sequences for the supplied text.
     *
     * @param text text
     * @return this
     * @since 2.2
     */
    public Ansi render0(final String text) {
        a1(AnsiRenderer.render0(text));
        return this;
    }

    /**
     * String formats and renders the supplied arguments.  Uses the {@link AnsiRenderer}
     * to generate the ANSI escape sequences.
     *
     * @param text format
     * @param args arguments
     * @return this
     * @since 2.2
     */
    public Ansi render1(final String text, Object... args) {
        a1(String.format(AnsiRenderer.render0(text), args));
        return this;
    }

    @Override
    public String toString() {
        flushAttributes();
        return builder.toString();
    }

    ///////////////////////////////////////////////////////////////////
    // Private Helper Methods
    ///////////////////////////////////////////////////////////////////

    private Ansi appendEscapeSequence0(char command) {
        flushAttributes();
        builder.append(FIRST_ESC_CHAR);
        builder.append(SECOND_ESC_CHAR);
        builder.append(command);
        return this;
    }

    private Ansi appendEscapeSequence1(char command, int option) {
        flushAttributes();
        builder.append(FIRST_ESC_CHAR);
        builder.append(SECOND_ESC_CHAR);
        builder.append(option);
        builder.append(command);
        return this;
    }

    private Ansi appendEscapeSequence2(char command, Object... options) {
        flushAttributes();
        return _appendEscapeSequence(command, options);
    }

    private void flushAttributes() {
        if (attributeOptions.isEmpty()) return;
        if (attributeOptions.size() == 1 && attributeOptions.get(0) == 0) {
            builder.append(FIRST_ESC_CHAR);
            builder.append(SECOND_ESC_CHAR);
            builder.append('m');
        } else {
            _appendEscapeSequence('m', attributeOptions.toArray());
        }
        attributeOptions.clear();
    }

    private Ansi _appendEscapeSequence(char command, Object... options) {
        builder.append(FIRST_ESC_CHAR);
        builder.append(SECOND_ESC_CHAR);
        int size = options.length;
        for (int i = 0; i < size; i++) {
            if (i != 0) {
                builder.append(';');
            }
            if (options[i] != null) {
                builder.append(options[i]);
            }
        }
        builder.append(command);
        return this;
    }

    @Override
    public Ansi append(CharSequence csq) {
        return append0(csq);
    }

    // @Override
    public Ansi append0(CharSequence csq) {
        builder.append(csq);
        return this;
    }

    @Override
    public Ansi append(CharSequence csq, int start, int end) {
        return append1(csq, start, end);
    }

    // @Override
    public Ansi append1(CharSequence csq, int start, int end) {
        builder.append(csq, start, end);
        return this;
    }

    @Override
    public Ansi append(char c) {
        return append2(c);
    }

    // @Override
    public Ansi append2(char c) {
        builder.append(c);
        return this;
    }
}
