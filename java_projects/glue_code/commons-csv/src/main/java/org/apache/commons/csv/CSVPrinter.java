package org.apache.commons.csv;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.csv.ContextInitializer;
import org.apache.commons.csv.ExceptionHandler;
import org.apache.commons.csv.IntegrationUtils;
import java.io.IOException;
import java.util.stream.Stream;
import java.io.Closeable;
import java.io.Flushable;
import java.util.Arrays;
import java.util.Objects;
import static org.apache.commons.csv.Constants.CR;
import static org.apache.commons.csv.Constants.LF;
import static org.apache.commons.csv.Constants.SP;
public final class CSVPrinter implements Flushable, Closeable {
    private boolean newRecord = true;
    private static Value clz = ContextInitializer.getPythonClass("/CSVPrinter.py", "CSVPrinter");
    private Value obj;
    public CSVPrinter(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public void flush() throws IOException {
try {
// 
// if (appendable instanceof Flushable) {
// ((Flushable) appendable).flush();
// }
// 

obj.invokeMember("flush");
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.flush");
}
}
    public void close() throws IOException {
try {
// 
// close1(true);
// 

obj.invokeMember("close");
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.close");
}
}
    public void printRecords1(final Object... values) throws IOException {
try {
// 
// printRecords0(Arrays.asList(values));
// 

obj.invokeMember("printRecords1", values);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.printRecords1");
}
}
    public void printRecords0(final Iterable<?> values) throws IOException {
try {
// 
// for (final Object value : values) {
// printRecordObject(value);
// }
// 

obj.invokeMember("printRecords0", values);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.printRecords0");
}
}
    public synchronized void printRecord2(final Stream<?> values) throws IOException {
try {
// 
// values.forEachOrdered(
// t -> {
// try {
// print(t);
// } catch (final IOException e) {
// throw IOUtils.rethrow(e);
// }
// });
// println();
// 

obj.invokeMember("printRecord2", values);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.printRecord2");
}
}
    public void printRecord1(final Object... values) throws IOException {
try {
// 
// printRecord0(Arrays.asList(values));
// 

obj.invokeMember("printRecord1", values);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.printRecord1");
}
}
    public synchronized void printRecord0(final Iterable<?> values) throws IOException {
try {
// 
// for (final Object value : values) {
// print(value);
// }
// println();
// 

obj.invokeMember("printRecord0", values);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.printRecord0");
}
}
    public synchronized void println() throws IOException {
try {
// 
// format.println(appendable);
// newRecord = true;
// 

obj.invokeMember("println");
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.println");
}
}
    public synchronized void printComment(final String comment) throws IOException {
try {
// 
// if (comment == null || !format.isCommentMarkerSet()) {
// return;
// }
// if (!newRecord) {
// println();
// }
// appendable.append(format.getCommentMarker().charValue());
// appendable.append(SP);
// for (int i = 0; i < comment.length(); i++) {
// final char c = comment.charAt(i);
// switch (c) {
// case CR:
// if (i + 1 < comment.length() && comment.charAt(i + 1) == LF) {
// i++;
// }
// case LF:
// println();
// appendable.append(format.getCommentMarker().charValue());
// appendable.append(SP);
// break;
// default:
// appendable.append(c);
// break;
// }
// }
// println();
// 

obj.invokeMember("printComment", comment);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.printComment");
}
}
    public synchronized void print(final Object value) throws IOException {
try {
// 
// format.print2(value, appendable, newRecord);
// newRecord = false;
// 

obj.invokeMember("print", value);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.print");
}
}
    public Appendable getOut() {
// 
// return this.appendable;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getOut").as(Appendable.class);
}
    public void close1(final boolean flush) throws IOException {
try {
// 
// if (flush || format.getAutoFlush()) {
// flush();
// }
// if (appendable instanceof Closeable) {
// ((Closeable) appendable).close();
// }
// 

obj.invokeMember("close1", flush);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.close1");
}
}
    public void close0() throws IOException {
try {
// 
// close1(false);
// 

obj.invokeMember("close0");
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.close0");
}
}
    public CSVPrinter(final Appendable appendable, final CSVFormat format) throws IOException {
try {
// 
// Objects.requireNonNull(appendable, "appendable");
// Objects.requireNonNull(format, "format");
// 
// this.appendable = appendable;
// this.format = format.copy();
// final String[] headerComments = format.getHeaderComments();
// if (headerComments != null) {
// for (final String line : headerComments) {
// this.printComment(line);
// }
// }
// if (format.getHeader() != null && !format.getSkipHeaderRecord()) {
// this.printRecord1((Object[]) format.getHeader());
// }
// 

this.obj = clz.invokeMember("__init__", appendable, format);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.__init__");
}
}
    private void printRecordObject(final Object value) throws IOException {
try {
// 
// if (value instanceof Object[]) {
// this.printRecord1((Object[]) value);
// } else if (value instanceof Iterable) {
// this.printRecord0((Iterable<?>) value);
// } else {
// this.printRecord1(value);
// }
// 

obj.invokeMember("printRecordObject", value);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "CSVPrinter.printRecordObject");
}
}
                t -> {
                    try {
                        print(t);
                    } catch (final IOException e) {
                        throw IOUtils.rethrow(e);
                    }
                });
    private static Value clz = ContextInitializer.getPythonClass("/CSVPrinter.py", "new Consumer<?>(...) { ... }");
    private Value obj;
    public new Consumer<?>(...) { ... }(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
                t -> {
                    try {
                        print(t);
                    } catch (final IOException e) {
                        throw IOUtils.rethrow(e);
                    }
                });
}
}
