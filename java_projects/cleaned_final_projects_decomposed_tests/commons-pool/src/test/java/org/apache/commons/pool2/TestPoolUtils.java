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

package org.apache.commons.pool2;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.fail;

import org.apache.commons.pool2.impl.DefaultPooledObject;
import org.junit.jupiter.api.Test;
import org.opentest4j.AssertionFailedError;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TimerTask;

/**
 * Unit tests for {@link PoolUtils}.
 *
 * <p>TODO Replace our own mocking with a mocking library like Mockito.
 */
public class TestPoolUtils {

    private static class MethodCallLogger implements InvocationHandler {
        private final List<String> calledMethods;

        MethodCallLogger(final List<String> calledMethods) {
            this.calledMethods = calledMethods;
        }

        @Override
        public Object invoke(final Object proxy, final Method method, final Object[] args)
                throws Throwable {
            if (calledMethods == null) {
                return null;
            }
            calledMethods.add(method.getName());
            if (boolean.class.equals(method.getReturnType())) {
                return Boolean.FALSE;
            }
            if (int.class.equals(method.getReturnType())) {
                return Integer.valueOf(0);
            }
            if (long.class.equals(method.getReturnType())) {
                return Long.valueOf(0);
            }
            if (Object.class.equals(method.getReturnType())) {
                return new Object();
            }
            if (PooledObject.class.equals(method.getReturnType())) {
                return new DefaultPooledObject<>(new Object());
            }
            return null;
        }
    }

    /**
     * Period between checks for minIdle tests. Increase this if you happen to get too many false
     * failures.
     */
    private static final int CHECK_PERIOD = 300;

    /** Times to let the minIdle check run. */
    private static final int CHECK_COUNT = 4;

    /** Sleep time to let the minIdle tests run CHECK_COUNT times. */
    private static final int CHECK_SLEEP_PERIOD =
            CHECK_PERIOD * (CHECK_COUNT - 1) + CHECK_PERIOD / 2;

    @SuppressWarnings("unchecked")
    private static <T> T createProxy0(final Class<T> clazz, final InvocationHandler handler) {
        return (T) Proxy.newProxyInstance(clazz.getClassLoader(), new Class[] {clazz}, handler);
    }

    private static <T> T createProxy1(final Class<T> clazz, final List<String> logger) {
        return createProxy0(clazz, new MethodCallLogger(logger));
    }

    private static List<String> invokeEveryMethod0(final KeyedObjectPool<Object, Object> kop)
            throws Exception {
        kop.addObject(null);
        kop.borrowObject(null);
        kop.clear0();
        kop.clear1(null);
        kop.close();
        kop.getNumActive0();
        kop.getNumActive1(null);
        kop.getNumIdle0();
        kop.getNumIdle1(null);
        kop.invalidateObject0(null, new Object());
        kop.returnObject(null, new Object());
        kop.toString();

        return Arrays.asList(
                "addObject",
                "borrowObject",
                "clear0",
                "clear1",
                "close",
                "getNumActive0",
                "getNumActive1",
                "getNumIdle0",
                "getNumIdle1",
                "invalidateObject0",
                "returnObject",
                "toString");
    }

    private static <K, V> List<String> invokeEveryMethod1(final KeyedPooledObjectFactory<K, V> kpof)
            throws Exception {
        kpof.activateObject(null, null);
        kpof.destroyObject0(null, null);
        kpof.makeObject(null);
        kpof.passivateObject(null, null);
        kpof.validateObject(null, null);
        kpof.toString();

        return Arrays.asList(
                "activateObject",
                "destroyObject0",
                "makeObject",
                "passivateObject",
                "validateObject",
                "toString");
    }

    private static List<String> invokeEveryMethod2(final ObjectPool<Object> op) throws Exception {
        op.addObject();
        op.borrowObject();
        op.clear();
        op.close();
        op.getNumActive();
        op.getNumIdle();
        op.invalidateObject0(new Object());
        op.returnObject(new Object());
        op.toString();

        return Arrays.asList(
                "addObject",
                "borrowObject",
                "clear",
                "close",
                "getNumActive",
                "getNumIdle",
                "invalidateObject0",
                "returnObject",
                "toString");
    }

    private static <T> List<String> invokeEveryMethod3(final PooledObjectFactory<T> pof)
            throws Exception {
        pof.activateObject(null);
        pof.destroyObject0(null);
        pof.makeObject();
        pof.passivateObject(null);
        pof.validateObject(null);
        pof.toString();

        return Arrays.asList(
                "activateObject",
                "destroyObject",
                "makeObject",
                "passivateObject",
                "validateObject",
                "toString");
    }

    

    

    

    

    

    

    

    

    

    

    /** Tests the {@link PoolUtils} timer holder. */

    @Test
    public void testCheckMinIdleKeyedObjectPoolKeys_test0_decomposed() throws Exception {
        AssertionFailedError afe = null;
        int triesLeft = 3;
        do {
            afe = null;
            final List<String> calledMethods = new ArrayList<>();
            try (@SuppressWarnings("unchecked")
                    final KeyedObjectPool<String, Object> pool =
                            createProxy1(KeyedObjectPool.class, calledMethods)) {
                final Collection<String> keys = new ArrayList<>(2);
                keys.add("one");
                keys.add("two");
                final Map<String, TimerTask> tasks =
                        PoolUtils.checkMinIdle0(pool, keys, 1, CHECK_PERIOD);

                Thread.sleep(CHECK_SLEEP_PERIOD); // will check CHECK_COUNT more times.
                for (final TimerTask task : tasks.values()) {
                    task.cancel();
                }

                final List<String> expectedMethods = new ArrayList<>();
                for (int i = 0; i < CHECK_COUNT * keys.size(); i++) {
                    expectedMethods.add("getNumIdle1");
                    expectedMethods.add("addObject");
                }
                assertEquals(
                        expectedMethods, calledMethods); // may fail because of the thread scheduler
            } catch (final AssertionFailedError e) {
                afe = e;
            }
        } while (--triesLeft > 0 && afe != null);
    }

    @Test
    public void testCheckMinIdleKeyedObjectPoolKeys_test1_decomposed() throws Exception {
        AssertionFailedError afe = null;
        int triesLeft = 3;
        do {
            afe = null;
            final List<String> calledMethods = new ArrayList<>();
            try (@SuppressWarnings("unchecked")
                    final KeyedObjectPool<String, Object> pool =
                            createProxy1(KeyedObjectPool.class, calledMethods)) {
                final Collection<String> keys = new ArrayList<>(2);
                keys.add("one");
                keys.add("two");
                final Map<String, TimerTask> tasks =
                        PoolUtils.checkMinIdle0(pool, keys, 1, CHECK_PERIOD);

                Thread.sleep(CHECK_SLEEP_PERIOD); // will check CHECK_COUNT more times.
                for (final TimerTask task : tasks.values()) {
                    task.cancel();
                }

                final List<String> expectedMethods = new ArrayList<>();
                for (int i = 0; i < CHECK_COUNT * keys.size(); i++) {
                    expectedMethods.add("getNumIdle1");
                    expectedMethods.add("addObject");
                }
                assertEquals(
                        expectedMethods, calledMethods); // may fail because of the thread scheduler
            } catch (final AssertionFailedError e) {
                afe = e;
            }
        } while (--triesLeft > 0 && afe != null);
        if (afe != null) {
            throw afe;
        }
    }

    @Test
    public void testCheckMinIdleKeyedObjectPoolKeysNulls_test0_decomposed()  {
        try (@SuppressWarnings("unchecked")
                final KeyedObjectPool<Object, Object> pool =
                        createProxy1(KeyedObjectPool.class, (List<String>) null)) {
            assertThrows(
                    IllegalArgumentException.class,
                    () -> PoolUtils.checkMinIdle1(pool, (Collection<?>) null, 1, 1),
                    "PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long) must not accept"
                            + " null keys.");
        }
    }

    @Test
    public void testCheckMinIdleKeyedObjectPoolKeysNulls_test1_decomposed()  {
        try (@SuppressWarnings("unchecked")
                final KeyedObjectPool<Object, Object> pool =
                        createProxy1(KeyedObjectPool.class, (List<String>) null)) {
            assertThrows(
                    IllegalArgumentException.class,
                    () -> PoolUtils.checkMinIdle1(pool, (Collection<?>) null, 1, 1),
                    "PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long) must not accept"
                            + " null keys.");
        }
        try (@SuppressWarnings("unchecked")
                final KeyedObjectPool<Object, Object> pool =
                        createProxy1(KeyedObjectPool.class, (List<String>) null)) {
            PoolUtils.checkMinIdle1(pool, (Collection<?>) Collections.emptyList(), 1, 1);
        } catch (final IllegalArgumentException iae) {
            fail(
                    "PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long) must accept empty"
                            + " lists.");
        }
    }

    @Test
    public void testCheckRethrow_test0_decomposed()  {
        try {
            PoolUtils.checkRethrow(new Exception());
        } catch (final Throwable t) {
            fail(
                    "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                            + " VirtualMachineError.");
        }
        try {
            PoolUtils.checkRethrow(new ThreadDeath());
            fail("PoolUtils.checkRethrow(Throwable) must rethrow ThreadDeath.");
        } catch (final ThreadDeath td) {
        } catch (final Throwable t) {
            fail(
                    "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                            + " VirtualMachineError.");
        }
        try {
            PoolUtils.checkRethrow(
                    new InternalError()); // InternalError extends VirtualMachineError
            fail("PoolUtils.checkRethrow(Throwable) must rethrow VirtualMachineError.");
        } catch (final VirtualMachineError td) {
        } catch (final Throwable t) {
            fail(
                    "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                            + " VirtualMachineError.");
        }
    }

    @Test
    public void testErodingObjectPoolDefaultFactor_test0_decomposed()  {
        try (@SuppressWarnings("unchecked")
                        final ObjectPool<Object> internalPool =
                                createProxy0(ObjectPool.class, (arg0, arg1, arg2) -> null);
                final ObjectPool<Object> pool = PoolUtils.erodingPool3(internalPool)) {
            final String expectedToString =
                    "ErodingObjectPool{factor=ErodingFactor{factor=1.0, idleHighWaterMark=1}, pool="
                            + internalPool
                            + "}";
            assertEquals(expectedToString, pool.toString());
        }
    }

    @Test
    public void testErodingPoolKeyedObjectPoolDefaultFactor_test0_decomposed()  {
        try (@SuppressWarnings("unchecked")
                        final KeyedObjectPool<Object, Object> internalPool =
                                createProxy0(KeyedObjectPool.class, (arg0, arg1, arg2) -> null);
                final KeyedObjectPool<Object, Object> pool = PoolUtils.erodingPool0(internalPool)) {
            final String expectedToString =
                    "ErodingKeyedObjectPool{factor=ErodingFactor{factor=1.0, idleHighWaterMark=1},"
                            + " keyedPool="
                            + internalPool
                            + "}";
            assertEquals(expectedToString, pool.toString());
        }
    }

    @Test
    public void testJavaBeanInstantiation_test0_decomposed()  {
        assertNotNull(new PoolUtils());
    }

    @Test
    public void testPrefillKeyedObjectPoolCollection_test0_decomposed() throws Exception {
        try (@SuppressWarnings("unchecked")
                final KeyedObjectPool<String, String> pool =
                        createProxy1(KeyedObjectPool.class, (List<String>) null)) {
            assertThrows(
                    IllegalArgumentException.class,
                    () -> PoolUtils.prefill0(pool, (Collection<String>) null, 1),
                    "PoolUtils.prefill(KeyedObjectPool,Collection,int) must not accept null keys.");
        }
    }

    @Test
    public void testPrefillKeyedObjectPoolCollection_test1_decomposed() throws Exception {
        try (@SuppressWarnings("unchecked")
                final KeyedObjectPool<String, String> pool =
                        createProxy1(KeyedObjectPool.class, (List<String>) null)) {
            assertThrows(
                    IllegalArgumentException.class,
                    () -> PoolUtils.prefill0(pool, (Collection<String>) null, 1),
                    "PoolUtils.prefill(KeyedObjectPool,Collection,int) must not accept null keys.");
        }
        final List<String> calledMethods = new ArrayList<>();
        try (@SuppressWarnings("unchecked")
                final KeyedObjectPool<String, Object> pool =
                        createProxy1(KeyedObjectPool.class, calledMethods)) {

            final Set<String> keys = new HashSet<>();
            PoolUtils.prefill0(pool, keys, 0);
            final List<String> expectedMethods = new ArrayList<>();
            expectedMethods.add("addObjects0");
            assertEquals(expectedMethods, calledMethods);

            calledMethods.clear();
            keys.add("one");
            keys.add("two");
            keys.add("three");
            final int count = 3;
            PoolUtils.prefill0(pool, keys, count);
            assertEquals(expectedMethods, calledMethods);
        }
    }

    @Test
    public void testPrefillObjectPool_test0_decomposed() throws Exception {
        assertThrows(
                IllegalArgumentException.class,
                () -> PoolUtils.prefill2(null, 1),
                "PoolUtils.prefill(ObjectPool,int) must not allow null pool.");
    }

    @Test
    public void testPrefillObjectPool_test1_decomposed() throws Exception {
        assertThrows(
                IllegalArgumentException.class,
                () -> PoolUtils.prefill2(null, 1),
                "PoolUtils.prefill(ObjectPool,int) must not allow null pool.");
        final List<String> calledMethods = new ArrayList<>();
        try (@SuppressWarnings("unchecked")
                final ObjectPool<Object> pool = createProxy1(ObjectPool.class, calledMethods)) {

            PoolUtils.prefill2(pool, 0);
            final List<String> expectedMethods = new ArrayList<>();
            expectedMethods.add("addObjects");
            assertEquals(expectedMethods, calledMethods);

            calledMethods.clear();
            PoolUtils.prefill2(pool, 3);
            assertEquals(expectedMethods, calledMethods);
        }
    }

    @Test
    public void testSynchronizedPoolKeyedObjectPool_test0_decomposed() throws Exception {
        assertThrows(
                IllegalArgumentException.class,
                () -> PoolUtils.synchronizedPool0((KeyedObjectPool<Object, Object>) null),
                "PoolUtils.synchronizedPool(KeyedObjectPool) must not allow a null pool.");
    }

    @Test
    public void testSynchronizedPoolKeyedObjectPool_test1_decomposed() throws Exception {
        assertThrows(
                IllegalArgumentException.class,
                () -> PoolUtils.synchronizedPool0((KeyedObjectPool<Object, Object>) null),
                "PoolUtils.synchronizedPool(KeyedObjectPool) must not allow a null pool.");
        final List<String> calledMethods = new ArrayList<>();
        try (@SuppressWarnings("unchecked")
                        final KeyedObjectPool<Object, Object> kop =
                                createProxy1(KeyedObjectPool.class, calledMethods);
                final KeyedObjectPool<Object, Object> skop = PoolUtils.synchronizedPool0(kop)) {
            final List<String> expectedMethods = invokeEveryMethod0(skop);
            assertEquals(expectedMethods, calledMethods);
        }
    }

    @Test
    public void testSynchronizedPoolObjectPool_test0_decomposed() throws Exception {
        assertThrows(
                IllegalArgumentException.class,
                () -> PoolUtils.synchronizedPool1((ObjectPool<Object>) null),
                "PoolUtils.synchronizedPool(ObjectPool) must not allow a null pool.");
    }

    @Test
    public void testSynchronizedPoolObjectPool_test1_decomposed() throws Exception {
        assertThrows(
                IllegalArgumentException.class,
                () -> PoolUtils.synchronizedPool1((ObjectPool<Object>) null),
                "PoolUtils.synchronizedPool(ObjectPool) must not allow a null pool.");
        final List<String> calledMethods = new ArrayList<>();
        try (@SuppressWarnings("unchecked")
                        final ObjectPool<Object> op =
                                createProxy1(ObjectPool.class, calledMethods);
                final ObjectPool<Object> sop = PoolUtils.synchronizedPool1(op)) {
            final List<String> expectedMethods = invokeEveryMethod2(sop);
            assertEquals(expectedMethods, calledMethods);
        }
    }

    @Test
    public void testTimerHolder_test0_decomposed()  {
        final PoolUtils.TimerHolder h = new PoolUtils.TimerHolder();
    }

    @Test
    public void testTimerHolder_test1_decomposed()  {
        final PoolUtils.TimerHolder h = new PoolUtils.TimerHolder();
        assertNotNull(h);
        assertNotNull(PoolUtils.TimerHolder.MIN_IDLE_TIMER);
    }
}