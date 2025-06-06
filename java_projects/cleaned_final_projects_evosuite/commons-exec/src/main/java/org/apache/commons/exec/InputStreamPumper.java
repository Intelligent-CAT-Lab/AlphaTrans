
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

import java.io.InputStream;
import java.io.OutputStream;

import org.apache.commons.exec.util.DebugUtils;

/**
 * Copies all data from an System.input stream to an output stream of the executed process.
 */
public class InputStreamPumper implements Runnable {

    /**
     * Sleep time in milliseconds.
     */
    public static final int SLEEPING_TIME = 100;

    /** The input stream to pump from. */
    private final InputStream is;

    /** The output stream to pmp into. */
    private final OutputStream os;

    /** Flag to stop the stream pumping. */
    private volatile boolean stop;

    /**
     * Create a new stream pumper.
     *
     * @param is input stream to read data from.
     * @param os output stream to write data to.
     */
    public InputStreamPumper(final InputStream is, final OutputStream os) {
        this.is = is;
        this.os = os;
        this.stop = false;
    }

    /**
     * Copies data from the input stream to the output stream. Terminates as soon as the input stream is closed or an error occurs.
     */
    @Override
    public void run() {
        try {
            while (!stop) {
                while (is.available() > 0 && !stop) {
                    os.write(is.read());
                }
                os.flush();
                Thread.sleep(SLEEPING_TIME);
            }
        } catch (final Exception e) {
            final String msg = "Got exception while reading/writing the stream";
            DebugUtils.handleException(msg, e);
        }
    }

    /**
     * Requests processing to stop.
     */
    public void stopProcessing() {
        stop = true;
    }

}
