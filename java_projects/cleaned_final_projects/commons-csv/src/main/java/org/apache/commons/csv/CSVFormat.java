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

package org.apache.commons.csv;

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

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Reader;
import java.io.Serializable;
import java.io.StringWriter;
import java.io.Writer;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

/**
 * Specifies the format of a CSV file for parsing and writing.
 *
 * <h2>Using predefined formats</h2>
 *
 * <p>You can use one of the predefined formats:
 *
 * <ul>
 *   <li>{@link #DEFAULT}
 *   <li>{@link #EXCEL}
 *   <li>{@link #INFORMIX_UNLOAD}
 *   <li>{@link #INFORMIX_UNLOAD_CSV}
 *   <li>{@link #MYSQL}
 *   <li>{@link #RFC4180}
 *   <li>{@link #ORACLE}
 *   <li>{@link #POSTGRESQL_CSV}
 *   <li>{@link #POSTGRESQL_TEXT}
 *   <li>{@link #TDF}
 * </ul>
 *
 * <p>For example:
 *
 * <pre>
 * CSVParser parser = CSVFormat.EXCEL.parse(reader);
 * </pre>
 *
 * <p>The {@link CSVParser} provides static methods to parse other input types, for example:
 *
 * <pre>
 * CSVParser parser = CSVParser.parse(file, StandardCharsets.US_ASCII, CSVFormat.EXCEL);
 * </pre>
 *
 * <h2>Defining formats</h2>
 *
 * <p>You can extend a format by calling the {@code set} methods. For example:
 *
 * <pre>
 * CSVFormat.EXCEL.withNullString(&quot;N/A&quot;).withIgnoreSurroundingSpaces(true);
 * </pre>
 *
 * <h2>Defining column names</h2>
 *
 * <p>To define the column names you want to use to access records, write:
 *
 * <pre>
 * CSVFormat.EXCEL.withHeader(&quot;Col1&quot;, &quot;Col2&quot;, &quot;Col3&quot;);
 * </pre>
 *
 * <p>Calling {@link Builder#setHeader(String...)} lets you use the given names to address values in
 * a {@link CSVRecord}, and assumes that your CSV source does not contain a first record that also
 * defines column names.
 *
 * <p>If it does, then you are overriding this metadata with your names and you should skip the
 * first record by calling {@link Builder#setSkipHeaderRecord(boolean)} with {@code true}.
 *
 * <h2>Parsing</h2>
 *
 * <p>You can use a format directly to parse a reader. For example, to parse an Excel file with
 * columns header, write:
 *
 * <pre>
 * Reader in = ...;
 * CSVFormat.EXCEL.withHeader(&quot;Col1&quot;, &quot;Col2&quot;, &quot;Col3&quot;).parse(in);
 * </pre>
 *
 * <p>For other input types, like resources, files, and URLs, use the static methods on {@link
 * CSVParser}.
 *
 * <h2>Referencing columns safely</h2>
 *
 * <p>If your source contains a header record, you can simplify your code and safely reference
 * columns, by using {@link Builder#setHeader(String...)} with no arguments:
 *
 * <pre>
 * CSVFormat.EXCEL.withHeader();
 * </pre>
 *
 * <p>This causes the parser to read the first record and use its values as column names.
 *
 * <p>Then, call one of the {@link CSVRecord} get method that takes a String column name argument:
 *
 * <pre>
 * String value = record.get(&quot;Col1&quot;);
 * </pre>
 *
 * <p>This makes your code impervious to changes in column order in the CSV file.
 *
 * <h2>Serialization</h2>
 *
 * <p>This class implements the {@link Serializable} interface with the following caveats:
 *
 * <ul>
 *   <li>This class will no longer implement Serializable in 2.0.
 *   <li>Serialization is not supported from one version to the next.
 * </ul>
 *
 * <p>The {@code serialVersionUID} values are:
 *
 * <ul>
 *   <li>Version 1.10.0: {@code 2L}
 *   <li>Version 1.9.0 through 1.0: {@code 1L}
 * </ul>
 *
 * <h2>Notes</h2>
 *
 * <p>This class is immutable.
 *
 * <p>Not all settings are used for both parsing and writing.
 */
public final class CSVFormat implements Serializable {

    /**
     * Builds CSVFormat instances.
     *
     * @since 1.9.0
     */
    public static class Builder {

        /**
         * Creates a new default builder.
         *
         * @return a copy of the builder
         */
        public static Builder create0() {
            return new Builder(CSVFormat.DEFAULT);
        }

        /**
         * Creates a new builder for the given format.
         *
         * @param csvFormat the source format.
         * @return a copy of the builder
         */
        public static Builder create1(final CSVFormat csvFormat) {
            return new Builder(csvFormat);
        }

        private boolean allowMissingColumnNames;

        private boolean autoFlush;

        private Character commentMarker;

        private String delimiter;

        private DuplicateHeaderMode duplicateHeaderMode;

        private Character escapeCharacter;

        private String[] headerComments;

        private String[] headers;

        private boolean ignoreEmptyLines;

        private boolean ignoreHeaderCase;

        private boolean ignoreSurroundingSpaces;

        private String nullString;

        private Character quoteCharacter;

        private String quotedNullString;

        private QuoteMode quoteMode;

        private String recordSeparator;

        private boolean skipHeaderRecord;

        private boolean trailingDelimiter;

        private boolean trim;

        private Builder(final CSVFormat csvFormat) {
            this.delimiter = csvFormat.delimiter;
            this.quoteCharacter = csvFormat.quoteCharacter;
            this.quoteMode = csvFormat.quoteMode;
            this.commentMarker = csvFormat.commentMarker;
            this.escapeCharacter = csvFormat.escapeCharacter;
            this.ignoreSurroundingSpaces = csvFormat.ignoreSurroundingSpaces;
            this.allowMissingColumnNames = csvFormat.allowMissingColumnNames;
            this.ignoreEmptyLines = csvFormat.ignoreEmptyLines;
            this.recordSeparator = csvFormat.recordSeparator;
            this.nullString = csvFormat.nullString;
            this.headerComments = csvFormat.headerComments;
            this.headers = csvFormat.headers;
            this.skipHeaderRecord = csvFormat.skipHeaderRecord;
            this.ignoreHeaderCase = csvFormat.ignoreHeaderCase;
            this.trailingDelimiter = csvFormat.trailingDelimiter;
            this.trim = csvFormat.trim;
            this.autoFlush = csvFormat.autoFlush;
            this.quotedNullString = csvFormat.quotedNullString;
            this.duplicateHeaderMode = csvFormat.duplicateHeaderMode;
        }

        /**
         * Builds a new CSVFormat instance.
         *
         * @return a new CSVFormat instance.
         */
        public CSVFormat build() {
            return new CSVFormat(
                    1, false, false, null, null, null, false, false, this, null, false, null, null,
                    false, null, null, false, false, null, null);
        }

        /**
         * Sets the duplicate header names behavior, true to allow, false to disallow.
         *
         * @param allowDuplicateHeaderNames the duplicate header names behavior, true to allow,
         *     false to disallow.
         * @return This instance.
         * @deprecated Use {@link #setDuplicateHeaderMode(DuplicateHeaderMode)}.
         */
        @Deprecated
        public Builder setAllowDuplicateHeaderNames(final boolean allowDuplicateHeaderNames) {
            setDuplicateHeaderMode(
                    allowDuplicateHeaderNames
                            ? DuplicateHeaderMode.ALLOW_ALL
                            : DuplicateHeaderMode.ALLOW_EMPTY);
            return this;
        }

        /**
         * Sets the parser missing column names behavior, {@code true} to allow missing column names
         * in the header line, {@code false} to cause an {@link IllegalArgumentException} to be
         * thrown.
         *
         * @param allowMissingColumnNames the missing column names behavior, {@code true} to allow
         *     missing column names in the header line, {@code false} to cause an {@link
         *     IllegalArgumentException} to be thrown.
         * @return This instance.
         */
        public Builder setAllowMissingColumnNames(final boolean allowMissingColumnNames) {
            this.allowMissingColumnNames = allowMissingColumnNames;
            return this;
        }

        /**
         * Sets whether to flush on close.
         *
         * @param autoFlush whether to flush on close.
         * @return This instance.
         */
        public Builder setAutoFlush(final boolean autoFlush) {
            this.autoFlush = autoFlush;
            return this;
        }

        /**
         * Sets the comment start marker, use {@code null} to disable.
         *
         * <p>Note that the comment start character is only recognized at the start of a line.
         *
         * @param commentMarker the comment start marker, use {@code null} to disable.
         * @return This instance.
         * @throws IllegalArgumentException thrown if the specified character is a line break
         */
        public Builder setCommentMarker0(final char commentMarker) {
            setCommentMarker1(Character.valueOf(commentMarker));
            return this;
        }

        /**
         * Sets the comment start marker, use {@code null} to disable.
         *
         * <p>Note that the comment start character is only recognized at the start of a line.
         *
         * @param commentMarker the comment start marker, use {@code null} to disable.
         * @return This instance.
         * @throws IllegalArgumentException thrown if the specified character is a line break
         */
        public Builder setCommentMarker1(final Character commentMarker) {
            if (isLineBreak1(commentMarker)) {
                throw new IllegalArgumentException(
                        "The comment start marker character cannot be a line break");
            }
            this.commentMarker = commentMarker;
            return this;
        }

        /**
         * Sets the delimiter character.
         *
         * @param delimiter the delimiter character.
         * @return This instance.
         */
        public Builder setDelimiter0(final char delimiter) {
            return setDelimiter1(String.valueOf(delimiter));
        }

        /**
         * Sets the delimiter character.
         *
         * @param delimiter the delimiter character.
         * @return This instance.
         */
        public Builder setDelimiter1(final String delimiter) {
            if (containsLineBreak(delimiter)) {
                throw new IllegalArgumentException("The delimiter cannot be a line break");
            }
            if (delimiter.isEmpty()) {
                throw new IllegalArgumentException("The delimiter cannot be empty");
            }
            this.delimiter = delimiter;
            return this;
        }

        /**
         * Sets the duplicate header names behavior.
         *
         * @param duplicateHeaderMode the duplicate header names behavior
         * @return This instance.
         * @since 1.10.0
         */
        public Builder setDuplicateHeaderMode(final DuplicateHeaderMode duplicateHeaderMode) {
            this.duplicateHeaderMode =
                    Objects.requireNonNull(duplicateHeaderMode, "duplicateHeaderMode");
            return this;
        }

        /**
         * Sets the escape character.
         *
         * @param escapeCharacter the escape character.
         * @return This instance.
         * @throws IllegalArgumentException thrown if the specified character is a line break
         */
        public Builder setEscape0(final char escapeCharacter) {
            setEscape1(Character.valueOf(escapeCharacter));
            return this;
        }

        /**
         * Sets the escape character.
         *
         * @param escapeCharacter the escape character.
         * @return This instance.
         * @throws IllegalArgumentException thrown if the specified character is a line break
         */
        public Builder setEscape1(final Character escapeCharacter) {
            if (isLineBreak1(escapeCharacter)) {
                throw new IllegalArgumentException("The escape character cannot be a line break");
            }
            this.escapeCharacter = escapeCharacter;
            return this;
        }

        /**
         * Sets the header defined by the given {@link Enum} class.
         *
         * <p>Example:
         *
         * <pre>
         * public enum HeaderEnum {
         *     Name, Email, Phone
         * }
         *
         * Builder builder = builder.setHeader(HeaderEnum.class);
         * </pre>
         *
         * <p>The header is also used by the {@link CSVPrinter}.
         *
         * @param headerEnum the enum defining the header, {@code null} if disabled, empty if parsed
         *     automatically, user specified otherwise.
         * @return This instance.
         */

        /**
         * Sets the header from the result set metadata. The header can either be parsed
         * automatically from the input file with:
         *
         * <pre>
         * builder.setHeader();
         * </pre>
         *
         * or specified manually with:
         *
         * <pre>
         * builder.setHeader(resultSet);
         * </pre>
         *
         * <p>The header is also used by the {@link CSVPrinter}.
         *
         * @param resultSet the resultSet for the header, {@code null} if disabled, empty if parsed
         *     automatically, user specified otherwise.
         * @return This instance.
         * @throws SQLException SQLException if a database access error occurs or this method is
         *     called on a closed result set.
         */

        /**
         * Sets the header from the result set metadata. The header can either be parsed
         * automatically from the input file with:
         *
         * <pre>
         * builder.setHeader();
         * </pre>
         *
         * or specified manually with:
         *
         * <pre>
         * builder.setHeader(resultSetMetaData);
         * </pre>
         *
         * <p>The header is also used by the {@link CSVPrinter}.
         *
         * @param resultSetMetaData the metaData for the header, {@code null} if disabled, empty if
         *     parsed automatically, user specified otherwise.
         * @return This instance.
         * @throws SQLException SQLException if a database access error occurs or this method is
         *     called on a closed result set.
         */

        /**
         * Sets the header to the given values. The header can either be parsed automatically from
         * the input file with:
         *
         * <pre>
         * builder.setHeader();
         * </pre>
         *
         * or specified manually with:
         *
         * <pre>
         * builder.setHeader(&quot;name&quot;, &quot;email&quot;, &quot;phone&quot;);
         * </pre>
         *
         * <p>The header is also used by the {@link CSVPrinter}.
         *
         * @param header the header, {@code null} if disabled, empty if parsed automatically, user
         *     specified otherwise.
         * @return This instance.
         */

        /**
         * Sets the header comments set to the given values. The comments will be printed first,
         * before the headers. This setting is ignored by the parser.
         *
         * <pre>
         * builder.setHeaderComments(&quot;Generated by Apache Commons CSV.&quot;, Instant.now());
         * </pre>
         *
         * @param headerComments the headerComments which will be printed by the Printer before the
         *     actual CSV data.
         * @return This instance.
         */
        public Builder setHeaderComments0(final Object... headerComments) {
            this.headerComments = CSVFormat.clone(toStringArray(headerComments));
            return this;
        }

        /**
         * Sets the header comments set to the given values. The comments will be printed first,
         * before the headers. This setting is ignored by the parser.
         *
         * <pre>
         * Builder.setHeaderComments(&quot;Generated by Apache Commons CSV.&quot;, Instant.now());
         * </pre>
         *
         * @param headerComments the headerComments which will be printed by the Printer before the
         *     actual CSV data.
         * @return This instance.
         */
        public Builder setHeaderComments1(final String... headerComments) {
            this.headerComments = CSVFormat.clone(headerComments);
            return this;
        }

        /**
         * Sets the empty line skipping behavior, {@code true} to ignore the empty lines between the
         * records, {@code false} to translate empty lines to empty records.
         *
         * @param ignoreEmptyLines the empty line skipping behavior, {@code true} to ignore the
         *     empty lines between the records, {@code false} to translate empty lines to empty
         *     records.
         * @return This instance.
         */
        public Builder setIgnoreEmptyLines(final boolean ignoreEmptyLines) {
            this.ignoreEmptyLines = ignoreEmptyLines;
            return this;
        }

        /**
         * Sets the parser case mapping behavior, {@code true} to access name/values, {@code false}
         * to leave the mapping as is.
         *
         * @param ignoreHeaderCase the case mapping behavior, {@code true} to access name/values,
         *     {@code false} to leave the mapping as is.
         * @return This instance.
         */
        public Builder setIgnoreHeaderCase(final boolean ignoreHeaderCase) {
            this.ignoreHeaderCase = ignoreHeaderCase;
            return this;
        }

        /**
         * Sets the parser trimming behavior, {@code true} to remove the surrounding spaces, {@code
         * false} to leave the spaces as is.
         *
         * @param ignoreSurroundingSpaces the parser trimming behavior, {@code true} to remove the
         *     surrounding spaces, {@code false} to leave the spaces as is.
         * @return This instance.
         */
        public Builder setIgnoreSurroundingSpaces(final boolean ignoreSurroundingSpaces) {
            this.ignoreSurroundingSpaces = ignoreSurroundingSpaces;
            return this;
        }

        /**
         * Sets the String to convert to and from {@code null}. No substitution occurs if {@code
         * null}.
         *
         * <ul>
         *   <li><strong>Reading:</strong> Converts strings equal to the given {@code nullString} to
         *       {@code null} when reading records.
         *   <li><strong>Writing:</strong> Writes {@code null} as the given {@code nullString} when
         *       writing records.
         * </ul>
         *
         * @param nullString the String to convert to and from {@code null}. No substitution occurs
         *     if {@code null}.
         * @return This instance.
         */
        public Builder setNullString(final String nullString) {
            this.nullString = nullString;
            this.quotedNullString = quoteCharacter + nullString + quoteCharacter;
            return this;
        }

        /**
         * Sets the quote character.
         *
         * @param quoteCharacter the quote character.
         * @return This instance.
         */
        public Builder setQuote0(final char quoteCharacter) {
            setQuote1(Character.valueOf(quoteCharacter));
            return this;
        }

        /**
         * Sets the quote character, use {@code null} to disable.
         *
         * @param quoteCharacter the quote character, use {@code null} to disable.
         * @return This instance.
         */
        public Builder setQuote1(final Character quoteCharacter) {
            if (isLineBreak1(quoteCharacter)) {
                throw new IllegalArgumentException("The quoteChar cannot be a line break");
            }
            this.quoteCharacter = quoteCharacter;
            return this;
        }

        /**
         * Sets the quote policy to use for output.
         *
         * @param quoteMode the quote policy to use for output.
         * @return This instance.
         */
        public Builder setQuoteMode(final QuoteMode quoteMode) {
            this.quoteMode = quoteMode;
            return this;
        }

        /**
         * Sets the record separator to use for output.
         *
         * <p><strong>Note:</strong> This setting is only used during printing and does not affect
         * parsing. Parsing currently only works for inputs with '\n', '\r' and "\r\n"
         *
         * @param recordSeparator the record separator to use for output.
         * @return This instance.
         */
        public Builder setRecordSeparator0(final char recordSeparator) {
            this.recordSeparator = String.valueOf(recordSeparator);
            return this;
        }

        /**
         * Sets the record separator to use for output.
         *
         * <p><strong>Note:</strong> This setting is only used during printing and does not affect
         * parsing. Parsing currently only works for inputs with '\n', '\r' and "\r\n"
         *
         * @param recordSeparator the record separator to use for output.
         * @return This instance.
         */
        public Builder setRecordSeparator1(final String recordSeparator) {
            this.recordSeparator = recordSeparator;
            return this;
        }

        /**
         * Sets whether to skip the header record.
         *
         * @param skipHeaderRecord whether to skip the header record.
         * @return This instance.
         */
        public Builder setSkipHeaderRecord(final boolean skipHeaderRecord) {
            this.skipHeaderRecord = skipHeaderRecord;
            return this;
        }

        /**
         * Sets whether to add a trailing delimiter.
         *
         * @param trailingDelimiter whether to add a trailing delimiter.
         * @return This instance.
         */
        public Builder setTrailingDelimiter(final boolean trailingDelimiter) {
            this.trailingDelimiter = trailingDelimiter;
            return this;
        }

        /**
         * Sets whether to trim leading and trailing blanks.
         *
         * @param trim whether to trim leading and trailing blanks.
         * @return This instance.
         */
        public Builder setTrim(final boolean trim) {
            this.trim = trim;
            return this;
        }
    }

    /**
     * Predefines formats.
     *
     * @since 1.2
     */
    public enum Predefined {

        /**
         * @see CSVFormat#DEFAULT
         */
        Default(CSVFormat.DEFAULT),

        /**
         * @see CSVFormat#EXCEL
         */
        Excel(CSVFormat.EXCEL),

        /**
         * @see CSVFormat#INFORMIX_UNLOAD
         * @since 1.3
         */
        InformixUnload(CSVFormat.INFORMIX_UNLOAD),

        /**
         * @see CSVFormat#INFORMIX_UNLOAD_CSV
         * @since 1.3
         */
        InformixUnloadCsv(CSVFormat.INFORMIX_UNLOAD_CSV),

        /**
         * @see CSVFormat#MONGODB_CSV
         * @since 1.7
         */
        MongoDBCsv(CSVFormat.MONGODB_CSV),

        /**
         * @see CSVFormat#MONGODB_TSV
         * @since 1.7
         */
        MongoDBTsv(CSVFormat.MONGODB_TSV),

        /**
         * @see CSVFormat#MYSQL
         */
        MySQL(CSVFormat.MYSQL),

        /**
         * @see CSVFormat#ORACLE
         */
        Oracle(CSVFormat.ORACLE),

        /**
         * @see CSVFormat#POSTGRESQL_CSV
         * @since 1.5
         */
        PostgreSQLCsv(CSVFormat.POSTGRESQL_CSV),

        /**
         * @see CSVFormat#POSTGRESQL_CSV
         */
        PostgreSQLText(CSVFormat.POSTGRESQL_TEXT),

        /**
         * @see CSVFormat#RFC4180
         */
        RFC4180(CSVFormat.RFC4180),

        /**
         * @see CSVFormat#TDF
         */
        TDF(CSVFormat.TDF);

        private final CSVFormat format;

        Predefined(final CSVFormat format) {
            this.format = format;
        }

        /**
         * Gets the format.
         *
         * @return the format.
         */
        public CSVFormat getFormat() {
            return format;
        }
    }

    /**
     * Standard Comma Separated Value format, as for {@link #RFC4180} but allowing empty lines.
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter(',')}
     *   <li>{@code setQuote('"')}
     *   <li>{@code setRecordSeparator("\r\n")}
     *   <li>{@code setIgnoreEmptyLines(true)}
     *   <li>{@code setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL)}
     * </ul>
     *
     * @see Predefined#Default
     */
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

    /**
     * Excel file format (using a comma as the value delimiter). Note that the actual value
     * delimiter used by Excel is locale dependent, it might be necessary to customize this format
     * to accommodate to your regional settings.
     *
     * <p>For example for parsing or generating a CSV file on a French system the following format
     * will be used:
     *
     * <pre>
     * CSVFormat fmt = CSVFormat.EXCEL.withDelimiter(';');
     * </pre>
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter(',')}
     *   <li>{@code setQuote('"')}
     *   <li>{@code setRecordSeparator("\r\n")}
     *   <li>{@code setIgnoreEmptyLines(false)}
     *   <li>{@code setAllowMissingColumnNames(true)}
     *   <li>{@code setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL)}
     * </ul>
     *
     * <p>Note: This is currently like {@link #RFC4180} plus {@link
     * Builder#setAllowMissingColumnNames(boolean) Builder#setAllowMissingColumnNames(true)} and
     * {@link Builder#setIgnoreEmptyLines(boolean) Builder#setIgnoreEmptyLines(false)}.
     *
     * @see Predefined#Excel
     */
    public static final CSVFormat EXCEL =
            DEFAULT.builder().setIgnoreEmptyLines(false).setAllowMissingColumnNames(true).build();

    /**
     * Default Informix CSV UNLOAD format used by the {@code UNLOAD TO file_name} operation.
     *
     * <p>This is a comma-delimited format with a LF character as the line separator. Values are not
     * quoted and special characters are escaped with {@code '\'}. The default NULL string is {@code
     * "\\N"}.
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter(',')}
     *   <li>{@code setEscape('\\')}
     *   <li>{@code setQuote("\"")}
     *   <li>{@code setRecordSeparator('\n')}
     * </ul>
     *
     * @see Predefined#MySQL
     * @see <a href=
     *     "http://www.ibm.com/support/knowledgecenter/SSBJG3_2.5.0/com.ibm.gen_busug.doc/c_fgl_InOutSql_UNLOAD.htm">
     *     http://www.ibm.com/support/knowledgecenter/SSBJG3_2.5.0/com.ibm.gen_busug.doc/c_fgl_InOutSql_UNLOAD.htm</a>
     * @since 1.3
     */
    public static final CSVFormat INFORMIX_UNLOAD =
            DEFAULT.builder()
                    .setDelimiter0(PIPE)
                    .setEscape0(BACKSLASH)
                    .setQuote1(DOUBLE_QUOTE_CHAR)
                    .setRecordSeparator0(LF)
                    .build();

    /**
     * Default Informix CSV UNLOAD format used by the {@code UNLOAD TO file_name} operation
     * (escaping is disabled.)
     *
     * <p>This is a comma-delimited format with a LF character as the line separator. Values are not
     * quoted and special characters are escaped with {@code '\'}. The default NULL string is {@code
     * "\\N"}.
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter(',')}
     *   <li>{@code setQuote("\"")}
     *   <li>{@code setRecordSeparator('\n')}
     * </ul>
     *
     * @see Predefined#MySQL
     * @see <a href=
     *     "http://www.ibm.com/support/knowledgecenter/SSBJG3_2.5.0/com.ibm.gen_busug.doc/c_fgl_InOutSql_UNLOAD.htm">
     *     http://www.ibm.com/support/knowledgecenter/SSBJG3_2.5.0/com.ibm.gen_busug.doc/c_fgl_InOutSql_UNLOAD.htm</a>
     * @since 1.3
     */
    public static final CSVFormat INFORMIX_UNLOAD_CSV =
            DEFAULT.builder()
                    .setDelimiter1(COMMA)
                    .setQuote1(DOUBLE_QUOTE_CHAR)
                    .setRecordSeparator0(LF)
                    .build();

    /**
     * Default MongoDB CSV format used by the {@code mongoexport} operation.
     *
     * <p><b>Parsing is not supported yet.</b>
     *
     * <p>This is a comma-delimited format. Values are double quoted only if needed and special
     * characters are escaped with {@code '"'}. A header line with field names is expected.
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter(',')}
     *   <li>{@code setEscape('"')}
     *   <li>{@code setQuote('"')}
     *   <li>{@code setQuoteMode(QuoteMode.ALL_NON_NULL)}
     *   <li>{@code setSkipHeaderRecord(false)}
     * </ul>
     *
     * @see Predefined#MongoDBCsv
     * @see <a href="https://docs.mongodb.com/manual/reference/program/mongoexport/">MongoDB
     *     mongoexport command documentation</a>
     * @since 1.7
     */
    public static final CSVFormat MONGODB_CSV =
            DEFAULT.builder()
                    .setDelimiter1(COMMA)
                    .setEscape1(DOUBLE_QUOTE_CHAR)
                    .setQuote1(DOUBLE_QUOTE_CHAR)
                    .setQuoteMode(QuoteMode.MINIMAL)
                    .setSkipHeaderRecord(false)
                    .build();

    /**
     * Default MongoDB TSV format used by the {@code mongoexport} operation.
     *
     * <p><b>Parsing is not supported yet.</b>
     *
     * <p>This is a tab-delimited format. Values are double quoted only if needed and special
     * characters are escaped with {@code '"'}. A header line with field names is expected.
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter('\t')}
     *   <li>{@code setEscape('"')}
     *   <li>{@code setQuote('"')}
     *   <li>{@code setQuoteMode(QuoteMode.ALL_NON_NULL)}
     *   <li>{@code setSkipHeaderRecord(false)}
     * </ul>
     *
     * @see Predefined#MongoDBCsv
     * @see <a href="https://docs.mongodb.com/manual/reference/program/mongoexport/">MongoDB
     *     mongoexport command documentation</a>
     * @since 1.7
     */
    public static final CSVFormat MONGODB_TSV =
            DEFAULT.builder()
                    .setDelimiter0(TAB)
                    .setEscape1(DOUBLE_QUOTE_CHAR)
                    .setQuote1(DOUBLE_QUOTE_CHAR)
                    .setQuoteMode(QuoteMode.MINIMAL)
                    .setSkipHeaderRecord(false)
                    .build();

    /**
     * Default MySQL format used by the {@code SELECT INTO OUTFILE} and {@code LOAD DATA INFILE}
     * operations.
     *
     * <p>This is a tab-delimited format with a LF character as the line separator. Values are not
     * quoted and special characters are escaped with {@code '\'}. The default NULL string is {@code
     * "\\N"}.
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter('\t')}
     *   <li>{@code setEscape('\\')}
     *   <li>{@code setIgnoreEmptyLines(false)}
     *   <li>{@code setQuote(null)}
     *   <li>{@code setRecordSeparator('\n')}
     *   <li>{@code setNullString("\\N")}
     *   <li>{@code setQuoteMode(QuoteMode.ALL_NON_NULL)}
     * </ul>
     *
     * @see Predefined#MySQL
     * @see <a href="http://dev.mysql.com/doc/refman/5.1/en/load-data.html">
     *     http://dev.mysql.com/doc/refman/5.1/en/load -data.html</a>
     */
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

    /**
     * Default Oracle format used by the SQL*Loader utility.
     *
     * <p>This is a comma-delimited format with the system line separator character as the record
     * separator.Values are double quoted when needed and special characters are escaped with {@code
     * '"'}. The default NULL string is {@code ""}. Values are trimmed.
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter(',') // default is {@code FIELDS TERMINATED BY ','}}
     *   <li>{@code setEscape('\\')}
     *   <li>{@code setIgnoreEmptyLines(false)}
     *   <li>{@code setQuote('"') // default is {@code OPTIONALLY ENCLOSED BY '"'}}
     *   <li>{@code setNullString("\\N")}
     *   <li>{@code setTrim()}
     *   <li>{@code setSystemRecordSeparator()}
     *   <li>{@code setQuoteMode(QuoteMode.MINIMAL)}
     * </ul>
     *
     * @see Predefined#Oracle
     * @see <a href="https://s.apache.org/CGXG">Oracle CSV Format Specification</a>
     * @since 1.6
     */
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

    /**
     * Default PostgreSQL CSV format used by the {@code COPY} operation.
     *
     * <p>This is a comma-delimited format with a LF character as the line separator. Values are
     * double quoted and special characters are not escaped. The default NULL string is {@code ""}.
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter(',')}
     *   <li>{@code setEscape(null)}
     *   <li>{@code setIgnoreEmptyLines(false)}
     *   <li>{@code setQuote('"')}
     *   <li>{@code setRecordSeparator('\n')}
     *   <li>{@code setNullString("")}
     *   <li>{@code setQuoteMode(QuoteMode.ALL_NON_NULL)}
     * </ul>
     *
     * @see Predefined#MySQL
     * @see <a href="https://www.postgresql.org/docs/current/static/sql-copy.html">PostgreSQL COPY
     *     command documentation</a>
     * @since 1.5
     */
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

    /**
     * Default PostgreSQL text format used by the {@code COPY} operation.
     *
     * <p>This is a tab-delimited format with a LF character as the line separator. Values are not
     * quoted and special characters are escaped with {@code '\\'}. The default NULL string is
     * {@code "\\N"}.
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter('\t')}
     *   <li>{@code setEscape('\\')}
     *   <li>{@code setIgnoreEmptyLines(false)}
     *   <li>{@code setQuote(null)}
     *   <li>{@code setRecordSeparator('\n')}
     *   <li>{@code setNullString("\\N")}
     *   <li>{@code setQuoteMode(QuoteMode.ALL_NON_NULL)}
     * </ul>
     *
     * @see Predefined#MySQL
     * @see <a href="https://www.postgresql.org/docs/current/static/sql-copy.html">PostgreSQL COPY
     *     command documentation</a>
     * @since 1.5
     */
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

    /**
     * Comma separated format as defined by <a href="http://tools.ietf.org/html/rfc4180">RFC
     * 4180</a>.
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter(',')}
     *   <li>{@code setQuote('"')}
     *   <li>{@code setRecordSeparator("\r\n")}
     *   <li>{@code setIgnoreEmptyLines(false)}
     * </ul>
     *
     * @see Predefined#RFC4180
     */
    public static final CSVFormat RFC4180 = DEFAULT.builder().setIgnoreEmptyLines(false).build();

    private static final long serialVersionUID = 2L;

    /**
     * Tab-delimited format.
     *
     * <p>The {@link Builder} settings are:
     *
     * <ul>
     *   <li>{@code setDelimiter('\t')}
     *   <li>{@code setQuote('"')}
     *   <li>{@code setRecordSeparator("\r\n")}
     *   <li>{@code setIgnoreSurroundingSpaces(true)}
     * </ul>
     *
     * @see Predefined#TDF
     */
    public static final CSVFormat TDF =
            DEFAULT.builder().setDelimiter0(TAB).setIgnoreSurroundingSpaces(true).build();

    /**
     * Null-safe clone of an array.
     *
     * @param <T> The array element type.
     * @param values the source array
     * @return the cloned array.
     */
    @SafeVarargs
    static <T> T[] clone(final T... values) {
        return values == null ? null : values.clone();
    }

    /**
     * Returns true if the given string contains the search char.
     *
     * @param source the string to check.
     * @param searchCh the character to search.
     * @return true if {@code c} contains a line break character
     */
    private static boolean contains(final String source, final char searchCh) {
        return Objects.requireNonNull(source, "source").indexOf(searchCh) >= 0;
    }

    /**
     * Returns true if the given string contains a line break character.
     *
     * @param source the string to check.
     * @return true if {@code c} contains a line break character.
     */
    private static boolean containsLineBreak(final String source) {
        return contains(source, CR) || contains(source, LF);
    }

    static boolean isBlank(final String value) {
        return value == null || value.trim().isEmpty();
    }

    /**
     * Returns true if the given character is a line break character.
     *
     * @param c the character to check.
     * @return true if {@code c} is a line break character.
     */
    private static boolean isLineBreak0(final char c) {
        return c == LF || c == CR;
    }

    /**
     * Returns true if the given character is a line break character.
     *
     * @param c the character to check, may be null.
     * @return true if {@code c} is a line break character (and not null).
     */
    private static boolean isLineBreak1(final Character c) {
        return c != null && isLineBreak0(c.charValue());
    }

    /** Same test as in as {@link String#trim()}. */
    private static boolean isTrimChar0(final char ch) {
        return ch <= SP;
    }

    /** Same test as in as {@link String#trim()}. */
    private static boolean isTrimChar1(final CharSequence charSequence, final int pos) {
        return isTrimChar0(charSequence.charAt(pos));
    }

    /**
     * Creates a new CSV format with the specified delimiter.
     *
     * <p>Use this method if you want to create a CSVFormat from scratch. All fields but the
     * delimiter will be initialized with null/false.
     *
     * @param delimiter the char used for value separation, must not be a line break character
     * @return a new CSV format.
     * @throws IllegalArgumentException if the delimiter is a line break character
     * @see #DEFAULT
     * @see #RFC4180
     * @see #MYSQL
     * @see #EXCEL
     * @see #TDF
     */
    public static CSVFormat newFormat(final char delimiter) {
        return new CSVFormat(
                0,
                false,
                false,
                String.valueOf(delimiter),
                null,
                null,
                false,
                false,
                null,
                null,
                false,
                null,
                null,
                false,
                DuplicateHeaderMode.ALLOW_ALL,
                null,
                false,
                false,
                null,
                null);
    }

    static String[] toStringArray(final Object[] values) {
        if (values == null) {
            return null;
        }
        final String[] strings = new String[values.length];
        Arrays.setAll(strings, i -> Objects.toString(values[i], null));
        return strings;
    }

    static CharSequence trim0(final CharSequence charSequence) {
        if (charSequence instanceof String) {
            return ((String) charSequence).trim();
        }
        final int count = charSequence.length();
        int len = count;
        int pos = 0;

        while (pos < len && isTrimChar1(charSequence, pos)) {
            pos++;
        }
        while (pos < len && isTrimChar1(charSequence, len - 1)) {
            len--;
        }
        return pos > 0 || len < count ? charSequence.subSequence(pos, len) : charSequence;
    }

    /**
     * Gets one of the predefined formats from {@link CSVFormat.Predefined}.
     *
     * @param format name
     * @return one of the predefined formats
     * @since 1.2
     */
    public static CSVFormat valueOf(final String format) {
        return CSVFormat.Predefined.valueOf(format).getFormat();
    }

    private final DuplicateHeaderMode duplicateHeaderMode;

    private final boolean allowMissingColumnNames;

    private final boolean autoFlush;

    private final Character commentMarker; // null if commenting is disabled

    private final String delimiter;

    private final Character escapeCharacter; // null if escaping is disabled

    private final String[] headers; // array of header column names

    private final String[] headerComments; // array of header comment lines

    private final boolean ignoreEmptyLines;

    private final boolean ignoreHeaderCase; // should ignore header names case

    private final boolean
            ignoreSurroundingSpaces; // Should leading/trailing spaces be ignored around values?

    private final String nullString; // the string to be used for null values

    private final Character quoteCharacter; // null if quoting is disabled

    private final String quotedNullString;

    private final QuoteMode quoteMode;

    private final String recordSeparator; // for outputs

    private final boolean skipHeaderRecord;

    private final boolean trailingDelimiter;

    private final boolean trim;

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
        if (constructorId == 0) {

            this.delimiter = delimiter;
            this.quoteCharacter = quoteChar;
            this.quoteMode = quoteMode;
            this.commentMarker = commentStart;
            this.escapeCharacter = escape;
            this.ignoreSurroundingSpaces = ignoreSurroundingSpaces;
            this.allowMissingColumnNames = allowMissingColumnNames;
            this.ignoreEmptyLines = ignoreEmptyLines;
            this.recordSeparator = recordSeparator;
            this.nullString = nullString;
            this.headerComments = toStringArray(headerComments);
            this.headers = clone(header);
            this.skipHeaderRecord = skipHeaderRecord;
            this.ignoreHeaderCase = ignoreHeaderCase;
            this.trailingDelimiter = trailingDelimiter;
            this.trim = trim;
            this.autoFlush = autoFlush;
            this.quotedNullString = quoteCharacter + nullString + quoteCharacter;
            this.duplicateHeaderMode = duplicateHeaderMode;
            validate();
        } else {

            this.delimiter = builder.delimiter;
            this.quoteCharacter = builder.quoteCharacter;
            this.quoteMode = builder.quoteMode;
            this.commentMarker = builder.commentMarker;
            this.escapeCharacter = builder.escapeCharacter;
            this.ignoreSurroundingSpaces = builder.ignoreSurroundingSpaces;
            this.allowMissingColumnNames = builder.allowMissingColumnNames;
            this.ignoreEmptyLines = builder.ignoreEmptyLines;
            this.recordSeparator = builder.recordSeparator;
            this.nullString = builder.nullString;
            this.headerComments = builder.headerComments;
            this.headers = builder.headers;
            this.skipHeaderRecord = builder.skipHeaderRecord;
            this.ignoreHeaderCase = builder.ignoreHeaderCase;
            this.trailingDelimiter = builder.trailingDelimiter;
            this.trim = builder.trim;
            this.autoFlush = builder.autoFlush;
            this.quotedNullString = builder.quotedNullString;
            this.duplicateHeaderMode = builder.duplicateHeaderMode;
            validate();
        }
    }

    /**
     * Creates a customized CSV format.
     *
     * @param delimiter the char used for value separation, must not be a line break character.
     * @param quoteChar the Character used as value encapsulation marker, may be {@code null} to
     *     disable.
     * @param quoteMode the quote mode.
     * @param commentStart the Character used for comment identification, may be {@code null} to
     *     disable.
     * @param escape the Character used to escape special characters in values, may be {@code null}
     *     to disable.
     * @param ignoreSurroundingSpaces {@code true} when whitespaces enclosing values should be
     *     ignored.
     * @param ignoreEmptyLines {@code true} when the parser should skip empty lines.
     * @param recordSeparator the line separator to use for output.
     * @param nullString the line separator to use for output.
     * @param headerComments the comments to be printed by the Printer before the actual CSV data.
     * @param header the header
     * @param skipHeaderRecord TODO Doc me.
     * @param allowMissingColumnNames TODO Doc me.
     * @param ignoreHeaderCase TODO Doc me.
     * @param trim TODO Doc me.
     * @param trailingDelimiter TODO Doc me.
     * @param autoFlush TODO Doc me.
     * @param duplicateHeaderMode the behavior when handling duplicate headers
     * @throws IllegalArgumentException if the delimiter is a line break character.
     */
    private void append0(final char c, final Appendable appendable) throws IOException {
        appendable.append(c);
    }

    private void append1(final CharSequence csq, final Appendable appendable) throws IOException {
        appendable.append(csq);
    }

    /**
     * Creates a new Builder for this instance.
     *
     * @return a new Builder.
     */
    public Builder builder() {
        return Builder.create1(this);
    }

    /**
     * Creates a copy of this instance.
     *
     * @return a copy of this instance.
     */
    CSVFormat copy() {
        return builder().build();
    }

    @Override
    public boolean equals(final Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        final CSVFormat other = (CSVFormat) obj;
        return duplicateHeaderMode == other.duplicateHeaderMode
                && allowMissingColumnNames == other.allowMissingColumnNames
                && autoFlush == other.autoFlush
                && Objects.equals(commentMarker, other.commentMarker)
                && Objects.equals(delimiter, other.delimiter)
                && Objects.equals(escapeCharacter, other.escapeCharacter)
                && Arrays.equals(headers, other.headers)
                && Arrays.equals(headerComments, other.headerComments)
                && ignoreEmptyLines == other.ignoreEmptyLines
                && ignoreHeaderCase == other.ignoreHeaderCase
                && ignoreSurroundingSpaces == other.ignoreSurroundingSpaces
                && Objects.equals(nullString, other.nullString)
                && Objects.equals(quoteCharacter, other.quoteCharacter)
                && quoteMode == other.quoteMode
                && Objects.equals(quotedNullString, other.quotedNullString)
                && Objects.equals(recordSeparator, other.recordSeparator)
                && skipHeaderRecord == other.skipHeaderRecord
                && trailingDelimiter == other.trailingDelimiter
                && trim == other.trim;
    }

    /**
     * Formats the specified values.
     *
     * @param values the values to format
     * @return the formatted values
     */
    public String format(final Object... values) {
        final StringWriter out = new StringWriter();
        try (CSVPrinter csvPrinter = new CSVPrinter(out, this)) {
            csvPrinter.printRecord1(values);
            final String res = out.toString();
            final int len =
                    recordSeparator != null
                            ? res.length() - recordSeparator.length()
                            : res.length();
            return res.substring(0, len);
        } catch (final IOException e) {
            throw new IllegalStateException(e);
        }
    }

    /**
     * Gets whether duplicate names are allowed in the headers.
     *
     * @return whether duplicate header names are allowed
     * @since 1.7
     * @deprecated Use {@link #getDuplicateHeaderMode()}.
     */
    @Deprecated
    public boolean getAllowDuplicateHeaderNames() {
        return duplicateHeaderMode == DuplicateHeaderMode.ALLOW_ALL;
    }

    /**
     * Gets whether missing column names are allowed when parsing the header line.
     *
     * @return {@code true} if missing column names are allowed when parsing the header line, {@code
     *     false} to throw an {@link IllegalArgumentException}.
     */
    public boolean getAllowMissingColumnNames() {
        return allowMissingColumnNames;
    }

    /**
     * Gets whether to flush on close.
     *
     * @return whether to flush on close.
     * @since 1.6
     */
    public boolean getAutoFlush() {
        return autoFlush;
    }

    /**
     * Gets the character marking the start of a line comment.
     *
     * @return the comment start marker, may be {@code null}
     */
    public Character getCommentMarker() {
        return commentMarker;
    }

    /**
     * Gets the first character delimiting the values (typically ';', ',' or '\t').
     *
     * @return the first delimiter character.
     * @deprecated Use {@link #getDelimiterString()}.
     */
    @Deprecated
    public char getDelimiter() {
        return delimiter.charAt(0);
    }

    /**
     * Gets the character delimiting the values (typically ";", "," or "\t").
     *
     * @return the delimiter.
     * @since 1.9.0
     */
    public String getDelimiterString() {
        return delimiter;
    }

    /**
     * Gets how duplicate headers are handled.
     *
     * @return if duplicate header values are allowed, allowed conditionally, or disallowed.
     * @since 1.10.0
     */
    public DuplicateHeaderMode getDuplicateHeaderMode() {
        return duplicateHeaderMode;
    }

    /**
     * Gets the escape character.
     *
     * @return the escape character, may be {@code null}
     */
    public Character getEscapeCharacter() {
        return escapeCharacter;
    }

    /**
     * Gets a copy of the header array.
     *
     * @return a copy of the header array; {@code null} if disabled, the empty array if to be read
     *     from the file
     */
    public String[] getHeader() {
        return headers != null ? headers.clone() : null;
    }

    /**
     * Gets a copy of the header comment array.
     *
     * @return a copy of the header comment array; {@code null} if disabled.
     */
    public String[] getHeaderComments() {
        return headerComments != null ? headerComments.clone() : null;
    }

    /**
     * Gets whether empty lines between records are ignored when parsing input.
     *
     * @return {@code true} if empty lines between records are ignored, {@code false} if they are
     *     turned into empty records.
     */
    public boolean getIgnoreEmptyLines() {
        return ignoreEmptyLines;
    }

    /**
     * Gets whether header names will be accessed ignoring case when parsing input.
     *
     * @return {@code true} if header names cases are ignored, {@code false} if they are case
     *     sensitive.
     * @since 1.3
     */
    public boolean getIgnoreHeaderCase() {
        return ignoreHeaderCase;
    }

    /**
     * Gets whether spaces around values are ignored when parsing input.
     *
     * @return {@code true} if spaces around values are ignored, {@code false} if they are treated
     *     as part of the value.
     */
    public boolean getIgnoreSurroundingSpaces() {
        return ignoreSurroundingSpaces;
    }

    /**
     * Gets the String to convert to and from {@code null}.
     *
     * <ul>
     *   <li><strong>Reading:</strong> Converts strings equal to the given {@code nullString} to
     *       {@code null} when reading records.
     *   <li><strong>Writing:</strong> Writes {@code null} as the given {@code nullString} when
     *       writing records.
     * </ul>
     *
     * @return the String to convert to and from {@code null}. No substitution occurs if {@code
     *     null}
     */
    public String getNullString() {
        return nullString;
    }

    /**
     * Gets the character used to encapsulate values containing special characters.
     *
     * @return the quoteChar character, may be {@code null}
     */
    public Character getQuoteCharacter() {
        return quoteCharacter;
    }

    /**
     * Gets the quote policy output fields.
     *
     * @return the quote policy
     */
    public QuoteMode getQuoteMode() {
        return quoteMode;
    }

    /**
     * Gets the record separator delimiting output records.
     *
     * @return the record separator
     */
    public String getRecordSeparator() {
        return recordSeparator;
    }

    /**
     * Gets whether to skip the header record.
     *
     * @return whether to skip the header record.
     */
    public boolean getSkipHeaderRecord() {
        return skipHeaderRecord;
    }

    /**
     * Gets whether to add a trailing delimiter.
     *
     * @return whether to add a trailing delimiter.
     * @since 1.3
     */
    public boolean getTrailingDelimiter() {
        return trailingDelimiter;
    }

    /**
     * Gets whether to trim leading and trailing blanks. This is used by {@link #print(Object,
     * Appendable, boolean)} Also by {CSVParser#addRecordValue(boolean)}
     *
     * @return whether to trim leading and trailing blanks.
     */
    public boolean getTrim() {
        return trim;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + Arrays.hashCode(headers);
        result = prime * result + Arrays.hashCode(headerComments);
        return prime * result
                + Objects.hash(
                        duplicateHeaderMode,
                        allowMissingColumnNames,
                        autoFlush,
                        commentMarker,
                        delimiter,
                        escapeCharacter,
                        ignoreEmptyLines,
                        ignoreHeaderCase,
                        ignoreSurroundingSpaces,
                        nullString,
                        quoteCharacter,
                        quoteMode,
                        quotedNullString,
                        recordSeparator,
                        skipHeaderRecord,
                        trailingDelimiter,
                        trim);
    }

    /**
     * Tests whether comments are supported by this format.
     *
     * <p>Note that the comment introducer character is only recognized at the start of a line.
     *
     * @return {@code true} is comments are supported, {@code false} otherwise
     */
    public boolean isCommentMarkerSet() {
        return commentMarker != null;
    }

    /**
     * Tests whether the next characters constitute a delimiter
     *
     * @param ch the current char
     * @param charSeq the match char sequence
     * @param startIndex where start to match
     * @param delimiter the delimiter
     * @param delimiterLength the delimiter length
     * @return true if the match is successful
     */
    private boolean isDelimiter(
            final char ch,
            final CharSequence charSeq,
            final int startIndex,
            final char[] delimiter,
            final int delimiterLength) {
        if (ch != delimiter[0]) {
            return false;
        }
        final int len = charSeq.length();
        if (startIndex + delimiterLength > len) {
            return false;
        }
        for (int i = 1; i < delimiterLength; i++) {
            if (charSeq.charAt(startIndex + i) != delimiter[i]) {
                return false;
            }
        }
        return true;
    }

    /**
     * Tests whether escape are being processed.
     *
     * @return {@code true} if escapes are processed
     */
    public boolean isEscapeCharacterSet() {
        return escapeCharacter != null;
    }

    /**
     * Tests whether a nullString has been defined.
     *
     * @return {@code true} if a nullString is defined
     */
    public boolean isNullStringSet() {
        return nullString != null;
    }

    /**
     * Tests whether a quoteChar has been defined.
     *
     * @return {@code true} if a quoteChar is defined
     */
    public boolean isQuoteCharacterSet() {
        return quoteCharacter != null;
    }

    /**
     * Parses the specified content.
     *
     * <p>See also the various static parse methods on {@link CSVParser}.
     *
     * @param reader the input stream
     * @return a parser over a stream of {@link CSVRecord}s.
     * @throws IOException If an I/O error occurs
     */
    public CSVParser parse(final Reader reader) throws IOException {
        return CSVParser.CSVParser1(reader, this);
    }

    /**
     * Prints to the specified output.
     *
     * <p>See also {@link CSVPrinter}.
     *
     * @param out the output.
     * @return a printer to an output.
     * @throws IOException thrown if the optional header cannot be printed.
     */
    public CSVPrinter print0(final Appendable out) throws IOException {
        return new CSVPrinter(out, this);
    }

    /**
     * Prints to the specified output.
     *
     * <p>See also {@link CSVPrinter}.
     *
     * @param out the output.
     * @param charset A charset.
     * @return a printer to an output.
     * @throws IOException thrown if the optional header cannot be printed.
     * @since 1.5
     */
    @SuppressWarnings("resource")
    public CSVPrinter print1(final File out, final Charset charset) throws IOException {
        return new CSVPrinter(new OutputStreamWriter(new FileOutputStream(out), charset), this);
    }

    /**
     * Prints the {@code value} as the next value on the line to {@code out}. The value will be
     * escaped or encapsulated as needed. Useful when one wants to avoid creating CSVPrinters. Trims
     * the value if {@link #getTrim()} is true.
     *
     * @param value value to output.
     * @param out where to print the value.
     * @param newRecord if this a new record.
     * @throws IOException If an I/O error occurs.
     * @since 1.4
     */
    public synchronized void print2(
            final Object value, final Appendable out, final boolean newRecord) throws IOException {
        CharSequence charSequence;
        if (value == null) {
            if (null == nullString) {
                charSequence = EMPTY;
            } else if (QuoteMode.ALL == quoteMode) {
                charSequence = quotedNullString;
            } else {
                charSequence = nullString;
            }
        } else if (value instanceof CharSequence) {
            charSequence = (CharSequence) value;
        } else if (value instanceof Reader) {
            print5((Reader) value, out, newRecord);
            return;
        } else {
            charSequence = value.toString();
        }
        charSequence = getTrim() ? trim0(charSequence) : charSequence;
        print3(value, charSequence, out, newRecord);
    }

    private synchronized void print3(
            final Object object,
            final CharSequence value,
            final Appendable out,
            final boolean newRecord)
            throws IOException {
        final int offset = 0;
        final int len = value.length();
        if (!newRecord) {
            out.append(getDelimiterString());
        }
        if (object == null) {
            out.append(value);
        } else if (isQuoteCharacterSet()) {
            printWithQuotes0(object, value, out, newRecord);
        } else if (isEscapeCharacterSet()) {
            printWithEscapes0(value, out);
        } else {
            out.append(value, offset, len);
        }
    }

    /**
     * Prints to the specified output, returns a {@code CSVPrinter} which the caller MUST close.
     *
     * <p>See also {@link CSVPrinter}.
     *
     * @param out the output.
     * @param charset A charset.
     * @return a printer to an output.
     * @throws IOException thrown if the optional header cannot be printed.
     * @since 1.5
     */
    @SuppressWarnings("resource")
    public CSVPrinter print4(final Path out, final Charset charset) throws IOException {
        return print0(Files.newBufferedWriter(out, charset));
    }

    private void print5(final Reader reader, final Appendable out, final boolean newRecord)
            throws IOException {
        if (!newRecord) {
            append1(getDelimiterString(), out);
        }
        if (isQuoteCharacterSet()) {
            printWithQuotes1(reader, out);
        } else if (isEscapeCharacterSet()) {
            printWithEscapes1(reader, out);
        } else if (out instanceof Writer) {
            IOUtils.copyLarge0(reader, (Writer) out);
        } else {
            IOUtils.copy0(reader, out);
        }
    }

    /**
     * Prints to the {@link System#out}.
     *
     * <p>See also {@link CSVPrinter}.
     *
     * @return a printer to {@link System#out}.
     * @throws IOException thrown if the optional header cannot be printed.
     * @since 1.5
     */
    public CSVPrinter printer() throws IOException {
        return new CSVPrinter(System.out, this);
    }

    /**
     * Outputs the trailing delimiter (if set) followed by the record separator (if set).
     *
     * @param appendable where to write
     * @throws IOException If an I/O error occurs.
     * @since 1.4
     */
    public synchronized void println(final Appendable appendable) throws IOException {
        if (getTrailingDelimiter()) {
            append1(getDelimiterString(), appendable);
        }
        if (recordSeparator != null) {
            append1(recordSeparator, appendable);
        }
    }

    /**
     * Prints the given {@code values} to {@code out} as a single record of delimiter separated
     * values followed by the record separator.
     *
     * <p>The values will be quoted if needed. Quotes and new-line characters will be escaped. This
     * method adds the record separator to the output after printing the record, so there is no need
     * to call {@link #println(Appendable)}.
     *
     * @param appendable where to write.
     * @param values values to output.
     * @throws IOException If an I/O error occurs.
     * @since 1.4
     */
    public synchronized void printRecord(final Appendable appendable, final Object... values)
            throws IOException {
        for (int i = 0; i < values.length; i++) {
            print2(values[i], appendable, i == 0);
        }
        println(appendable);
    }

    /*
     * Note: Must only be called if escaping is enabled, otherwise will generate NPE.
     */
    private void printWithEscapes0(final CharSequence charSeq, final Appendable appendable)
            throws IOException {
        int start = 0;
        int pos = 0;
        final int end = charSeq.length();

        final char[] delim = getDelimiterString().toCharArray();
        final int delimLength = delim.length;
        final char escape = getEscapeCharacter().charValue();

        while (pos < end) {
            char c = charSeq.charAt(pos);
            final boolean isDelimiterStart = isDelimiter(c, charSeq, pos, delim, delimLength);
            if (c == CR || c == LF || c == escape || isDelimiterStart) {
                if (pos > start) {
                    appendable.append(charSeq, start, pos);
                }
                if (c == LF) {
                    c = 'n';
                } else if (c == CR) {
                    c = 'r';
                }

                appendable.append(escape);
                appendable.append(c);

                if (isDelimiterStart) {
                    for (int i = 1; i < delimLength; i++) {
                        pos++;
                        c = charSeq.charAt(pos);
                        appendable.append(escape);
                        appendable.append(c);
                    }
                }

                start = pos + 1; // start on the current char after this one
            }
            pos++;
        }

        if (pos > start) {
            appendable.append(charSeq, start, pos);
        }
    }

    private void printWithEscapes1(final Reader reader, final Appendable appendable)
            throws IOException {
        int start = 0;
        int pos = 0;

        @SuppressWarnings("resource") // Temp reader on input reader.
        final ExtendedBufferedReader bufferedReader = new ExtendedBufferedReader(reader);
        final char[] delim = getDelimiterString().toCharArray();
        final int delimLength = delim.length;
        final char escape = getEscapeCharacter().charValue();
        final StringBuilder builder = new StringBuilder(IOUtils.DEFAULT_BUFFER_SIZE);

        int c;
        while (-1 != (c = bufferedReader.read0())) {
            builder.append((char) c);
            final boolean isDelimiterStart =
                    isDelimiter(
                            (char) c,
                            builder.toString()
                                    + new String(bufferedReader.lookAhead2(delimLength - 1)),
                            pos,
                            delim,
                            delimLength);
            if (c == CR || c == LF || c == escape || isDelimiterStart) {
                if (pos > start) {
                    append1(builder.substring(start, pos), appendable);
                    builder.setLength(0);
                    pos = -1;
                }
                if (c == LF) {
                    c = 'n';
                } else if (c == CR) {
                    c = 'r';
                }

                append0(escape, appendable);
                append0((char) c, appendable);

                if (isDelimiterStart) {
                    for (int i = 1; i < delimLength; i++) {
                        c = bufferedReader.read0();
                        append0(escape, appendable);
                        append0((char) c, appendable);
                    }
                }

                start = pos + 1; // start on the current char after this one
            }
            pos++;
        }

        if (pos > start) {
            append1(builder.substring(start, pos), appendable);
        }
    }

    /*
     * Note: must only be called if quoting is enabled, otherwise will generate NPE
     */
    private void printWithQuotes0(
            final Object object,
            final CharSequence charSeq,
            final Appendable out,
            final boolean newRecord)
            throws IOException {
        boolean quote = false;
        int start = 0;
        int pos = 0;
        final int len = charSeq.length();

        final char[] delim = getDelimiterString().toCharArray();
        final int delimLength = delim.length;
        final char quoteChar = getQuoteCharacter().charValue();
        final char escapeChar =
                isEscapeCharacterSet() ? getEscapeCharacter().charValue() : quoteChar;

        QuoteMode quoteModePolicy = getQuoteMode();
        if (quoteModePolicy == null) {
            quoteModePolicy = QuoteMode.MINIMAL;
        }
        switch (quoteModePolicy) {
            case ALL:
            case ALL_NON_NULL:
                quote = true;
                break;
            case NON_NUMERIC:
                quote = !(object instanceof Number);
                break;
            case NONE:
                printWithEscapes0(charSeq, out);
                return;
            case MINIMAL:
                if (len <= 0) {
                    if (newRecord) {
                        quote = true;
                    }
                } else {
                    char c = charSeq.charAt(pos);

                    if (c <= COMMENT) {
                        quote = true;
                    } else {
                        while (pos < len) {
                            c = charSeq.charAt(pos);
                            if (c == LF
                                    || c == CR
                                    || c == quoteChar
                                    || c == escapeChar
                                    || isDelimiter(c, charSeq, pos, delim, delimLength)) {
                                quote = true;
                                break;
                            }
                            pos++;
                        }

                        if (!quote) {
                            pos = len - 1;
                            c = charSeq.charAt(pos);
                            if (isTrimChar0(c)) {
                                quote = true;
                            }
                        }
                    }
                }

                if (!quote) {
                    out.append(charSeq, start, len);
                    return;
                }
                break;
            default:
                throw new IllegalStateException("Unexpected Quote value: " + quoteModePolicy);
        }

        if (!quote) {
            out.append(charSeq, start, len);
            return;
        }

        out.append(quoteChar);

        while (pos < len) {
            final char c = charSeq.charAt(pos);
            if (c == quoteChar || c == escapeChar) {
                out.append(charSeq, start, pos);
                out.append(escapeChar); // now output the escape
                start = pos; // and restart with the matched char
            }
            pos++;
        }

        out.append(charSeq, start, pos);
        out.append(quoteChar);
    }

    /**
     * Always use quotes unless QuoteMode is NONE, so we not have to look ahead.
     *
     * @param reader What to print
     * @param appendable Where to print it
     * @throws IOException If an I/O error occurs
     */
    private void printWithQuotes1(final Reader reader, final Appendable appendable)
            throws IOException {

        if (getQuoteMode() == QuoteMode.NONE) {
            printWithEscapes1(reader, appendable);
            return;
        }

        int pos = 0;

        final char quote = getQuoteCharacter().charValue();
        final StringBuilder builder = new StringBuilder(IOUtils.DEFAULT_BUFFER_SIZE);

        append0(quote, appendable);

        int c;
        while (-1 != (c = reader.read())) {
            builder.append((char) c);
            if (c == quote) {
                if (pos > 0) {
                    append1(builder.substring(0, pos), appendable);
                    append0(quote, appendable);
                    builder.setLength(0);
                    pos = -1;
                }

                append0((char) c, appendable);
            }
            pos++;
        }

        if (pos > 0) {
            append1(builder.substring(0, pos), appendable);
        }

        append0(quote, appendable);
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder();
        sb.append("Delimiter=<").append(delimiter).append('>');
        if (isEscapeCharacterSet()) {
            sb.append(' ');
            sb.append("Escape=<").append(escapeCharacter).append('>');
        }
        if (isQuoteCharacterSet()) {
            sb.append(' ');
            sb.append("QuoteChar=<").append(quoteCharacter).append('>');
        }
        if (quoteMode != null) {
            sb.append(' ');
            sb.append("QuoteMode=<").append(quoteMode).append('>');
        }
        if (isCommentMarkerSet()) {
            sb.append(' ');
            sb.append("CommentStart=<").append(commentMarker).append('>');
        }
        if (isNullStringSet()) {
            sb.append(' ');
            sb.append("NullString=<").append(nullString).append('>');
        }
        if (recordSeparator != null) {
            sb.append(' ');
            sb.append("RecordSeparator=<").append(recordSeparator).append('>');
        }
        if (getIgnoreEmptyLines()) {
            sb.append(" EmptyLines:ignored");
        }
        if (getIgnoreSurroundingSpaces()) {
            sb.append(" SurroundingSpaces:ignored");
        }
        if (getIgnoreHeaderCase()) {
            sb.append(" IgnoreHeaderCase:ignored");
        }
        sb.append(" SkipHeaderRecord:").append(skipHeaderRecord);
        if (headerComments != null) {
            sb.append(' ');
            sb.append("HeaderComments:").append(Arrays.toString(headerComments));
        }
        if (headers != null) {
            sb.append(' ');
            sb.append("Header:").append(Arrays.toString(headers));
        }
        return sb.toString();
    }

    String trim1(final String value) {
        return getTrim() ? value.trim() : value;
    }

    /**
     * Verifies the validity and consistency of the attributes, and throws an {@link
     * IllegalArgumentException} if necessary.
     *
     * <p>Because an instance can be used for both writing an parsing, not all conditions can be
     * tested here. For example allowMissingColumnNames is only used for parsing, so it cannot be
     * used here.
     *
     * @throws IllegalArgumentException Throw when any attribute is invalid or inconsistent with
     *     other attributes.
     */
    private void validate() throws IllegalArgumentException {
        if (containsLineBreak(delimiter)) {
            throw new IllegalArgumentException("The delimiter cannot be a line break");
        }

        if (quoteCharacter != null && contains(delimiter, quoteCharacter.charValue())) {
            throw new IllegalArgumentException(
                    "The quoteChar character and the delimiter cannot be the same ('"
                            + quoteCharacter
                            + "')");
        }

        if (escapeCharacter != null && contains(delimiter, escapeCharacter.charValue())) {
            throw new IllegalArgumentException(
                    "The escape character and the delimiter cannot be the same ('"
                            + escapeCharacter
                            + "')");
        }

        if (commentMarker != null && contains(delimiter, commentMarker.charValue())) {
            throw new IllegalArgumentException(
                    "The comment start character and the delimiter cannot be the same ('"
                            + commentMarker
                            + "')");
        }

        if (quoteCharacter != null && quoteCharacter.equals(commentMarker)) {
            throw new IllegalArgumentException(
                    "The comment start character and the quoteChar cannot be the same ('"
                            + commentMarker
                            + "')");
        }

        if (escapeCharacter != null && escapeCharacter.equals(commentMarker)) {
            throw new IllegalArgumentException(
                    "The comment start and the escape character cannot be the same ('"
                            + commentMarker
                            + "')");
        }

        if (escapeCharacter == null && quoteMode == QuoteMode.NONE) {
            throw new IllegalArgumentException("No quotes mode set but no escape character is set");
        }

        if (headers != null && duplicateHeaderMode != DuplicateHeaderMode.ALLOW_ALL) {
            final Set<String> dupCheckSet = new HashSet<>(headers.length);
            final boolean emptyDuplicatesAllowed =
                    duplicateHeaderMode == DuplicateHeaderMode.ALLOW_EMPTY;
            for (final String header : headers) {
                final boolean blank = isBlank(header);
                final boolean containsHeader = !dupCheckSet.add(blank ? "" : header);
                if (containsHeader && !(blank && emptyDuplicatesAllowed)) {
                    throw new IllegalArgumentException(
                            String.format(
                                    "The header contains a duplicate name: \"%s\" in %s. If this is"
                                            + " valid then use"
                                            + " CSVFormat.Builder.setDuplicateHeaderMode().",
                                    header, Arrays.toString(headers)));
                }
            }
        }
    }

    /**
     * Builds a new {@code CSVFormat} that allows duplicate header names.
     *
     * @return a new {@code CSVFormat} that allows duplicate header names
     * @since 1.7
     * @deprecated Use {@link Builder#setAllowDuplicateHeaderNames(boolean)
     *     Builder#setAllowDuplicateHeaderNames(true)}
     */
    @Deprecated
    public CSVFormat withAllowDuplicateHeaderNames0() {
        return builder().setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL).build();
    }

    /**
     * Builds a new {@code CSVFormat} with duplicate header names behavior set to the given value.
     *
     * @param allowDuplicateHeaderNames the duplicate header names behavior, true to allow, false to
     *     disallow.
     * @return a new {@code CSVFormat} with duplicate header names behavior set to the given value.
     * @since 1.7
     * @deprecated Use {@link Builder#setAllowDuplicateHeaderNames(boolean)}
     */
    @Deprecated
    public CSVFormat withAllowDuplicateHeaderNames1(final boolean allowDuplicateHeaderNames) {
        final DuplicateHeaderMode mode =
                allowDuplicateHeaderNames
                        ? DuplicateHeaderMode.ALLOW_ALL
                        : DuplicateHeaderMode.ALLOW_EMPTY;
        return builder().setDuplicateHeaderMode(mode).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the missing column names behavior of the format set to
     * {@code true}.
     *
     * @return A new CSVFormat that is equal to this but with the specified missing column names
     *     behavior.
     * @see Builder#setAllowMissingColumnNames(boolean)
     * @since 1.1
     * @deprecated Use {@link Builder#setAllowMissingColumnNames(boolean)
     *     Builder#setAllowMissingColumnNames(true)}
     */
    @Deprecated
    public CSVFormat withAllowMissingColumnNames0() {
        return builder().setAllowMissingColumnNames(true).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the missing column names behavior of the format set to
     * the given value.
     *
     * @param allowMissingColumnNames the missing column names behavior, {@code true} to allow
     *     missing column names in the header line, {@code false} to cause an {@link
     *     IllegalArgumentException} to be thrown.
     * @return A new CSVFormat that is equal to this but with the specified missing column names
     *     behavior.
     * @deprecated Use {@link Builder#setAllowMissingColumnNames(boolean)}
     */
    @Deprecated
    public CSVFormat withAllowMissingColumnNames1(final boolean allowMissingColumnNames) {
        return builder().setAllowMissingColumnNames(allowMissingColumnNames).build();
    }

    /**
     * Builds a new {@code CSVFormat} with whether to flush on close.
     *
     * @param autoFlush whether to flush on close.
     * @return A new CSVFormat that is equal to this but with the specified autoFlush setting.
     * @since 1.6
     * @deprecated Use {@link Builder#setAutoFlush(boolean)}
     */
    @Deprecated
    public CSVFormat withAutoFlush(final boolean autoFlush) {
        return builder().setAutoFlush(autoFlush).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the comment start marker of the format set to the
     * specified character.
     *
     * <p>Note that the comment start character is only recognized at the start of a line.
     *
     * @param commentMarker the comment start marker
     * @return A new CSVFormat that is equal to this one but with the specified character as the
     *     comment start marker
     * @throws IllegalArgumentException thrown if the specified character is a line break
     * @deprecated Use {@link Builder#setCommentMarker(char)}
     */
    @Deprecated
    public CSVFormat withCommentMarker0(final char commentMarker) {
        return builder().setCommentMarker0(commentMarker).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the comment start marker of the format set to the
     * specified character.
     *
     * <p>Note that the comment start character is only recognized at the start of a line.
     *
     * @param commentMarker the comment start marker, use {@code null} to disable
     * @return A new CSVFormat that is equal to this one but with the specified character as the
     *     comment start marker
     * @throws IllegalArgumentException thrown if the specified character is a line break
     * @deprecated Use {@link Builder#setCommentMarker(Character)}
     */
    @Deprecated
    public CSVFormat withCommentMarker1(final Character commentMarker) {
        return builder().setCommentMarker1(commentMarker).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the delimiter of the format set to the specified
     * character.
     *
     * @param delimiter the delimiter character
     * @return A new CSVFormat that is equal to this with the specified character as delimiter
     * @throws IllegalArgumentException thrown if the specified character is a line break
     * @deprecated Use {@link Builder#setDelimiter(char)}
     */
    @Deprecated
    public CSVFormat withDelimiter(final char delimiter) {
        return builder().setDelimiter0(delimiter).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the escape character of the format set to the specified
     * character.
     *
     * @param escape the escape character
     * @return A new CSVFormat that is equal to this but with the specified character as the escape
     *     character
     * @throws IllegalArgumentException thrown if the specified character is a line break
     * @deprecated Use {@link Builder#setEscape(char)}
     */
    @Deprecated
    public CSVFormat withEscape0(final char escape) {
        return builder().setEscape0(escape).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the escape character of the format set to the specified
     * character.
     *
     * @param escape the escape character, use {@code null} to disable
     * @return A new CSVFormat that is equal to this but with the specified character as the escape
     *     character
     * @throws IllegalArgumentException thrown if the specified character is a line break
     * @deprecated Use {@link Builder#setEscape(Character)}
     */
    @Deprecated
    public CSVFormat withEscape1(final Character escape) {
        return builder().setEscape1(escape).build();
    }

    /**
     * Builds a new {@code CSVFormat} using the first record as header.
     *
     * <p>Calling this method is equivalent to calling:
     *
     * <pre>
     * CSVFormat format = aFormat.withHeader().withSkipHeaderRecord();
     * </pre>
     *
     * @return A new CSVFormat that is equal to this but using the first record as header.
     * @see Builder#setSkipHeaderRecord(boolean)
     * @see Builder#setHeader(String...)
     * @since 1.3
     * @deprecated Use {@link Builder#setHeader(String...) Builder#setHeader()}.{@link
     *     Builder#setSkipHeaderRecord(boolean) setSkipHeaderRecord(true)}.
     */

    /**
     * Builds a new {@code CSVFormat} with the header of the format defined by the enum class.
     *
     * <p>Example:
     *
     * <pre>
     * public enum Header {
     *     Name, Email, Phone
     * }
     *
     * CSVFormat format = aformat.withHeader(Header.class);
     * </pre>
     *
     * <p>The header is also used by the {@link CSVPrinter}.
     *
     * @param headerEnum the enum defining the header, {@code null} if disabled, empty if parsed
     *     automatically, user specified otherwise.
     * @return A new CSVFormat that is equal to this but with the specified header
     * @see Builder#setHeader(String...)
     * @see Builder#setSkipHeaderRecord(boolean)
     * @since 1.3
     * @deprecated Use {@link Builder#setHeader(Class)}
     */

    /**
     * Builds a new {@code CSVFormat} with the header of the format set from the result set
     * metadata. The header can either be parsed automatically from the input file with:
     *
     * <pre>
     * CSVFormat format = aformat.withHeader();
     * </pre>
     *
     * or specified manually with:
     *
     * <pre>
     * CSVFormat format = aformat.withHeader(resultSet);
     * </pre>
     *
     * <p>The header is also used by the {@link CSVPrinter}.
     *
     * @param resultSet the resultSet for the header, {@code null} if disabled, empty if parsed
     *     automatically, user specified otherwise.
     * @return A new CSVFormat that is equal to this but with the specified header
     * @throws SQLException SQLException if a database access error occurs or this method is called
     *     on a closed result set.
     * @since 1.1
     * @deprecated Use {@link Builder#setHeader(ResultSet)}
     */

    /**
     * Builds a new {@code CSVFormat} with the header of the format set from the result set
     * metadata. The header can either be parsed automatically from the input file with:
     *
     * <pre>
     * CSVFormat format = aformat.withHeader();
     * </pre>
     *
     * or specified manually with:
     *
     * <pre>
     * CSVFormat format = aformat.withHeader(metaData);
     * </pre>
     *
     * <p>The header is also used by the {@link CSVPrinter}.
     *
     * @param resultSetMetaData the metaData for the header, {@code null} if disabled, empty if
     *     parsed automatically, user specified otherwise.
     * @return A new CSVFormat that is equal to this but with the specified header
     * @throws SQLException SQLException if a database access error occurs or this method is called
     *     on a closed result set.
     * @since 1.1
     * @deprecated Use {@link Builder#setHeader(ResultSetMetaData)}
     */

    /**
     * Builds a new {@code CSVFormat} with the header of the format set to the given values. The
     * header can either be parsed automatically from the input file with:
     *
     * <pre>
     * CSVFormat format = aformat.withHeader();
     * </pre>
     *
     * or specified manually with:
     *
     * <pre>
     * CSVFormat format = aformat.withHeader(&quot;name&quot;, &quot;email&quot;, &quot;phone&quot;);
     * </pre>
     *
     * <p>The header is also used by the {@link CSVPrinter}.
     *
     * @param header the header, {@code null} if disabled, empty if parsed automatically, user
     *     specified otherwise.
     * @return A new CSVFormat that is equal to this but with the specified header
     * @see Builder#setSkipHeaderRecord(boolean)
     * @deprecated Use {@link Builder#setHeader(String...)}
     */

    /**
     * Builds a new {@code CSVFormat} with the header comments of the format set to the given
     * values. The comments will be printed first, before the headers. This setting is ignored by
     * the parser.
     *
     * <pre>
     * CSVFormat format = aformat.withHeaderComments(&quot;Generated by Apache Commons CSV.&quot;, Instant.now());
     * </pre>
     *
     * @param headerComments the headerComments which will be printed by the Printer before the
     *     actual CSV data.
     * @return A new CSVFormat that is equal to this but with the specified header
     * @see Builder#setSkipHeaderRecord(boolean)
     * @since 1.1
     * @deprecated Use {@link Builder#setHeaderComments(Object...)}
     */
    @Deprecated
    public CSVFormat withHeaderComments(final Object... headerComments) {
        return builder().setHeaderComments0(headerComments).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the empty line skipping behavior of the format set to
     * {@code true}.
     *
     * @return A new CSVFormat that is equal to this but with the specified empty line skipping
     *     behavior.
     * @see Builder#setIgnoreEmptyLines(boolean)
     * @since 1.1
     * @deprecated Use {@link Builder#setIgnoreEmptyLines(boolean)
     *     Builder#setIgnoreEmptyLines(true)}
     */
    @Deprecated
    public CSVFormat withIgnoreEmptyLines0() {
        return builder().setIgnoreEmptyLines(true).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the empty line skipping behavior of the format set to the
     * given value.
     *
     * @param ignoreEmptyLines the empty line skipping behavior, {@code true} to ignore the empty
     *     lines between the records, {@code false} to translate empty lines to empty records.
     * @return A new CSVFormat that is equal to this but with the specified empty line skipping
     *     behavior.
     * @deprecated Use {@link Builder#setIgnoreEmptyLines(boolean)}
     */
    @Deprecated
    public CSVFormat withIgnoreEmptyLines1(final boolean ignoreEmptyLines) {
        return builder().setIgnoreEmptyLines(ignoreEmptyLines).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the header ignore case behavior set to {@code true}.
     *
     * @return A new CSVFormat that will ignore case header name.
     * @see Builder#setIgnoreHeaderCase(boolean)
     * @since 1.3
     * @deprecated Use {@link Builder#setIgnoreHeaderCase(boolean)
     *     Builder#setIgnoreHeaderCase(true)}
     */
    @Deprecated
    public CSVFormat withIgnoreHeaderCase0() {
        return builder().setIgnoreHeaderCase(true).build();
    }

    /**
     * Builds a new {@code CSVFormat} with whether header names should be accessed ignoring case.
     *
     * @param ignoreHeaderCase the case mapping behavior, {@code true} to access name/values, {@code
     *     false} to leave the mapping as is.
     * @return A new CSVFormat that will ignore case header name if specified as {@code true}
     * @since 1.3
     * @deprecated Use {@link Builder#setIgnoreHeaderCase(boolean)}
     */
    @Deprecated
    public CSVFormat withIgnoreHeaderCase1(final boolean ignoreHeaderCase) {
        return builder().setIgnoreHeaderCase(ignoreHeaderCase).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the parser trimming behavior of the format set to {@code
     * true}.
     *
     * @return A new CSVFormat that is equal to this but with the specified parser trimming
     *     behavior.
     * @see Builder#setIgnoreSurroundingSpaces(boolean)
     * @since 1.1
     * @deprecated Use {@link Builder#setIgnoreSurroundingSpaces(boolean)
     *     Builder#setIgnoreSurroundingSpaces(true)}
     */
    @Deprecated
    public CSVFormat withIgnoreSurroundingSpaces0() {
        return builder().setIgnoreSurroundingSpaces(true).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the parser trimming behavior of the format set to the
     * given value.
     *
     * @param ignoreSurroundingSpaces the parser trimming behavior, {@code true} to remove the
     *     surrounding spaces, {@code false} to leave the spaces as is.
     * @return A new CSVFormat that is equal to this but with the specified trimming behavior.
     * @deprecated Use {@link Builder#setIgnoreSurroundingSpaces(boolean)}
     */
    @Deprecated
    public CSVFormat withIgnoreSurroundingSpaces1(final boolean ignoreSurroundingSpaces) {
        return builder().setIgnoreSurroundingSpaces(ignoreSurroundingSpaces).build();
    }

    /**
     * Builds a new {@code CSVFormat} with conversions to and from null for strings on input and
     * output.
     *
     * <ul>
     *   <li><strong>Reading:</strong> Converts strings equal to the given {@code nullString} to
     *       {@code null} when reading records.
     *   <li><strong>Writing:</strong> Writes {@code null} as the given {@code nullString} when
     *       writing records.
     * </ul>
     *
     * @param nullString the String to convert to and from {@code null}. No substitution occurs if
     *     {@code null}
     * @return A new CSVFormat that is equal to this but with the specified null conversion string.
     * @deprecated Use {@link Builder#setNullString(String)}
     */
    @Deprecated
    public CSVFormat withNullString(final String nullString) {
        return builder().setNullString(nullString).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the quoteChar of the format set to the specified
     * character.
     *
     * @param quoteChar the quote character
     * @return A new CSVFormat that is equal to this but with the specified character as quoteChar
     * @throws IllegalArgumentException thrown if the specified character is a line break
     * @deprecated Use {@link Builder#setQuote(char)}
     */
    @Deprecated
    public CSVFormat withQuote0(final char quoteChar) {
        return builder().setQuote0(quoteChar).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the quoteChar of the format set to the specified
     * character.
     *
     * @param quoteChar the quote character, use {@code null} to disable.
     * @return A new CSVFormat that is equal to this but with the specified character as quoteChar
     * @throws IllegalArgumentException thrown if the specified character is a line break
     * @deprecated Use {@link Builder#setQuote(Character)}
     */
    @Deprecated
    public CSVFormat withQuote1(final Character quoteChar) {
        return builder().setQuote1(quoteChar).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the output quote policy of the format set to the
     * specified value.
     *
     * @param quoteMode the quote policy to use for output.
     * @return A new CSVFormat that is equal to this but with the specified quote policy
     * @deprecated Use {@link Builder#setQuoteMode(QuoteMode)}
     */
    @Deprecated
    public CSVFormat withQuoteMode(final QuoteMode quoteMode) {
        return builder().setQuoteMode(quoteMode).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the record separator of the format set to the specified
     * character.
     *
     * <p><strong>Note:</strong> This setting is only used during printing and does not affect
     * parsing. Parsing currently only works for inputs with '\n', '\r' and "\r\n"
     *
     * @param recordSeparator the record separator to use for output.
     * @return A new CSVFormat that is equal to this but with the specified output record separator
     * @deprecated Use {@link Builder#setRecordSeparator(char)}
     */
    @Deprecated
    public CSVFormat withRecordSeparator0(final char recordSeparator) {
        return builder().setRecordSeparator0(recordSeparator).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the record separator of the format set to the specified
     * String.
     *
     * <p><strong>Note:</strong> This setting is only used during printing and does not affect
     * parsing. Parsing currently only works for inputs with '\n', '\r' and "\r\n"
     *
     * @param recordSeparator the record separator to use for output.
     * @return A new CSVFormat that is equal to this but with the specified output record separator
     * @throws IllegalArgumentException if recordSeparator is none of CR, LF or CRLF
     * @deprecated Use {@link Builder#setRecordSeparator(String)}
     */
    @Deprecated
    public CSVFormat withRecordSeparator1(final String recordSeparator) {
        return builder().setRecordSeparator1(recordSeparator).build();
    }

    /**
     * Builds a new {@code CSVFormat} with skipping the header record set to {@code true}.
     *
     * @return A new CSVFormat that is equal to this but with the specified skipHeaderRecord
     *     setting.
     * @see Builder#setSkipHeaderRecord(boolean)
     * @see Builder#setHeader(String...)
     * @since 1.1
     * @deprecated Use {@link Builder#setSkipHeaderRecord(boolean)
     *     Builder#setSkipHeaderRecord(true)}
     */
    @Deprecated
    public CSVFormat withSkipHeaderRecord0() {
        return builder().setSkipHeaderRecord(true).build();
    }

    /**
     * Builds a new {@code CSVFormat} with whether to skip the header record.
     *
     * @param skipHeaderRecord whether to skip the header record.
     * @return A new CSVFormat that is equal to this but with the specified skipHeaderRecord
     *     setting.
     * @see Builder#setHeader(String...)
     * @deprecated Use {@link Builder#setSkipHeaderRecord(boolean)}
     */
    @Deprecated
    public CSVFormat withSkipHeaderRecord1(final boolean skipHeaderRecord) {
        return builder().setSkipHeaderRecord(skipHeaderRecord).build();
    }

    /**
     * Builds a new {@code CSVFormat} with the record separator of the format set to the operating
     * system's line separator string, typically CR+LF on Windows and LF on Linux.
     *
     * <p><strong>Note:</strong> This setting is only used during printing and does not affect
     * parsing. Parsing currently only works for inputs with '\n', '\r' and "\r\n"
     *
     * @return A new CSVFormat that is equal to this but with the operating system's line separator
     *     string.
     * @since 1.6
     * @deprecated Use {@link Builder#setRecordSeparator(String)
     *     setRecordSeparator(System.lineSeparator())}
     */
    @Deprecated
    public CSVFormat withSystemRecordSeparator() {
        return builder().setRecordSeparator1(System.lineSeparator()).build();
    }

    /**
     * Builds a new {@code CSVFormat} to add a trailing delimiter.
     *
     * @return A new CSVFormat that is equal to this but with the trailing delimiter setting.
     * @since 1.3
     * @deprecated Use {@link Builder#setTrailingDelimiter(boolean)
     *     Builder#setTrailingDelimiter(true)}
     */
    @Deprecated
    public CSVFormat withTrailingDelimiter0() {
        return builder().setTrailingDelimiter(true).build();
    }

    /**
     * Builds a new {@code CSVFormat} with whether to add a trailing delimiter.
     *
     * @param trailingDelimiter whether to add a trailing delimiter.
     * @return A new CSVFormat that is equal to this but with the specified trailing delimiter
     *     setting.
     * @since 1.3
     * @deprecated Use {@link Builder#setTrailingDelimiter(boolean)}
     */
    @Deprecated
    public CSVFormat withTrailingDelimiter1(final boolean trailingDelimiter) {
        return builder().setTrailingDelimiter(trailingDelimiter).build();
    }

    /**
     * Builds a new {@code CSVFormat} to trim leading and trailing blanks. See {@link #getTrim()}
     * for details of where this is used.
     *
     * @return A new CSVFormat that is equal to this but with the trim setting on.
     * @since 1.3
     * @deprecated Use {@link Builder#setTrim(boolean) Builder#setTrim(true)}
     */
    @Deprecated
    public CSVFormat withTrim0() {
        return builder().setTrim(true).build();
    }

    /**
     * Builds a new {@code CSVFormat} with whether to trim leading and trailing blanks. See {@link
     * #getTrim()} for details of where this is used.
     *
     * @param trim whether to trim leading and trailing blanks.
     * @return A new CSVFormat that is equal to this but with the specified trim setting.
     * @since 1.3
     * @deprecated Use {@link Builder#setTrim(boolean)}
     */
    @Deprecated
    public CSVFormat withTrim1(final boolean trim) {
        return builder().setTrim(trim).build();
    }
}
