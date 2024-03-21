package org.apache.commons.csv;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.csv.ContextInitializer;
import org.apache.commons.csv.ExceptionHandler;
import org.apache.commons.csv.IntegrationUtils;
import java.io.Serializable;
import java.util.stream.Stream;
import java.util.Map;
import java.util.List;
import java.util.Iterator;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.stream.Collectors;

public final class CSVRecord implements Serializable, Iterable<String> {
    private static final long serialVersionUID = 1L;
    private static Value clz = ContextInitializer.getPythonClass("/CSVRecord.py", "CSVRecord");
    private Value obj;

    public CSVRecord(Value obj) {
        this.obj = obj;
    }

    public Value getPythonObject() {
        return obj;
    }

    public String toString() {
        //
        // return "CSVRecord [comment='"
        // + comment
        // + "', recordNumber="
        // + recordNumber
        // + ", values="
        // + Arrays.toString(values)
        // + "]";
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("toString").as(String.class);
    }

    public Iterator<String> iterator() {
        //
        // return toList().iterator();
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("iterator").as(Iterator.class);
    }

    public String[] values() {
        //
        // return values;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("values").as(String[].class);
    }

    public Map<String, String> toMap() {
        //
        // return putIn(new LinkedHashMap<>(values.length));
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("toMap").as(Map.class);
    }

    public List<String> toList() {
        //
        // return stream().collect(Collectors.toList());
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("toList").as(List.class);
    }

    public Stream<String> stream() {
        //
        // return Stream.of(values);
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("stream").as(Stream.class);
    }

    public int size() {
        //
        // return values.length;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("size").as(int.class);
    }

    public <M extends Map<String, String>> M putIn(final M map) {
        //
        // if (getHeaderMapRaw() == null) {
        // return map;
        // }
        // getHeaderMapRaw()
        // .forEach(
        // (key, value) -> {
        // if (value < values.length) {
        // map.put(key, values[value]);
        // }
        // });
        // return map;
        //

        // TODO: Check the type mapping below!
        return (M) obj.invokeMember("putIn", map).as(Map.class);
    }

    public boolean isSet1(final String name) {
        //
        // return isMapped(name) && getHeaderMapRaw().get(name).intValue() <
        // values.length;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("isSet1", name).as(boolean.class);
    }

    public boolean isSet0(final int index) {
        //
        // return 0 <= index && index < values.length;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("isSet0", index).as(boolean.class);
    }

    public boolean isMapped(final String name) {
        //
        // final Map<String, Integer> headerMap = getHeaderMapRaw();
        // return headerMap != null && headerMap.containsKey(name);
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("isMapped", name).as(boolean.class);
    }

    public boolean isConsistent() {
        //
        // final Map<String, Integer> headerMap = getHeaderMapRaw();
        // return headerMap == null || headerMap.size() == values.length;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("isConsistent").as(boolean.class);
    }

    public boolean hasComment() {
        //
        // return comment != null;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("hasComment").as(boolean.class);
    }

    public long getRecordNumber() {
        //
        // return recordNumber;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("getRecordNumber").as(long.class);
    }

    public CSVParser getParser() {
        //
        // return parser;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("getParser").as(CSVParser.class);
    }

    public String getComment() {
        //
        // return comment;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("getComment").as(String.class);
    }

    public long getCharacterPosition() {
        //
        // return characterPosition;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("getCharacterPosition").as(long.class);
    }

    public String get2(final String name) {
        //
        // final Map<String, Integer> headerMap = getHeaderMapRaw();
        // if (headerMap == null) {
        // throw new IllegalStateException(
        // "No header mapping was specified, the record values can't be accessed by
        // name");
        // }
        // final Integer index = headerMap.get(name);
        // if (index == null) {
        // throw new IllegalArgumentException(
        // String.format(
        // "Mapping for %s not found, expected one of %s",
        // name, headerMap.keySet()));
        // }
        // try {
        // return values[index.intValue()];
        // } catch (final ArrayIndexOutOfBoundsException e) {
        // throw new IllegalArgumentException(
        // String.format(
        // "Index for header '%s' is %d but CSVRecord only has %d values!",
        // name, index, Integer.valueOf(values.length)));
        // }
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("get2", name).as(String.class);
    }

    public String get1(final int i) {
        //
        // return values[i];
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("get1", i).as(String.class);
    }

    public String get0(final Enum<?> e) {
        //
        // return get2(e == null ? null : e.name());
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("get0", e).as(String.class);
    }

    private Map<String, Integer> getHeaderMapRaw() {
        //
        // return parser == null ? null : parser.getHeaderMapRaw();
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("getHeaderMapRaw").as(Map.class);
    }

    CSVRecord(
            final CSVParser parser,
            final String[] values,
            final String comment,
            final long recordNumber,
            final long characterPosition) {
        //
        // this.recordNumber = recordNumber;
        // this.values = values != null ? values : Constants.EMPTY_STRING_ARRAY;
        // this.parser = parser;
        // this.comment = comment;
        // this.characterPosition = characterPosition;
        //

        this.obj = clz.invokeMember("__init__", parser, values, comment, recordNumber, characterPosition);
    }
    // (key, value) -> {
    // if (value < values.length) {
    // map.put(key, values[value]);
    // }
    // });
    // private static Value clz = ContextInitializer.getPythonClass("/CSVRecord.py",
    // "new BiConsumer<String,Integer>(...) { ... }");
    // private Value obj;
    // public new BiConsumer<String,Integer>(...) { ... }(Value obj) {
    // this.obj = obj;
    // }
    // public Value getPythonObject() {
    // return obj;
    // }
    // (key, value) -> {
    // if (value < values.length) {
    // map.put(key, values[value]);
    // }
    // });
    // }
}
