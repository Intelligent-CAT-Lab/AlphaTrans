
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

package org.apache.commons.pool2.impl;

import org.apache.commons.pool2.PooledObject;
import org.apache.commons.pool2.PooledObjectState;
import org.apache.commons.pool2.TrackedUse;

import java.io.PrintWriter;
import java.time.Clock;
import java.time.Duration;
import java.time.Instant;

/**
 * This wrapper is used to track the additional information, such as state, for the pooled objects.
 *
 * <p>This class is intended to be thread-safe.
 *
 * @param <T> the type of object in the pool
 * @since 2.0
 */
public class DefaultPooledObject<T> {

    private final T object;
    private PooledObjectState state =
            PooledObjectState.IDLE; // @GuardedBy("this") to ensure transitions are valid
    private final Clock systemClock = Clock.systemUTC();
    private final Instant createInstant = now();

    private volatile Instant lastBorrowInstant = createInstant;
    private volatile Instant lastUseInstant = createInstant;
    private volatile Instant lastReturnInstant = createInstant;
    private volatile boolean logAbandoned;
    private volatile CallStack borrowedBy = NoOpCallStack.INSTANCE;
    private volatile CallStack usedBy = NoOpCallStack.INSTANCE;
    private volatile long borrowedCount;

    /**
     * Creates a new instance that wraps the provided object so that the pool can track the state of
     * the pooled object.
     *
     * @param object The object to wrap
     */
    public DefaultPooledObject(final T object) {
        this.object = object;
    }

    /**
     * Allocates the object.
     *
     * @return {@code true} if the original state was {@link PooledObjectState#IDLE IDLE}
     */
    public synchronized boolean allocate() {
        if (state == PooledObjectState.IDLE) {
            state = PooledObjectState.ALLOCATED;
            lastBorrowInstant = now();
            lastUseInstant = lastBorrowInstant;
            borrowedCount++;
            if (logAbandoned) {
                borrowedBy.fillInStackTrace();
            }
            return true;
        }
        if (state == PooledObjectState.EVICTION) {
            state = PooledObjectState.EVICTION_RETURN_TO_HEAD;
        }
        return false;
    }

    public int compareTo(final PooledObject<T> other) {
        final int compareTo = getLastReturnInstant().compareTo(other.getLastReturnInstant());
        if (compareTo == 0) {
            return System.identityHashCode(this) - System.identityHashCode(other);
        }
        return compareTo;
    }

    /**
     * Deallocates the object and sets it {@link PooledObjectState#IDLE IDLE} if it is currently
     * {@link PooledObjectState#ALLOCATED ALLOCATED} or {@link PooledObjectState#RETURNING
     * RETURNING}.
     *
     * @return {@code true} if the state was {@link PooledObjectState#ALLOCATED ALLOCATED} or {@link
     *     PooledObjectState#RETURNING RETURNING}.
     */
    public synchronized boolean deallocate() {
        if (state == PooledObjectState.ALLOCATED || state == PooledObjectState.RETURNING) {
            state = PooledObjectState.IDLE;
            lastReturnInstant = now();
            borrowedBy.clear();
            return true;
        }

        return false;
    }

    /**
     * Gets the number of times this object has been borrowed.
     *
     * @return The number of times this object has been borrowed.
     * @since 2.1
     */
    public long getBorrowedCount() {
        return borrowedCount;
    }

    public Instant getCreateInstant() {
        return createInstant;
    }

    public long getCreateTime() {
        return createInstant.toEpochMilli();
    }

    public Duration getIdleDuration() {
        final Duration elapsed = Duration.between(lastReturnInstant, now());
        return elapsed.isNegative() ? Duration.ZERO : elapsed;
    }

    public Duration getIdleTime() {
        return getIdleDuration();
    }

    public long getIdleTimeMillis() {
        return getIdleDuration().toMillis();
    }

    public Instant getLastBorrowInstant() {
        return lastBorrowInstant;
    }

    public long getLastBorrowTime() {
        return lastBorrowInstant.toEpochMilli();
    }

    public Instant getLastReturnInstant() {
        return lastReturnInstant;
    }

    public long getLastReturnTime() {
        return lastReturnInstant.toEpochMilli();
    }

    /**
     * Gets an estimate of the last time this object was used. If the class of the pooled object
     * implements {@link TrackedUse}, what is returned is the maximum of {@link
     * TrackedUse#getLastUsedInstant()} and {@link #getLastBorrowTime()}; otherwise this method
     * gives the same value as {@link #getLastBorrowTime()}.
     *
     * @return the last Instant this object was used.
     */
    public Instant getLastUsedInstant() {
        if (object instanceof TrackedUse) {
            return PoolImplUtils.max(((TrackedUse) object).getLastUsedInstant(), lastUseInstant);
        }
        return lastUseInstant;
    }

    /**
     * Gets an estimate of the last time this object was used. If the class of the pooled object
     * implements {@link TrackedUse}, what is returned is the maximum of {@link
     * TrackedUse#getLastUsedInstant()} and {@link #getLastBorrowTime()}; otherwise this method
     * gives the same value as {@link #getLastBorrowTime()}.
     *
     * @return the last time this object was used
     */
    public long getLastUsedTime() {
        return getLastUsedInstant().toEpochMilli();
    }

    public T getObject() {
        return object;
    }

    /**
     * Gets the state of this object.
     *
     * @return state
     */
    public synchronized PooledObjectState getState() {
        return state;
    }

    /** Sets the state to {@link PooledObjectState#INVALID INVALID}. */
    public synchronized void invalidate() {
        state = PooledObjectState.INVALID;
    }

    /** Marks the pooled object as {@link PooledObjectState#ABANDONED ABANDONED}. */
    public synchronized void markAbandoned() {
        state = PooledObjectState.ABANDONED;
    }

    /** Marks the pooled object as {@link PooledObjectState#RETURNING RETURNING}. */
    public synchronized void markReturning() {
        state = PooledObjectState.RETURNING;
    }

    /**
     * Gets the current instant of the clock.
     *
     * @return the current instant of the clock.
     */
    private Instant now() {
        return systemClock.instant();
    }

    public void printStackTrace(final PrintWriter writer) {
        boolean written = borrowedBy.printStackTrace(writer);
        written |= usedBy.printStackTrace(writer);
        if (written) {
            writer.flush();
        }
    }

    public void setLogAbandoned(final boolean logAbandoned) {
        this.logAbandoned = logAbandoned;
    }

    /**
     * Configures the stack trace generation strategy based on whether or not fully detailed stack
     * traces are required. When set to false, abandoned logs may only include caller class
     * information rather than method names, line numbers, and other normal metadata available in a
     * full stack trace.
     *
     * @param requireFullStackTrace the new configuration setting for abandoned object logging
     * @since 2.5
     */
    public synchronized boolean startEvictionTest() {
        if (state == PooledObjectState.IDLE) {
            state = PooledObjectState.EVICTION;
            return true;
        }
        return false;
    }

    public String toString() {
        final StringBuilder result = new StringBuilder();
        result.append("Object: ");
        result.append(object.toString());
        result.append(", State: ");
        synchronized (this) {
            result.append(state.toString());
        }
        return result.toString();
    }

    public void use() {
        lastUseInstant = now();
        usedBy.fillInStackTrace();
    }
}
