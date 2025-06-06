
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

package org.apache.commons.pool2;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

/** Abstract test case for {@link ObjectPool} implementations. */
public abstract class TestKeyedObjectPool {

    protected static class FailingKeyedPooledObjectFactory {
        private final List<MethodCall> methodCalls = new ArrayList<>();
        private int count;
        private boolean makeObjectFail;
        private boolean activateObjectFail;
        private boolean validateObjectFail;
        private boolean passivateObjectFail;
        private boolean destroyObjectFail;

        public FailingKeyedPooledObjectFactory() {}

        public void activateObject(final Object key, final PooledObject<Object> obj)
                throws Exception {
            methodCalls.add(MethodCall.MethodCall0("activateObject", key, obj.getObject()));
            if (activateObjectFail) {
                throw new PrivateException("activateObject");
            }
        }

        public void destroyObject(final Object key, final PooledObject<Object> obj)
                throws Exception {
            methodCalls.add(MethodCall.MethodCall0("destroyObject", key, obj.getObject()));
            if (destroyObjectFail) {
                throw new PrivateException("destroyObject");
            }
        }

        public int getCurrentCount() {
            return count;
        }

        public List<MethodCall> getMethodCalls() {
            return methodCalls;
        }

        public boolean isActivateObjectFail() {
            return activateObjectFail;
        }

        public boolean isDestroyObjectFail() {
            return destroyObjectFail;
        }

        public boolean isMakeObjectFail() {
            return makeObjectFail;
        }

        public boolean isPassivateObjectFail() {
            return passivateObjectFail;
        }

        public boolean isValidateObjectFail() {
            return validateObjectFail;
        }

        public void passivateObject(final Object key, final PooledObject<Object> obj)
                throws Exception {
            methodCalls.add(MethodCall.MethodCall0("passivateObject", key, obj.getObject()));
            if (passivateObjectFail) {
                throw new PrivateException("passivateObject");
            }
        }

        public void reset() {
            count = 0;
            getMethodCalls().clear();
            setMakeObjectFail(false);
            setActivateObjectFail(false);
            setValidateObjectFail(false);
            setPassivateObjectFail(false);
            setDestroyObjectFail(false);
        }

        public void setActivateObjectFail(final boolean activateObjectFail) {
            this.activateObjectFail = activateObjectFail;
        }

        public void setCurrentCount(final int count) {
            this.count = count;
        }

        public void setDestroyObjectFail(final boolean destroyObjectFail) {
            this.destroyObjectFail = destroyObjectFail;
        }

        public void setMakeObjectFail(final boolean makeObjectFail) {
            this.makeObjectFail = makeObjectFail;
        }

        public void setPassivateObjectFail(final boolean passivateObjectFail) {
            this.passivateObjectFail = passivateObjectFail;
        }

        public void setValidateObjectFail(final boolean validateObjectFail) {
            this.validateObjectFail = validateObjectFail;
        }

        public boolean validateObject(final Object key, final PooledObject<Object> obj) {
            final MethodCall call = MethodCall.MethodCall0("validateObject", key, obj.getObject());
            methodCalls.add(call);
            if (validateObjectFail) {
                throw new PrivateException("validateObject");
            }
            final boolean r = true;
            call.returned(Boolean.valueOf(r));
            return r;
        }
    }

    protected static final String KEY = "key";

    private KeyedObjectPool<Object, Object> pool;

    private final Integer ZERO = Integer.valueOf(0);

    private final Integer ONE = Integer.valueOf(1);

    private void clear(
            final FailingKeyedPooledObjectFactory factory, final List<MethodCall> expectedMethods) {
        factory.getMethodCalls().clear();
        expectedMethods.clear();
    }

    /**
     * Return what we expect to be the n<sup>th</sup> object (zero indexed) created by the pool for
     * the given key.
     *
     * @param key Key for the object to be obtained
     * @param n index of the object to be obtained
     * @return the requested object
     */
    protected abstract Object getNthObject(Object key, int n);

    protected abstract boolean isFifo();

    protected abstract boolean isLifo();

    /**
     * Creates an {@link KeyedObjectPool} instance that can contain at least <i>minCapacity</i> idle
     * and active objects, or throw {@link IllegalArgumentException} if such a pool cannot be
     * created.
     *
     * @param minCapacity Minimum capacity of the pool to create
     * @return the newly created keyed object pool
     */
    protected abstract KeyedObjectPool<Object, Object> makeEmptyPool0(int minCapacity);

    /**
     * Creates an {@code KeyedObjectPool} with the specified factory. The pool should be in a
     * default configuration and conform to the expected behaviors described in {@link
     * KeyedObjectPool}. Generally speaking there should be no limits on the various object counts.
     *
     * @param factory Factory to use to associate with the pool
     * @return The newly created empty pool
     */
    protected abstract KeyedObjectPool<Object, Object> makeEmptyPool1(
            KeyedPooledObjectFactory<Object, Object> factory);

    protected abstract Object makeKey(int n);

    private void reset(
            final KeyedObjectPool<Object, Object> pool,
            final FailingKeyedPooledObjectFactory factory,
            final List<MethodCall> expectedMethods)
            throws Exception {
        pool.clear0();
        clear(factory, expectedMethods);
        factory.reset();
    }

    @AfterEach
    public void tearDown() {
        pool = null;
    }

    @Test
    public void testBaseAddObject() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException uoe) {
            return; // skip this test if unsupported
        }
        final Object key = makeKey(0);
        try {
            assertEquals(0, pool.getNumIdle0());
            assertEquals(0, pool.getNumActive0());
            assertEquals(0, pool.getNumIdle1(key));
            assertEquals(0, pool.getNumActive1(key));
            pool.addObject(key);
            assertEquals(1, pool.getNumIdle0());
            assertEquals(0, pool.getNumActive0());
            assertEquals(1, pool.getNumIdle1(key));
            assertEquals(0, pool.getNumActive1(key));
            final Object obj = pool.borrowObject(key);
            assertEquals(getNthObject(key, 0), obj);
            assertEquals(0, pool.getNumIdle0());
            assertEquals(1, pool.getNumActive0());
            assertEquals(0, pool.getNumIdle1(key));
            assertEquals(1, pool.getNumActive1(key));
            pool.returnObject(key, obj);
            assertEquals(1, pool.getNumIdle0());
            assertEquals(0, pool.getNumActive0());
            assertEquals(1, pool.getNumIdle1(key));
            assertEquals(0, pool.getNumActive1(key));
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if one of those calls is unsupported
        } finally {
            pool.close();
        }
    }

    @Test
    public void testBaseBorrow() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException uoe) {
            return; // skip this test if unsupported
        }
        final Object keya = makeKey(0);
        final Object keyb = makeKey(1);
        assertEquals(getNthObject(keya, 0), pool.borrowObject(keya), "1");
        assertEquals(getNthObject(keyb, 0), pool.borrowObject(keyb), "2");
        assertEquals(getNthObject(keyb, 1), pool.borrowObject(keyb), "3");
        assertEquals(getNthObject(keya, 1), pool.borrowObject(keya), "4");
        assertEquals(getNthObject(keyb, 2), pool.borrowObject(keyb), "5");
        assertEquals(getNthObject(keya, 2), pool.borrowObject(keya), "6");
        pool.close();
    }

    @Test
    public void testBaseBorrowReturn() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException uoe) {
            return; // skip this test if unsupported
        }
        final Object keya = makeKey(0);
        Object obj0 = pool.borrowObject(keya);
        assertEquals(getNthObject(keya, 0), obj0);
        Object obj1 = pool.borrowObject(keya);
        assertEquals(getNthObject(keya, 1), obj1);
        Object obj2 = pool.borrowObject(keya);
        assertEquals(getNthObject(keya, 2), obj2);
        pool.returnObject(keya, obj2);
        obj2 = pool.borrowObject(keya);
        assertEquals(getNthObject(keya, 2), obj2);
        pool.returnObject(keya, obj1);
        obj1 = pool.borrowObject(keya);
        assertEquals(getNthObject(keya, 1), obj1);
        pool.returnObject(keya, obj0);
        pool.returnObject(keya, obj2);
        obj2 = pool.borrowObject(keya);
        if (isLifo()) {
            assertEquals(getNthObject(keya, 2), obj2);
        }
        if (isFifo()) {
            assertEquals(getNthObject(keya, 0), obj2);
        }
        obj0 = pool.borrowObject(keya);
        if (isLifo()) {
            assertEquals(getNthObject(keya, 0), obj0);
        }
        if (isFifo()) {
            assertEquals(getNthObject(keya, 2), obj0);
        }
        pool.close();
    }

    @Test
    public void testBaseClear() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException uoe) {
            return; // skip this test if unsupported
        }
        final Object keya = makeKey(0);
        assertEquals(0, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        final Object obj0 = pool.borrowObject(keya);
        final Object obj1 = pool.borrowObject(keya);
        assertEquals(2, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        pool.returnObject(keya, obj1);
        pool.returnObject(keya, obj0);
        assertEquals(0, pool.getNumActive1(keya));
        assertEquals(2, pool.getNumIdle1(keya));
        pool.clear1(keya);
        assertEquals(0, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        final Object obj2 = pool.borrowObject(keya);
        assertEquals(getNthObject(keya, 2), obj2);
        pool.close();
    }

    @Test
    public void testBaseInvalidateObject() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException uoe) {
            return; // skip this test if unsupported
        }
        final Object keya = makeKey(0);
        assertEquals(0, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        final Object obj0 = pool.borrowObject(keya);
        final Object obj1 = pool.borrowObject(keya);
        assertEquals(2, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        pool.invalidateObject0(keya, obj0);
        assertEquals(1, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        pool.invalidateObject0(keya, obj1);
        assertEquals(0, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        pool.close();
    }

    @Test
    public void testBaseNumActiveNumIdle() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException uoe) {
            return; // skip this test if unsupported
        }
        final Object keya = makeKey(0);
        assertEquals(0, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        final Object obj0 = pool.borrowObject(keya);
        assertEquals(1, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        final Object obj1 = pool.borrowObject(keya);
        assertEquals(2, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        pool.returnObject(keya, obj1);
        assertEquals(1, pool.getNumActive1(keya));
        assertEquals(1, pool.getNumIdle1(keya));
        pool.returnObject(keya, obj0);
        assertEquals(0, pool.getNumActive1(keya));
        assertEquals(2, pool.getNumIdle1(keya));

        assertEquals(0, pool.getNumActive1("xyzzy12345"));
        assertEquals(0, pool.getNumIdle1("xyzzy12345"));

        pool.close();
    }

    @Test
    public void testBaseNumActiveNumIdle2() throws Exception {
        try {
            pool = makeEmptyPool0(6);
        } catch (final UnsupportedOperationException uoe) {
            return; // skip this test if unsupported
        }
        final Object keya = makeKey(0);
        final Object keyb = makeKey(1);
        assertEquals(0, pool.getNumActive0());
        assertEquals(0, pool.getNumIdle0());
        assertEquals(0, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        assertEquals(0, pool.getNumActive1(keyb));
        assertEquals(0, pool.getNumIdle1(keyb));

        final Object objA0 = pool.borrowObject(keya);
        final Object objB0 = pool.borrowObject(keyb);

        assertEquals(2, pool.getNumActive0());
        assertEquals(0, pool.getNumIdle0());
        assertEquals(1, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        assertEquals(1, pool.getNumActive1(keyb));
        assertEquals(0, pool.getNumIdle1(keyb));

        final Object objA1 = pool.borrowObject(keya);
        final Object objB1 = pool.borrowObject(keyb);

        assertEquals(4, pool.getNumActive0());
        assertEquals(0, pool.getNumIdle0());
        assertEquals(2, pool.getNumActive1(keya));
        assertEquals(0, pool.getNumIdle1(keya));
        assertEquals(2, pool.getNumActive1(keyb));
        assertEquals(0, pool.getNumIdle1(keyb));

        pool.returnObject(keya, objA0);
        pool.returnObject(keyb, objB0);

        assertEquals(2, pool.getNumActive0());
        assertEquals(2, pool.getNumIdle0());
        assertEquals(1, pool.getNumActive1(keya));
        assertEquals(1, pool.getNumIdle1(keya));
        assertEquals(1, pool.getNumActive1(keyb));
        assertEquals(1, pool.getNumIdle1(keyb));

        pool.returnObject(keya, objA1);
        pool.returnObject(keyb, objB1);

        assertEquals(0, pool.getNumActive0());
        assertEquals(4, pool.getNumIdle0());
        assertEquals(0, pool.getNumActive1(keya));
        assertEquals(2, pool.getNumIdle1(keya));
        assertEquals(0, pool.getNumActive1(keyb));
        assertEquals(2, pool.getNumIdle1(keyb));

        pool.close();
    }
}
