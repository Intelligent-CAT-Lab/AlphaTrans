package org.apache.commons.csv;

import java.io.Closeable;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class CSVParser implements Iterable<CSVRecord>, Closeable {
  private final Token reusableToken = new Token();
  private final List<String> recordList = new ArrayList<>();
  private static Value clz = ContextInitializer.getPythonClass("/CSVParser.py", "CSVParser");
  private Value obj;

  public CSVParser(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Iterator<CSVRecord> iterator() {
    //
    // return csvRecordIterator;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("iterator").as(Iterator.class);
  }

  public void close() throws IOException {
    try {
      //
      // if (this.lexer != null) {
      // this.lexer.close();
      // }
      //

      obj.invokeMember("close");
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "CSVParser.close");
    }
  }

  public static CSVParser parse5(final URL url, final Charset charset, final CSVFormat format)
      throws IOException {
    try {
      //
      // Objects.requireNonNull(url, "url");
      // Objects.requireNonNull(charset, "charset");
      // Objects.requireNonNull(format, "format");
      //
      // return CSVParser.CSVParser1(new InputStreamReader(url.openStream(), charset),
      // format);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("parse5", url, charset, format).as(CSVParser.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "CSVParser.parse5");
    }
  }

  public static CSVParser parse2(final Path path, final Charset charset, final CSVFormat format)
      throws IOException {
    try {
      //
      // Objects.requireNonNull(path, "path");
      // Objects.requireNonNull(format, "format");
      // return parse1(Files.newInputStream(path), charset, format);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("parse2", path, charset, format).as(CSVParser.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "CSVParser.parse2");
    }
  }

  public static CSVParser parse1(
      final InputStream inputStream, final Charset charset, final CSVFormat format)
      throws IOException {
    try {
      //
      // Objects.requireNonNull(inputStream, "inputStream");
      // Objects.requireNonNull(format, "format");
      // return parse3(new InputStreamReader(inputStream, charset), format);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("parse1", inputStream, charset, format).as(CSVParser.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "CSVParser.parse1");
    }
  }

  private void addRecordValue(final boolean lastRecord) {
    //
    // final String input =
    // this.format.trim1(this.reusableToken.content.toString());
    // if (lastRecord && input.isEmpty() && this.format.getTrailingDelimiter()) {
    // return;
    // }
    // this.recordList.add(handleNull(input));
    //

    obj.invokeMember("addRecordValue", lastRecord);
  }

  public Stream<CSVRecord> stream() {
    //
    // return StreamSupport.stream(
    // Spliterators.spliteratorUnknownSize(iterator(), Spliterator.ORDERED), false);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("stream").as(Stream.class);
  }

  public boolean isClosed() {
    //
    // return this.lexer.isClosed();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isClosed").as(boolean.class);
  }

  public boolean hasTrailerComment() {
    //
    // return trailerComment != null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasTrailerComment").as(boolean.class);
  }

  public boolean hasHeaderComment() {
    //
    // return headerComment != null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasHeaderComment").as(boolean.class);
  }

  public String getTrailerComment() {
    //
    // return trailerComment;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getTrailerComment").as(String.class);
  }

  public List<CSVRecord> getRecords() {
    //
    // return stream().collect(Collectors.toList());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRecords").as(List.class);
  }

  public long getRecordNumber() {
    //
    // return this.recordNumber;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRecordNumber").as(long.class);
  }

  public List<String> getHeaderNames() {
    //
    // return Collections.unmodifiableList(headers.headerNames);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeaderNames").as(List.class);
  }

  public Map<String, Integer> getHeaderMap() {
    //
    // if (this.headers.headerMap == null) {
    // return null;
    // }
    // final Map<String, Integer> map = createEmptyHeaderMap();
    // map.putAll(this.headers.headerMap);
    // return map;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeaderMap").as(Map.class);
  }

  public String getHeaderComment() {
    //
    // return headerComment;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeaderComment").as(String.class);
  }

  public String getFirstEndOfLine() {
    //
    // return lexer.getFirstEol();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFirstEndOfLine").as(String.class);
  }

  public long getCurrentLineNumber() {
    //
    // return this.lexer.getCurrentLineNumber();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCurrentLineNumber").as(long.class);
  }

  public static CSVParser CSVParser1(final Reader reader, final CSVFormat format)
      throws IOException {
    try {
      //
      // return new CSVParser(reader, format, 0, 1);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("CSVParser1", reader, format).as(CSVParser.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "CSVParser.CSVParser1");
    }
  }

  public CSVParser(
      final Reader reader,
      final CSVFormat format,
      final long characterOffset,
      final long recordNumber)
      throws IOException {
    try {
      //
      // Objects.requireNonNull(reader, "reader");
      // Objects.requireNonNull(format, "format");
      //
      // this.format = format.copy();
      // this.lexer = new Lexer(format, new ExtendedBufferedReader(reader));
      // this.csvRecordIterator = new CSVRecordIterator();
      // this.headers = createHeaders();
      // this.characterOffset = characterOffset;
      // this.recordNumber = recordNumber - 1;
      //

      this.obj = clz.invokeMember("__init__", reader, format, characterOffset, recordNumber);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "CSVParser.__init__");
    }
  }

  public static CSVParser parse4(final String string, final CSVFormat format) throws IOException {
    try {
      //
      // Objects.requireNonNull(string, "string");
      // Objects.requireNonNull(format, "format");
      //
      // return CSVParser.CSVParser1(new StringReader(string), format);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("parse4", string, format).as(CSVParser.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "CSVParser.parse4");
    }
  }

  public static CSVParser parse3(final Reader reader, final CSVFormat format) throws IOException {
    try {
      //
      // return CSVParser.CSVParser1(reader, format);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("parse3", reader, format).as(CSVParser.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "CSVParser.parse3");
    }
  }

  public static CSVParser parse0(final File file, final Charset charset, final CSVFormat format)
      throws IOException {
    try {
      //
      // Objects.requireNonNull(file, "file");
      // return parse2(file.toPath(), charset, format);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("parse0", file, charset, format).as(CSVParser.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "CSVParser.parse0");
    }
  }

  private boolean isStrictQuoteMode() {
    //
    // return this.format.getQuoteMode() == QuoteMode.ALL_NON_NULL
    // || this.format.getQuoteMode() == QuoteMode.NON_NUMERIC;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isStrictQuoteMode").as(boolean.class);
  }

  private String handleNull(final String input) {
    //
    // final boolean isQuoted = this.reusableToken.isQuoted;
    // final String nullString = format.getNullString();
    // final boolean strictQuoteMode = isStrictQuoteMode();
    // if (input.equals(nullString)) {
    // return strictQuoteMode && isQuoted ? input : null;
    // }
    // return strictQuoteMode && nullString == null && input.isEmpty() && !isQuoted
    // ? null : input;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleNull", input).as(String.class);
  }

  private Headers createHeaders() throws IOException {
    try {
      //
      // Map<String, Integer> hdrMap = null;
      // List<String> headerNames = null;
      // final String[] formatHeader = this.format.getHeader();
      // if (formatHeader != null) {
      // hdrMap = createEmptyHeaderMap();
      // String[] headerRecord = null;
      // if (formatHeader.length == 0) {
      // final CSVRecord nextRecord = this.nextRecord();
      // if (nextRecord != null) {
      // headerRecord = nextRecord.values();
      // headerComment = nextRecord.getComment();
      // }
      // } else {
      // if (this.format.getSkipHeaderRecord()) {
      // final CSVRecord nextRecord = this.nextRecord();
      // if (nextRecord != null) {
      // headerComment = nextRecord.getComment();
      // }
      // }
      // headerRecord = formatHeader;
      // }
      //
      // if (headerRecord != null) {
      // boolean observedMissing = false;
      // for (int i = 0; i < headerRecord.length; i++) {
      // final String header = headerRecord[i];
      // final boolean blankHeader = CSVFormat.isBlank(header);
      // if (blankHeader && !this.format.getAllowMissingColumnNames()) {
      // throw new IllegalArgumentException(
      // "A header name is missing in " + Arrays.toString(headerRecord));
      // }
      //
      // final boolean containsHeader =
      // blankHeader ? observedMissing : hdrMap.containsKey(header);
      // final DuplicateHeaderMode headerMode = this.format.getDuplicateHeaderMode();
      // final boolean duplicatesAllowed = headerMode ==
      // DuplicateHeaderMode.ALLOW_ALL;
      // final boolean emptyDuplicatesAllowed =
      // headerMode == DuplicateHeaderMode.ALLOW_EMPTY;
      //
      // if (containsHeader
      // && !duplicatesAllowed
      // && !(blankHeader && emptyDuplicatesAllowed)) {
      // throw new IllegalArgumentException(
      // String.format(
      // "The header contains a duplicate name: \"%s\" in %s. If"
      // + " this is valid then use"
      // + " CSVFormat.Builder.setDuplicateHeaderMode().",
      // header, Arrays.toString(headerRecord)));
      // }
      // observedMissing |= blankHeader;
      // if (header != null) {
      // hdrMap.put(header, Integer.valueOf(i));
      // if (headerNames == null) {
      // headerNames = new ArrayList<>(headerRecord.length);
      // }
      // headerNames.add(header);
      // }
      // }
      // }
      // }
      // if (headerNames == null) {
      // headerNames = Collections.emptyList(); // immutable
      // } else {
      // headerNames = Collections.unmodifiableList(headerNames);
      // }
      // return new Headers(hdrMap, headerNames);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("createHeaders").as(Headers.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "CSVParser.createHeaders");
    }
  }

  private Map<String, Integer> createEmptyHeaderMap() {
    //
    // return this.format.getIgnoreHeaderCase()
    // ? new TreeMap<>(String.CASE_INSENSITIVE_ORDER)
    // : new LinkedHashMap<>();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("createEmptyHeaderMap").as(Map.class);
  }

  CSVRecord nextRecord() throws IOException {
    try {
      //
      // CSVRecord result = null;
      // this.recordList.clear();
      // StringBuilder sb = null;
      // final long startCharPosition = lexer.getCharacterPosition() +
      // this.characterOffset;
      // do {
      // this.reusableToken.reset();
      // this.lexer.nextToken(this.reusableToken);
      // switch (this.reusableToken.type) {
      // case TOKEN:
      // this.addRecordValue(false);
      // break;
      // case EORECORD:
      // this.addRecordValue(true);
      // break;
      // case EOF:
      // if (this.reusableToken.isReady) {
      // this.addRecordValue(true);
      // } else if (sb != null) {
      // trailerComment = sb.toString();
      // }
      // break;
      // case INVALID:
      // throw new IOException(
      // "(line " + this.getCurrentLineNumber() + ") invalid parse sequence");
      // case COMMENT: // Ignored currently
      // if (sb == null) { // first comment for this record
      // sb = new StringBuilder();
      // } else {
      // sb.append(Constants.LF);
      // }
      // sb.append(this.reusableToken.content);
      // this.reusableToken.type = TOKEN; // Read another token
      // break;
      // default:
      // throw new IllegalStateException(
      // "Unexpected Token type: " + this.reusableToken.type);
      // }
      // } while (this.reusableToken.type == TOKEN);
      //
      // if (!this.recordList.isEmpty()) {
      // this.recordNumber++;
      // final String comment = sb == null ? null : sb.toString();
      // result =
      // new CSVRecord(
      // this,
      // this.recordList.toArray(Constants.EMPTY_STRING_ARRAY),
      // comment,
      // this.recordNumber,
      // startCharPosition);
      // }
      // return result;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("nextRecord").as(CSVRecord.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "CSVParser.nextRecord");
    }
  }

  Map<String, Integer> getHeaderMapRaw() {
    //
    // return this.headers.headerMap;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeaderMapRaw").as(Map.class);
  }

  class CSVRecordIterator implements Iterator<CSVRecord> {
    private Value clz = ContextInitializer.getPythonClass("/CSVParser.py", "CSVRecordIterator");
    private Value obj;

    public CSVRecordIterator(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public void remove() {
      //
      // throw new UnsupportedOperationException();
      //

      obj.invokeMember("remove");
    }

    public CSVRecord next() {
      //
      // if (CSVParser.this.isClosed()) {
      // throw new NoSuchElementException("CSVParser has been closed");
      // }
      // CSVRecord next = this.current;
      // this.current = null;
      //
      // if (next == null) {
      // next = this.getNextRecord();
      // if (next == null) {
      // throw new NoSuchElementException("No more CSV records available");
      // }
      // }
      //
      // return next;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("next").as(CSVRecord.class);
    }

    public boolean hasNext() {
      //
      // if (CSVParser.this.isClosed()) {
      // return false;
      // }
      // if (this.current == null) {
      // this.current = this.getNextRecord();
      // }
      //
      // return this.current != null;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("hasNext").as(boolean.class);
    }

    private CSVRecord getNextRecord() {
      //
      // try {
      // return CSVParser.this.nextRecord();
      // } catch (final IOException e) {
      // throw new UncheckedIOException(
      // e.getClass().getSimpleName() + " reading next record: " + e.toString(), e);
      // }
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getNextRecord").as(CSVRecord.class);
    }
  }

  private static final class Headers {
    private static Value clz = ContextInitializer.getPythonClass("/CSVParser.py", "Headers");
    private Value obj;

    public Headers(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    Headers(final Map<String, Integer> headerMap, final List<String> headerNames) {
      //
      // this.headerMap = headerMap;
      // this.headerNames = headerNames;
      //

      this.obj = clz.invokeMember("__init__", headerMap, headerNames);
    }
  }
}
