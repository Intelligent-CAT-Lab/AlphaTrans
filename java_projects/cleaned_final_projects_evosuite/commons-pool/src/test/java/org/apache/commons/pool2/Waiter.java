
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

import java.util.concurrent.atomic.AtomicInteger;

/**
 * Object created by {@link WaiterFactory}. Maintains active / valid state, last passivated and idle
 * times. Waits with configurable latency when {@link #doWait()} method is called.
 *
 * <p>This class is *not* threadsafe.
 */
public class Waiter {
    private static final AtomicInteger instanceCount = new AtomicInteger();
    private boolean active;
    private boolean valid;
    private long latency;
    private long lastPassivatedMillis;
    private long lastIdleTimeMillis;
    private long passivationCount;
    private long validationCount;
    private final int id = instanceCount.getAndIncrement();

    public Waiter(final boolean active, final boolean valid, final long latency) {
        this.active = active;
        this.valid = valid;
        this.latency = latency;
        this.lastPassivatedMillis = System.currentTimeMillis();
    }

    /** Wait for {@link #getLatency()} milliseconds. */
    public void doWait() {
        sleepQuietly(latency);
    }

    @Override
    public boolean equals(final Object obj) {
        if (!(obj instanceof Waiter)) {
            return false;
        }
        return obj.hashCode() == id;
    }

    /**
     * Returns the last idle time for this instance in ms.
     *
     * <p>When an instance is created, and each subsequent time it is passivated, the {@link
     * #getLastPassivatedMillis() lastPassivated} property is updated with the current time. When
     * the next activation occurs, {@code lastIdleTime} is updated with the elapsed time since
     * passivation.
     *
     * <p>
     *
     * @return last idle time
     */
    public long getLastIdleTimeMillis() {
        return lastIdleTimeMillis;
    }

    /**
     * Returns the system time of this instance's last passivation.
     *
     * <p>When an instance is created, this field is initialized to the system time.
     *
     * @return time of last passivation
     */
    public long getLastPassivatedMillis() {
        return lastPassivatedMillis;
    }

    public long getLatency() {
        return latency;
    }

    /**
     * @return how many times this instance has been passivated
     */
    public long getPassivationCount() {
        return passivationCount;
    }

    /**
     * @return how many times this instance has been validated
     */
    public long getValidationCount() {
        return validationCount;
    }

    @Override
    public int hashCode() {
        return id;
    }

    /**
     * Whether or not the instance is active.
     *
     * @return true if the last lifecycle event for this instance was activation.
     */
    public boolean isActive() {
        return active;
    }

    public boolean isValid() {
        validationCount++;
        return valid;
    }

    /**
     * Sets the active state and updates {@link #getLastIdleTimeMillis() lastIdleTime} or {@link
     * #getLastPassivatedMillis() lastPassivated} as appropriate.
     *
     * <p>If the active state is changing from inactive to active, lastIdleTime is updated with the
     * current time minus lastPassivated. If the state is changing from active to inactive,
     * lastPassivated is updated with the current time.
     *
     * <p>{@link WaiterFactory#activateObject(PooledObject)} and {@link
     * WaiterFactory#passivateObject(PooledObject)} invoke this method on their actual parameter,
     * passing {@code true} and {@code false}, respectively.
     *
     * @param active new active state
     */
    public void setActive(final boolean active) {
        final boolean activeState = this.active;
        if (activeState == active) {
            return;
        }
        this.active = active;
        final long currentTimeMillis = System.currentTimeMillis();
        if (active) { // activating
            lastIdleTimeMillis = currentTimeMillis - lastPassivatedMillis;
        } else { // passivating
            lastPassivatedMillis = currentTimeMillis;
            passivationCount++;
        }
    }

    public void setLatency(final long latency) {
        this.latency = latency;
    }

    public void setValid(final boolean valid) {
        this.valid = valid;
    }

    @Override
    public String toString() {
        final StringBuilder buff = new StringBuilder();
        buff.append("ID = " + id + '\n');
        buff.append("valid = " + valid + '\n');
        buff.append("active = " + active + '\n');
        buff.append("lastPassivated = " + lastPassivatedMillis + '\n');
        buff.append("lastIdleTimeMs = " + lastIdleTimeMillis + '\n');
        buff.append("latency = " + latency + '\n');
        return buff.toString();
    }

    /** TODO Reuse Apache Commons Lang ThreadUtils */
    public static void sleepQuietly(final long millis) {
        try {
            Thread.sleep(millis);
        } catch (final InterruptedException e) {
        }
    }
}
