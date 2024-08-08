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

import java.util.List;

/** Abstract test case for {@link ObjectPool} implementations. */
public abstract class TestObjectPool {

    private static void clear(
            final MethodCallPoolableObjectFactory factory, final List<MethodCall> expectedMethods) {
        factory.getMethodCalls().clear();
        expectedMethods.clear();
    }

    static void removeDestroyObjectCall(final List<MethodCall> calls) {
        calls.removeIf(call -> "destroyObject".equals(call.getName()));
    }

    private static void reset(
            final ObjectPool<Object> pool,
            final MethodCallPoolableObjectFactory factory,
            final List<MethodCall> expectedMethods)
            throws Exception {
        pool.clear();
        clear(factory, expectedMethods);
        factory.reset();
    }

    private final Integer ZERO = Integer.valueOf(0);

    private final Integer ONE = Integer.valueOf(1);

    /**
     * Create an {@code ObjectPool} with the specified factory. The pool should be in a default
     * configuration and conform to the expected behaviors described in {@link ObjectPool}.
     * Generally speaking there should be no limits on the various object counts.
     *
     * @param factory The factory to be used by the object pool
     * @return the newly created empty pool
     * @throws UnsupportedOperationException if the pool being tested does not follow pool
     *     contracts.
     */
    protected abstract ObjectPool<Object> makeEmptyPool(PooledObjectFactory<Object> factory)
            throws UnsupportedOperationException;

    
}
