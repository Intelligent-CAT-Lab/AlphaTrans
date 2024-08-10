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
package org.apache.commons.pool2.impl;

import static org.junit.jupiter.api.Assertions.assertFalse;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.atomic.AtomicBoolean;

/** Tests {@link DefaultPooledObject}. */
public class TestDefaultPooledObject {

    /**
     * JIRA: POOL-279
     *
     * @throws Exception May occur in some failure modes
     */

    @Test
    public void testGetIdleTimeMillis_test0_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
    }

    @Test
    public void testGetIdleTimeMillis_test1_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
        dpo.deallocate();
    }

    @Test
    public void testGetIdleTimeMillis_test2_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
        dpo.deallocate();
        dpo.getIdleTime();
    }

    @Test
    public void testGetIdleTimeMillis_test3_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
        dpo.deallocate();
        dpo.getIdleTime();
        dpo.getIdleDuration();
    }

    @Test
    public void testGetIdleTimeMillis_test4_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
        dpo.deallocate();
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
    }

    @Test
    public void testGetIdleTimeMillis_test5_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
        dpo.deallocate();
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
        final Runnable allocateAndDeallocateTask =
                () -> {
                    for (int i1 = 0; i1 < 10000; i1++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.allocate();
                    for (int i2 = 0; i2 < 10000; i2++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.deallocate();
                };
    }

    @Test
    public void testGetIdleTimeMillis_test6_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
        dpo.deallocate();
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
        final Runnable allocateAndDeallocateTask =
                () -> {
                    for (int i1 = 0; i1 < 10000; i1++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.allocate();
                    for (int i2 = 0; i2 < 10000; i2++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.deallocate();
                };
        dpo.getIdleTime();
    }

    @Test
    public void testGetIdleTimeMillis_test7_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
        dpo.deallocate();
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
        final Runnable allocateAndDeallocateTask =
                () -> {
                    for (int i1 = 0; i1 < 10000; i1++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.allocate();
                    for (int i2 = 0; i2 < 10000; i2++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.deallocate();
                };
        dpo.getIdleTime();
        dpo.getIdleDuration();
    }

    @Test
    public void testGetIdleTimeMillis_test8_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
        dpo.deallocate();
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
        final Runnable allocateAndDeallocateTask =
                () -> {
                    for (int i1 = 0; i1 < 10000; i1++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.allocate();
                    for (int i2 = 0; i2 < 10000; i2++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.deallocate();
                };
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
    }

    @Test
    public void testGetIdleTimeMillis_test9_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
        dpo.deallocate();
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
        final Runnable allocateAndDeallocateTask =
                () -> {
                    for (int i1 = 0; i1 < 10000; i1++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.allocate();
                    for (int i2 = 0; i2 < 10000; i2++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.deallocate();
                };
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
        final Runnable getIdleTimeTask =
                () -> {
                    for (int i = 0; i < 10000; i++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                };
    }

    @Test
    public void testGetIdleTimeMillis_test10_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
        dpo.deallocate();
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
        final Runnable allocateAndDeallocateTask =
                () -> {
                    for (int i1 = 0; i1 < 10000; i1++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.allocate();
                    for (int i2 = 0; i2 < 10000; i2++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.deallocate();
                };
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
        final Runnable getIdleTimeTask =
                () -> {
                    for (int i = 0; i < 10000; i++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                };
        final double probabilityOfAllocationTask = 0.7;
        final List<Future<?>> futures = new ArrayList<>();
        for (int i = 1; i <= 10000; i++) {
            final Runnable randomTask =
                    Math.random() < probabilityOfAllocationTask
                            ? allocateAndDeallocateTask
                            : getIdleTimeTask;
            futures.add(executor.submit(randomTask));
        }
    }

    @Test
    public void testGetIdleTimeMillis_test11_decomposed() throws Exception {
        final DefaultPooledObject<Object> dpo = new DefaultPooledObject<>(new Object());
        final AtomicBoolean negativeIdleTimeReturned = new AtomicBoolean(false);
        final ExecutorService executor =
                Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 3);
        dpo.allocate();
        dpo.deallocate();
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
        final Runnable allocateAndDeallocateTask =
                () -> {
                    for (int i1 = 0; i1 < 10000; i1++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.allocate();
                    for (int i2 = 0; i2 < 10000; i2++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                    dpo.deallocate();
                };
        dpo.getIdleTime();
        dpo.getIdleDuration();
        dpo.getIdleTime().isNegative();
        final Runnable getIdleTimeTask =
                () -> {
                    for (int i = 0; i < 10000; i++) {
                        if (dpo.getIdleDuration().isNegative() || dpo.getIdleTime().isNegative()) {
                            negativeIdleTimeReturned.set(true);
                            break;
                        }
                    }
                };
        final double probabilityOfAllocationTask = 0.7;
        final List<Future<?>> futures = new ArrayList<>();
        for (int i = 1; i <= 10000; i++) {
            final Runnable randomTask =
                    Math.random() < probabilityOfAllocationTask
                            ? allocateAndDeallocateTask
                            : getIdleTimeTask;
            futures.add(executor.submit(randomTask));
        }
        for (final Future<?> future : futures) {
            future.get();
        }
        assertFalse(
                negativeIdleTimeReturned.get(),
                "DefaultPooledObject.getIdleTimeMillis() returned a negative value");
    }
}