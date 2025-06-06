package org.apache.commons.graph.utils;

import java.util.ArrayList;
import java.util.List;


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


/** Simple utility class. It is used for executing multi-thread test case. */
public class MultiThreadedTestRunner {
    private final List<Thread> th;
    long maxWait = 60L * 60L * 1000;
    private final List<Throwable> exceptions;

    public MultiThreadedTestRunner(TestRunner[] runnables) {
        th = new ArrayList<Thread>();
        exceptions = new ArrayList<Throwable>();
        for (int i = 0; i < runnables.length; i++) {
            runnables[i].setTestRunner(this);
            th.add(new Thread(runnables[i]));
        }
    }

    /**
     * @param e
     */
    public void addException(Throwable e) {
        exceptions.add(e);
    }

    public void runRunnables() throws Throwable {
        for (Thread t : th) {
            t.start();
        }

        for (Thread t : th) {
            t.join(maxWait);
        }

        if (this.exceptions.size() > 0) {
            throw this.exceptions.get(0);
        }
    }
}
