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
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.fail;

import org.junit.jupiter.api.Test;

/** */
public class TestBaseObjectPool extends TestObjectPool {
    private static class TestObjectPool extends BaseObjectPool<Object> {
        @Override
        public Object borrowObject() {
            return null;
        }

        @Override
        public void invalidateObject0(final Object obj) {}

        @Override
        public void returnObject(final Object obj) {}
    }

    private ObjectPool<String> pool;

    /**
     * @param n Ignored by this implemented. Used by sub-classes.
     * @return the Nth object (zero indexed)
     */
    protected Object getNthObject(final int n) {
        if (this.getClass() != TestBaseObjectPool.class) {
            fail("Subclasses of TestBaseObjectPool must reimplement this method.");
        }
        throw new UnsupportedOperationException("BaseObjectPool isn't a complete implementation.");
    }

    protected boolean isFifo() {
        if (this.getClass() != TestBaseObjectPool.class) {
            fail("Subclasses of TestBaseObjectPool must reimplement this method.");
        }
        return false;
    }

    protected boolean isLifo() {
        if (this.getClass() != TestBaseObjectPool.class) {
            fail("Subclasses of TestBaseObjectPool must reimplement this method.");
        }
        return false;
    }

    /**
     * @param minCapacity Ignored by this implemented. Used by sub-classes.
     * @return A newly created empty pool
     */
    protected ObjectPool<String> makeEmptyPool0(final int minCapacity) {
        if (this.getClass() != TestBaseObjectPool.class) {
            fail("Subclasses of TestBaseObjectPool must reimplement this method.");
        }
        throw new UnsupportedOperationException("BaseObjectPool isn't a complete implementation.");
    }

    @Override
    protected ObjectPool<Object> makeEmptyPool(final PooledObjectFactory<Object> factory) {
        return makeEmptyPool1(factory);
    }

    protected ObjectPool<Object> makeEmptyPool1(final PooledObjectFactory<Object> factory) {
        if (this.getClass() != TestBaseObjectPool.class) {
            fail("Subclasses of TestBaseObjectPool must reimplement this method.");
        }
        throw new UnsupportedOperationException("BaseObjectPool isn't a complete implementation.");
    }

    @Test
    public void testBaseAddObject_test0_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
    }

    @Test
    public void testBaseAddObject_test1_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        try {
            assertEquals(0, pool.getNumIdle());
            assertEquals(0, pool.getNumActive());
            pool.addObject();
            assertEquals(1, pool.getNumIdle());
            assertEquals(0, pool.getNumActive());
            final String obj = pool.borrowObject();
            assertEquals(getNthObject(0), obj);
            assertEquals(0, pool.getNumIdle());
            assertEquals(1, pool.getNumActive());
            pool.returnObject(obj);
            assertEquals(1, pool.getNumIdle());
            assertEquals(0, pool.getNumActive());
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if one of those calls is unsupported
        } finally {
            pool.close();
        }
    }

    @Test
    public void testBaseBorrow_test0_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
    }

    @Test
    public void testBaseBorrow_test1_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        getNthObject(0);
    }

    @Test
    public void testBaseBorrow_test2_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        getNthObject(0);
        assertEquals(getNthObject(0), pool.borrowObject());
    }

    @Test
    public void testBaseBorrow_test3_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        getNthObject(0);
        assertEquals(getNthObject(0), pool.borrowObject());
        getNthObject(1);
    }

    @Test
    public void testBaseBorrow_test4_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        getNthObject(0);
        assertEquals(getNthObject(0), pool.borrowObject());
        getNthObject(1);
        assertEquals(getNthObject(1), pool.borrowObject());
    }

    @Test
    public void testBaseBorrow_test5_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        getNthObject(0);
        assertEquals(getNthObject(0), pool.borrowObject());
        getNthObject(1);
        assertEquals(getNthObject(1), pool.borrowObject());
        getNthObject(2);
    }

    @Test
    public void testBaseBorrow_test6_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        getNthObject(0);
        assertEquals(getNthObject(0), pool.borrowObject());
        getNthObject(1);
        assertEquals(getNthObject(1), pool.borrowObject());
        getNthObject(2);
        assertEquals(getNthObject(2), pool.borrowObject());
    }

    @Test
    public void testBaseBorrow_test7_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        getNthObject(0);
        assertEquals(getNthObject(0), pool.borrowObject());
        getNthObject(1);
        assertEquals(getNthObject(1), pool.borrowObject());
        getNthObject(2);
        assertEquals(getNthObject(2), pool.borrowObject());
        pool.close();
    }

    @Test
    public void testBaseBorrowReturn_test0_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
    }

    @Test
    public void testBaseBorrowReturn_test1_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
    }

    @Test
    public void testBaseBorrowReturn_test2_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
    }

    @Test
    public void testBaseBorrowReturn_test3_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
    }

    @Test
    public void testBaseBorrowReturn_test4_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
    }

    @Test
    public void testBaseBorrowReturn_test5_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
    }

    @Test
    public void testBaseBorrowReturn_test6_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
    }

    @Test
    public void testBaseBorrowReturn_test7_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
    }

    @Test
    public void testBaseBorrowReturn_test8_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
    }

    @Test
    public void testBaseBorrowReturn_test9_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
    }

    @Test
    public void testBaseBorrowReturn_test10_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj1);
    }

    @Test
    public void testBaseBorrowReturn_test11_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj1);
        obj1 = pool.borrowObject();
    }

    @Test
    public void testBaseBorrowReturn_test12_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj1);
        obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
    }

    @Test
    public void testBaseBorrowReturn_test13_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj1);
        obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        pool.returnObject(obj0);
        pool.returnObject(obj2);
    }

    @Test
    public void testBaseBorrowReturn_test14_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj1);
        obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        pool.returnObject(obj0);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
    }

    @Test
    public void testBaseBorrowReturn_test15_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj1);
        obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        pool.returnObject(obj0);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        if (isLifo()) {
            assertEquals(getNthObject(2), obj2);
        }
    }

    @Test
    public void testBaseBorrowReturn_test16_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj1);
        obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        pool.returnObject(obj0);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        if (isLifo()) {
            assertEquals(getNthObject(2), obj2);
        }
        if (isFifo()) {
            assertEquals(getNthObject(0), obj2);
        }
    }

    @Test
    public void testBaseBorrowReturn_test17_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj1);
        obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        pool.returnObject(obj0);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        if (isLifo()) {
            assertEquals(getNthObject(2), obj2);
        }
        if (isFifo()) {
            assertEquals(getNthObject(0), obj2);
        }
        obj0 = pool.borrowObject();
    }

    @Test
    public void testBaseBorrowReturn_test18_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj1);
        obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        pool.returnObject(obj0);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        if (isLifo()) {
            assertEquals(getNthObject(2), obj2);
        }
        if (isFifo()) {
            assertEquals(getNthObject(0), obj2);
        }
        obj0 = pool.borrowObject();
        if (isLifo()) {
            assertEquals(getNthObject(0), obj0);
        }
    }

    @Test
    public void testBaseBorrowReturn_test19_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj1);
        obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        pool.returnObject(obj0);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        if (isLifo()) {
            assertEquals(getNthObject(2), obj2);
        }
        if (isFifo()) {
            assertEquals(getNthObject(0), obj2);
        }
        obj0 = pool.borrowObject();
        if (isLifo()) {
            assertEquals(getNthObject(0), obj0);
        }
        if (isFifo()) {
            assertEquals(getNthObject(2), obj0);
        }
    }

    @Test
    public void testBaseBorrowReturn_test20_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        String obj0 = pool.borrowObject();
        assertEquals(getNthObject(0), obj0);
        String obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        String obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.returnObject(obj1);
        obj1 = pool.borrowObject();
        assertEquals(getNthObject(1), obj1);
        pool.returnObject(obj0);
        pool.returnObject(obj2);
        obj2 = pool.borrowObject();
        if (isLifo()) {
            assertEquals(getNthObject(2), obj2);
        }
        if (isFifo()) {
            assertEquals(getNthObject(0), obj2);
        }
        obj0 = pool.borrowObject();
        if (isLifo()) {
            assertEquals(getNthObject(0), obj0);
        }
        if (isFifo()) {
            assertEquals(getNthObject(2), obj0);
        }
        pool.close();
    }

    @Test
    public void testBaseClear_test0_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
    }

    @Test
    public void testBaseClear_test1_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
    }

    @Test
    public void testBaseClear_test2_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
    }

    @Test
    public void testBaseClear_test3_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
    }

    @Test
    public void testBaseClear_test4_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
    }

    @Test
    public void testBaseClear_test5_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
    }

    @Test
    public void testBaseClear_test6_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        pool.returnObject(obj0);
    }

    @Test
    public void testBaseClear_test7_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        pool.returnObject(obj0);
        assertEquals(0, pool.getNumActive());
    }

    @Test
    public void testBaseClear_test8_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        pool.returnObject(obj0);
        assertEquals(0, pool.getNumActive());
        assertEquals(2, pool.getNumIdle());
    }

    @Test
    public void testBaseClear_test9_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        pool.returnObject(obj0);
        assertEquals(0, pool.getNumActive());
        assertEquals(2, pool.getNumIdle());
        pool.clear();
    }

    @Test
    public void testBaseClear_test10_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        pool.returnObject(obj0);
        assertEquals(0, pool.getNumActive());
        assertEquals(2, pool.getNumIdle());
        pool.clear();
        assertEquals(0, pool.getNumActive());
    }

    @Test
    public void testBaseClear_test11_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        pool.returnObject(obj0);
        assertEquals(0, pool.getNumActive());
        assertEquals(2, pool.getNumIdle());
        pool.clear();
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
    }

    @Test
    public void testBaseClear_test12_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        pool.returnObject(obj0);
        assertEquals(0, pool.getNumActive());
        assertEquals(2, pool.getNumIdle());
        pool.clear();
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final Object obj2 = pool.borrowObject();
    }

    @Test
    public void testBaseClear_test13_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        pool.returnObject(obj0);
        assertEquals(0, pool.getNumActive());
        assertEquals(2, pool.getNumIdle());
        pool.clear();
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final Object obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
    }

    @Test
    public void testBaseClear_test14_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        pool.returnObject(obj0);
        assertEquals(0, pool.getNumActive());
        assertEquals(2, pool.getNumIdle());
        pool.clear();
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final Object obj2 = pool.borrowObject();
        assertEquals(getNthObject(2), obj2);
        pool.close();
    }

    @Test
    public void testBaseClosePool_test0_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
    }

    @Test
    public void testBaseClosePool_test1_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        final String obj = pool.borrowObject();
    }

    @Test
    public void testBaseClosePool_test2_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        final String obj = pool.borrowObject();
        pool.returnObject(obj);
    }

    @Test
    public void testBaseClosePool_test3_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        final String obj = pool.borrowObject();
        pool.returnObject(obj);
        pool.close();
    }

    @Test
    public void testBaseClosePool_test4_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        final String obj = pool.borrowObject();
        pool.returnObject(obj);
        pool.close();
        assertThrows(IllegalStateException.class, pool::borrowObject);
    }

    @Test
    public void testBaseInvalidateObject_test0_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
    }

    @Test
    public void testBaseInvalidateObject_test1_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
    }

    @Test
    public void testBaseInvalidateObject_test2_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
    }

    @Test
    public void testBaseInvalidateObject_test3_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
    }

    @Test
    public void testBaseInvalidateObject_test4_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
    }

    @Test
    public void testBaseInvalidateObject_test5_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
    }

    @Test
    public void testBaseInvalidateObject_test6_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.invalidateObject0(obj0);
    }

    @Test
    public void testBaseInvalidateObject_test7_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.invalidateObject0(obj0);
        assertEquals(1, pool.getNumActive());
    }

    @Test
    public void testBaseInvalidateObject_test8_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.invalidateObject0(obj0);
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
    }

    @Test
    public void testBaseInvalidateObject_test9_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.invalidateObject0(obj0);
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.invalidateObject0(obj1);
    }

    @Test
    public void testBaseInvalidateObject_test10_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.invalidateObject0(obj0);
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.invalidateObject0(obj1);
        assertEquals(0, pool.getNumActive());
    }

    @Test
    public void testBaseInvalidateObject_test11_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.invalidateObject0(obj0);
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.invalidateObject0(obj1);
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
    }

    @Test
    public void testBaseInvalidateObject_test12_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.invalidateObject0(obj0);
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.invalidateObject0(obj1);
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.close();
    }

    @Test
    public void testBaseNumActiveNumIdle_test0_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
    }

    @Test
    public void testBaseNumActiveNumIdle_test1_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
    }

    @Test
    public void testBaseNumActiveNumIdle_test2_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
    }

    @Test
    public void testBaseNumActiveNumIdle_test3_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
    }

    @Test
    public void testBaseNumActiveNumIdle_test4_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
    }

    @Test
    public void testBaseNumActiveNumIdle_test5_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
    }

    @Test
    public void testBaseNumActiveNumIdle_test6_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj1 = pool.borrowObject();
    }

    @Test
    public void testBaseNumActiveNumIdle_test7_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
    }

    @Test
    public void testBaseNumActiveNumIdle_test8_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
    }

    @Test
    public void testBaseNumActiveNumIdle_test9_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
    }

    @Test
    public void testBaseNumActiveNumIdle_test10_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        assertEquals(1, pool.getNumActive());
    }

    @Test
    public void testBaseNumActiveNumIdle_test11_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        assertEquals(1, pool.getNumActive());
        assertEquals(1, pool.getNumIdle());
    }

    @Test
    public void testBaseNumActiveNumIdle_test12_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        assertEquals(1, pool.getNumActive());
        assertEquals(1, pool.getNumIdle());
        pool.returnObject(obj0);
    }

    @Test
    public void testBaseNumActiveNumIdle_test13_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        assertEquals(1, pool.getNumActive());
        assertEquals(1, pool.getNumIdle());
        pool.returnObject(obj0);
        assertEquals(0, pool.getNumActive());
    }

    @Test
    public void testBaseNumActiveNumIdle_test14_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        assertEquals(1, pool.getNumActive());
        assertEquals(1, pool.getNumIdle());
        pool.returnObject(obj0);
        assertEquals(0, pool.getNumActive());
        assertEquals(2, pool.getNumIdle());
    }

    @Test
    public void testBaseNumActiveNumIdle_test15_decomposed() throws Exception {
        try {
            pool = makeEmptyPool0(3);
        } catch (final UnsupportedOperationException e) {
            return; // skip this test if unsupported
        }
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj0 = pool.borrowObject();
        assertEquals(1, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        final String obj1 = pool.borrowObject();
        assertEquals(2, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
        pool.returnObject(obj1);
        assertEquals(1, pool.getNumActive());
        assertEquals(1, pool.getNumIdle());
        pool.returnObject(obj0);
        assertEquals(0, pool.getNumActive());
        assertEquals(2, pool.getNumIdle());
        pool.close();
    }

    @Test
    public void testClose_test0_decomposed()  {
        @SuppressWarnings("resource")
        final ObjectPool<Object> pool = new TestObjectPool();
    }

    @Test
    public void testClose_test1_decomposed()  {
        @SuppressWarnings("resource")
        final ObjectPool<Object> pool = new TestObjectPool();
        pool.close();
        pool.close();
    }

    @Test
    public void testUnsupportedOperations_test0_decomposed() throws Exception {
        if (!getClass().equals(TestBaseObjectPool.class)) {
            return; // skip redundant tests
        }
    }

    @Test
    public void testUnsupportedOperations_test1_decomposed() throws Exception {
        if (!getClass().equals(TestBaseObjectPool.class)) {
            return; // skip redundant tests
        }
        try (final ObjectPool<Object> pool = new TestObjectPool()) {

            assertTrue(pool.getNumIdle() < 0, "Negative expected.");
            assertTrue(pool.getNumActive() < 0, "Negative expected.");

            assertThrows(UnsupportedOperationException.class, pool::clear);
            assertThrows(UnsupportedOperationException.class, pool::addObject);
        }
    }
}