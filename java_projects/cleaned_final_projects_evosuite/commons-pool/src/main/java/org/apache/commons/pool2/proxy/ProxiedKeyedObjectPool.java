
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

import org.apache.commons.pool2.KeyedObjectPool;
import org.apache.commons.pool2.UsageTracking;

import java.util.NoSuchElementException;

/**
 * Create a new keyed object pool where the pooled objects are wrapped in proxies allowing better
 * control of pooled objects and in particular the prevention of the continued use of an object by a
 * client after that client returns the object to the pool.
 *
 * @param <K> type of the key
 * @param <V> type of the pooled object
 * @since 2.0
 */
public class ProxiedKeyedObjectPool<K, V> implements KeyedObjectPool<K, V> {

    private final KeyedObjectPool<K, V> pool;
    private final ProxySource<V> proxySource;

    /**
     * Constructs a new proxied object pool.
     *
     * @param pool The object pool to wrap
     * @param proxySource The source of the proxy objects
     */
    public ProxiedKeyedObjectPool(
            final KeyedObjectPool<K, V> pool, final ProxySource<V> proxySource) {
        this.pool = pool;
        this.proxySource = proxySource;
    }

    @Override
    public void addObject(final K key)
            throws Exception, IllegalStateException, UnsupportedOperationException {
        pool.addObject(key);
    }

    @SuppressWarnings("unchecked")
    @Override
    public V borrowObject(final K key)
            throws Exception, NoSuchElementException, IllegalStateException {
        UsageTracking<V> usageTracking = null;
        if (pool instanceof UsageTracking) {
            usageTracking = (UsageTracking<V>) pool;
        }
        return proxySource.createProxy(pool.borrowObject(key), usageTracking);
    }

    public void clear0() throws Exception, UnsupportedOperationException {
        pool.clear0();
    }

    public void clear1(final K key) throws Exception, UnsupportedOperationException {
        pool.clear1(key);
    }

    @Override
    public void close() {
        pool.close();
    }

    public int getNumActive0() {
        return pool.getNumActive0();
    }

    public int getNumActive1(final K key) {
        return pool.getNumActive1(key);
    }

    public int getNumIdle0() {
        return pool.getNumIdle0();
    }

    public int getNumIdle1(final K key) {
        return pool.getNumIdle1(key);
    }

    @Override
    public void invalidateObject0(final K key, final V proxy) throws Exception {
        pool.invalidateObject0(key, proxySource.resolveProxy(proxy));
    }

    @Override
    public void returnObject(final K key, final V proxy) throws Exception {
        pool.returnObject(key, proxySource.resolveProxy(proxy));
    }

    /**
     * @since 2.4.3
     */
    @Override
    public String toString() {
        final StringBuilder builder = new StringBuilder();
        builder.append("ProxiedKeyedObjectPool [pool=");
        builder.append(pool);
        builder.append(", proxySource=");
        builder.append(proxySource);
        builder.append("]");
        return builder.toString();
    }
}
