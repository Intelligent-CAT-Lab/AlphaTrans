package org.apache.commons.pool;

import java.time.Duration;
import org.apache.commons.pool2.BaseObject;
import org.graalvm.polyglot.Value;

public abstract class BaseObjectPoolConfig<T> extends BaseObject implements Cloneable {
  public static final String DEFAULT_EVICTION_POLICY_CLASS_NAME =
      DefaultEvictionPolicy.class.getName();
  public static final String DEFAULT_JMX_NAME_BASE = null;
  public static final String DEFAULT_JMX_NAME_PREFIX = "pool";
  public static final boolean DEFAULT_JMX_ENABLE = true;
  public static final boolean DEFAULT_BLOCK_WHEN_EXHAUSTED = true;
  public static final Duration DEFAULT_TIME_BETWEEN_EVICTION_RUNS =
      Duration.ofMillis(DEFAULT_TIME_BETWEEN_EVICTION_RUNS_MILLIS);
  @Deprecated public static final long DEFAULT_TIME_BETWEEN_EVICTION_RUNS_MILLIS = -1L;
  public static final boolean DEFAULT_TEST_WHILE_IDLE = false;
  public static final boolean DEFAULT_TEST_ON_RETURN = false;
  public static final boolean DEFAULT_TEST_ON_BORROW = false;
  public static final boolean DEFAULT_TEST_ON_CREATE = false;
  public static final int DEFAULT_NUM_TESTS_PER_EVICTION_RUN = 3;
  public static final Duration DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT =
      Duration.ofMillis(DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT_MILLIS);
  @Deprecated public static final long DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT_MILLIS = 10L * 1000L;
  public static final Duration DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION =
      Duration.ofMillis(DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME_MILLIS);

  @Deprecated
  public static final Duration DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME =
      Duration.ofMillis(DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME_MILLIS);

  @Deprecated public static final long DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME_MILLIS = -1;

  @Deprecated
  public static final Duration DEFAULT_MIN_EVICTABLE_IDLE_TIME =
      Duration.ofMillis(DEFAULT_MIN_EVICTABLE_IDLE_TIME_MILLIS);

  public static final Duration DEFAULT_MIN_EVICTABLE_IDLE_DURATION =
      Duration.ofMillis(DEFAULT_MIN_EVICTABLE_IDLE_TIME_MILLIS);
  @Deprecated public static final long DEFAULT_MIN_EVICTABLE_IDLE_TIME_MILLIS = 1000L * 60L * 30L;
  public static final Duration DEFAULT_MAX_WAIT = Duration.ofMillis(DEFAULT_MAX_WAIT_MILLIS);
  @Deprecated public static final long DEFAULT_MAX_WAIT_MILLIS = -1L;
  public static final boolean DEFAULT_FAIRNESS = false;
  public static final boolean DEFAULT_LIFO = true;
  private String jmxNameBase = DEFAULT_JMX_NAME_BASE;
  private String jmxNamePrefix = DEFAULT_JMX_NAME_PREFIX;
  private boolean jmxEnabled = DEFAULT_JMX_ENABLE;
  private boolean blockWhenExhausted = DEFAULT_BLOCK_WHEN_EXHAUSTED;
  private Duration durationBetweenEvictionRuns = DEFAULT_TIME_BETWEEN_EVICTION_RUNS;
  private boolean testWhileIdle = DEFAULT_TEST_WHILE_IDLE;
  private boolean testOnReturn = DEFAULT_TEST_ON_RETURN;
  private boolean testOnBorrow = DEFAULT_TEST_ON_BORROW;
  private boolean testOnCreate = DEFAULT_TEST_ON_CREATE;
  private String evictionPolicyClassName = DEFAULT_EVICTION_POLICY_CLASS_NAME;
  private int numTestsPerEvictionRun = DEFAULT_NUM_TESTS_PER_EVICTION_RUN;
  private Duration softMinEvictableIdleDuration = DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME;
  private Duration evictorShutdownTimeoutDuration = DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT;
  private Duration minEvictableIdleDuration = DEFAULT_MIN_EVICTABLE_IDLE_TIME;
  private Duration maxWaitDuration = DEFAULT_MAX_WAIT;
  private boolean fairness = DEFAULT_FAIRNESS;
  private boolean lifo = DEFAULT_LIFO;
  private static Value clz =
      ContextInitializer.getPythonClass("/BaseObjectPoolConfig.py", "BaseObjectPoolConfig");
  private Value obj;

  public BaseObjectPoolConfig(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected void toStringAppendFields(final StringBuilder builder) {
    //
    // builder.append("lifo=");
    // builder.append(lifo);
    // builder.append(", fairness=");
    // builder.append(fairness);
    // builder.append(", maxWaitDuration=");
    // builder.append(maxWaitDuration);
    // builder.append(", minEvictableIdleTime=");
    // builder.append(minEvictableIdleDuration);
    // builder.append(", softMinEvictableIdleTime=");
    // builder.append(softMinEvictableIdleDuration);
    // builder.append(", numTestsPerEvictionRun=");
    // builder.append(numTestsPerEvictionRun);
    // builder.append(", evictionPolicyClassName=");
    // builder.append(evictionPolicyClassName);
    // builder.append(", testOnCreate=");
    // builder.append(testOnCreate);
    // builder.append(", testOnBorrow=");
    // builder.append(testOnBorrow);
    // builder.append(", testOnReturn=");
    // builder.append(testOnReturn);
    // builder.append(", testWhileIdle=");
    // builder.append(testWhileIdle);
    // builder.append(", timeBetweenEvictionRuns=");
    // builder.append(durationBetweenEvictionRuns);
    // builder.append(", blockWhenExhausted=");
    // builder.append(blockWhenExhausted);
    // builder.append(", jmxEnabled=");
    // builder.append(jmxEnabled);
    // builder.append(", jmxNamePrefix=");
    // builder.append(jmxNamePrefix);
    // builder.append(", jmxNameBase=");
    // builder.append(jmxNameBase);
    //

    obj.invokeMember("toStringAppendFields", builder);
  }

  public void setTimeBetweenEvictionRunsMillis(final long timeBetweenEvictionRunsMillis) {
    //
    // setTimeBetweenEvictionRuns(Duration.ofMillis(timeBetweenEvictionRunsMillis));
    //

    obj.invokeMember("setTimeBetweenEvictionRunsMillis", timeBetweenEvictionRunsMillis);
  }

  public void setSoftMinEvictableIdleTimeMillis(final long softMinEvictableIdleTimeMillis) {
    //
    // setSoftMinEvictableIdleTime(Duration.ofMillis(softMinEvictableIdleTimeMillis));
    //

    obj.invokeMember("setSoftMinEvictableIdleTimeMillis", softMinEvictableIdleTimeMillis);
  }

  public void setMinEvictableIdleTimeMillis(final long minEvictableIdleTimeMillis) {
    //
    // this.minEvictableIdleDuration = Duration.ofMillis(minEvictableIdleTimeMillis);
    //

    obj.invokeMember("setMinEvictableIdleTimeMillis", minEvictableIdleTimeMillis);
  }

  public void setMaxWaitMillis(final long maxWaitMillis) {
    //
    // setMaxWait(Duration.ofMillis(maxWaitMillis));
    //

    obj.invokeMember("setMaxWaitMillis", maxWaitMillis);
  }

  public void setEvictorShutdownTimeoutMillis1(final long evictorShutdownTimeoutMillis) {
    //
    // setEvictorShutdownTimeout(Duration.ofMillis(evictorShutdownTimeoutMillis));
    //

    obj.invokeMember("setEvictorShutdownTimeoutMillis1", evictorShutdownTimeoutMillis);
  }

  public void setEvictorShutdownTimeoutMillis0(final Duration evictorShutdownTimeout) {
    //
    // setEvictorShutdownTimeout(evictorShutdownTimeout);
    //

    obj.invokeMember("setEvictorShutdownTimeoutMillis0", evictorShutdownTimeout);
  }

  public long getTimeBetweenEvictionRunsMillis() {
    //
    // return durationBetweenEvictionRuns.toMillis();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getTimeBetweenEvictionRunsMillis").as(long.class);
  }

  public Duration getTimeBetweenEvictionRuns() {
    //
    // return durationBetweenEvictionRuns;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getTimeBetweenEvictionRuns").as(Duration.class);
  }

  public long getSoftMinEvictableIdleTimeMillis() {
    //
    // return softMinEvictableIdleDuration.toMillis();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSoftMinEvictableIdleTimeMillis").as(long.class);
  }

  public Duration getSoftMinEvictableIdleTime() {
    //
    // return softMinEvictableIdleDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSoftMinEvictableIdleTime").as(Duration.class);
  }

  public long getMinEvictableIdleTimeMillis() {
    //
    // return minEvictableIdleDuration.toMillis();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMinEvictableIdleTimeMillis").as(long.class);
  }

  public Duration getMinEvictableIdleTime() {
    //
    // return minEvictableIdleDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMinEvictableIdleTime").as(Duration.class);
  }

  public long getMaxWaitMillis() {
    //
    // return maxWaitDuration.toMillis();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxWaitMillis").as(long.class);
  }

  public long getEvictorShutdownTimeoutMillis() {
    //
    // return evictorShutdownTimeoutDuration.toMillis();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEvictorShutdownTimeoutMillis").as(long.class);
  }

  public Duration getEvictorShutdownTimeout() {
    //
    // return evictorShutdownTimeoutDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEvictorShutdownTimeout").as(Duration.class);
  }

  public void setTimeBetweenEvictionRuns(final Duration timeBetweenEvictionRuns) {
    //
    // this.durationBetweenEvictionRuns =
    // PoolImplUtils.nonNull(timeBetweenEvictionRuns, DEFAULT_TIME_BETWEEN_EVICTION_RUNS);
    //

    obj.invokeMember("setTimeBetweenEvictionRuns", timeBetweenEvictionRuns);
  }

  public void setTestWhileIdle(final boolean testWhileIdle) {
    //
    // this.testWhileIdle = testWhileIdle;
    //

    obj.invokeMember("setTestWhileIdle", testWhileIdle);
  }

  public void setTestOnReturn(final boolean testOnReturn) {
    //
    // this.testOnReturn = testOnReturn;
    //

    obj.invokeMember("setTestOnReturn", testOnReturn);
  }

  public void setTestOnCreate(final boolean testOnCreate) {
    //
    // this.testOnCreate = testOnCreate;
    //

    obj.invokeMember("setTestOnCreate", testOnCreate);
  }

  public void setTestOnBorrow(final boolean testOnBorrow) {
    //
    // this.testOnBorrow = testOnBorrow;
    //

    obj.invokeMember("setTestOnBorrow", testOnBorrow);
  }

  public void setSoftMinEvictableIdleTime(final Duration softMinEvictableIdleTime) {
    //
    // this.softMinEvictableIdleDuration =
    // PoolImplUtils.nonNull(
    // softMinEvictableIdleTime, DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME);
    //

    obj.invokeMember("setSoftMinEvictableIdleTime", softMinEvictableIdleTime);
  }

  public void setNumTestsPerEvictionRun(final int numTestsPerEvictionRun) {
    //
    // this.numTestsPerEvictionRun = numTestsPerEvictionRun;
    //

    obj.invokeMember("setNumTestsPerEvictionRun", numTestsPerEvictionRun);
  }

  public void setMinEvictableIdleTime(final Duration minEvictableIdleTime) {
    //
    // this.minEvictableIdleDuration =
    // PoolImplUtils.nonNull(minEvictableIdleTime, DEFAULT_MIN_EVICTABLE_IDLE_TIME);
    //

    obj.invokeMember("setMinEvictableIdleTime", minEvictableIdleTime);
  }

  public void setMaxWait(final Duration maxWaitDuration) {
    //
    // this.maxWaitDuration = PoolImplUtils.nonNull(maxWaitDuration, DEFAULT_MAX_WAIT);
    //

    obj.invokeMember("setMaxWait", maxWaitDuration);
  }

  public void setLifo(final boolean lifo) {
    //
    // this.lifo = lifo;
    //

    obj.invokeMember("setLifo", lifo);
  }

  public void setJmxNamePrefix(final String jmxNamePrefix) {
    //
    // this.jmxNamePrefix = jmxNamePrefix;
    //

    obj.invokeMember("setJmxNamePrefix", jmxNamePrefix);
  }

  public void setJmxNameBase(final String jmxNameBase) {
    //
    // this.jmxNameBase = jmxNameBase;
    //

    obj.invokeMember("setJmxNameBase", jmxNameBase);
  }

  public void setJmxEnabled(final boolean jmxEnabled) {
    //
    // this.jmxEnabled = jmxEnabled;
    //

    obj.invokeMember("setJmxEnabled", jmxEnabled);
  }

  public void setFairness(final boolean fairness) {
    //
    // this.fairness = fairness;
    //

    obj.invokeMember("setFairness", fairness);
  }

  public void setEvictorShutdownTimeout(final Duration evictorShutdownTimeoutDuration) {
    //
    // this.evictorShutdownTimeoutDuration =
    // PoolImplUtils.nonNull(
    // evictorShutdownTimeoutDuration, DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT);
    //

    obj.invokeMember("setEvictorShutdownTimeout", evictorShutdownTimeoutDuration);
  }

  public void setEvictionPolicyClassName(final String evictionPolicyClassName) {
    //
    // this.evictionPolicyClassName = evictionPolicyClassName;
    //

    obj.invokeMember("setEvictionPolicyClassName", evictionPolicyClassName);
  }

  public void setEvictionPolicy(final EvictionPolicy<T> evictionPolicy) {
    //
    // this.evictionPolicy = evictionPolicy;
    //

    obj.invokeMember("setEvictionPolicy", evictionPolicy);
  }

  public void setBlockWhenExhausted(final boolean blockWhenExhausted) {
    //
    // this.blockWhenExhausted = blockWhenExhausted;
    //

    obj.invokeMember("setBlockWhenExhausted", blockWhenExhausted);
  }

  public Duration getDurationBetweenEvictionRuns() {
    //
    // return durationBetweenEvictionRuns;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDurationBetweenEvictionRuns").as(Duration.class);
  }

  public boolean getTestWhileIdle() {
    //
    // return testWhileIdle;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getTestWhileIdle").as(boolean.class);
  }

  public boolean getTestOnReturn() {
    //
    // return testOnReturn;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getTestOnReturn").as(boolean.class);
  }

  public boolean getTestOnCreate() {
    //
    // return testOnCreate;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getTestOnCreate").as(boolean.class);
  }

  public boolean getTestOnBorrow() {
    //
    // return testOnBorrow;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getTestOnBorrow").as(boolean.class);
  }

  public Duration getSoftMinEvictableIdleDuration() {
    //
    // return softMinEvictableIdleDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSoftMinEvictableIdleDuration").as(Duration.class);
  }

  public int getNumTestsPerEvictionRun() {
    //
    // return numTestsPerEvictionRun;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getNumTestsPerEvictionRun").as(int.class);
  }

  public Duration getMinEvictableIdleDuration() {
    //
    // return minEvictableIdleDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMinEvictableIdleDuration").as(Duration.class);
  }

  public Duration getMaxWaitDuration() {
    //
    // return maxWaitDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxWaitDuration").as(Duration.class);
  }

  public boolean getLifo() {
    //
    // return lifo;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLifo").as(boolean.class);
  }

  public String getJmxNamePrefix() {
    //
    // return jmxNamePrefix;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getJmxNamePrefix").as(String.class);
  }

  public String getJmxNameBase() {
    //
    // return jmxNameBase;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getJmxNameBase").as(String.class);
  }

  public boolean getJmxEnabled() {
    //
    // return jmxEnabled;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getJmxEnabled").as(boolean.class);
  }

  public boolean getFairness() {
    //
    // return fairness;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFairness").as(boolean.class);
  }

  public Duration getEvictorShutdownTimeoutDuration() {
    //
    // return evictorShutdownTimeoutDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEvictorShutdownTimeoutDuration").as(Duration.class);
  }

  public String getEvictionPolicyClassName() {
    //
    // return evictionPolicyClassName;
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

  public boolean getBlockWhenExhausted() {
    //
    // return blockWhenExhausted;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getBlockWhenExhausted").as(boolean.class);
  }
}
