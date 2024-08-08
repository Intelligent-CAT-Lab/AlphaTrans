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

package org.apache.commons.pool2.performance;

import org.apache.commons.pool2.PooledObject;
import org.apache.commons.pool2.Waiter;

/** Sleepy ObjectFactory (everything takes a while longer) */
public class SleepingObjectFactory {

    private int counter;
    private boolean debug;

    public void activateObject(final PooledObject<Integer> obj) throws Exception {
        debug("activateObject", obj);
        Waiter.sleepQuietly(10);
    }

    private void debug(final String method, final Object obj) {
        if (debug) {
            final String thread = "thread" + Thread.currentThread().getName();
            System.out.println(thread + ": " + method + " " + obj);
        }
    }

    public void destroyObject(final PooledObject<Integer> obj) throws Exception {
        debug("destroyObject", obj);
        Waiter.sleepQuietly(250);
    }

    public boolean isDebug() {
        return debug;
    }

    public void passivateObject(final PooledObject<Integer> obj) throws Exception {
        debug("passivateObject", obj);
        Waiter.sleepQuietly(10);
    }

    public void setDebug(final boolean b) {
        debug = b;
    }

    public boolean validateObject(final PooledObject<Integer> obj) {
        debug("validateObject", obj);
        Waiter.sleepQuietly(30);
        return true;
    }

    
}
