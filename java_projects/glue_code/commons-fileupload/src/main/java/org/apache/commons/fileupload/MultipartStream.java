package org.apache.commons.fileupload;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.fileupload.ContextInitializer;
import java.io.IOException;
import java.io.InputStream;
import java.io.ByteArrayOutputStream;
import java.io.UnsupportedEncodingException;
import org.apache.commons.fileupload.FileUploadBase.FileUploadIOException;
import org.apache.commons.fileupload.util.Closeable;
import static java.lang.String.format;

public class MultipartStream {
    protected static final int DEFAULT_BUFSIZE = 4096;
    public static final int HEADER_PART_SIZE_MAX = 10240;
    public static final byte DASH = 0x2D;
    public static final byte LF = 0x0A;
    public static final byte CR = 0x0D;
    protected static final byte[] BOUNDARY_PREFIX = { CR, LF, DASH, DASH };
    protected static final byte[] STREAM_TERMINATOR = { DASH, DASH };
    protected static final byte[] FIELD_SEPARATOR = { CR, LF };
    protected static final byte[] HEADER_SEPARATOR = { CR, LF, CR, LF };
    private static Value clz = ContextInitializer.getPythonClass("MultipartStream.py", "MultipartStream");
    private Value obj;

    public MultipartStream(Value obj) {
        this.obj = obj;
    }

    public Value getPythonObject() {
        return obj;
    }

    public static MultipartStream MultipartStream3(InputStream input, byte[] boundary) {
        //
        // return new MultipartStream(input, boundary, DEFAULT_BUFSIZE, null);
        //

        // TODO: Check the type mapping below!
        return clz.invokeMember("MultipartStream3", input, boundary).as(MultipartStream.class);
    }

    public static MultipartStream MultipartStream1(
            InputStream input, byte[] boundary, int bufSize) {
        //
        // return new MultipartStream(input, boundary, bufSize, null);
        //

        // TODO: Check the type mapping below!
        return clz.invokeMember("MultipartStream1", input, boundary, bufSize).as(MultipartStream.class);
    }

    public static MultipartStream MultipartStream0() {
        //
        // return MultipartStream2(null, null, null);
        //

        // TODO: Check the type mapping below!
        return clz.invokeMember("MultipartStream0").as(MultipartStream.class);
    }

    protected int findSeparator() {
        //
        //
        // int bufferPos = this.head;
        // int tablePos = 0;
        //
        // while (bufferPos < this.tail) {
        // while (tablePos >= 0 && buffer[bufferPos] != boundary[tablePos]) {
        // tablePos = boundaryTable[tablePos];
        // }
        // bufferPos++;
        // tablePos++;
        // if (tablePos == boundaryLength) {
        // return bufferPos - boundaryLength;
        // }
        // }
        // return -1;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("findSeparator").as(int.class);
    }

    protected int findByte(byte value, int pos) {
        //
        // for (int i = pos; i < tail; i++) {
        // if (buffer[i] == value) {
        // return i;
        // }
        // }
        //
        // return -1;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("findByte", value, pos).as(int.class);
    }

    public static boolean arrayequals(byte[] a, byte[] b, int count) {
        //
        // for (int i = 0; i < count; i++) {
        // if (a[i] != b[i]) {
        // return false;
        // }
        // }
        // return true;
        //

        // TODO: Check the type mapping below!
        return clz.invokeMember("arrayequals", a, b, count).as(boolean.class);
    }

    public String readHeaders() throws FileUploadIOException, MalformedStreamException {
        try {
            //
            // int i = 0;
            // byte b;
            // ByteArrayOutputStream baos = new ByteArrayOutputStream();
            // int size = 0;
            // while (i < HEADER_SEPARATOR.length) {
            // try {
            // b = readByte();
            // } catch (FileUploadIOException e) {
            // throw e;
            // } catch (IOException e) {
            // throw new MalformedStreamException("Stream ended unexpectedly");
            // }
            // if (++size > HEADER_PART_SIZE_MAX) {
            // throw new MalformedStreamException(
            // format(
            // "Header section has more than %s bytes (maybe it is not properly"
            // + " terminated)",
            // Integer.valueOf(HEADER_PART_SIZE_MAX)));
            // }
            // if (b == HEADER_SEPARATOR[i]) {
            // i++;
            // } else {
            // i = 0;
            // }
            // baos.write(b);
            // }
            //
            // String headers = null;
            // if (headerEncoding != null) {
            // try {
            // headers = baos.toString(headerEncoding);
            // } catch (UnsupportedEncodingException e) {
            // headers = baos.toString();
            // }
            // } else {
            // headers = baos.toString();
            // }
            //
            // return headers;
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("readHeaders").as(String.class);
        } catch (PolyglotException e) {
            // TODO: Handle FileUploadIOException, MalformedStreamException
            // throw (FileUploadIOException, MalformedStreamException)
            // ExceptionHandler.handle(e, "MultipartStream.readHeaders");
            throw (MalformedStreamException) ExceptionHandler.handle(e, "MultipartStream.readHeaders");
        }
    }

    public void setBoundary(byte[] boundary) throws IllegalBoundaryException {
        try {
            //
            // if (boundary.length != boundaryLength - BOUNDARY_PREFIX.length) {
            // throw new IllegalBoundaryException("The length of a boundary token cannot be
            // changed");
            // }
            // System.arraycopy(boundary, 0, this.boundary, BOUNDARY_PREFIX.length,
            // boundary.length);
            // computeBoundaryTable();
            //

            obj.invokeMember("setBoundary", boundary);
        } catch (PolyglotException e) {
            // TODO: Handle IllegalBoundaryException
            throw (IllegalBoundaryException) ExceptionHandler.handle(e, "MultipartStream.setBoundary");
        }
    }

    public boolean readBoundary() throws FileUploadIOException, MalformedStreamException {
        try {
            //
            // byte[] marker = new byte[2];
            // boolean nextChunk = false;
            //
            // head += boundaryLength;
            // try {
            // marker[0] = readByte();
            // if (marker[0] == LF) {
            // return true;
            // }
            //
            // marker[1] = readByte();
            // if (arrayequals(marker, STREAM_TERMINATOR, 2)) {
            // nextChunk = false;
            // } else if (arrayequals(marker, FIELD_SEPARATOR, 2)) {
            // nextChunk = true;
            // } else {
            // throw new MalformedStreamException("Unexpected characters follow a
            // boundary");
            // }
            // } catch (FileUploadIOException e) {
            // throw e;
            // } catch (IOException e) {
            // throw new MalformedStreamException("Stream ended unexpectedly");
            // }
            // return nextChunk;
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("readBoundary").as(boolean.class);
        } catch (PolyglotException e) {
            // TODO: Handle FileUploadIOException, MalformedStreamException
            // throw (FileUploadIOException, MalformedStreamException)
            // ExceptionHandler.handle(e, "MultipartStream.readBoundary");
            throw (MalformedStreamException) ExceptionHandler.handle(e, "MultipartStream.readBoundary");
        }
    }

    public byte readByte() throws IOException {
        try {
            //
            // if (head == tail) {
            // head = 0;
            // tail = input.read(buffer, head, bufSize);
            // if (tail == -1) {
            // throw new IOException("No more data is available");
            // }
            // if (notifier != null) {
            // notifier.noteBytesRead(tail);
            // }
            // }
            // return buffer[head++];
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("readByte").as(byte.class);
        } catch (PolyglotException e) {
            // TODO: Handle IOException
            throw (IOException) ExceptionHandler.handle(e, "MultipartStream.readByte");
        }
    }

    public void setHeaderEncoding(String encoding) {
        //
        // headerEncoding = encoding;
        //

        obj.invokeMember("setHeaderEncoding", encoding);
    }

    public String getHeaderEncoding() {
        //
        // return headerEncoding;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("getHeaderEncoding").as(String.class);
    }

    public static MultipartStream MultipartStream2(
            InputStream input, byte[] boundary, ProgressNotifier pNotifier) {
        //
        // return new MultipartStream(input, boundary, DEFAULT_BUFSIZE, pNotifier);
        //

        // TODO: Check the type mapping below!
        return clz.invokeMember("MultipartStream2", input, boundary, pNotifier).as(MultipartStream.class);
    }

    public MultipartStream(
            InputStream input, byte[] boundary, int bufSize, ProgressNotifier pNotifier) {
        //
        //
        // if (boundary == null) {
        // throw new IllegalArgumentException("boundary may not be null");
        // }
        // this.boundaryLength = boundary.length + BOUNDARY_PREFIX.length;
        // if (bufSize < this.boundaryLength + 1) {
        // throw new IllegalArgumentException(
        // "The buffer size specified for the MultipartStream is too small");
        // }
        //
        // this.input = input;
        // this.bufSize = Math.max(bufSize, boundaryLength * 2);
        // this.buffer = new byte[this.bufSize];
        // this.notifier = pNotifier;
        //
        // this.boundary = new byte[this.boundaryLength];
        // this.boundaryTable = new int[this.boundaryLength + 1];
        // this.keepRegion = this.boundary.length;
        //
        // System.arraycopy(BOUNDARY_PREFIX, 0, this.boundary, 0,
        // BOUNDARY_PREFIX.length);
        // System.arraycopy(boundary, 0, this.boundary, BOUNDARY_PREFIX.length,
        // boundary.length);
        // computeBoundaryTable();
        //
        // head = 0;
        // tail = 0;
        //

        this.obj = clz.invokeMember("__init__", input, boundary, bufSize, pNotifier);
    }

    private void computeBoundaryTable() {
        //
        // int position = 2;
        // int candidate = 0;
        //
        // boundaryTable[0] = -1;
        // boundaryTable[1] = 0;
        //
        // while (position <= boundaryLength) {
        // if (boundary[position - 1] == boundary[candidate]) {
        // boundaryTable[position] = candidate + 1;
        // candidate++;
        // position++;
        // } else if (candidate > 0) {
        // candidate = boundaryTable[candidate];
        // } else {
        // boundaryTable[position] = 0;
        // position++;
        // }
        // }
        //

        obj.invokeMember("computeBoundaryTable");
    }

    ItemInputStream newInputStream() {
        //
        // return new ItemInputStream();
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("newInputStream").as(ItemInputStream.class);
    }

    public class ItemInputStream extends InputStream implements Closeable {
        private static final int BYTE_POSITIVE_OFFSET = 256;
        private Value clz = ContextInitializer.getPythonClass("MultipartStream.py", "MultipartStream.ItemInputStream");
        private Value obj;

        public ItemInputStream(Value obj) {
            this.obj = obj;
        }

        public Value getPythonObject() {
            return obj;
        }

        public boolean isClosed() {
            //
            // return closed;
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("isClosed").as(boolean.class);
        }

        public long skip(long bytes) throws IOException {
            try {
                //
                // if (closed) {
                // throw new FileItemStream.ItemSkippedException();
                // }
                // int av = available();
                // if (av == 0) {
                // av = makeAvailable();
                // if (av == 0) {
                // return 0;
                // }
                // }
                // long res = Math.min(av, bytes);
                // head += res;
                // return res;
                //

                // TODO: Check the type mapping below!
                return obj.invokeMember("skip", bytes).as(long.class);
            } catch (PolyglotException e) {
                // TODO: Handle IOException
                throw (IOException) ExceptionHandler.handle(e, "ItemInputStream.skip");
            }
        }

        public int read() throws IOException {
            try {
                //
                // return read0();
                //

                // TODO: Check the type mapping below!
                return obj.invokeMember("read").as(int.class);
            } catch (PolyglotException e) {
                // TODO: Handle IOException
                throw (IOException) ExceptionHandler.handle(e, "ItemInputStream.read");
            }
        }

        public int available() throws IOException {
            try {
                //
                // if (pos == -1) {
                // return tail - head - pad;
                // }
                // return pos - head;
                //

                // TODO: Check the type mapping below!
                return obj.invokeMember("available").as(int.class);
            } catch (PolyglotException e) {
                // TODO: Handle IOException
                throw (IOException) ExceptionHandler.handle(e, "ItemInputStream.available");
            }
        }

        public void close1(boolean pCloseUnderlying) throws IOException {
            try {
                //
                // if (closed) {
                // return;
                // }
                // if (pCloseUnderlying) {
                // closed = true;
                // input.close();
                // } else {
                // for (; ; ) {
                // int av = available();
                // if (av == 0) {
                // av = makeAvailable();
                // if (av == 0) {
                // break;
                // }
                // }
                // skip(av);
                // }
                // }
                // closed = true;
                //

                obj.invokeMember("close1", pCloseUnderlying);
            } catch (PolyglotException e) {
                // TODO: Handle IOException
                throw (IOException) ExceptionHandler.handle(e, "ItemInputStream.close1");
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
                throw (IOException) ExceptionHandler.handle(e, "ItemInputStream.close0");
            }
        }

        public int read1(byte[] b, int off, int len) throws IOException {
            try {
                //
                // if (closed) {
                // throw new FileItemStream.ItemSkippedException();
                // }
                // if (len == 0) {
                // return 0;
                // }
                // int res = available();
                // if (res == 0) {
                // res = makeAvailable();
                // if (res == 0) {
                // return -1;
                // }
                // }
                // res = Math.min(res, len);
                // System.arraycopy(buffer, head, b, off, res);
                // head += res;
                // total += res;
                // return res;
                //

                // TODO: Check the type mapping below!
                return obj.invokeMember("read1", b, off, len).as(int.class);
            } catch (PolyglotException e) {
                // TODO: Handle IOException
                throw (IOException) ExceptionHandler.handle(e, "ItemInputStream.read1");
            }
        }

        public int read0() throws IOException {
            try {
                //
                // if (closed) {
                // throw new FileItemStream.ItemSkippedException();
                // }
                // if (available() == 0 && makeAvailable() == 0) {
                // return -1;
                // }
                // ++total;
                // int b = buffer[head++];
                // if (b >= 0) {
                // return b;
                // }
                // return b + BYTE_POSITIVE_OFFSET;
                //

                // TODO: Check the type mapping below!
                return obj.invokeMember("read0").as(int.class);
            } catch (PolyglotException e) {
                // TODO: Handle IOException
                throw (IOException) ExceptionHandler.handle(e, "ItemInputStream.read0");
            }
        }

        public long getBytesRead() {
            //
            // return total;
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("getBytesRead").as(long.class);
        }

        private int makeAvailable() throws IOException {
            try {
                //
                // if (pos != -1) {
                // return 0;
                // }
                //
                // total += tail - head - pad;
                // System.arraycopy(buffer, tail - pad, buffer, 0, pad);
                //
                // head = 0;
                // tail = pad;
                //
                // for (; ; ) {
                // int bytesRead = input.read(buffer, tail, bufSize - tail);
                // if (bytesRead == -1) {
                // final String msg = "Stream ended unexpectedly";
                // throw new MalformedStreamException(msg);
                // }
                // if (notifier != null) {
                // notifier.noteBytesRead(bytesRead);
                // }
                // tail += bytesRead;
                //
                // findSeparator();
                // int av = available();
                //
                // if (av > 0 || pos != -1) {
                // return av;
                // }
                // }
                //

                // TODO: Check the type mapping below!
                return obj.invokeMember("makeAvailable").as(int.class);
            } catch (PolyglotException e) {
                // TODO: Handle IOException
                throw (IOException) ExceptionHandler.handle(e, "ItemInputStream.makeAvailable");
            }
        }

        private void findSeparator() {
            //
            // pos = MultipartStream.this.findSeparator();
            // if (pos == -1) {
            // if (tail - head > keepRegion) {
            // pad = keepRegion;
            // } else {
            // pad = tail - head;
            // }
            // }
            //

            obj.invokeMember("findSeparator");
        }

        ItemInputStream() {
            //
            // findSeparator();
            //

            this.obj = clz.invokeMember("__init__");
        }
    }

    public static class IllegalBoundaryException extends IOException {
        private static final long serialVersionUID = -161533165102632918L;
        private static Value clz = ContextInitializer.getPythonClass("MultipartStream.py", "IllegalBoundaryException");
        private Value obj;

        public IllegalBoundaryException(Value obj) {
            this.obj = obj;
        }

        public Value getPythonObject() {
            return obj;
        }

        public IllegalBoundaryException(String message) {
            //
            // super(message);
            //

            this.obj = clz.invokeMember("__init__", message);
        }
    }

    public static class MalformedStreamException extends IOException {
        private static final long serialVersionUID = 6466926458059796677L;
        private static Value clz = ContextInitializer.getPythonClass("MultipartStream.py", "MalformedStreamException");
        private Value obj;

        public MalformedStreamException(Value obj) {
            this.obj = obj;
        }

        public Value getPythonObject() {
            return obj;
        }

        public MalformedStreamException(String message) {
            //
            // super(message);
            //

            this.obj = clz.invokeMember("__init__", message);
        }
    }

    public static class ProgressNotifier {
        private static Value clz = ContextInitializer.getPythonClass("MultipartStream.py", "ProgressNotifier");
        private Value obj;

        public ProgressNotifier(Value obj) {
            this.obj = obj;
        }

        public Value getPythonObject() {
            return obj;
        }

        private void notifyListener() {
            //
            // if (listener != null) {
            // listener.update(bytesRead, contentLength, items);
            // }
            //

            obj.invokeMember("notifyListener");
        }

        void noteItem() {
            //
            // ++items;
            // notifyListener();
            //

            obj.invokeMember("noteItem");
        }

        void noteBytesRead(int pBytes) {
            //
            // /* Indicates, that the given number of bytes have been read from
            // * the input stream.
            // */
            // bytesRead += pBytes;
            // notifyListener();
            //

            obj.invokeMember("noteBytesRead", pBytes);
        }

        ProgressNotifier(ProgressListener pListener, long pContentLength) {
            //
            // listener = pListener;
            // contentLength = pContentLength;
            //

            this.obj = clz.invokeMember("__init__", pListener, pContentLength);
        }
    }
}
