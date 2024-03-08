package org.apache.commons.pool;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.pool.ContextInitializer;
import org.apache.commons.pool.ExceptionHandler;
import org.apache.commons.pool.IntegrationUtils;
import java.io.Writer;
import java.io.PrintWriter;
import java.util.Map;
import java.lang.reflect.InvocationTargetException;
import java.io.StringWriter;
import java.util.List;
import java.util.Iterator;
import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.TimerTask;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.atomic.AtomicReference;
import java.util.stream.Collectors;
import org.apache.commons.pool2.BaseObject;
import org.apache.commons.pool2.PooledObject;
import org.apache.commons.pool2.PooledObjectState;
import org.apache.commons.pool2.SwallowedExceptionListener;
    class EvictionIterator implements Iterator<PooledObject<T>> {
    private static Value clz = ContextInitializer.getPythonClass("/BaseGenericObjectPool.py", "EvictionIterator");
    private Value obj;
    public EvictionIterator(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public void remove() {
// 
// idleObjectIterator.remove();
// 

obj.invokeMember("remove");
}
        public PooledObject<T> next() {
// 
// return idleObjectIterator.next();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("next").as(PooledObject.class);
}
        public boolean hasNext() {
// 
// return idleObjectIterator.hasNext();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("hasNext").as(boolean.class);
}
        public Deque<PooledObject<T>> getIdleObjects() {
// 
// return idleObjects;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getIdleObjects").as(Deque.class);
}
        EvictionIterator(final Deque<PooledObject<T>> idleObjects) {
// 
// this.idleObjects = idleObjects;
// 
// if (getLifo()) {
// idleObjectIterator = idleObjects.descendingIterator();
// } else {
// idleObjectIterator = idleObjects.iterator();
// }
// 

this.obj = clz.invokeMember("__init__", idleObjects);
}
}
public abstract class BaseGenericObjectPool<T> extends BaseObject {
    final AtomicLong destroyedByBorrowValidationCount = new AtomicLong();
    final AtomicLong destroyedByEvictorCount = new AtomicLong();
    final AtomicLong destroyedCount = new AtomicLong();
    final AtomicLong createdCount = new AtomicLong();
    final Object evictionLock = new Object();
    final Object closeLock = new Object();
    public static final int MEAN_TIMING_STATS_CACHE_SIZE = 100;
    private final AtomicReference<Duration> maxBorrowWaitDuration =
            new AtomicReference<>(Duration.ZERO);
    private final StatsStore waitTimes = new StatsStore(MEAN_TIMING_STATS_CACHE_SIZE);
    private final StatsStore idleTimes = new StatsStore(MEAN_TIMING_STATS_CACHE_SIZE);
    private final StatsStore activeTimes = new StatsStore(MEAN_TIMING_STATS_CACHE_SIZE);
    private final AtomicLong returnedCount = new AtomicLong();
    private final AtomicLong borrowedCount = new AtomicLong();
    private volatile Duration evictorShutdownTimeoutDuration =
            BaseObjectPoolConfig.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT;
    private volatile Duration softMinEvictableIdleDuration =
            BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION;
    private volatile Duration minEvictableIdleDuration =
            BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION;
    private volatile int numTestsPerEvictionRun =
            BaseObjectPoolConfig.DEFAULT_NUM_TESTS_PER_EVICTION_RUN;
    private volatile Duration durationBetweenEvictionRuns =
            BaseObjectPoolConfig.DEFAULT_TIME_BETWEEN_EVICTION_RUNS;
    private volatile boolean testWhileIdle = BaseObjectPoolConfig.DEFAULT_TEST_WHILE_IDLE;
    private volatile boolean testOnReturn = BaseObjectPoolConfig.DEFAULT_TEST_ON_RETURN;
    private volatile boolean testOnBorrow = BaseObjectPoolConfig.DEFAULT_TEST_ON_BORROW;
    private volatile boolean testOnCreate = BaseObjectPoolConfig.DEFAULT_TEST_ON_CREATE;
    private volatile boolean lifo = BaseObjectPoolConfig.DEFAULT_LIFO;
    private volatile Duration maxWaitDuration = BaseObjectPoolConfig.DEFAULT_MAX_WAIT;
    private volatile boolean blockWhenExhausted = BaseObjectPoolConfig.DEFAULT_BLOCK_WHEN_EXHAUSTED;
    private volatile int maxTotal = GenericKeyedObjectPoolConfig.DEFAULT_MAX_TOTAL;
    private static final Duration DEFAULT_REMOVE_ABANDONED_TIMEOUT =
            Duration.ofSeconds(Integer.MAX_VALUE);
    private static final String EVICTION_POLICY_TYPE_NAME = EvictionPolicy.class.getName();
    private static Value clz = ContextInitializer.getPythonClass("/BaseGenericObjectPool.py", "BaseGenericObjectPool");
    private Value obj;
    public BaseGenericObjectPool(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    protected void toStringAppendFields(final StringBuilder builder) {
// 
// builder.append("maxTotal=");
// builder.append(maxTotal);
// builder.append(", blockWhenExhausted=");
// builder.append(blockWhenExhausted);
// builder.append(", maxWaitDuration=");
// builder.append(maxWaitDuration);
// builder.append(", lifo=");
// builder.append(lifo);
// builder.append(", fairness=");
// builder.append(", testOnCreate=");
// builder.append(testOnCreate);
// builder.append(", testOnBorrow=");
// builder.append(testOnBorrow);
// builder.append(", testOnReturn=");
// builder.append(testOnReturn);
// builder.append(", testWhileIdle=");
// builder.append(testWhileIdle);
// builder.append(", durationBetweenEvictionRuns=");
// builder.append(durationBetweenEvictionRuns);
// builder.append(", numTestsPerEvictionRun=");
// builder.append(numTestsPerEvictionRun);
// builder.append(", minEvictableIdleTimeDuration=");
// builder.append(minEvictableIdleDuration);
// builder.append(", softMinEvictableIdleTimeDuration=");
// builder.append(softMinEvictableIdleDuration);
// builder.append(", evictionPolicy=");
// builder.append(evictionPolicy);
// builder.append(", closeLock=");
// builder.append(closeLock);
// builder.append(", closed=");
// builder.append(closed);
// builder.append(", evictionLock=");
// builder.append(evictionLock);
// builder.append(", evictor=");
// builder.append(evictor);
// builder.append(", evictionIterator=");
// builder.append(evictionIterator);
// builder.append(", factoryClassLoader=");
// builder.append(", oname=");
// builder.append(", creationStackTrace=");
// builder.append(", borrowedCount=");
// builder.append(borrowedCount);
// builder.append(", returnedCount=");
// builder.append(returnedCount);
// builder.append(", createdCount=");
// builder.append(createdCount);
// builder.append(", destroyedCount=");
// builder.append(destroyedCount);
// builder.append(", destroyedByEvictorCount=");
// builder.append(destroyedByEvictorCount);
// builder.append(", destroyedByBorrowValidationCount=");
// builder.append(destroyedByBorrowValidationCount);
// builder.append(", activeTimes=");
// builder.append(activeTimes);
// builder.append(", idleTimes=");
// builder.append(idleTimes);
// builder.append(", waitTimes=");
// builder.append(waitTimes);
// builder.append(", maxBorrowWaitDuration=");
// builder.append(maxBorrowWaitDuration);
// builder.append(", swallowedExceptionListener=");
// builder.append(swallowedExceptionListener);
// 

obj.invokeMember("toStringAppendFields", builder);
}
    public final void setSoftMinEvictableIdleTimeMillis(final long softMinEvictableIdleTimeMillis) {
// 
// setSoftMinEvictableIdleTime(Duration.ofMillis(softMinEvictableIdleTimeMillis));
// 

obj.invokeMember("setSoftMinEvictableIdleTimeMillis", softMinEvictableIdleTimeMillis);
}
    public final void setSoftMinEvictableIdleTime(final Duration softMinEvictableIdleTime) {
// 
// this.softMinEvictableIdleDuration =
// PoolImplUtils.nonNull(
// softMinEvictableIdleTime,
// BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION);
// 

obj.invokeMember("setSoftMinEvictableIdleTime", softMinEvictableIdleTime);
}
    public final void setMinEvictableIdleTimeMillis(final long minEvictableIdleTimeMillis) {
// 
// setMinEvictableIdleTime(Duration.ofMillis(minEvictableIdleTimeMillis));
// 

obj.invokeMember("setMinEvictableIdleTimeMillis", minEvictableIdleTimeMillis);
}
    public final void setMinEvictableIdleTime(final Duration minEvictableIdleTime) {
// 
// this.minEvictableIdleDuration =
// PoolImplUtils.nonNull(
// minEvictableIdleTime,
// BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION);
// 

obj.invokeMember("setMinEvictableIdleTime", minEvictableIdleTime);
}
    public final void setMaxWaitMillis(final long maxWaitMillis) {
// 
// setMaxWait(Duration.ofMillis(maxWaitMillis));
// 

obj.invokeMember("setMaxWaitMillis", maxWaitMillis);
}
    public final void setEvictorShutdownTimeoutMillis(final long evictorShutdownTimeoutMillis) {
// 
// setEvictorShutdownTimeout(Duration.ofMillis(evictorShutdownTimeoutMillis));
// 

obj.invokeMember("setEvictorShutdownTimeoutMillis", evictorShutdownTimeoutMillis);
}
    public final long getTimeBetweenEvictionRunsMillis() {
// 
// return durationBetweenEvictionRuns.toMillis();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getTimeBetweenEvictionRunsMillis").as(long.class);
}
    public final Duration getTimeBetweenEvictionRuns() {
// 
// return durationBetweenEvictionRuns;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getTimeBetweenEvictionRuns").as(Duration.class);
}
    public final long getSoftMinEvictableIdleTimeMillis() {
// 
// return softMinEvictableIdleDuration.toMillis();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getSoftMinEvictableIdleTimeMillis").as(long.class);
}
    public final Duration getSoftMinEvictableIdleTime() {
// 
// return softMinEvictableIdleDuration;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getSoftMinEvictableIdleTime").as(Duration.class);
}
    public int getRemoveAbandonedTimeout() {
// 
// return (int) getRemoveAbandonedTimeoutDuration().getSeconds();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getRemoveAbandonedTimeout").as(int.class);
}
    public final long getMinEvictableIdleTimeMillis() {
// 
// return minEvictableIdleDuration.toMillis();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMinEvictableIdleTimeMillis").as(long.class);
}
    public final Duration getMinEvictableIdleTime() {
// 
// return minEvictableIdleDuration;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMinEvictableIdleTime").as(Duration.class);
}
    public final long getMaxWaitMillis() {
// 
// return maxWaitDuration.toMillis();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMaxWaitMillis").as(long.class);
}
    public final long getEvictorShutdownTimeoutMillis() {
// 
// return evictorShutdownTimeoutDuration.toMillis();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getEvictorShutdownTimeoutMillis").as(long.class);
}
    public final Duration getEvictorShutdownTimeout() {
// 
// return evictorShutdownTimeoutDuration;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getEvictorShutdownTimeout").as(Duration.class);
}
    private void setEvictionPolicy1(final String className, final ClassLoader classLoader)
            throws ClassNotFoundException,
                    InstantiationException,
                    IllegalAccessException,
                    InvocationTargetException,
                    NoSuchMethodException {
try {
// 
// final Class<?> clazz = Class.forName(className, true, classLoader);
// final Object policy = clazz.getConstructor().newInstance();
// this.evictionPolicy = (EvictionPolicy<T>) policy;
// 

obj.invokeMember("setEvictionPolicy1", className, classLoader);
} catch (PolyglotException e) {
    // TODO: Handle ClassNotFoundException,
                    InstantiationException,
                    IllegalAccessException,
                    InvocationTargetException,
                    NoSuchMethodException
    throw (ClassNotFoundException,
                    InstantiationException,
                    IllegalAccessException,
                    InvocationTargetException,
                    NoSuchMethodException) ExceptionHandler.handle(e, "BaseGenericObjectPool.setEvictionPolicy1");
}
}
    final void updateStatsReturn(final Duration activeTime) {
// 
// returnedCount.incrementAndGet();
// activeTimes.add0(activeTime);
// 

obj.invokeMember("updateStatsReturn", activeTime);
}
    final void updateStatsBorrow(final PooledObject<T> p, final Duration waitDuration) {
// 
// borrowedCount.incrementAndGet();
// idleTimes.add0(p.getIdleDuration());
// waitTimes.add0(waitDuration);
// 
// Duration currentMaxDuration;
// do {
// currentMaxDuration = maxBorrowWaitDuration.get();
// if (currentMaxDuration.compareTo(waitDuration) >= 0) {
// break;
// }
// } while (!maxBorrowWaitDuration.compareAndSet(currentMaxDuration, waitDuration));
// 

obj.invokeMember("updateStatsBorrow", p, waitDuration);
}
    final void swallowException(final Exception swallowException) {
// 
// final SwallowedExceptionListener listener = getSwallowedExceptionListener();
// 
// if (listener == null) {
// return;
// }
// 
// try {
// listener.onSwallowException(swallowException);
// } catch (final VirtualMachineError e) {
// throw e;
// } catch (final Throwable t) {
// }
// 

obj.invokeMember("swallowException", swallowException);
}
    public final void setTestWhileIdle(final boolean testWhileIdle) {
// 
// this.testWhileIdle = testWhileIdle;
// 

obj.invokeMember("setTestWhileIdle", testWhileIdle);
}
    public final void setTestOnReturn(final boolean testOnReturn) {
// 
// this.testOnReturn = testOnReturn;
// 

obj.invokeMember("setTestOnReturn", testOnReturn);
}
    public final void setTestOnCreate(final boolean testOnCreate) {
// 
// this.testOnCreate = testOnCreate;
// 

obj.invokeMember("setTestOnCreate", testOnCreate);
}
    public final void setTestOnBorrow(final boolean testOnBorrow) {
// 
// this.testOnBorrow = testOnBorrow;
// 

obj.invokeMember("setTestOnBorrow", testOnBorrow);
}
    public final void setSwallowedExceptionListener(
            final SwallowedExceptionListener swallowedExceptionListener) {
// 
// this.swallowedExceptionListener = swallowedExceptionListener;
// 

obj.invokeMember("setSwallowedExceptionListener", swallowedExceptionListener);
}
    public final void setSoftMinEvictableIdle(final Duration softMinEvictableIdleTime) {
// 
// this.softMinEvictableIdleDuration =
// PoolImplUtils.nonNull(
// softMinEvictableIdleTime,
// BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION);
// 

obj.invokeMember("setSoftMinEvictableIdle", softMinEvictableIdleTime);
}
    public final void setNumTestsPerEvictionRun(final int numTestsPerEvictionRun) {
// 
// this.numTestsPerEvictionRun = numTestsPerEvictionRun;
// 

obj.invokeMember("setNumTestsPerEvictionRun", numTestsPerEvictionRun);
}
    public final void setMinEvictableIdle(final Duration minEvictableIdleTime) {
// 
// this.minEvictableIdleDuration =
// PoolImplUtils.nonNull(
// minEvictableIdleTime,
// BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION);
// 

obj.invokeMember("setMinEvictableIdle", minEvictableIdleTime);
}
    public void setMessagesStatistics(final boolean messagesDetails) {
// 
// this.messageStatistics = messagesDetails;
// 

obj.invokeMember("setMessagesStatistics", messagesDetails);
}
    public final void setMaxWait(final Duration maxWaitDuration) {
// 
// this.maxWaitDuration =
// PoolImplUtils.nonNull(maxWaitDuration, BaseObjectPoolConfig.DEFAULT_MAX_WAIT);
// 

obj.invokeMember("setMaxWait", maxWaitDuration);
}
    public final void setMaxTotal(final int maxTotal) {
// 
// this.maxTotal = maxTotal;
// 

obj.invokeMember("setMaxTotal", maxTotal);
}
    public final void setLifo(final boolean lifo) {
// 
// this.lifo = lifo;
// 

obj.invokeMember("setLifo", lifo);
}
    public final void setEvictorShutdownTimeout(final Duration evictorShutdownTimeout) {
// 
// this.evictorShutdownTimeoutDuration =
// PoolImplUtils.nonNull(
// evictorShutdownTimeout,
// BaseObjectPoolConfig.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT);
// 

obj.invokeMember("setEvictorShutdownTimeout", evictorShutdownTimeout);
}
    public final void setEvictionPolicyClassName1(
            final String evictionPolicyClassName, final ClassLoader classLoader) {
// 
// final Class<?> epClass = EvictionPolicy.class;
// final ClassLoader epClassLoader = epClass.getClassLoader();
// try {
// try {
// setEvictionPolicy1(evictionPolicyClassName, classLoader);
// } catch (final ClassCastException | ClassNotFoundException e) {
// setEvictionPolicy1(evictionPolicyClassName, epClassLoader);
// }
// } catch (final ClassCastException e) {
// throw new IllegalArgumentException(
// "Class "
// + evictionPolicyClassName
// + " from class loaders ["
// + classLoader
// + ", "
// + epClassLoader
// + "] do not implement "
// + EVICTION_POLICY_TYPE_NAME);
// } catch (final ClassNotFoundException
// | InstantiationException
// | IllegalAccessException
// | InvocationTargetException
// | NoSuchMethodException e) {
// throw new IllegalArgumentException(
// "Unable to create "
// + EVICTION_POLICY_TYPE_NAME
// + " instance of type "
// + evictionPolicyClassName,
// e);
// }
// 

obj.invokeMember("setEvictionPolicyClassName1", evictionPolicyClassName, classLoader);
}
    public final void setEvictionPolicyClassName0(final String evictionPolicyClassName) {
// 
// setEvictionPolicyClassName1(
// evictionPolicyClassName, Thread.currentThread().getContextClassLoader());
// 

obj.invokeMember("setEvictionPolicyClassName0", evictionPolicyClassName);
}
    public void setEvictionPolicy0(final EvictionPolicy<T> evictionPolicy) {
// 
// this.evictionPolicy = evictionPolicy;
// 

obj.invokeMember("setEvictionPolicy0", evictionPolicy);
}
    public final void setBlockWhenExhausted(final boolean blockWhenExhausted) {
// 
// this.blockWhenExhausted = blockWhenExhausted;
// 

obj.invokeMember("setBlockWhenExhausted", blockWhenExhausted);
}
    public void setAbandonedConfig(final AbandonedConfig abandonedConfig) {
// 
// this.abandonedConfig = AbandonedConfig.copy(abandonedConfig);
// 

obj.invokeMember("setAbandonedConfig", abandonedConfig);
}
    protected void markReturningState(final PooledObject<T> pooledObject) {
// 
// synchronized (pooledObject) {
// if (pooledObject.getState() != PooledObjectState.ALLOCATED) {
// throw new IllegalStateException(
// "Object has already been returned to this pool or is invalid");
// }
// pooledObject.markReturning(); // Keep from being marked abandoned
// }
// 

obj.invokeMember("markReturningState", pooledObject);
}
    public final boolean isClosed() {
// 
// return closed;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isClosed").as(boolean.class);
}
    public boolean isAbandonedConfig() {
// 
// return abandonedConfig != null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isAbandonedConfig").as(boolean.class);
}
    public final Duration getDurationBetweenEvictionRuns() {
// 
// return durationBetweenEvictionRuns;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getDurationBetweenEvictionRuns").as(Duration.class);
}
    public final boolean getTestWhileIdle() {
// 
// return testWhileIdle;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getTestWhileIdle").as(boolean.class);
}
    public final boolean getTestOnReturn() {
// 
// return testOnReturn;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getTestOnReturn").as(boolean.class);
}
    public final boolean getTestOnCreate() {
// 
// return testOnCreate;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getTestOnCreate").as(boolean.class);
}
    public final boolean getTestOnBorrow() {
// 
// return testOnBorrow;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getTestOnBorrow").as(boolean.class);
}
    public final SwallowedExceptionListener getSwallowedExceptionListener() {
// 
// return swallowedExceptionListener;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getSwallowedExceptionListener").as(SwallowedExceptionListener.class);
}
    public final Duration getSoftMinEvictableIdleDuration() {
// 
// return softMinEvictableIdleDuration;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getSoftMinEvictableIdleDuration").as(Duration.class);
}
    public final long getReturnedCount() {
// 
// return returnedCount.get();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getReturnedCount").as(long.class);
}
    public Duration getRemoveAbandonedTimeoutDuration() {
// 
// final AbandonedConfig ac = this.abandonedConfig;
// return ac != null
// ? ac.getRemoveAbandonedTimeoutDuration()
// : DEFAULT_REMOVE_ABANDONED_TIMEOUT;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getRemoveAbandonedTimeoutDuration").as(Duration.class);
}
    public boolean getRemoveAbandonedOnMaintenance() {
// 
// final AbandonedConfig ac = this.abandonedConfig;
// return ac != null && ac.getRemoveAbandonedOnMaintenance();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getRemoveAbandonedOnMaintenance").as(boolean.class);
}
    public boolean getRemoveAbandonedOnBorrow() {
// 
// final AbandonedConfig ac = this.abandonedConfig;
// return ac != null && ac.getRemoveAbandonedOnBorrow();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getRemoveAbandonedOnBorrow").as(boolean.class);
}
    public final int getNumTestsPerEvictionRun() {
// 
// return numTestsPerEvictionRun;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumTestsPerEvictionRun").as(int.class);
}
    public final Duration getMinEvictableIdleDuration() {
// 
// return minEvictableIdleDuration;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMinEvictableIdleDuration").as(Duration.class);
}
    public boolean getMessageStatistics() {
// 
// return messageStatistics;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMessageStatistics").as(boolean.class);
}
    public final long getMeanIdleTimeMillis() {
// 
// return idleTimes.getMean();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMeanIdleTimeMillis").as(long.class);
}
    public final long getMeanBorrowWaitTimeMillis() {
// 
// return waitTimes.getMean();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMeanBorrowWaitTimeMillis").as(long.class);
}
    public final long getMeanActiveTimeMillis() {
// 
// return activeTimes.getMean();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMeanActiveTimeMillis").as(long.class);
}
    public final Duration getMaxWaitDuration() {
// 
// return maxWaitDuration;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMaxWaitDuration").as(Duration.class);
}
    public final int getMaxTotal() {
// 
// return maxTotal;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMaxTotal").as(int.class);
}
    public final long getMaxBorrowWaitTimeMillis() {
// 
// return maxBorrowWaitDuration.get().toMillis();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMaxBorrowWaitTimeMillis").as(long.class);
}
    public boolean getLogAbandoned() {
// 
// final AbandonedConfig ac = this.abandonedConfig;
// return ac != null && ac.getLogAbandoned();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getLogAbandoned").as(boolean.class);
}
    public final boolean getLifo() {
// 
// return lifo;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getLifo").as(boolean.class);
}
    public final Duration getEvictorShutdownTimeoutDuration() {
// 
// return evictorShutdownTimeoutDuration;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getEvictorShutdownTimeoutDuration").as(Duration.class);
}
    public final String getEvictionPolicyClassName() {
// 
// return evictionPolicy.getClass().getName();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getEvictionPolicyClassName").as(String.class);
}
    public EvictionPolicy<T> getEvictionPolicy() {
// 
// return evictionPolicy;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getEvictionPolicy").as(EvictionPolicy.class);
}
    public final long getDestroyedCount() {
// 
// return destroyedCount.get();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getDestroyedCount").as(long.class);
}
    public final long getDestroyedByEvictorCount() {
// 
// return destroyedByEvictorCount.get();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getDestroyedByEvictorCount").as(long.class);
}
    public final long getDestroyedByBorrowValidationCount() {
// 
// return destroyedByBorrowValidationCount.get();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getDestroyedByBorrowValidationCount").as(long.class);
}
    public final long getCreatedCount() {
// 
// return createdCount.get();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getCreatedCount").as(long.class);
}
    public final long getBorrowedCount() {
// 
// return borrowedCount.get();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getBorrowedCount").as(long.class);
}
    public final boolean getBlockWhenExhausted() {
// 
// return blockWhenExhausted;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getBlockWhenExhausted").as(boolean.class);
}
    final void assertOpen() throws IllegalStateException {
try {
// 
// if (isClosed()) {
// throw new IllegalStateException("Pool not open");
// }
// 

obj.invokeMember("assertOpen");
} catch (PolyglotException e) {
    // TODO: Handle IllegalStateException
    throw (IllegalStateException) ExceptionHandler.handle(e, "BaseGenericObjectPool.assertOpen");
}
}
    private String getStackTrace(final Exception e) {
// 
// final Writer w = new StringWriter();
// final PrintWriter pw = new PrintWriter(w);
// e.printStackTrace(pw);
// return w.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getStackTrace", e).as(String.class);
}
    ArrayList<PooledObject<T>> createRemoveList(
            final AbandonedConfig abandonedConfig,
            final Map<IdentityWrapper<T>, PooledObject<T>> allObjects) {
// 
// final Instant timeout =
// Instant.now().minus(abandonedConfig.getRemoveAbandonedTimeoutDuration());
// final ArrayList<PooledObject<T>> remove = new ArrayList<>();
// allObjects
// .values()
// .forEach(
// pooledObject -> {
// synchronized (pooledObject) {
// if (pooledObject.getState() == PooledObjectState.ALLOCATED
// && pooledObject.getLastUsedInstant().compareTo(timeout)
// <= 0) {
// pooledObject.markAbandoned();
// remove.add(pooledObject);
// }
// }
// });
// return remove;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("createRemoveList", abandonedConfig, allObjects).as(ArrayList.class);
}
    public abstract int getNumIdle();
    public abstract void evict() throws Exception;
    abstract void ensureMinIdle() throws Exception;
    public abstract void close();
    static class IdentityWrapper<T> {
    private static Value clz = ContextInitializer.getPythonClass("/BaseGenericObjectPool.py", "IdentityWrapper");
    private Value obj;
    public IdentityWrapper(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// final StringBuilder builder = new StringBuilder();
// builder.append("IdentityWrapper [instance=");
// builder.append(instance);
// builder.append("]");
// return builder.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public int hashCode() {
// 
// return System.identityHashCode(instance);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("hashCode").as(int.class);
}
        public boolean equals(final Object other) {
// 
// return other instanceof IdentityWrapper
// && ((IdentityWrapper) other).instance == instance;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("equals", other).as(boolean.class);
}
        public T getObject() {
// 
// return instance;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getObject").as(T.class);
}
        public IdentityWrapper(final T instance) {
// 
// this.instance = instance;
// 

this.obj = clz.invokeMember("__init__", instance);
}
}
    private class StatsStore {
        private static final int NULL = -1;
    private static Value clz = ContextInitializer.getPythonClass("/BaseGenericObjectPool.py", "StatsStore");
    private Value obj;
    public StatsStore(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// final StringBuilder builder = new StringBuilder();
// builder.append("StatsStore [");
// builder.append(getCurrentValues());
// builder.append("], size=");
// builder.append(size);
// builder.append(", index=");
// builder.append(index);
// builder.append("]");
// return builder.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public long getMean() {
// 
// double result = 0;
// int counter = 0;
// for (int i = 0; i < size; i++) {
// final long value = values[i].get();
// if (value != NULL) {
// counter++;
// result = result * ((counter - 1) / (double) counter) + value / (double) counter;
// }
// }
// return (long) result;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getMean").as(long.class);
}
        synchronized List<AtomicLong> getCurrentValues() {
// 
// return Arrays.stream(values, 0, index).collect(Collectors.toList());
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getCurrentValues").as(List.class);
}
        synchronized void add1(final long value) {
// 
// values[index].set(value);
// index++;
// if (index == size) {
// index = 0;
// }
// 

obj.invokeMember("add1", value);
}
        void add0(final Duration value) {
// 
// add1(value.toMillis());
// 

obj.invokeMember("add0", value);
}
        StatsStore(final int size) {
// 
// this.size = size;
// values = new AtomicLong[size];
// for (int i = 0; i < size; i++) {
// values[i] = new AtomicLong(NULL);
// }
// 

this.obj = clz.invokeMember("__init__", size);
}
}
    class Evictor {
    private static Value clz = ContextInitializer.getPythonClass("/BaseGenericObjectPool.py", "Evictor");
    private Value obj;
    public Evictor(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        void setScheduledFuture(final ScheduledFuture<?> scheduledFuture) {
// 
// this.scheduledFuture = scheduledFuture;
// 

obj.invokeMember("setScheduledFuture", scheduledFuture);
}
        void cancel() {
// 
// scheduledFuture.cancel(false);
// 

obj.invokeMember("cancel");
}
}
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
    private static Value clz = ContextInitializer.getPythonClass("/BaseGenericObjectPool.py", "new Consumer<PooledObject<T>>(...) { ... }");
    private Value obj;
    public new Consumer<PooledObject<T>>(...) { ... }(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
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
}
}
