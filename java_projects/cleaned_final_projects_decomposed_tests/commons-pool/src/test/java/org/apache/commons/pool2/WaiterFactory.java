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

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 * Object factory with configurable latencies for object lifecycle methods. This factory will also
 * track and enforce maxActive, maxActivePerKey contracts. If the factory's maxActive /
 * maxActivePerKey are set to match those of the pool, makeObject will throw IllegalStateException
 * if the number of makes - destroys (per key) exceeds the configured max.
 */
public class WaiterFactory<K> {

    /** Latency of activateObject */
    private final long activateLatency;

    /** Latency of destroyObject */
    private final long destroyLatency;

    /** Latency of makeObject */
    private final long makeLatency;

    /** Latency of passivateObject */
    private final long passivateLatency;

    /** Latency of validateObject */
    private final long validateLatency;

    /** Latency of doWait for Waiter instances created by this factory */
    private final long waiterLatency;

    /** Probability that passivation will invalidate Waiter instances */
    private final double passivateInvalidationProbability;

    /** Count of (makes - destroys) since last reset */
    private long activeCount;

    /** Count of (makes - destroys) per key since last reset */
    private final Map<K, Integer> activeCounts = new HashMap<>();

    /** Maximum of (makes - destroys) - if exceeded IllegalStateException */
    private final long maxActive; // GKOP 1.x calls this maxTotal

    /** Maximum of (makes - destroys) per key */
    private final long maxActivePerKey; // GKOP 1.x calls this maxActive

    public WaiterFactory(
            final long activateLatency,
            final long destroyLatency,
            final long makeLatency,
            final long passivateLatency,
            final long validateLatency,
            final long waiterLatency,
            final long maxActive,
            final long maxActivePerKey,
            final double passivateInvalidationProbability) {
        this.activateLatency = activateLatency;
        this.destroyLatency = destroyLatency;
        this.makeLatency = makeLatency;
        this.passivateLatency = passivateLatency;
        this.validateLatency = validateLatency;
        this.waiterLatency = waiterLatency;
        this.maxActive = maxActive;
        this.maxActivePerKey = maxActivePerKey;
        this.passivateInvalidationProbability = passivateInvalidationProbability;
    }

    public static WaiterFactory WaiterFactory1(
            final long activateLatency,
            final long destroyLatency,
            final long makeLatency,
            final long passivateLatency,
            final long validateLatency,
            final long waiterLatency,
            final long maxActive) {
        return new WaiterFactory(
                activateLatency,
                destroyLatency,
                makeLatency,
                passivateLatency,
                validateLatency,
                waiterLatency,
                maxActive,
                Long.MAX_VALUE,
                0);
    }

    public static WaiterFactory WaiterFactory2(
            final long activateLatency,
            final long destroyLatency,
            final long makeLatency,
            final long passivateLatency,
            final long validateLatency,
            final long waiterLatency) {
        return new WaiterFactory(
                activateLatency,
                destroyLatency,
                makeLatency,
                passivateLatency,
                validateLatency,
                waiterLatency,
                Long.MAX_VALUE,
                Long.MAX_VALUE,
                0);
    }

    public void activateObject0(final K key, final PooledObject<Waiter> obj) throws Exception {
        activateObject1(obj);
    }

    public void activateObject1(final PooledObject<Waiter> obj) throws Exception {
        doWait(activateLatency);
        obj.getObject().setActive(true);
    }

    public void destroyObject0(final K key, final PooledObject<Waiter> obj) throws Exception {
        destroyObject1(obj);
        synchronized (this) {
            final Integer count = activeCounts.get(key);
            activeCounts.put(key, Integer.valueOf(count.intValue() - 1));
        }
    }

    public void destroyObject1(final PooledObject<Waiter> obj) throws Exception {
        doWait(destroyLatency);
        obj.getObject().setValid(false);
        obj.getObject().setActive(false);
        synchronized (this) {
            activeCount--;
        }
    }

    protected void doWait(final long latency) {
        if (latency == 0) {
            return;
        }
        Waiter.sleepQuietly(latency);
    }

    /**
     * @return the maxActive
     */
    public synchronized long getMaxActive() {
        return maxActive;
    }

    public void passivateObject0(final K key, final PooledObject<Waiter> obj) throws Exception {
        passivateObject1(obj);
    }

    public void passivateObject1(final PooledObject<Waiter> obj) throws Exception {
        obj.getObject().setActive(false);
        doWait(passivateLatency);
        if (Math.random() < passivateInvalidationProbability) {
            obj.getObject().setValid(false);
        }
    }

    public synchronized void reset() {
        activeCount = 0;
        if (activeCounts.isEmpty()) {
            return;
        }
        final Iterator<K> it = activeCounts.keySet().iterator();
        while (it.hasNext()) {
            final K key = it.next();
            activeCounts.put(key, Integer.valueOf(0));
        }
    }

    public boolean validateObject0(final K key, final PooledObject<Waiter> obj) {
        return validateObject1(obj);
    }

    public boolean validateObject1(final PooledObject<Waiter> obj) {
        doWait(validateLatency);
        return obj.getObject().isValid();
    }

    
}
