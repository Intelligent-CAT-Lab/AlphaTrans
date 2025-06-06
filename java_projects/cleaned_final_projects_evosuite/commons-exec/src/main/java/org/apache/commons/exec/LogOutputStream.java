
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */


package org.apache.commons.exec;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.charset.Charset;

/**
 * Base class to connect a logging system to the output and/or error stream of then external process. The implementation parses the incoming data to construct a
 * line and passes the complete line to an user-defined implementation.
 */
public abstract class LogOutputStream extends OutputStream {

    private static final class ByteArrayOutputStreamX extends ByteArrayOutputStream {
        private ByteArrayOutputStreamX(final int size) {
            super(size);
        }

        public synchronized String toString(final Charset charset) {
            return new String(buf, 0, count, charset);
        }
    }

    /** Initial buffer size. */
    private static final int INTIAL_SIZE = 132;

    /** Carriage return. */
    private static final int CR = 0x0d;

    /** Line-feed. */
    private static final int LF = 0x0a;

    /** The internal buffer. */
    private final ByteArrayOutputStreamX buffer = new ByteArrayOutputStreamX(INTIAL_SIZE);

    private boolean skip;

    private final int level;

    private final Charset charset;

    /**
     * Creates a new instance of this class. Uses the default level of 999.
     */
    // public LogOutputStream() {
    //     this(999);
    // }

    /**
     * Creates a new instance of this class.
     *
     * @param level level used to log data written to this stream.
     */
    // public LogOutputStream(final int level) {
    //     this(level, null);
    // }

    /**
     * Creates a new instance of this class, specifying the character set that should be used for outputting the string for each line
     *
     * @param level   level used to log data written to this stream.
     * @param charset Character Set to use when processing lines.
     */
    public LogOutputStream(int constructorId, final int level, final Charset charset) {
        if (constructorId == 0) {
            this.level = 999;
            this.charset = null;
        } else if (constructorId == 1) {
            this.level = level;
            this.charset = null;
        } else {
            this.level = level;
            this.charset = charset == null ? Charset.defaultCharset() : charset;    
        }
    }

    /**
     * Writes all remaining data from the buffer.
     *
     * @see OutputStream#close()
     */
    @Override
    public void close() throws IOException {
        if (buffer.size() > 0) {
            processBuffer();
        }
        super.close();
    }

    /**
     * Flushes this log stream.
     *
     * @see OutputStream#flush()
     */
    @Override
    public void flush() {
        if (buffer.size() > 0) {
            processBuffer();
        }
    }

    /**
     * Gets the trace level of the log system.
     *
     * @return the trace level of the log system.
     */
    public int getMessageLevel() {
        return level;
    }

    /**
     * Converts the buffer to a string and sends it to {@code processLine}.
     */
    protected void processBuffer() {
        processLine0(buffer.toString(charset));
        buffer.reset();
    }

    /**
     * Logs a line to the log system of the user.
     *
     * @param line the line to log.
     */
    protected void processLine0(final String line) {
        processLine1(line, level);
    }

    /**
     * Logs a line to the log system of the user.
     *
     * @param line     the line to log.
     * @param logLevel the log level to use
     */
    protected abstract void processLine1(final String line, final int logLevel);

    /**
     * Writes a block of characters to the output stream.
     *
     * @param b   the array containing the data.
     * @param off the offset into the array where data starts.
     * @param len the length of block.
     * @throws IOException if the data cannot be written into the stream.
     * @see OutputStream#write(byte[], int, int)
     */
    //@Override
    public void write0(final byte[] b, final int off, final int len) throws IOException {
        // find the line breaks and pass other chars through in blocks
        int offset = off;
        int blockStartOffset = offset;
        int remaining = len;
        while (remaining > 0) {
            while (remaining > 0 && b[offset] != LF && b[offset] != CR) {
                offset++;
                remaining--;
            }
            // either end of buffer or a line separator char
            final int blockLength = offset - blockStartOffset;
            if (blockLength > 0) {
                buffer.write(b, blockStartOffset, blockLength);
            }
            while (remaining > 0 && (b[offset] == LF || b[offset] == CR)) {
                write1(b[offset]);
                offset++;
                remaining--;
            }
            blockStartOffset = offset;
        }
    }

    /**
     * Writes the data to the buffer and flush the buffer, if a line separator is detected.
     *
     * @param cc data to log (byte).
     * @see OutputStream#write(int)
     */
    //@Override
    public void write1(final int cc) throws IOException {
        final byte c = (byte) cc;
        if (c == '\n' || c == '\r') {
            if (!skip) {
                processBuffer();
            }
        } else {
            buffer.write(cc);
        }
        skip = c == '\r';
    }
}
