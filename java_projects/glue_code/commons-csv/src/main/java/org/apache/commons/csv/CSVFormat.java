package org.apache.commons.csv;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.csv.ContextInitializer;
import org.apache.commons.csv.ExceptionHandler;
import org.apache.commons.csv.IntegrationUtils;
import java.io.IOException;
import java.io.Serializable;
import java.io.Reader;
import java.io.Writer;
import java.nio.charset.Charset;
import java.io.File;
import java.nio.file.Path;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;
import java.io.StringWriter;
import java.util.Set;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Objects;
import static org.apache.commons.csv.Constants.BACKSLASH;
import static org.apache.commons.csv.Constants.COMMA;
import static org.apache.commons.csv.Constants.COMMENT;
import static org.apache.commons.csv.Constants.CR;
import static org.apache.commons.csv.Constants.CRLF;
import static org.apache.commons.csv.Constants.DOUBLE_QUOTE_CHAR;
import static org.apache.commons.csv.Constants.EMPTY;
import static org.apache.commons.csv.Constants.LF;
import static org.apache.commons.csv.Constants.PIPE;
import static org.apache.commons.csv.Constants.SP;
import static org.apache.commons.csv.Constants.TAB;
    public static class Builder {
    private static Value clz = ContextInitializer.getPythonClass("/CSVFormat.py", "Builder");
    private Value obj;
    public Builder(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public Builder setAllowDuplicateHeaderNames(final boolean allowDuplicateHeaderNames) {
// 
// setDuplicateHeaderMode(
// allowDuplicateHeaderNames
// ? DuplicateHeaderMode.ALLOW_ALL
// : DuplicateHeaderMode.ALLOW_EMPTY);
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setAllowDuplicateHeaderNames", allowDuplicateHeaderNames).as(Builder.class);
}
        public Builder setTrim(final boolean trim) {
// 
// this.trim = trim;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setTrim", trim).as(Builder.class);
}
        public Builder setTrailingDelimiter(final boolean trailingDelimiter) {
// 
// this.trailingDelimiter = trailingDelimiter;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setTrailingDelimiter", trailingDelimiter).as(Builder.class);
}
        public Builder setSkipHeaderRecord(final boolean skipHeaderRecord) {
// 
// this.skipHeaderRecord = skipHeaderRecord;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setSkipHeaderRecord", skipHeaderRecord).as(Builder.class);
}
        public Builder setRecordSeparator1(final String recordSeparator) {
// 
// this.recordSeparator = recordSeparator;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setRecordSeparator1", recordSeparator).as(Builder.class);
}
        public Builder setRecordSeparator0(final char recordSeparator) {
// 
// this.recordSeparator = String.valueOf(recordSeparator);
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setRecordSeparator0", recordSeparator).as(Builder.class);
}
        public Builder setQuoteMode(final QuoteMode quoteMode) {
// 
// this.quoteMode = quoteMode;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setQuoteMode", quoteMode).as(Builder.class);
}
        public Builder setQuote1(final Character quoteCharacter) {
// 
// if (isLineBreak1(quoteCharacter)) {
// throw new IllegalArgumentException("The quoteChar cannot be a line break");
// }
// this.quoteCharacter = quoteCharacter;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setQuote1", quoteCharacter).as(Builder.class);
}
        public Builder setQuote0(final char quoteCharacter) {
// 
// setQuote1(Character.valueOf(quoteCharacter));
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setQuote0", quoteCharacter).as(Builder.class);
}
        public Builder setNullString(final String nullString) {
// 
// this.nullString = nullString;
// this.quotedNullString = quoteCharacter + nullString + quoteCharacter;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setNullString", nullString).as(Builder.class);
}
        public Builder setIgnoreSurroundingSpaces(final boolean ignoreSurroundingSpaces) {
// 
// this.ignoreSurroundingSpaces = ignoreSurroundingSpaces;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setIgnoreSurroundingSpaces", ignoreSurroundingSpaces).as(Builder.class);
}
        public Builder setIgnoreHeaderCase(final boolean ignoreHeaderCase) {
// 
// this.ignoreHeaderCase = ignoreHeaderCase;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setIgnoreHeaderCase", ignoreHeaderCase).as(Builder.class);
}
        public Builder setIgnoreEmptyLines(final boolean ignoreEmptyLines) {
// 
// this.ignoreEmptyLines = ignoreEmptyLines;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setIgnoreEmptyLines", ignoreEmptyLines).as(Builder.class);
}
        public Builder setHeaderComments1(final String... headerComments) {
// 
// this.headerComments = CSVFormat.clone(headerComments);
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setHeaderComments1", headerComments).as(Builder.class);
}
        public Builder setHeaderComments0(final Object... headerComments) {
// 
// this.headerComments = CSVFormat.clone(toStringArray(headerComments));
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setHeaderComments0", headerComments).as(Builder.class);
}
        public Builder setEscape1(final Character escapeCharacter) {
// 
// if (isLineBreak1(escapeCharacter)) {
// throw new IllegalArgumentException("The escape character cannot be a line break");
// }
// this.escapeCharacter = escapeCharacter;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setEscape1", escapeCharacter).as(Builder.class);
}
        public Builder setEscape0(final char escapeCharacter) {
// 
// setEscape1(Character.valueOf(escapeCharacter));
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setEscape0", escapeCharacter).as(Builder.class);
}
        public Builder setDuplicateHeaderMode(final DuplicateHeaderMode duplicateHeaderMode) {
// 
// this.duplicateHeaderMode =
// Objects.requireNonNull(duplicateHeaderMode, "duplicateHeaderMode");
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setDuplicateHeaderMode", duplicateHeaderMode).as(Builder.class);
}
        public Builder setDelimiter1(final String delimiter) {
// 
// if (containsLineBreak(delimiter)) {
// throw new IllegalArgumentException("The delimiter cannot be a line break");
// }
// if (delimiter.isEmpty()) {
// throw new IllegalArgumentException("The delimiter cannot be empty");
// }
// this.delimiter = delimiter;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setDelimiter1", delimiter).as(Builder.class);
}
        public Builder setDelimiter0(final char delimiter) {
// 
// return setDelimiter1(String.valueOf(delimiter));
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setDelimiter0", delimiter).as(Builder.class);
}
        public Builder setCommentMarker1(final Character commentMarker) {
// 
// if (isLineBreak1(commentMarker)) {
// throw new IllegalArgumentException(
// "The comment start marker character cannot be a line break");
// }
// this.commentMarker = commentMarker;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setCommentMarker1", commentMarker).as(Builder.class);
}
        public Builder setCommentMarker0(final char commentMarker) {
// 
// setCommentMarker1(Character.valueOf(commentMarker));
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setCommentMarker0", commentMarker).as(Builder.class);
}
        public Builder setAutoFlush(final boolean autoFlush) {
// 
// this.autoFlush = autoFlush;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setAutoFlush", autoFlush).as(Builder.class);
}
        public Builder setAllowMissingColumnNames(final boolean allowMissingColumnNames) {
// 
// this.allowMissingColumnNames = allowMissingColumnNames;
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("setAllowMissingColumnNames", allowMissingColumnNames).as(Builder.class);
}
        public CSVFormat build() {
// 
// return new CSVFormat(
// 1, false, false, null, null, null, false, false, this, null, false, null, null,
// false, null, null, false, false, null, null);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("build").as(CSVFormat.class);
}
        public static Builder create1(final CSVFormat csvFormat) {
// 
// return new Builder(csvFormat);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("create1", csvFormat).as(Builder.class);
}
        public static Builder create0() {
// 
// return new Builder(CSVFormat.DEFAULT);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("create0").as(Builder.class);
}
        private Builder(final CSVFormat csvFormat) {
// 
// this.delimiter = csvFormat.delimiter;
// this.quoteCharacter = csvFormat.quoteCharacter;
// this.quoteMode = csvFormat.quoteMode;
// this.commentMarker = csvFormat.commentMarker;
// this.escapeCharacter = csvFormat.escapeCharacter;
// this.ignoreSurroundingSpaces = csvFormat.ignoreSurroundingSpaces;
// this.allowMissingColumnNames = csvFormat.allowMissingColumnNames;
// this.ignoreEmptyLines = csvFormat.ignoreEmptyLines;
// this.recordSeparator = csvFormat.recordSeparator;
// this.nullString = csvFormat.nullString;
// this.headerComments = csvFormat.headerComments;
// this.headers = csvFormat.headers;
// this.skipHeaderRecord = csvFormat.skipHeaderRecord;
// this.ignoreHeaderCase = csvFormat.ignoreHeaderCase;
// this.trailingDelimiter = csvFormat.trailingDelimiter;
// this.trim = csvFormat.trim;
// this.autoFlush = csvFormat.autoFlush;
// this.quotedNullString = csvFormat.quotedNullString;
// this.duplicateHeaderMode = csvFormat.duplicateHeaderMode;
// 

this.obj = clz.invokeMember("__init__", csvFormat);
}
}
public final class CSVFormat implements Serializable {
    public static final CSVFormat TDF =
            DEFAULT.builder().setDelimiter0(TAB).setIgnoreSurroundingSpaces(true).build();
    public static final CSVFormat RFC4180 = DEFAULT.builder().setIgnoreEmptyLines(false).build();
    public static final CSVFormat POSTGRESQL_TEXT =
            DEFAULT.builder()
                    .setDelimiter0(TAB)
                    .setEscape0(BACKSLASH)
                    .setIgnoreEmptyLines(false)
                    .setQuote1(null)
                    .setRecordSeparator0(LF)
                    .setNullString(Constants.SQL_NULL_STRING)
                    .setQuoteMode(QuoteMode.ALL_NON_NULL)
                    .build();
    public static final CSVFormat POSTGRESQL_CSV =
            DEFAULT.builder()
                    .setDelimiter1(COMMA)
                    .setEscape1(null)
                    .setIgnoreEmptyLines(false)
                    .setQuote1(DOUBLE_QUOTE_CHAR)
                    .setRecordSeparator0(LF)
                    .setNullString(EMPTY)
                    .setQuoteMode(QuoteMode.ALL_NON_NULL)
                    .build();
    public static final CSVFormat ORACLE =
            DEFAULT.builder()
                    .setDelimiter1(COMMA)
                    .setEscape0(BACKSLASH)
                    .setIgnoreEmptyLines(false)
                    .setQuote1(DOUBLE_QUOTE_CHAR)
                    .setNullString(Constants.SQL_NULL_STRING)
                    .setTrim(true)
                    .setRecordSeparator1(System.lineSeparator())
                    .setQuoteMode(QuoteMode.MINIMAL)
                    .build();
    public static final CSVFormat MYSQL =
            DEFAULT.builder()
                    .setDelimiter0(TAB)
                    .setEscape0(BACKSLASH)
                    .setIgnoreEmptyLines(false)
                    .setQuote1(null)
                    .setRecordSeparator0(LF)
                    .setNullString(Constants.SQL_NULL_STRING)
                    .setQuoteMode(QuoteMode.ALL_NON_NULL)
                    .build();
    public static final CSVFormat MONGODB_TSV =
            DEFAULT.builder()
                    .setDelimiter0(TAB)
                    .setEscape1(DOUBLE_QUOTE_CHAR)
                    .setQuote1(DOUBLE_QUOTE_CHAR)
                    .setQuoteMode(QuoteMode.MINIMAL)
                    .setSkipHeaderRecord(false)
                    .build();
    public static final CSVFormat MONGODB_CSV =
            DEFAULT.builder()
                    .setDelimiter1(COMMA)
                    .setEscape1(DOUBLE_QUOTE_CHAR)
                    .setQuote1(DOUBLE_QUOTE_CHAR)
                    .setQuoteMode(QuoteMode.MINIMAL)
                    .setSkipHeaderRecord(false)
                    .build();
    public static final CSVFormat INFORMIX_UNLOAD_CSV =
            DEFAULT.builder()
                    .setDelimiter1(COMMA)
                    .setQuote1(DOUBLE_QUOTE_CHAR)
                    .setRecordSeparator0(LF)
                    .build();
    public static final CSVFormat INFORMIX_UNLOAD =
            DEFAULT.builder()
                    .setDelimiter0(PIPE)
                    .setEscape0(BACKSLASH)
                    .setQuote1(DOUBLE_QUOTE_CHAR)
                    .setRecordSeparator0(LF)
                    .build();
    public static final CSVFormat EXCEL =
            DEFAULT.builder().setIgnoreEmptyLines(false).setAllowMissingColumnNames(true).build();
    public static final CSVFormat DEFAULT =
            new CSVFormat(
                    0,
                    false,
                    false,
                    COMMA,
                    null,
                    null,
                    false,
                    false,
                    null,
                    null,
                    false,
                    DOUBLE_QUOTE_CHAR,
                    null,
                    true,
                    DuplicateHeaderMode.ALLOW_ALL,
                    null,
                    false,
                    false,
                    null,
                    CRLF);
    private static final long serialVersionUID = 2L;
    private static Value clz = ContextInitializer.getPythonClass("/CSVFormat.py", "CSVFormat");
    private Value obj;
    public CSVFormat(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public CSVFormat withTrim1(final boolean trim) {
// 
// return builder().setTrim(trim).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withTrim1", trim).as(CSVFormat.class);
}
    public CSVFormat withTrim0() {
// 
// return builder().setTrim(true).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withTrim0").as(CSVFormat.class);
}
    public CSVFormat withTrailingDelimiter1(final boolean trailingDelimiter) {
// 
// return builder().setTrailingDelimiter(trailingDelimiter).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withTrailingDelimiter1", trailingDelimiter).as(CSVFormat.class);
}
    public CSVFormat withTrailingDelimiter0() {
// 
// return builder().setTrailingDelimiter(true).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withTrailingDelimiter0").as(CSVFormat.class);
}
    public CSVFormat withSystemRecordSeparator() {
// 
// return builder().setRecordSeparator1(System.lineSeparator()).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withSystemRecordSeparator").as(CSVFormat.class);
}
    public CSVFormat withSkipHeaderRecord1(final boolean skipHeaderRecord) {
// 
// return builder().setSkipHeaderRecord(skipHeaderRecord).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withSkipHeaderRecord1", skipHeaderRecord).as(CSVFormat.class);
}
    public CSVFormat withSkipHeaderRecord0() {
// 
// return builder().setSkipHeaderRecord(true).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withSkipHeaderRecord0").as(CSVFormat.class);
}
    public CSVFormat withRecordSeparator1(final String recordSeparator) {
// 
// return builder().setRecordSeparator1(recordSeparator).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withRecordSeparator1", recordSeparator).as(CSVFormat.class);
}
    public CSVFormat withRecordSeparator0(final char recordSeparator) {
// 
// return builder().setRecordSeparator0(recordSeparator).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withRecordSeparator0", recordSeparator).as(CSVFormat.class);
}
    public CSVFormat withQuoteMode(final QuoteMode quoteMode) {
// 
// return builder().setQuoteMode(quoteMode).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withQuoteMode", quoteMode).as(CSVFormat.class);
}
    public CSVFormat withQuote1(final Character quoteChar) {
// 
// return builder().setQuote1(quoteChar).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withQuote1", quoteChar).as(CSVFormat.class);
}
    public CSVFormat withQuote0(final char quoteChar) {
// 
// return builder().setQuote0(quoteChar).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withQuote0", quoteChar).as(CSVFormat.class);
}
    public CSVFormat withNullString(final String nullString) {
// 
// return builder().setNullString(nullString).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withNullString", nullString).as(CSVFormat.class);
}
    public CSVFormat withIgnoreSurroundingSpaces1(final boolean ignoreSurroundingSpaces) {
// 
// return builder().setIgnoreSurroundingSpaces(ignoreSurroundingSpaces).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withIgnoreSurroundingSpaces1", ignoreSurroundingSpaces).as(CSVFormat.class);
}
    public CSVFormat withIgnoreSurroundingSpaces0() {
// 
// return builder().setIgnoreSurroundingSpaces(true).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withIgnoreSurroundingSpaces0").as(CSVFormat.class);
}
    public CSVFormat withIgnoreHeaderCase1(final boolean ignoreHeaderCase) {
// 
// return builder().setIgnoreHeaderCase(ignoreHeaderCase).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withIgnoreHeaderCase1", ignoreHeaderCase).as(CSVFormat.class);
}
    public CSVFormat withIgnoreHeaderCase0() {
// 
// return builder().setIgnoreHeaderCase(true).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withIgnoreHeaderCase0").as(CSVFormat.class);
}
    public CSVFormat withIgnoreEmptyLines1(final boolean ignoreEmptyLines) {
// 
// return builder().setIgnoreEmptyLines(ignoreEmptyLines).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withIgnoreEmptyLines1", ignoreEmptyLines).as(CSVFormat.class);
}
    public CSVFormat withIgnoreEmptyLines0() {
// 
// return builder().setIgnoreEmptyLines(true).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withIgnoreEmptyLines0").as(CSVFormat.class);
}
    public CSVFormat withHeaderComments(final Object... headerComments) {
// 
// return builder().setHeaderComments0(headerComments).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withHeaderComments", headerComments).as(CSVFormat.class);
}
    public CSVFormat withEscape1(final Character escape) {
// 
// return builder().setEscape1(escape).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withEscape1", escape).as(CSVFormat.class);
}
    public CSVFormat withEscape0(final char escape) {
// 
// return builder().setEscape0(escape).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withEscape0", escape).as(CSVFormat.class);
}
    public CSVFormat withDelimiter(final char delimiter) {
// 
// return builder().setDelimiter0(delimiter).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withDelimiter", delimiter).as(CSVFormat.class);
}
    public CSVFormat withCommentMarker1(final Character commentMarker) {
// 
// return builder().setCommentMarker1(commentMarker).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withCommentMarker1", commentMarker).as(CSVFormat.class);
}
    public CSVFormat withCommentMarker0(final char commentMarker) {
// 
// return builder().setCommentMarker0(commentMarker).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withCommentMarker0", commentMarker).as(CSVFormat.class);
}
    public CSVFormat withAutoFlush(final boolean autoFlush) {
// 
// return builder().setAutoFlush(autoFlush).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withAutoFlush", autoFlush).as(CSVFormat.class);
}
    public CSVFormat withAllowMissingColumnNames1(final boolean allowMissingColumnNames) {
// 
// return builder().setAllowMissingColumnNames(allowMissingColumnNames).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withAllowMissingColumnNames1", allowMissingColumnNames).as(CSVFormat.class);
}
    public CSVFormat withAllowMissingColumnNames0() {
// 
// return builder().setAllowMissingColumnNames(true).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withAllowMissingColumnNames0").as(CSVFormat.class);
}
    public CSVFormat withAllowDuplicateHeaderNames1(final boolean allowDuplicateHeaderNames) {
// 
// final DuplicateHeaderMode mode =
// allowDuplicateHeaderNames
// ? DuplicateHeaderMode.ALLOW_ALL
// : DuplicateHeaderMode.ALLOW_EMPTY;
// return builder().setDuplicateHeaderMode(mode).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withAllowDuplicateHeaderNames1", allowDuplicateHeaderNames).as(CSVFormat.class);
}
    public CSVFormat withAllowDuplicateHeaderNames0() {
// 
// return builder().setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL).build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withAllowDuplicateHeaderNames0").as(CSVFormat.class);
}
    public String toString() {
// 
// final StringBuilder sb = new StringBuilder();
// sb.append("Delimiter=<").append(delimiter).append('>');
// if (isEscapeCharacterSet()) {
// sb.append(' ');
// sb.append("Escape=<").append(escapeCharacter).append('>');
// }
// if (isQuoteCharacterSet()) {
// sb.append(' ');
// sb.append("QuoteChar=<").append(quoteCharacter).append('>');
// }
// if (quoteMode != null) {
// sb.append(' ');
// sb.append("QuoteMode=<").append(quoteMode).append('>');
// }
// if (isCommentMarkerSet()) {
// sb.append(' ');
// sb.append("CommentStart=<").append(commentMarker).append('>');
// }
// if (isNullStringSet()) {
// sb.append(' ');
// sb.append("NullString=<").append(nullString).append('>');
// }
// if (recordSeparator != null) {
// sb.append(' ');
// sb.append("RecordSeparator=<").append(recordSeparator).append('>');
// }
// if (getIgnoreEmptyLines()) {
// sb.append(" EmptyLines:ignored");
// }
// if (getIgnoreSurroundingSpaces()) {
// sb.append(" SurroundingSpaces:ignored");
// }
// if (getIgnoreHeaderCase()) {
// sb.append(" IgnoreHeaderCase:ignored");
// }
// sb.append(" SkipHeaderRecord:").append(skipHeaderRecord);
// if (headerComments != null) {
// sb.append(' ');
// sb.append("HeaderComments:").append(Arrays.toString(headerComments));
// }
// if (headers != null) {
// sb.append(' ');
// sb.append("Header:").append(Arrays.toString(headers));
// }
// return sb.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
    public CSVPrinter print4(final Path out, final Charset charset) throws IOException {
try {
// 
// return print0(Files.newBufferedWriter(out, charset));
// 


// TODO: Check the type mapping below!
return obj.invokeMember("print4", out, charset).as(CSVPrinter.class);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.print4");
}
}
    public CSVPrinter print1(final File out, final Charset charset) throws IOException {
try {
// 
// return new CSVPrinter(new OutputStreamWriter(new FileOutputStream(out), charset), this);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("print1", out, charset).as(CSVPrinter.class);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.print1");
}
}
    public int hashCode() {
// 
// final int prime = 31;
// int result = 1;
// result = prime * result + Arrays.hashCode(headers);
// result = prime * result + Arrays.hashCode(headerComments);
// return prime * result
// + Objects.hash(
// duplicateHeaderMode,
// allowMissingColumnNames,
// autoFlush,
// commentMarker,
// delimiter,
// escapeCharacter,
// ignoreEmptyLines,
// ignoreHeaderCase,
// ignoreSurroundingSpaces,
// nullString,
// quoteCharacter,
// quoteMode,
// quotedNullString,
// recordSeparator,
// skipHeaderRecord,
// trailingDelimiter,
// trim);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("hashCode").as(int.class);
}
    public char getDelimiter() {
// 
// return delimiter.charAt(0);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getDelimiter").as(char.class);
}
    public boolean getAllowDuplicateHeaderNames() {
// 
// return duplicateHeaderMode == DuplicateHeaderMode.ALLOW_ALL;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getAllowDuplicateHeaderNames").as(boolean.class);
}
    public boolean equals(final Object obj) {
// 
// if (this == obj) {
// return true;
// }
// if (obj == null || getClass() != obj.getClass()) {
// return false;
// }
// final CSVFormat other = (CSVFormat) obj;
// return duplicateHeaderMode == other.duplicateHeaderMode
// && allowMissingColumnNames == other.allowMissingColumnNames
// && autoFlush == other.autoFlush
// && Objects.equals(commentMarker, other.commentMarker)
// && Objects.equals(delimiter, other.delimiter)
// && Objects.equals(escapeCharacter, other.escapeCharacter)
// && Arrays.equals(headers, other.headers)
// && Arrays.equals(headerComments, other.headerComments)
// && ignoreEmptyLines == other.ignoreEmptyLines
// && ignoreHeaderCase == other.ignoreHeaderCase
// && ignoreSurroundingSpaces == other.ignoreSurroundingSpaces
// && Objects.equals(nullString, other.nullString)
// && Objects.equals(quoteCharacter, other.quoteCharacter)
// && quoteMode == other.quoteMode
// && Objects.equals(quotedNullString, other.quotedNullString)
// && Objects.equals(recordSeparator, other.recordSeparator)
// && skipHeaderRecord == other.skipHeaderRecord
// && trailingDelimiter == other.trailingDelimiter
// && trim == other.trim;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("equals", obj).as(boolean.class);
}
    static <T> T[] clone(final T... values) {
// 
// return values == null ? null : values.clone();
// 


// TODO: Check the type mapping below!
return clz.invokeMember("clone", values).as(T[].class);
}
    public synchronized void printRecord(final Appendable appendable, final Object... values)
            throws IOException {
try {
// 
// for (int i = 0; i < values.length; i++) {
// print2(values[i], appendable, i == 0);
// }
// println(appendable);
// 

obj.invokeMember("printRecord", appendable, values);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.printRecord");
}
}
    public synchronized void println(final Appendable appendable) throws IOException {
try {
// 
// if (getTrailingDelimiter()) {
// append1(getDelimiterString(), appendable);
// }
// if (recordSeparator != null) {
// append1(recordSeparator, appendable);
// }
// 

obj.invokeMember("println", appendable);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.println");
}
}
    public CSVPrinter printer() throws IOException {
try {
// 
// return new CSVPrinter(System.out, this);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("printer").as(CSVPrinter.class);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.printer");
}
}
    public synchronized void print2(
            final Object value, final Appendable out, final boolean newRecord) throws IOException {
try {
// 
// CharSequence charSequence;
// if (value == null) {
// if (null == nullString) {
// charSequence = EMPTY;
// } else if (QuoteMode.ALL == quoteMode) {
// charSequence = quotedNullString;
// } else {
// charSequence = nullString;
// }
// } else if (value instanceof CharSequence) {
// charSequence = (CharSequence) value;
// } else if (value instanceof Reader) {
// print5((Reader) value, out, newRecord);
// return;
// } else {
// charSequence = value.toString();
// }
// charSequence = getTrim() ? trim0(charSequence) : charSequence;
// print3(value, charSequence, out, newRecord);
// 

obj.invokeMember("print2", value, out, newRecord);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.print2");
}
}
    public CSVPrinter print0(final Appendable out) throws IOException {
try {
// 
// return new CSVPrinter(out, this);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("print0", out).as(CSVPrinter.class);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.print0");
}
}
    public CSVParser parse(final Reader reader) throws IOException {
try {
// 
// return CSVParser.CSVParser1(reader, this);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("parse", reader).as(CSVParser.class);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.parse");
}
}
    public boolean isQuoteCharacterSet() {
// 
// return quoteCharacter != null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isQuoteCharacterSet").as(boolean.class);
}
    public boolean isNullStringSet() {
// 
// return nullString != null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isNullStringSet").as(boolean.class);
}
    public boolean isEscapeCharacterSet() {
// 
// return escapeCharacter != null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isEscapeCharacterSet").as(boolean.class);
}
    public boolean isCommentMarkerSet() {
// 
// return commentMarker != null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isCommentMarkerSet").as(boolean.class);
}
    public boolean getTrim() {
// 
// return trim;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getTrim").as(boolean.class);
}
    public boolean getTrailingDelimiter() {
// 
// return trailingDelimiter;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getTrailingDelimiter").as(boolean.class);
}
    public boolean getSkipHeaderRecord() {
// 
// return skipHeaderRecord;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getSkipHeaderRecord").as(boolean.class);
}
    public String getRecordSeparator() {
// 
// return recordSeparator;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getRecordSeparator").as(String.class);
}
    public QuoteMode getQuoteMode() {
// 
// return quoteMode;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getQuoteMode").as(QuoteMode.class);
}
    public Character getQuoteCharacter() {
// 
// return quoteCharacter;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getQuoteCharacter").as(Character.class);
}
    public String getNullString() {
// 
// return nullString;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNullString").as(String.class);
}
    public boolean getIgnoreSurroundingSpaces() {
// 
// return ignoreSurroundingSpaces;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getIgnoreSurroundingSpaces").as(boolean.class);
}
    public boolean getIgnoreHeaderCase() {
// 
// return ignoreHeaderCase;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getIgnoreHeaderCase").as(boolean.class);
}
    public boolean getIgnoreEmptyLines() {
// 
// return ignoreEmptyLines;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getIgnoreEmptyLines").as(boolean.class);
}
    public String[] getHeaderComments() {
// 
// return headerComments != null ? headerComments.clone() : null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getHeaderComments").as(String[].class);
}
    public String[] getHeader() {
// 
// return headers != null ? headers.clone() : null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getHeader").as(String[].class);
}
    public Character getEscapeCharacter() {
// 
// return escapeCharacter;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getEscapeCharacter").as(Character.class);
}
    public DuplicateHeaderMode getDuplicateHeaderMode() {
// 
// return duplicateHeaderMode;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getDuplicateHeaderMode").as(DuplicateHeaderMode.class);
}
    public String getDelimiterString() {
// 
// return delimiter;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getDelimiterString").as(String.class);
}
    public Character getCommentMarker() {
// 
// return commentMarker;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getCommentMarker").as(Character.class);
}
    public boolean getAutoFlush() {
// 
// return autoFlush;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getAutoFlush").as(boolean.class);
}
    public boolean getAllowMissingColumnNames() {
// 
// return allowMissingColumnNames;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getAllowMissingColumnNames").as(boolean.class);
}
    public String format(final Object... values) {
// 
// final StringWriter out = new StringWriter();
// try (CSVPrinter csvPrinter = new CSVPrinter(out, this)) {
// csvPrinter.printRecord1(values);
// final String res = out.toString();
// final int len =
// recordSeparator != null
// ? res.length() - recordSeparator.length()
// : res.length();
// return res.substring(0, len);
// } catch (final IOException e) {
// throw new IllegalStateException(e);
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("format", values).as(String.class);
}
    public Builder builder() {
// 
// return Builder.create1(this);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("builder").as(Builder.class);
}
    public CSVFormat(
            int constructorId,
            final boolean autoFlush,
            final boolean skipHeaderRecord,
            final String delimiter,
            final String nullString,
            final Character escape,
            final boolean ignoreSurroundingSpaces,
            final boolean trim,
            final Builder builder,
            final Character commentStart,
            final boolean ignoreHeaderCase,
            final Character quoteChar,
            final QuoteMode quoteMode,
            final boolean ignoreEmptyLines,
            final DuplicateHeaderMode duplicateHeaderMode,
            final String[] header,
            final boolean allowMissingColumnNames,
            final boolean trailingDelimiter,
            final Object[] headerComments,
            final String recordSeparator) {
// 
// if (constructorId == 0) {
// 
// this.delimiter = delimiter;
// this.quoteCharacter = quoteChar;
// this.quoteMode = quoteMode;
// this.commentMarker = commentStart;
// this.escapeCharacter = escape;
// this.ignoreSurroundingSpaces = ignoreSurroundingSpaces;
// this.allowMissingColumnNames = allowMissingColumnNames;
// this.ignoreEmptyLines = ignoreEmptyLines;
// this.recordSeparator = recordSeparator;
// this.nullString = nullString;
// this.headerComments = toStringArray(headerComments);
// this.headers = clone(header);
// this.skipHeaderRecord = skipHeaderRecord;
// this.ignoreHeaderCase = ignoreHeaderCase;
// this.trailingDelimiter = trailingDelimiter;
// this.trim = trim;
// this.autoFlush = autoFlush;
// this.quotedNullString = quoteCharacter + nullString + quoteCharacter;
// this.duplicateHeaderMode = duplicateHeaderMode;
// validate();
// } else {
// 
// this.delimiter = builder.delimiter;
// this.quoteCharacter = builder.quoteCharacter;
// this.quoteMode = builder.quoteMode;
// this.commentMarker = builder.commentMarker;
// this.escapeCharacter = builder.escapeCharacter;
// this.ignoreSurroundingSpaces = builder.ignoreSurroundingSpaces;
// this.allowMissingColumnNames = builder.allowMissingColumnNames;
// this.ignoreEmptyLines = builder.ignoreEmptyLines;
// this.recordSeparator = builder.recordSeparator;
// this.nullString = builder.nullString;
// this.headerComments = builder.headerComments;
// this.headers = builder.headers;
// this.skipHeaderRecord = builder.skipHeaderRecord;
// this.ignoreHeaderCase = builder.ignoreHeaderCase;
// this.trailingDelimiter = builder.trailingDelimiter;
// this.trim = builder.trim;
// this.autoFlush = builder.autoFlush;
// this.quotedNullString = builder.quotedNullString;
// this.duplicateHeaderMode = builder.duplicateHeaderMode;
// validate();
// }
// 

this.obj = clz.invokeMember("__init__", constructorId, autoFlush, skipHeaderRecord, delimiter, nullString, escape, ignoreSurroundingSpaces, trim, builder, commentStart, ignoreHeaderCase, quoteChar, quoteMode, ignoreEmptyLines, duplicateHeaderMode, header, allowMissingColumnNames, trailingDelimiter, headerComments, recordSeparator);
}
    public static CSVFormat valueOf(final String format) {
// 
// return CSVFormat.Predefined.valueOf(format).getFormat();
// 


// TODO: Check the type mapping below!
return clz.invokeMember("valueOf", format).as(CSVFormat.class);
}
    static CharSequence trim0(final CharSequence charSequence) {
// 
// if (charSequence instanceof String) {
// return ((String) charSequence).trim();
// }
// final int count = charSequence.length();
// int len = count;
// int pos = 0;
// 
// while (pos < len && isTrimChar1(charSequence, pos)) {
// pos++;
// }
// while (pos < len && isTrimChar1(charSequence, len - 1)) {
// len--;
// }
// return pos > 0 || len < count ? charSequence.subSequence(pos, len) : charSequence;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("trim0", charSequence).as(CharSequence.class);
}
    static String[] toStringArray(final Object[] values) {
// 
// if (values == null) {
// return null;
// }
// final String[] strings = new String[values.length];
// Arrays.setAll(strings, i -> Objects.toString(values[i], null));
// return strings;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("toStringArray", values).as(String[].class);
}
    public static CSVFormat newFormat(final char delimiter) {
// 
// return new CSVFormat(
// 0,
// false,
// false,
// String.valueOf(delimiter),
// null,
// null,
// false,
// false,
// null,
// null,
// false,
// null,
// null,
// false,
// DuplicateHeaderMode.ALLOW_ALL,
// null,
// false,
// false,
// null,
// null);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("newFormat", delimiter).as(CSVFormat.class);
}
    static boolean isBlank(final String value) {
// 
// return value == null || value.trim().isEmpty();
// 


// TODO: Check the type mapping below!
return clz.invokeMember("isBlank", value).as(boolean.class);
}
    private void validate() throws IllegalArgumentException {
try {
// 
// if (containsLineBreak(delimiter)) {
// throw new IllegalArgumentException("The delimiter cannot be a line break");
// }
// 
// if (quoteCharacter != null && contains(delimiter, quoteCharacter.charValue())) {
// throw new IllegalArgumentException(
// "The quoteChar character and the delimiter cannot be the same ('"
// + quoteCharacter
// + "')");
// }
// 
// if (escapeCharacter != null && contains(delimiter, escapeCharacter.charValue())) {
// throw new IllegalArgumentException(
// "The escape character and the delimiter cannot be the same ('"
// + escapeCharacter
// + "')");
// }
// 
// if (commentMarker != null && contains(delimiter, commentMarker.charValue())) {
// throw new IllegalArgumentException(
// "The comment start character and the delimiter cannot be the same ('"
// + commentMarker
// + "')");
// }
// 
// if (quoteCharacter != null && quoteCharacter.equals(commentMarker)) {
// throw new IllegalArgumentException(
// "The comment start character and the quoteChar cannot be the same ('"
// + commentMarker
// + "')");
// }
// 
// if (escapeCharacter != null && escapeCharacter.equals(commentMarker)) {
// throw new IllegalArgumentException(
// "The comment start and the escape character cannot be the same ('"
// + commentMarker
// + "')");
// }
// 
// if (escapeCharacter == null && quoteMode == QuoteMode.NONE) {
// throw new IllegalArgumentException("No quotes mode set but no escape character is set");
// }
// 
// if (headers != null && duplicateHeaderMode != DuplicateHeaderMode.ALLOW_ALL) {
// final Set<String> dupCheckSet = new HashSet<>(headers.length);
// final boolean emptyDuplicatesAllowed =
// duplicateHeaderMode == DuplicateHeaderMode.ALLOW_EMPTY;
// for (final String header : headers) {
// final boolean blank = isBlank(header);
// final boolean containsHeader = !dupCheckSet.add(blank ? "" : header);
// if (containsHeader && !(blank && emptyDuplicatesAllowed)) {
// throw new IllegalArgumentException(
// String.format(
// "The header contains a duplicate name: \"%s\" in %s. If this is"
// + " valid then use"
// + " CSVFormat.Builder.setDuplicateHeaderMode().",
// header, Arrays.toString(headers)));
// }
// }
// }
// 

obj.invokeMember("validate");
} catch (PolyglotException e) {
    // TODO: Handle IllegalArgumentException
    throw (IllegalArgumentException) ExceptionHandler.handle(e, "CSVFormat.validate");
}
}
    private void printWithQuotes1(final Reader reader, final Appendable appendable)
            throws IOException {
try {
// 
// 
// if (getQuoteMode() == QuoteMode.NONE) {
// printWithEscapes1(reader, appendable);
// return;
// }
// 
// int pos = 0;
// 
// final char quote = getQuoteCharacter().charValue();
// final StringBuilder builder = new StringBuilder(IOUtils.DEFAULT_BUFFER_SIZE);
// 
// append0(quote, appendable);
// 
// int c;
// while (-1 != (c = reader.read())) {
// builder.append((char) c);
// if (c == quote) {
// if (pos > 0) {
// append1(builder.substring(0, pos), appendable);
// append0(quote, appendable);
// builder.setLength(0);
// pos = -1;
// }
// 
// append0((char) c, appendable);
// }
// pos++;
// }
// 
// if (pos > 0) {
// append1(builder.substring(0, pos), appendable);
// }
// 
// append0(quote, appendable);
// 

obj.invokeMember("printWithQuotes1", reader, appendable);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.printWithQuotes1");
}
}
    private void printWithQuotes0(
            final Object object,
            final CharSequence charSeq,
            final Appendable out,
            final boolean newRecord)
            throws IOException {
try {
// 
// boolean quote = false;
// int start = 0;
// int pos = 0;
// final int len = charSeq.length();
// 
// final char[] delim = getDelimiterString().toCharArray();
// final int delimLength = delim.length;
// final char quoteChar = getQuoteCharacter().charValue();
// final char escapeChar =
// isEscapeCharacterSet() ? getEscapeCharacter().charValue() : quoteChar;
// 
// QuoteMode quoteModePolicy = getQuoteMode();
// if (quoteModePolicy == null) {
// quoteModePolicy = QuoteMode.MINIMAL;
// }
// switch (quoteModePolicy) {
// case ALL:
// case ALL_NON_NULL:
// quote = true;
// break;
// case NON_NUMERIC:
// quote = !(object instanceof Number);
// break;
// case NONE:
// printWithEscapes0(charSeq, out);
// return;
// case MINIMAL:
// if (len <= 0) {
// if (newRecord) {
// quote = true;
// }
// } else {
// char c = charSeq.charAt(pos);
// 
// if (c <= COMMENT) {
// quote = true;
// } else {
// while (pos < len) {
// c = charSeq.charAt(pos);
// if (c == LF
// || c == CR
// || c == quoteChar
// || c == escapeChar
// || isDelimiter(c, charSeq, pos, delim, delimLength)) {
// quote = true;
// break;
// }
// pos++;
// }
// 
// if (!quote) {
// pos = len - 1;
// c = charSeq.charAt(pos);
// if (isTrimChar0(c)) {
// quote = true;
// }
// }
// }
// }
// 
// if (!quote) {
// out.append(charSeq, start, len);
// return;
// }
// break;
// default:
// throw new IllegalStateException("Unexpected Quote value: " + quoteModePolicy);
// }
// 
// if (!quote) {
// out.append(charSeq, start, len);
// return;
// }
// 
// out.append(quoteChar);
// 
// while (pos < len) {
// final char c = charSeq.charAt(pos);
// if (c == quoteChar || c == escapeChar) {
// out.append(charSeq, start, pos);
// out.append(escapeChar); // now output the escape
// start = pos; // and restart with the matched char
// }
// pos++;
// }
// 
// out.append(charSeq, start, pos);
// out.append(quoteChar);
// 

obj.invokeMember("printWithQuotes0", object, charSeq, out, newRecord);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.printWithQuotes0");
}
}
    private void printWithEscapes1(final Reader reader, final Appendable appendable)
            throws IOException {
try {
// 
// int start = 0;
// int pos = 0;
// 
// @SuppressWarnings("resource") // Temp reader on input reader.
// final ExtendedBufferedReader bufferedReader = new ExtendedBufferedReader(reader);
// final char[] delim = getDelimiterString().toCharArray();
// final int delimLength = delim.length;
// final char escape = getEscapeCharacter().charValue();
// final StringBuilder builder = new StringBuilder(IOUtils.DEFAULT_BUFFER_SIZE);
// 
// int c;
// while (-1 != (c = bufferedReader.read0())) {
// builder.append((char) c);
// final boolean isDelimiterStart =
// isDelimiter(
// (char) c,
// builder.toString()
// + new String(bufferedReader.lookAhead2(delimLength - 1)),
// pos,
// delim,
// delimLength);
// if (c == CR || c == LF || c == escape || isDelimiterStart) {
// if (pos > start) {
// append1(builder.substring(start, pos), appendable);
// builder.setLength(0);
// pos = -1;
// }
// if (c == LF) {
// c = 'n';
// } else if (c == CR) {
// c = 'r';
// }
// 
// append0(escape, appendable);
// append0((char) c, appendable);
// 
// if (isDelimiterStart) {
// for (int i = 1; i < delimLength; i++) {
// c = bufferedReader.read0();
// append0(escape, appendable);
// append0((char) c, appendable);
// }
// }
// 
// start = pos + 1; // start on the current char after this one
// }
// pos++;
// }
// 
// if (pos > start) {
// append1(builder.substring(start, pos), appendable);
// }
// 

obj.invokeMember("printWithEscapes1", reader, appendable);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.printWithEscapes1");
}
}
    private void printWithEscapes0(final CharSequence charSeq, final Appendable appendable)
            throws IOException {
try {
// 
// int start = 0;
// int pos = 0;
// final int end = charSeq.length();
// 
// final char[] delim = getDelimiterString().toCharArray();
// final int delimLength = delim.length;
// final char escape = getEscapeCharacter().charValue();
// 
// while (pos < end) {
// char c = charSeq.charAt(pos);
// final boolean isDelimiterStart = isDelimiter(c, charSeq, pos, delim, delimLength);
// if (c == CR || c == LF || c == escape || isDelimiterStart) {
// if (pos > start) {
// appendable.append(charSeq, start, pos);
// }
// if (c == LF) {
// c = 'n';
// } else if (c == CR) {
// c = 'r';
// }
// 
// appendable.append(escape);
// appendable.append(c);
// 
// if (isDelimiterStart) {
// for (int i = 1; i < delimLength; i++) {
// pos++;
// c = charSeq.charAt(pos);
// appendable.append(escape);
// appendable.append(c);
// }
// }
// 
// start = pos + 1; // start on the current char after this one
// }
// pos++;
// }
// 
// if (pos > start) {
// appendable.append(charSeq, start, pos);
// }
// 

obj.invokeMember("printWithEscapes0", charSeq, appendable);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.printWithEscapes0");
}
}
    private void print5(final Reader reader, final Appendable out, final boolean newRecord)
            throws IOException {
try {
// 
// if (!newRecord) {
// append1(getDelimiterString(), out);
// }
// if (isQuoteCharacterSet()) {
// printWithQuotes1(reader, out);
// } else if (isEscapeCharacterSet()) {
// printWithEscapes1(reader, out);
// } else if (out instanceof Writer) {
// IOUtils.copyLarge0(reader, (Writer) out);
// } else {
// IOUtils.copy0(reader, out);
// }
// 

obj.invokeMember("print5", reader, out, newRecord);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.print5");
}
}
    private synchronized void print3(
            final Object object,
            final CharSequence value,
            final Appendable out,
            final boolean newRecord)
            throws IOException {
try {
// 
// final int offset = 0;
// final int len = value.length();
// if (!newRecord) {
// out.append(getDelimiterString());
// }
// if (object == null) {
// out.append(value);
// } else if (isQuoteCharacterSet()) {
// printWithQuotes0(object, value, out, newRecord);
// } else if (isEscapeCharacterSet()) {
// printWithEscapes0(value, out);
// } else {
// out.append(value, offset, len);
// }
// 

obj.invokeMember("print3", object, value, out, newRecord);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.print3");
}
}
    private boolean isDelimiter(
            final char ch,
            final CharSequence charSeq,
            final int startIndex,
            final char[] delimiter,
            final int delimiterLength) {
// 
// if (ch != delimiter[0]) {
// return false;
// }
// final int len = charSeq.length();
// if (startIndex + delimiterLength > len) {
// return false;
// }
// for (int i = 1; i < delimiterLength; i++) {
// if (charSeq.charAt(startIndex + i) != delimiter[i]) {
// return false;
// }
// }
// return true;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isDelimiter", ch, charSeq, startIndex, delimiter, delimiterLength).as(boolean.class);
}
    private void append1(final CharSequence csq, final Appendable appendable) throws IOException {
try {
// 
// appendable.append(csq);
// 

obj.invokeMember("append1", csq, appendable);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.append1");
}
}
    private void append0(final char c, final Appendable appendable) throws IOException {
try {
// 
// appendable.append(c);
// 

obj.invokeMember("append0", c, appendable);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVFormat.append0");
}
}
    private static boolean isTrimChar1(final CharSequence charSequence, final int pos) {
// 
// return isTrimChar0(charSequence.charAt(pos));
// 


// TODO: Check the type mapping below!
return clz.invokeMember("isTrimChar1", charSequence, pos).as(boolean.class);
}
    private static boolean isTrimChar0(final char ch) {
// 
// return ch <= SP;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("isTrimChar0", ch).as(boolean.class);
}
    private static boolean isLineBreak1(final Character c) {
// 
// return c != null && isLineBreak0(c.charValue());
// 


// TODO: Check the type mapping below!
return clz.invokeMember("isLineBreak1", c).as(boolean.class);
}
    private static boolean isLineBreak0(final char c) {
// 
// return c == LF || c == CR;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("isLineBreak0", c).as(boolean.class);
}
    private static boolean containsLineBreak(final String source) {
// 
// return contains(source, CR) || contains(source, LF);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("containsLineBreak", source).as(boolean.class);
}
    private static boolean contains(final String source, final char searchCh) {
// 
// return Objects.requireNonNull(source, "source").indexOf(searchCh) >= 0;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("contains", source, searchCh).as(boolean.class);
}
    String trim1(final String value) {
// 
// return getTrim() ? value.trim() : value;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("trim1", value).as(String.class);
}
    CSVFormat copy() {
// 
// return builder().build();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("copy").as(CSVFormat.class);
}
    public enum Predefined {
    private static Value clz = ContextInitializer.getPythonClass("/CSVFormat.py", "Predefined");
    private Value obj;
    public Predefined(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public CSVFormat getFormat() {
// 
// return format;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getFormat").as(CSVFormat.class);
}
        Predefined(final CSVFormat format) {
// 
// this.format = format;
// 

this.obj = clz.invokeMember("__init__", format);
}
}
        Arrays.setAll(strings, i -> Objects.toString(values[i], null));
    private static Value clz = ContextInitializer.getPythonClass("/CSVFormat.py", "new IntFunction<String>(...) { ... }");
    private Value obj;
    public new IntFunction<String>(...) { ... }(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        Arrays.setAll(strings, i -> Objects.toString(values[i], null));
}
}
