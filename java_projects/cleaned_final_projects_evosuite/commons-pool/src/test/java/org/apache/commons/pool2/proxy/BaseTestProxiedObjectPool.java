
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

package org.apache.commons.pool2.proxy;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.apache.commons.pool2.ObjectPool;
import org.junit.jupiter.api.Test;

import java.io.StringWriter;
import java.time.Duration;

public abstract class BaseTestProxiedObjectPool {

    protected interface TestObject {
        String getData();

        void setData(String data);
    }

    private static class TestObjectImpl implements TestObject {

        private String data;

        @Override
        public String getData() {
            return data;
        }

        @Override
        public void setData(final String data) {
            this.data = data;
        }
    }

    private static final String DATA1 = "data1";

    private static final Duration ABANDONED_TIMEOUT_SECS = Duration.ofSeconds(3);

    private ObjectPool<TestObject> pool;

    private StringWriter log;

    protected abstract ProxySource<TestObject> getproxySource();

    @Test
    public void testAccessAfterInvalidate() throws Exception {
        final TestObject obj = pool.borrowObject();
        assertNotNull(obj);

        obj.setData(DATA1);
        assertEquals(DATA1, obj.getData());

        pool.invalidateObject0(obj);

        assertNotNull(obj);

        assertThrows(IllegalStateException.class, obj::getData);
    }

    @Test
    public void testAccessAfterReturn() throws Exception {
        final TestObject obj = pool.borrowObject();
        assertNotNull(obj);

        obj.setData(DATA1);
        assertEquals(DATA1, obj.getData());

        pool.returnObject(obj);

        assertNotNull(obj);

        assertThrows(IllegalStateException.class, obj::getData);
    }

    @Test
    public void testBorrowObject() throws Exception {
        final TestObject obj = pool.borrowObject();
        assertNotNull(obj);

        obj.setData(DATA1);
        assertEquals(DATA1, obj.getData());

        pool.returnObject(obj);
    }

    @Test
    public void testPassThroughMethods01() throws Exception {
        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());

        pool.addObject();

        assertEquals(0, pool.getNumActive());
        assertEquals(1, pool.getNumIdle());

        pool.clear();

        assertEquals(0, pool.getNumActive());
        assertEquals(0, pool.getNumIdle());
    }

    @Test
    public void testPassThroughMethods02() {
        pool.close();

        assertThrows(IllegalStateException.class, () -> pool.addObject());
    }

    @Test
    public void testUsageTracking() throws Exception {
        final TestObject obj = pool.borrowObject();
        assertNotNull(obj);

        obj.setData(DATA1);

        Thread.sleep(ABANDONED_TIMEOUT_SECS.plusSeconds(2).toMillis());

        pool.borrowObject();

        final String logOutput = log.getBuffer().toString();

        assertTrue(logOutput.contains("Pooled object created"));
        assertTrue(logOutput.contains("The last code to use this object was"));
    }
}
