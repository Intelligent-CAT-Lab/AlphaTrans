
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

import org.apache.commons.pool2.BaseObject;
import org.apache.commons.pool2.PooledObject;
import org.apache.commons.pool2.PooledObjectState;
import org.apache.commons.pool2.SwallowedExceptionListener;

import java.io.PrintWriter;
import java.io.StringWriter;
import java.io.Writer;
import java.lang.reflect.InvocationTargetException;
import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.TimerTask;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.atomic.AtomicReference;
import java.util.stream.Collectors;

/**
 * Base class that provides common functionality for {@link GenericObjectPool} and {@link
 * GenericKeyedObjectPool}. The primary reason this class exists is reduce code duplication between
 * the two pool implementations.
 *
 * @param <T> Type of element pooled in this pool.
 *     <p>This class is intended to be thread-safe.
 * @since 2.0
 */
public abstract class BaseGenericObjectPool<T> extends BaseObject {

    /** The idle object eviction iterator. Holds a reference to the idle objects. */
    class EvictionIterator implements Iterator<PooledObject<T>> {

        private final Deque<PooledObject<T>> idleObjects;
        private final Iterator<PooledObject<T>> idleObjectIterator;

        /**
         * Constructs an EvictionIterator for the provided idle instance deque.
         *
         * @param idleObjects underlying deque.
         */
        EvictionIterator(final Deque<PooledObject<T>> idleObjects) {
            this.idleObjects = idleObjects;

            if (getLifo()) {
                idleObjectIterator = idleObjects.descendingIterator();
            } else {
                idleObjectIterator = idleObjects.iterator();
            }
        }

        /**
         * Gets the idle object deque referenced by this iterator.
         *
         * @return the idle object deque
         */
        public Deque<PooledObject<T>> getIdleObjects() {
            return idleObjects;
        }

        /** {@inheritDoc} */
        @Override
        public boolean hasNext() {
            return idleObjectIterator.hasNext();
        }

        /** {@inheritDoc} */
        @Override
        public PooledObject<T> next() {
            return idleObjectIterator.next();
        }

        /** {@inheritDoc} */
        @Override
        public void remove() {
            idleObjectIterator.remove();
        }
    }

    /**
     * The idle object evictor {@link TimerTask}.
     *
     * @see GenericKeyedObjectPool#setTimeBetweenEvictionRunsMillis
     */
    class Evictor {

        private ScheduledFuture<?> scheduledFuture;

        /** Cancels the scheduled future. */
        void cancel() {
            scheduledFuture.cancel(false);
        }

        /**
         * Run pool maintenance. Evict objects qualifying for eviction and then ensure that the
         * minimum number of idle instances are available. Since the Timer that invokes Evictors is
         * shared for all Pools but pools may exist in different class loaders, the Evictor ensures
         * that any actions taken are under the class loader of the factory associated with the
         * pool.
         */

        /**
         * Sets the scheduled future.
         *
         * @param scheduledFuture the scheduled future.
         */
        void setScheduledFuture(final ScheduledFuture<?> scheduledFuture) {
            this.scheduledFuture = scheduledFuture;
        }
    }

    /**
     * Wrapper for objects under management by the pool.
     *
     * <p>GenericObjectPool and GenericKeyedObjectPool maintain references to all objects under
     * management using maps keyed on the objects. This wrapper class ensures that objects can work
     * as hash keys.
     *
     * @param <T> type of objects in the pool
     */
    static class IdentityWrapper<T> {
        /** Wrapped object */
        private final T instance;

        /**
         * Constructs a wrapper for an instance.
         *
         * @param instance object to wrap
         */
        public IdentityWrapper(final T instance) {
            this.instance = instance;
        }

        @Override
        @SuppressWarnings("rawtypes")
        public boolean equals(final Object other) {
            return other instanceof IdentityWrapper
                    && ((IdentityWrapper) other).instance == instance;
        }

        /**
         * @return the wrapped object
         */
        public T getObject() {
            return instance;
        }

        @Override
        public int hashCode() {
            return System.identityHashCode(instance);
        }

        @Override
        public String toString() {
            final StringBuilder builder = new StringBuilder();
            builder.append("IdentityWrapper [instance=");
            builder.append(instance);
            builder.append("]");
            return builder.toString();
        }
    }

    /**
     * Maintains a cache of values for a single metric and reports statistics on the cached values.
     */
    private class StatsStore {

        private static final int NULL = -1;
        private final AtomicLong[] values;
        private final int size;
        private int index;

        /**
         * Constructs a StatsStore with the given cache size.
         *
         * @param size number of values to maintain in the cache.
         */
        StatsStore(final int size) {
            this.size = size;
            values = new AtomicLong[size];
            for (int i = 0; i < size; i++) {
                values[i] = new AtomicLong(NULL);
            }
        }

        void add0(final Duration value) {
            add1(value.toMillis());
        }

        /**
         * Adds a value to the cache. If the cache is full, one of the existing values is replaced
         * by the new value.
         *
         * @param value new value to add to the cache.
         */
        synchronized void add1(final long value) {
            values[index].set(value);
            index++;
            if (index == size) {
                index = 0;
            }
        }

        /**
         * Gets the current values as a List.
         *
         * @return the current values as a List.
         */
        synchronized List<AtomicLong> getCurrentValues() {
            return Arrays.stream(values, 0, index).collect(Collectors.toList());
        }

        /**
         * Gets the mean of the cached values.
         *
         * @return the mean of the cache, truncated to long
         */
        public long getMean() {
            double result = 0;
            int counter = 0;
            for (int i = 0; i < size; i++) {
                final long value = values[i].get();
                if (value != NULL) {
                    counter++;
                    result = result * ((counter - 1) / (double) counter) + value / (double) counter;
                }
            }
            return (long) result;
        }

        @Override
        public String toString() {
            final StringBuilder builder = new StringBuilder();
            builder.append("StatsStore [");
            builder.append(getCurrentValues());
            builder.append("], size=");
            builder.append(size);
            builder.append(", index=");
            builder.append(index);
            builder.append("]");
            return builder.toString();
        }
    }

    /**
     * The size of the caches used to store historical data for some attributes so that rolling
     * means may be calculated.
     */
    public static final int MEAN_TIMING_STATS_CACHE_SIZE = 100;

    private static final String EVICTION_POLICY_TYPE_NAME = EvictionPolicy.class.getName();
    private static final Duration DEFAULT_REMOVE_ABANDONED_TIMEOUT =
            Duration.ofSeconds(Integer.MAX_VALUE);
    private volatile int maxTotal = GenericKeyedObjectPoolConfig.DEFAULT_MAX_TOTAL;
    private volatile boolean blockWhenExhausted = BaseObjectPoolConfig.DEFAULT_BLOCK_WHEN_EXHAUSTED;
    private volatile Duration maxWaitDuration = BaseObjectPoolConfig.DEFAULT_MAX_WAIT;
    private volatile boolean lifo = BaseObjectPoolConfig.DEFAULT_LIFO;
    private volatile boolean testOnCreate = BaseObjectPoolConfig.DEFAULT_TEST_ON_CREATE;
    private volatile boolean testOnBorrow = BaseObjectPoolConfig.DEFAULT_TEST_ON_BORROW;
    private volatile boolean testOnReturn = BaseObjectPoolConfig.DEFAULT_TEST_ON_RETURN;
    private volatile boolean testWhileIdle = BaseObjectPoolConfig.DEFAULT_TEST_WHILE_IDLE;
    private volatile Duration durationBetweenEvictionRuns =
            BaseObjectPoolConfig.DEFAULT_TIME_BETWEEN_EVICTION_RUNS;
    private volatile int numTestsPerEvictionRun =
            BaseObjectPoolConfig.DEFAULT_NUM_TESTS_PER_EVICTION_RUN;

    private volatile Duration minEvictableIdleDuration =
            BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION;
    private volatile Duration softMinEvictableIdleDuration =
            BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION;
    private volatile EvictionPolicy<T> evictionPolicy;
    private volatile Duration evictorShutdownTimeoutDuration =
            BaseObjectPoolConfig.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT;
    final Object closeLock = new Object();
    volatile boolean closed;

    final Object evictionLock = new Object();
    private Evictor evictor; // @GuardedBy("evictionLock")
    EvictionIterator evictionIterator; // @GuardedBy("evictionLock")

    /**
     * Class loader for evictor thread to use since, in a JavaEE or similar environment, the context
     * class loader for the evictor thread may not have visibility of the correct factory. See
     * POOL-161. Uses a weak reference to avoid potential memory leaks if the Pool is discarded
     * rather than closed.
     */
    private final AtomicLong borrowedCount = new AtomicLong();

    private final AtomicLong returnedCount = new AtomicLong();
    final AtomicLong createdCount = new AtomicLong();
    final AtomicLong destroyedCount = new AtomicLong();
    final AtomicLong destroyedByEvictorCount = new AtomicLong();
    final AtomicLong destroyedByBorrowValidationCount = new AtomicLong();

    private final StatsStore activeTimes = new StatsStore(MEAN_TIMING_STATS_CACHE_SIZE);
    private final StatsStore idleTimes = new StatsStore(MEAN_TIMING_STATS_CACHE_SIZE);
    private final StatsStore waitTimes = new StatsStore(MEAN_TIMING_STATS_CACHE_SIZE);

    private final AtomicReference<Duration> maxBorrowWaitDuration =
            new AtomicReference<>(Duration.ZERO);

    private volatile SwallowedExceptionListener swallowedExceptionListener;
    private volatile boolean messageStatistics;

    /** Additional configuration properties for abandoned object tracking. */
    protected volatile AbandonedConfig abandonedConfig;

    /**
     * Handles JMX registration (if required) and the initialization required for monitoring.
     *
     * @param config Pool configuration
     * @param jmxNameBase The default base JMX name for the new pool unless overridden by the config
     * @param jmxNamePrefix Prefix to be used for JMX name for the new pool
     */

    /**
     * Appends statistics if enabled.
     *
     * <p>Statistics may not accurately reflect snapshot state at the time of the exception because
     * we do not want to lock the pool when gathering this information.
     *
     * @param string The root string.
     * @return The root string plus statistics.
     */

    /**
     * Verifies that the pool is open.
     *
     * @throws IllegalStateException if the pool is closed.
     */
    final void assertOpen() throws IllegalStateException {
        if (isClosed()) {
            throw new IllegalStateException("Pool not open");
        }
    }

    /**
     * Closes the pool, destroys the remaining idle objects and, if registered in JMX, deregisters
     * it.
     */
    public abstract void close();

    /**
     * Creates a list of pooled objects to remove based on their state.
     *
     * @param abandonedConfig The abandoned configuration.
     * @param allObjects PooledObject instances to consider.
     * @return a list of pooled objects to remove based on their state.
     */
    ArrayList<PooledObject<T>> createRemoveList(
            final AbandonedConfig abandonedConfig,
            final Map<IdentityWrapper<T>, PooledObject<T>> allObjects) {
        final Instant timeout =
                Instant.now().minus(abandonedConfig.getRemoveAbandonedTimeoutDuration());
        final ArrayList<PooledObject<T>> remove = new ArrayList<>();
        allObjects
                .values()
                .forEach(
                        pooledObject -> {
                            synchronized (pooledObject) {
                                if (pooledObject.getState() == PooledObjectState.ALLOCATED
                                        && pooledObject.getLastUsedInstant().compareTo(timeout)
                                                <= 0) {
                                    pooledObject.markAbandoned();
                                    remove.add(pooledObject);
                                }
                            }
                        });
        return remove;
    }

    /**
     * Tries to ensure that the configured minimum number of idle instances are available in the
     * pool.
     *
     * @throws Exception if an error occurs creating idle instances
     */
    abstract void ensureMinIdle() throws Exception;

    /**
     * Perform {@code numTests} idle object eviction tests, evicting examined objects that meet the
     * criteria for eviction. If {@code testWhileIdle} is true, examined objects are validated when
     * visited (and removed if invalid); otherwise only objects that have been idle for more than
     * {@code minEvicableIdleTimeMillis} are removed.
     *
     * @throws Exception when there is a problem evicting idle objects.
     */
    public abstract void evict() throws Exception;

    /**
     * Gets whether to block when the {@code borrowObject()} method is invoked when the pool is
     * exhausted (the maximum number of "active" objects has been reached).
     *
     * @return {@code true} if {@code borrowObject()} should block when the pool is exhausted
     * @see #setBlockWhenExhausted
     */
    public final boolean getBlockWhenExhausted() {
        return blockWhenExhausted;
    }

    /**
     * The total number of objects successfully borrowed from this pool over the lifetime of the
     * pool.
     *
     * @return the borrowed object count
     */
    public final long getBorrowedCount() {
        return borrowedCount.get();
    }

    /**
     * The total number of objects created for this pool over the lifetime of the pool.
     *
     * @return the created object count
     */
    public final long getCreatedCount() {
        return createdCount.get();
    }

    /**
     * Provides the stack trace for the call that created this pool. JMX registration may trigger a
     * memory leak so it is important that pools are deregistered when no longer used by calling the
     * {@link #close()} method. This method is provided to assist with identifying code that creates
     * but does not close it thereby creating a memory leak.
     *
     * @return pool creation stack trace
     */

    /**
     * The total number of objects destroyed by this pool as a result of failing validation during
     * {@code borrowObject()} over the lifetime of the pool.
     *
     * @return validation destroyed object count
     */
    public final long getDestroyedByBorrowValidationCount() {
        return destroyedByBorrowValidationCount.get();
    }

    /**
     * The total number of objects destroyed by the evictor associated with this pool over the
     * lifetime of the pool.
     *
     * @return the evictor destroyed object count
     */
    public final long getDestroyedByEvictorCount() {
        return destroyedByEvictorCount.get();
    }

    /**
     * The total number of objects destroyed by this pool over the lifetime of the pool.
     *
     * @return the destroyed object count
     */
    public final long getDestroyedCount() {
        return destroyedCount.get();
    }

    /**
     * Gets the {@link EvictionPolicy} defined for this pool.
     *
     * @return the eviction policy
     * @since 2.4
     * @since 2.6.0 Changed access from protected to public.
     */
    public EvictionPolicy<T> getEvictionPolicy() {
        return evictionPolicy;
    }

    /**
     * Gets the name of the {@link EvictionPolicy} implementation that is used by this pool.
     *
     * @return The fully qualified class name of the {@link EvictionPolicy}
     * @see #setEvictionPolicyClassName(String)
     */
    public final String getEvictionPolicyClassName() {
        return evictionPolicy.getClass().getName();
    }

    /**
     * Gets the timeout that will be used when waiting for the Evictor to shutdown if this pool is
     * closed and it is the only pool still using the the value for the Evictor.
     *
     * @return The timeout that will be used while waiting for the Evictor to shut down.
     * @since 2.10.0
     * @deprecated Use {@link #getEvictorShutdownTimeoutDuration()}.
     */
    @Deprecated
    public final Duration getEvictorShutdownTimeout() {
        return evictorShutdownTimeoutDuration;
    }

    /**
     * Gets the timeout that will be used when waiting for the Evictor to shutdown if this pool is
     * closed and it is the only pool still using the the value for the Evictor.
     *
     * @return The timeout that will be used while waiting for the Evictor to shut down.
     * @since 2.11.0
     */
    public final Duration getEvictorShutdownTimeoutDuration() {
        return evictorShutdownTimeoutDuration;
    }

    /**
     * Gets the timeout that will be used when waiting for the Evictor to shutdown if this pool is
     * closed and it is the only pool still using the the value for the Evictor.
     *
     * @return The timeout in milliseconds that will be used while waiting for the Evictor to shut
     *     down.
     * @deprecated Use {@link #getEvictorShutdownTimeoutDuration()}.
     */
    @Deprecated
    public final long getEvictorShutdownTimeoutMillis() {
        return evictorShutdownTimeoutDuration.toMillis();
    }

    /**
     * Gets whether or not the pool serves threads waiting to borrow objects fairly. True means that
     * waiting threads are served as if waiting in a FIFO queue.
     *
     * @return {@code true} if waiting threads are to be served by the pool in arrival order
     */

    /**
     * Provides the name under which the pool has been registered with the platform MBean server or
     * {@code null} if the pool has not been registered.
     *
     * @return the JMX name
     */

    /**
     * Gets whether the pool has LIFO (last in, first out) behavior with respect to idle objects -
     * always returning the most recently used object from the pool, or as a FIFO (first in, first
     * out) queue, where the pool always returns the oldest object in the idle object pool.
     *
     * @return {@code true} if the pool is configured with LIFO behavior or {@code false} if the
     *     pool is configured with FIFO behavior
     * @see #setLifo
     */
    public final boolean getLifo() {
        return lifo;
    }

    /**
     * Gets whether this pool identifies and logs any abandoned objects.
     *
     * @return {@code true} if abandoned object removal is configured for this pool and removal
     *     events are to be logged otherwise {@code false}
     * @see AbandonedConfig#getLogAbandoned()
     * @since 2.11.0
     */
    public boolean getLogAbandoned() {
        final AbandonedConfig ac = this.abandonedConfig;
        return ac != null && ac.getLogAbandoned();
    }

    /**
     * Gets the maximum time a thread has waited to borrow objects from the pool.
     *
     * @return maximum wait time in milliseconds since the pool was created
     */
    public final long getMaxBorrowWaitTimeMillis() {
        return maxBorrowWaitDuration.get().toMillis();
    }

    /**
     * Gets the maximum number of objects that can be allocated by the pool (checked out to clients,
     * or idle awaiting checkout) at a given time. When negative, there is no limit to the number of
     * objects that can be managed by the pool at one time.
     *
     * @return the cap on the total number of object instances managed by the pool.
     * @see #setMaxTotal
     */
    public final int getMaxTotal() {
        return maxTotal;
    }

    /**
     * Gets the maximum duration the {@code borrowObject()} method should block before throwing an
     * exception when the pool is exhausted and {@link #getBlockWhenExhausted} is true. When less
     * than 0, the {@code borrowObject()} method may block indefinitely.
     *
     * @return the maximum number of milliseconds {@code borrowObject()} will block.
     * @see #setMaxWait
     * @see #setBlockWhenExhausted
     * @since 2.11.0
     */
    public final Duration getMaxWaitDuration() {
        return maxWaitDuration;
    }

    /**
     * Gets the maximum amount of time (in milliseconds) the {@code borrowObject()} method should
     * block before throwing an exception when the pool is exhausted and {@link
     * #getBlockWhenExhausted} is true. When less than 0, the {@code borrowObject()} method may
     * block indefinitely.
     *
     * @return the maximum number of milliseconds {@code borrowObject()} will block.
     * @see #setMaxWait
     * @see #setBlockWhenExhausted
     * @deprecated Use {@link #getMaxWaitDuration()}.
     */
    @Deprecated
    public final long getMaxWaitMillis() {
        return maxWaitDuration.toMillis();
    }

    /**
     * The mean time objects are active for based on the last {@link #MEAN_TIMING_STATS_CACHE_SIZE}
     * objects returned to the pool.
     *
     * @return mean time an object has been checked out from the pool among recently returned
     *     objects
     */
    public final long getMeanActiveTimeMillis() {
        return activeTimes.getMean();
    }

    /**
     * The mean time threads wait to borrow an object based on the last {@link
     * #MEAN_TIMING_STATS_CACHE_SIZE} objects borrowed from the pool.
     *
     * @return mean time in milliseconds that a recently served thread has had to wait to borrow an
     *     object from the pool
     */
    public final long getMeanBorrowWaitTimeMillis() {
        return waitTimes.getMean();
    }

    /**
     * The mean time objects are idle for based on the last {@link #MEAN_TIMING_STATS_CACHE_SIZE}
     * objects borrowed from the pool.
     *
     * @return mean time an object has been idle in the pool among recently borrowed objects
     */
    public final long getMeanIdleTimeMillis() {
        return idleTimes.getMean();
    }

    /**
     * Gets whether to include statistics in exception messages.
     *
     * <p>Statistics may not accurately reflect snapshot state at the time of the exception because
     * we do not want to lock the pool when gathering this information.
     *
     * @return whether to include statistics in exception messages.
     * @since 2.11.0
     */
    public boolean getMessageStatistics() {
        return messageStatistics;
    }

    /**
     * Gets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRuns(Duration)}). When non-positive, no objects will be evicted from
     * the pool due to idle time alone.
     *
     * @return minimum amount of time an object may sit idle in the pool before it is eligible for
     *     eviction
     * @see #setMinEvictableIdleTimeMillis
     * @see #setTimeBetweenEvictionRunsMillis
     * @since 2.11.0
     */
    public final Duration getMinEvictableIdleDuration() {
        return minEvictableIdleDuration;
    }

    /**
     * Gets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRuns(Duration)}). When non-positive, no objects will be evicted from
     * the pool due to idle time alone.
     *
     * @return minimum amount of time an object may sit idle in the pool before it is eligible for
     *     eviction
     * @see #setMinEvictableIdleTimeMillis
     * @see #setTimeBetweenEvictionRunsMillis
     * @since 2.10.0
     * @deprecated Use {@link #getMinEvictableIdleDuration()}.
     */
    @Deprecated
    public final Duration getMinEvictableIdleTime() {
        return minEvictableIdleDuration;
    }

    /**
     * Gets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRunsMillis(long)}). When non-positive, no objects will be evicted from
     * the pool due to idle time alone.
     *
     * @return minimum amount of time an object may sit idle in the pool before it is eligible for
     *     eviction
     * @see #setMinEvictableIdleTimeMillis
     * @see #setTimeBetweenEvictionRunsMillis
     * @deprecated Use {@link #getMinEvictableIdleDuration()}.
     */
    @Deprecated
    public final long getMinEvictableIdleTimeMillis() {
        return minEvictableIdleDuration.toMillis();
    }

    /**
     * The number of instances currently idle in this pool.
     *
     * @return count of instances available for checkout from the pool
     */
    public abstract int getNumIdle();

    /**
     * Gets the maximum number of objects to examine during each run (if any) of the idle object
     * evictor thread. When positive, the number of tests performed for a run will be the minimum of
     * the configured value and the number of idle instances in the pool. When negative, the number
     * of tests performed will be <code>ceil({@link #getNumIdle}/
     * abs({@link #getNumTestsPerEvictionRun}))</code> which means that when the value is {@code -n}
     * roughly one nth of the idle objects will be tested per run.
     *
     * @return max number of objects to examine during each evictor run
     * @see #setNumTestsPerEvictionRun
     * @see #setTimeBetweenEvictionRunsMillis
     */
    public final int getNumTestsPerEvictionRun() {
        return numTestsPerEvictionRun;
    }

    /**
     * Gets whether a check is made for abandoned objects when an object is borrowed from this pool.
     *
     * @return {@code true} if abandoned object removal is configured to be activated by
     *     borrowObject otherwise {@code false}
     * @see AbandonedConfig#getRemoveAbandonedOnBorrow()
     * @since 2.11.0
     */
    public boolean getRemoveAbandonedOnBorrow() {
        final AbandonedConfig ac = this.abandonedConfig;
        return ac != null && ac.getRemoveAbandonedOnBorrow();
    }

    /**
     * Gets whether a check is made for abandoned objects when the evictor runs.
     *
     * @return {@code true} if abandoned object removal is configured to be activated when the
     *     evictor runs otherwise {@code false}
     * @see AbandonedConfig#getRemoveAbandonedOnMaintenance()
     * @since 2.11.0
     */
    public boolean getRemoveAbandonedOnMaintenance() {
        final AbandonedConfig ac = this.abandonedConfig;
        return ac != null && ac.getRemoveAbandonedOnMaintenance();
    }

    /**
     * Gets the timeout before which an object will be considered to be abandoned by this pool.
     *
     * @return The abandoned object timeout in seconds if abandoned object removal is configured for
     *     this pool; Integer.MAX_VALUE otherwise.
     * @see AbandonedConfig#getRemoveAbandonedTimeoutDuration()
     * @see AbandonedConfig#getRemoveAbandonedTimeoutDuration()
     * @deprecated Use {@link #getRemoveAbandonedTimeoutDuration()}.
     * @since 2.11.0
     */
    @Deprecated
    public int getRemoveAbandonedTimeout() {
        return (int) getRemoveAbandonedTimeoutDuration().getSeconds();
    }

    /**
     * Gets the timeout before which an object will be considered to be abandoned by this pool.
     *
     * @return The abandoned object timeout in seconds if abandoned object removal is configured for
     *     this pool; Integer.MAX_VALUE otherwise.
     * @see AbandonedConfig#getRemoveAbandonedTimeoutDuration()
     * @since 2.11.0
     */
    public Duration getRemoveAbandonedTimeoutDuration() {
        final AbandonedConfig ac = this.abandonedConfig;
        return ac != null
                ? ac.getRemoveAbandonedTimeoutDuration()
                : DEFAULT_REMOVE_ABANDONED_TIMEOUT;
    }

    /**
     * The total number of objects returned to this pool over the lifetime of the pool. This
     * excludes attempts to return the same object multiple times.
     *
     * @return the returned object count
     */
    public final long getReturnedCount() {
        return returnedCount.get();
    }

    /**
     * Gets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRuns(Duration)}), with the extra condition that at least {@code
     * minIdle} object instances remain in the pool. This setting is overridden by {@link
     * #getMinEvictableIdleTime} (that is, if {@link #getMinEvictableIdleTime} is positive, then
     * {@link #getSoftMinEvictableIdleTime} is ignored).
     *
     * @return minimum amount of time an object may sit idle in the pool before it is eligible for
     *     eviction if minIdle instances are available
     * @see #setSoftMinEvictableIdle(Duration)
     * @since 2.11.0
     */
    public final Duration getSoftMinEvictableIdleDuration() {
        return softMinEvictableIdleDuration;
    }

    /**
     * Gets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRuns(Duration)}), with the extra condition that at least {@code
     * minIdle} object instances remain in the pool. This setting is overridden by {@link
     * #getMinEvictableIdleTime} (that is, if {@link #getMinEvictableIdleTime} is positive, then
     * {@link #getSoftMinEvictableIdleTime} is ignored).
     *
     * @return minimum amount of time an object may sit idle in the pool before it is eligible for
     *     eviction if minIdle instances are available
     * @see #setSoftMinEvictableIdle(Duration)
     * @since 2.10.0
     * @deprecated Use {@link #getSoftMinEvictableIdleDuration}.
     */
    @Deprecated
    public final Duration getSoftMinEvictableIdleTime() {
        return softMinEvictableIdleDuration;
    }

    /**
     * Gets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRunsMillis(long)}), with the extra condition that at least {@code
     * minIdle} object instances remain in the pool. This setting is overridden by {@link
     * #getMinEvictableIdleTimeMillis} (that is, if {@link #getMinEvictableIdleTimeMillis} is
     * positive, then {@link #getSoftMinEvictableIdleTimeMillis} is ignored).
     *
     * @return minimum amount of time an object may sit idle in the pool before it is eligible for
     *     eviction if minIdle instances are available
     * @see #setSoftMinEvictableIdleTimeMillis
     * @deprecated Use {@link #getSoftMinEvictableIdleTime()}.
     */
    @Deprecated
    public final long getSoftMinEvictableIdleTimeMillis() {
        return softMinEvictableIdleDuration.toMillis();
    }

    /**
     * Gets the stack trace of an exception as a string.
     *
     * @param e exception to trace
     * @return exception stack trace as a string
     */
    private String getStackTrace(final Exception e) {
        final Writer w = new StringWriter();
        final PrintWriter pw = new PrintWriter(w);
        e.printStackTrace(pw);
        return w.toString();
    }

    /**
     * Gets a statistics string.
     *
     * @return a statistics string.
     */

    /**
     * Gets the listener used (if any) to receive notifications of exceptions unavoidably swallowed
     * by the pool.
     *
     * @return The listener or {@code null} for no listener
     */
    public final SwallowedExceptionListener getSwallowedExceptionListener() {
        return swallowedExceptionListener;
    }

    /**
     * Gets whether objects borrowed from the pool will be validated before being returned from the
     * {@code borrowObject()} method. Validation is performed by the {@code validateObject()} method
     * of the factory associated with the pool. If the object fails to validate, it will be removed
     * from the pool and destroyed, and a new attempt will be made to borrow an object from the
     * pool.
     *
     * @return {@code true} if objects are validated before being returned from the {@code
     *     borrowObject()} method
     * @see #setTestOnBorrow
     */
    public final boolean getTestOnBorrow() {
        return testOnBorrow;
    }

    /**
     * Gets whether objects created for the pool will be validated before being returned from the
     * {@code borrowObject()} method. Validation is performed by the {@code validateObject()} method
     * of the factory associated with the pool. If the object fails to validate, then {@code
     * borrowObject()} will fail.
     *
     * @return {@code true} if newly created objects are validated before being returned from the
     *     {@code borrowObject()} method
     * @see #setTestOnCreate
     * @since 2.2
     */
    public final boolean getTestOnCreate() {
        return testOnCreate;
    }

    /**
     * Gets whether objects borrowed from the pool will be validated when they are returned to the
     * pool via the {@code returnObject()} method. Validation is performed by the {@code
     * validateObject()} method of the factory associated with the pool. Returning objects that fail
     * validation are destroyed rather then being returned the pool.
     *
     * @return {@code true} if objects are validated on return to the pool via the {@code
     *     returnObject()} method
     * @see #setTestOnReturn
     */
    public final boolean getTestOnReturn() {
        return testOnReturn;
    }

    /**
     * Gets whether objects sitting idle in the pool will be validated by the idle object evictor
     * (if any - see {@link #setTimeBetweenEvictionRuns(Duration)}). Validation is performed by the
     * {@code validateObject()} method of the factory associated with the pool. If the object fails
     * to validate, it will be removed from the pool and destroyed.
     *
     * @return {@code true} if objects will be validated by the evictor
     * @see #setTestWhileIdle
     * @see #setTimeBetweenEvictionRunsMillis
     */
    public final boolean getTestWhileIdle() {
        return testWhileIdle;
    }

    /**
     * Gets the duration to sleep between runs of the idle object evictor thread. When non-positive,
     * no idle object evictor thread will be run.
     *
     * @return number of milliseconds to sleep between evictor runs
     * @see #setTimeBetweenEvictionRuns
     * @since 2.11.0
     */
    public final Duration getDurationBetweenEvictionRuns() {
        return durationBetweenEvictionRuns;
    }

    /**
     * Gets the duration to sleep between runs of the idle object evictor thread. When non-positive,
     * no idle object evictor thread will be run.
     *
     * @return number of milliseconds to sleep between evictor runs
     * @see #setTimeBetweenEvictionRuns
     * @since 2.10.0
     * @deprecated {@link #getDurationBetweenEvictionRuns()}.
     */
    @Deprecated
    public final Duration getTimeBetweenEvictionRuns() {
        return durationBetweenEvictionRuns;
    }

    /**
     * Gets the number of milliseconds to sleep between runs of the idle object evictor thread. When
     * non-positive, no idle object evictor thread will be run.
     *
     * @return number of milliseconds to sleep between evictor runs
     * @see #setTimeBetweenEvictionRunsMillis
     * @deprecated Use {@link #getDurationBetweenEvictionRuns()}.
     */
    @Deprecated
    public final long getTimeBetweenEvictionRunsMillis() {
        return durationBetweenEvictionRuns.toMillis();
    }

    /**
     * Gets whether or not abandoned object removal is configured for this pool.
     *
     * @return true if this pool is configured to detect and remove abandoned objects
     * @since 2.11.0
     */
    public boolean isAbandonedConfig() {
        return abandonedConfig != null;
    }

    /**
     * Has this pool instance been closed.
     *
     * @return {@code true} when this pool has been closed.
     */
    public final boolean isClosed() {
        return closed;
    }

    /**
     * Registers the pool with the platform MBean server. The registered name will be {@code
     * jmxNameBase + jmxNamePrefix + i} where i is the least integer greater than or equal to 1 such
     * that the name is not already registered. Swallows MBeanRegistrationException,
     * NotCompliantMBeanException returning null.
     *
     * @param config Pool configuration
     * @param jmxNameBase default base JMX name for this pool
     * @param jmxNamePrefix name prefix
     * @return registered ObjectName, null if registration fails
     */

    /** Unregisters this pool's MBean. */

    /**
     * Marks the object as returning to the pool.
     *
     * @param pooledObject instance to return to the keyed pool
     */
    protected void markReturningState(final PooledObject<T> pooledObject) {
        synchronized (pooledObject) {
            if (pooledObject.getState() != PooledObjectState.ALLOCATED) {
                throw new IllegalStateException(
                        "Object has already been returned to this pool or is invalid");
            }
            pooledObject.markReturning(); // Keep from being marked abandoned
        }
    }

    /**
     * Sets the abandoned object removal configuration.
     *
     * @param abandonedConfig the new configuration to use. This is used by value.
     * @see AbandonedConfig
     * @since 2.11.0
     */
    public void setAbandonedConfig(final AbandonedConfig abandonedConfig) {
        this.abandonedConfig = AbandonedConfig.copy(abandonedConfig);
    }

    /**
     * Sets whether to block when the {@code borrowObject()} method is invoked when the pool is
     * exhausted (the maximum number of "active" objects has been reached).
     *
     * @param blockWhenExhausted {@code true} if {@code borrowObject()} should block when the pool
     *     is exhausted
     * @see #getBlockWhenExhausted
     */
    public final void setBlockWhenExhausted(final boolean blockWhenExhausted) {
        this.blockWhenExhausted = blockWhenExhausted;
    }

    /**
     * Initializes the receiver with the given configuration.
     *
     * @param config Initialization source.
     */

    /**
     * Sets the eviction policy for this pool.
     *
     * @param evictionPolicy the eviction policy for this pool.
     * @since 2.6.0
     */
    public void setEvictionPolicy0(final EvictionPolicy<T> evictionPolicy) {
        this.evictionPolicy = evictionPolicy;
    }

    /**
     * Sets the eviction policy.
     *
     * @param className Eviction policy class name.
     * @param classLoader Load the class from this class loader.
     */
    @SuppressWarnings("unchecked")
    private void setEvictionPolicy1(final String className, final ClassLoader classLoader)
            throws ClassNotFoundException,
                    InstantiationException,
                    IllegalAccessException,
                    InvocationTargetException,
                    NoSuchMethodException {
        final Class<?> clazz = Class.forName(className, true, classLoader);
        final Object policy = clazz.getConstructor().newInstance();
        this.evictionPolicy = (EvictionPolicy<T>) policy;
    }

    /**
     * Sets the name of the {@link EvictionPolicy} implementation that is used by this pool. The
     * Pool will attempt to load the class using the thread context class loader. If that fails, the
     * use the class loader for the {@link EvictionPolicy} interface.
     *
     * @param evictionPolicyClassName the fully qualified class name of the new eviction policy
     * @see #getEvictionPolicyClassName()
     * @since 2.6.0 If loading the class using the thread context class loader fails, use the class
     *     loader for the {@link EvictionPolicy} interface.
     */
    public final void setEvictionPolicyClassName0(final String evictionPolicyClassName) {
        setEvictionPolicyClassName1(
                evictionPolicyClassName, Thread.currentThread().getContextClassLoader());
    }

    /**
     * Sets the name of the {@link EvictionPolicy} implementation that is used by this pool. The
     * Pool will attempt to load the class using the given class loader. If that fails, use the
     * class loader for the {@link EvictionPolicy} interface.
     *
     * @param evictionPolicyClassName the fully qualified class name of the new eviction policy
     * @param classLoader the class loader to load the given {@code evictionPolicyClassName}.
     * @see #getEvictionPolicyClassName()
     * @since 2.6.0 If loading the class using the given class loader fails, use the class loader
     *     for the {@link EvictionPolicy} interface.
     */
    public final void setEvictionPolicyClassName1(
            final String evictionPolicyClassName, final ClassLoader classLoader) {
        final Class<?> epClass = EvictionPolicy.class;
        final ClassLoader epClassLoader = epClass.getClassLoader();
        try {
            try {
                setEvictionPolicy1(evictionPolicyClassName, classLoader);
            } catch (final ClassCastException | ClassNotFoundException e) {
                setEvictionPolicy1(evictionPolicyClassName, epClassLoader);
            }
        } catch (final ClassCastException e) {
            throw new IllegalArgumentException(
                    "Class "
                            + evictionPolicyClassName
                            + " from class loaders ["
                            + classLoader
                            + ", "
                            + epClassLoader
                            + "] do not implement "
                            + EVICTION_POLICY_TYPE_NAME);
        } catch (final ClassNotFoundException
                | InstantiationException
                | IllegalAccessException
                | InvocationTargetException
                | NoSuchMethodException e) {
            throw new IllegalArgumentException(
                    "Unable to create "
                            + EVICTION_POLICY_TYPE_NAME
                            + " instance of type "
                            + evictionPolicyClassName,
                    e);
        }
    }

    /**
     * Sets the timeout that will be used when waiting for the Evictor to shutdown if this pool is
     * closed and it is the only pool still using the the value for the Evictor.
     *
     * @param evictorShutdownTimeout the timeout in milliseconds that will be used while waiting for
     *     the Evictor to shut down.
     * @since 2.10.0
     */
    public final void setEvictorShutdownTimeout(final Duration evictorShutdownTimeout) {
        this.evictorShutdownTimeoutDuration =
                PoolImplUtils.nonNull(
                        evictorShutdownTimeout,
                        BaseObjectPoolConfig.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT);
    }

    /**
     * Sets the timeout that will be used when waiting for the Evictor to shutdown if this pool is
     * closed and it is the only pool still using the the value for the Evictor.
     *
     * @param evictorShutdownTimeoutMillis the timeout in milliseconds that will be used while
     *     waiting for the Evictor to shut down.
     * @deprecated Use {@link #setEvictorShutdownTimeout(Duration)}.
     */
    @Deprecated
    public final void setEvictorShutdownTimeoutMillis(final long evictorShutdownTimeoutMillis) {
        setEvictorShutdownTimeout(Duration.ofMillis(evictorShutdownTimeoutMillis));
    }

    /**
     * Sets whether the pool has LIFO (last in, first out) behavior with respect to idle objects -
     * always returning the most recently used object from the pool, or as a FIFO (first in, first
     * out) queue, where the pool always returns the oldest object in the idle object pool.
     *
     * @param lifo {@code true} if the pool is to be configured with LIFO behavior or {@code false}
     *     if the pool is to be configured with FIFO behavior
     * @see #getLifo()
     */
    public final void setLifo(final boolean lifo) {
        this.lifo = lifo;
    }

    /**
     * Sets the cap on the number of objects that can be allocated by the pool (checked out to
     * clients, or idle awaiting checkout) at a given time. Use a negative value for no limit.
     *
     * @param maxTotal The cap on the total number of object instances managed by the pool. Negative
     *     values mean that there is no limit to the number of objects allocated by the pool.
     * @see #getMaxTotal
     */
    public final void setMaxTotal(final int maxTotal) {
        this.maxTotal = maxTotal;
    }

    /**
     * Sets the maximum duration the {@code borrowObject()} method should block before throwing an
     * exception when the pool is exhausted and {@link #getBlockWhenExhausted} is true. When less
     * than 0, the {@code borrowObject()} method may block indefinitely.
     *
     * @param maxWaitDuration the maximum duration {@code borrowObject()} will block or negative for
     *     indefinitely.
     * @see #getMaxWaitDuration
     * @see #setBlockWhenExhausted
     * @since 2.11.0
     */
    public final void setMaxWait(final Duration maxWaitDuration) {
        this.maxWaitDuration =
                PoolImplUtils.nonNull(maxWaitDuration, BaseObjectPoolConfig.DEFAULT_MAX_WAIT);
    }

    /**
     * Sets the maximum amount of time (in milliseconds) the {@code borrowObject()} method should
     * block before throwing an exception when the pool is exhausted and {@link
     * #getBlockWhenExhausted} is true. When less than 0, the {@code borrowObject()} method may
     * block indefinitely.
     *
     * @param maxWaitMillis the maximum number of milliseconds {@code borrowObject()} will block or
     *     negative for indefinitely.
     * @see #getMaxWaitDuration
     * @see #setBlockWhenExhausted
     * @deprecated Use {@link #setMaxWait}.
     */
    @Deprecated
    public final void setMaxWaitMillis(final long maxWaitMillis) {
        setMaxWait(Duration.ofMillis(maxWaitMillis));
    }

    /**
     * Sets whether to include statistics in exception messages.
     *
     * <p>Statistics may not accurately reflect snapshot state at the time of the exception because
     * we do not want to lock the pool when gathering this information.
     *
     * @param messagesDetails whether to include statistics in exception messages.
     * @since 2.11.0
     */
    public void setMessagesStatistics(final boolean messagesDetails) {
        this.messageStatistics = messagesDetails;
    }

    /**
     * Sets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRuns(Duration)}). When non-positive, no objects will be evicted from
     * the pool due to idle time alone.
     *
     * @param minEvictableIdleTime minimum amount of time an object may sit idle in the pool before
     *     it is eligible for eviction
     * @see #getMinEvictableIdleTime
     * @see #setTimeBetweenEvictionRuns
     * @since 2.11.0
     */
    public final void setMinEvictableIdle(final Duration minEvictableIdleTime) {
        this.minEvictableIdleDuration =
                PoolImplUtils.nonNull(
                        minEvictableIdleTime,
                        BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION);
    }

    /**
     * Sets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRuns(Duration)}). When non-positive, no objects will be evicted from
     * the pool due to idle time alone.
     *
     * @param minEvictableIdleTime minimum amount of time an object may sit idle in the pool before
     *     it is eligible for eviction
     * @see #getMinEvictableIdleTime
     * @see #setTimeBetweenEvictionRuns
     * @since 2.10.0
     * @deprecated Use {@link #setMinEvictableIdle(Duration)}.
     */
    @Deprecated
    public final void setMinEvictableIdleTime(final Duration minEvictableIdleTime) {
        this.minEvictableIdleDuration =
                PoolImplUtils.nonNull(
                        minEvictableIdleTime,
                        BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION);
    }

    /**
     * Sets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRunsMillis(long)}). When non-positive, no objects will be evicted from
     * the pool due to idle time alone.
     *
     * @param minEvictableIdleTimeMillis minimum amount of time an object may sit idle in the pool
     *     before it is eligible for eviction
     * @see #getMinEvictableIdleTimeMillis
     * @see #setTimeBetweenEvictionRunsMillis
     * @deprecated Use {@link #setMinEvictableIdleTime(Duration)}.
     */
    @Deprecated
    public final void setMinEvictableIdleTimeMillis(final long minEvictableIdleTimeMillis) {
        setMinEvictableIdleTime(Duration.ofMillis(minEvictableIdleTimeMillis));
    }

    /**
     * Sets the maximum number of objects to examine during each run (if any) of the idle object
     * evictor thread. When positive, the number of tests performed for a run will be the minimum of
     * the configured value and the number of idle instances in the pool. When negative, the number
     * of tests performed will be <code>ceil({@link #getNumIdle}/
     * abs({@link #getNumTestsPerEvictionRun}))</code> which means that when the value is {@code -n}
     * roughly one nth of the idle objects will be tested per run.
     *
     * @param numTestsPerEvictionRun max number of objects to examine during each evictor run
     * @see #getNumTestsPerEvictionRun
     * @see #setTimeBetweenEvictionRunsMillis
     */
    public final void setNumTestsPerEvictionRun(final int numTestsPerEvictionRun) {
        this.numTestsPerEvictionRun = numTestsPerEvictionRun;
    }

    /**
     * Sets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRuns(Duration)}), with the extra condition that at least {@code
     * minIdle} object instances remain in the pool. This setting is overridden by {@link
     * #getMinEvictableIdleTime} (that is, if {@link #getMinEvictableIdleTime} is positive, then
     * {@link #getSoftMinEvictableIdleTime} is ignored).
     *
     * @param softMinEvictableIdleTime minimum amount of time an object may sit idle in the pool
     *     before it is eligible for eviction if minIdle instances are available
     * @see #getSoftMinEvictableIdleTimeMillis
     * @since 2.11.0
     */
    public final void setSoftMinEvictableIdle(final Duration softMinEvictableIdleTime) {
        this.softMinEvictableIdleDuration =
                PoolImplUtils.nonNull(
                        softMinEvictableIdleTime,
                        BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION);
    }

    /**
     * Sets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRuns(Duration)}), with the extra condition that at least {@code
     * minIdle} object instances remain in the pool. This setting is overridden by {@link
     * #getMinEvictableIdleTime} (that is, if {@link #getMinEvictableIdleTime} is positive, then
     * {@link #getSoftMinEvictableIdleTime} is ignored).
     *
     * @param softMinEvictableIdleTime minimum amount of time an object may sit idle in the pool
     *     before it is eligible for eviction if minIdle instances are available
     * @see #getSoftMinEvictableIdleTimeMillis
     * @since 2.10.0
     * @deprecated Use {@link #setSoftMinEvictableIdle(Duration)}.
     */
    @Deprecated
    public final void setSoftMinEvictableIdleTime(final Duration softMinEvictableIdleTime) {
        this.softMinEvictableIdleDuration =
                PoolImplUtils.nonNull(
                        softMinEvictableIdleTime,
                        BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION);
    }

    /**
     * Sets the minimum amount of time an object may sit idle in the pool before it is eligible for
     * eviction by the idle object evictor (if any - see {@link
     * #setTimeBetweenEvictionRunsMillis(long)}), with the extra condition that at least {@code
     * minIdle} object instances remain in the pool. This setting is overridden by {@link
     * #getMinEvictableIdleTimeMillis} (that is, if {@link #getMinEvictableIdleTimeMillis} is
     * positive, then {@link #getSoftMinEvictableIdleTimeMillis} is ignored).
     *
     * @param softMinEvictableIdleTimeMillis minimum amount of time an object may sit idle in the
     *     pool before it is eligible for eviction if minIdle instances are available
     * @see #getSoftMinEvictableIdleTimeMillis
     * @deprecated Use {@link #setSoftMinEvictableIdle(Duration)}.
     */
    @Deprecated
    public final void setSoftMinEvictableIdleTimeMillis(final long softMinEvictableIdleTimeMillis) {
        setSoftMinEvictableIdleTime(Duration.ofMillis(softMinEvictableIdleTimeMillis));
    }

    /**
     * The listener used (if any) to receive notifications of exceptions unavoidably swallowed by
     * the pool.
     *
     * @param swallowedExceptionListener The listener or {@code null} for no listener
     */
    public final void setSwallowedExceptionListener(
            final SwallowedExceptionListener swallowedExceptionListener) {
        this.swallowedExceptionListener = swallowedExceptionListener;
    }

    /**
     * Sets whether objects borrowed from the pool will be validated before being returned from the
     * {@code borrowObject()} method. Validation is performed by the {@code validateObject()} method
     * of the factory associated with the pool. If the object fails to validate, it will be removed
     * from the pool and destroyed, and a new attempt will be made to borrow an object from the
     * pool.
     *
     * @param testOnBorrow {@code true} if objects should be validated before being returned from
     *     the {@code borrowObject()} method
     * @see #getTestOnBorrow
     */
    public final void setTestOnBorrow(final boolean testOnBorrow) {
        this.testOnBorrow = testOnBorrow;
    }

    /**
     * Sets whether objects created for the pool will be validated before being returned from the
     * {@code borrowObject()} method. Validation is performed by the {@code validateObject()} method
     * of the factory associated with the pool. If the object fails to validate, then {@code
     * borrowObject()} will fail.
     *
     * @param testOnCreate {@code true} if newly created objects should be validated before being
     *     returned from the {@code borrowObject()} method
     * @see #getTestOnCreate
     * @since 2.2
     */
    public final void setTestOnCreate(final boolean testOnCreate) {
        this.testOnCreate = testOnCreate;
    }

    /**
     * Sets whether objects borrowed from the pool will be validated when they are returned to the
     * pool via the {@code returnObject()} method. Validation is performed by the {@code
     * validateObject()} method of the factory associated with the pool. Returning objects that fail
     * validation are destroyed rather then being returned the pool.
     *
     * @param testOnReturn {@code true} if objects are validated on return to the pool via the
     *     {@code returnObject()} method
     * @see #getTestOnReturn
     */
    public final void setTestOnReturn(final boolean testOnReturn) {
        this.testOnReturn = testOnReturn;
    }

    /**
     * Sets whether objects sitting idle in the pool will be validated by the idle object evictor
     * (if any - see {@link #setTimeBetweenEvictionRuns(Duration)}). Validation is performed by the
     * {@code validateObject()} method of the factory associated with the pool. If the object fails
     * to validate, it will be removed from the pool and destroyed. Note that setting this property
     * has no effect unless the idle object evictor is enabled by setting {@code
     * timeBetweenEvictionRunsMillis} to a positive value.
     *
     * @param testWhileIdle {@code true} so objects will be validated by the evictor
     * @see #getTestWhileIdle
     * @see #setTimeBetweenEvictionRuns
     */
    public final void setTestWhileIdle(final boolean testWhileIdle) {
        this.testWhileIdle = testWhileIdle;
    }

    /**
     * Sets the number of milliseconds to sleep between runs of the idle object evictor thread.
     *
     * <ul>
     *   <li>When positive, the idle object evictor thread starts.
     *   <li>When non-positive, no idle object evictor thread runs.
     * </ul>
     *
     * @param timeBetweenEvictionRuns duration to sleep between evictor runs
     * @see #getTimeBetweenEvictionRunsMillis
     * @since 2.10.0
     */

    /**
     * Sets the number of milliseconds to sleep between runs of the idle object evictor thread.
     *
     * <ul>
     *   <li>When positive, the idle object evictor thread starts.
     *   <li>When non-positive, no idle object evictor thread runs.
     * </ul>
     *
     * @param timeBetweenEvictionRunsMillis number of milliseconds to sleep between evictor runs
     * @see #getTimeBetweenEvictionRunsMillis
     * @deprecated Use {@link #setTimeBetweenEvictionRuns(Duration)}.
     */

    /**
     * Starts the evictor with the given delay. If there is an evictor running when this method is
     * called, it is stopped and replaced with a new evictor with the specified delay.
     *
     * <p>This method needs to be final, since it is called from a constructor. See POOL-195.
     *
     * @param delay time in milliseconds before start and between eviction runs
     */

    /** Stops the evictor. */

    /**
     * Swallows an exception and notifies the configured listener for swallowed exceptions queue.
     *
     * @param swallowException exception to be swallowed
     */
    final void swallowException(final Exception swallowException) {
        final SwallowedExceptionListener listener = getSwallowedExceptionListener();

        if (listener == null) {
            return;
        }

        try {
            listener.onSwallowException(swallowException);
        } catch (final VirtualMachineError e) {
            throw e;
        } catch (final Throwable t) {
        }
    }

    @Override
    protected void toStringAppendFields(final StringBuilder builder) {
        builder.append("maxTotal=");
        builder.append(maxTotal);
        builder.append(", blockWhenExhausted=");
        builder.append(blockWhenExhausted);
        builder.append(", maxWaitDuration=");
        builder.append(maxWaitDuration);
        builder.append(", lifo=");
        builder.append(lifo);
        builder.append(", fairness=");
        builder.append(", testOnCreate=");
        builder.append(testOnCreate);
        builder.append(", testOnBorrow=");
        builder.append(testOnBorrow);
        builder.append(", testOnReturn=");
        builder.append(testOnReturn);
        builder.append(", testWhileIdle=");
        builder.append(testWhileIdle);
        builder.append(", durationBetweenEvictionRuns=");
        builder.append(durationBetweenEvictionRuns);
        builder.append(", numTestsPerEvictionRun=");
        builder.append(numTestsPerEvictionRun);
        builder.append(", minEvictableIdleTimeDuration=");
        builder.append(minEvictableIdleDuration);
        builder.append(", softMinEvictableIdleTimeDuration=");
        builder.append(softMinEvictableIdleDuration);
        builder.append(", evictionPolicy=");
        builder.append(evictionPolicy);
        builder.append(", closeLock=");
        builder.append(closeLock);
        builder.append(", closed=");
        builder.append(closed);
        builder.append(", evictionLock=");
        builder.append(evictionLock);
        builder.append(", evictor=");
        builder.append(evictor);
        builder.append(", evictionIterator=");
        builder.append(evictionIterator);
        builder.append(", factoryClassLoader=");
        builder.append(", oname=");
        builder.append(", creationStackTrace=");
        builder.append(", borrowedCount=");
        builder.append(borrowedCount);
        builder.append(", returnedCount=");
        builder.append(returnedCount);
        builder.append(", createdCount=");
        builder.append(createdCount);
        builder.append(", destroyedCount=");
        builder.append(destroyedCount);
        builder.append(", destroyedByEvictorCount=");
        builder.append(destroyedByEvictorCount);
        builder.append(", destroyedByBorrowValidationCount=");
        builder.append(destroyedByBorrowValidationCount);
        builder.append(", activeTimes=");
        builder.append(activeTimes);
        builder.append(", idleTimes=");
        builder.append(idleTimes);
        builder.append(", waitTimes=");
        builder.append(waitTimes);
        builder.append(", maxBorrowWaitDuration=");
        builder.append(maxBorrowWaitDuration);
        builder.append(", swallowedExceptionListener=");
        builder.append(swallowedExceptionListener);
    }

    /**
     * Updates statistics after an object is borrowed from the pool.
     *
     * @param p object borrowed from the pool
     * @param waitDuration that the borrowing thread had to wait
     */
    final void updateStatsBorrow(final PooledObject<T> p, final Duration waitDuration) {
        borrowedCount.incrementAndGet();
        idleTimes.add0(p.getIdleDuration());
        waitTimes.add0(waitDuration);

        Duration currentMaxDuration;
        do {
            currentMaxDuration = maxBorrowWaitDuration.get();
            if (currentMaxDuration.compareTo(waitDuration) >= 0) {
                break;
            }
        } while (!maxBorrowWaitDuration.compareAndSet(currentMaxDuration, waitDuration));
    }

    /**
     * Updates statistics after an object is returned to the pool.
     *
     * @param activeTime the amount of time (in milliseconds) that the returning object was checked
     *     out
     */
    final void updateStatsReturn(final Duration activeTime) {
        returnedCount.incrementAndGet();
        activeTimes.add0(activeTime);
    }
}
