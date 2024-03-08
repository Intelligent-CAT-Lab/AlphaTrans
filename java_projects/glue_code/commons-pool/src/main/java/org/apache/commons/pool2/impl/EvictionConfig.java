package org.apache.commons.pool;

import java.time.Duration;
import org.graalvm.polyglot.Value;

public class EvictionConfig {
  private static final Duration MAX_DURATION = Duration.ofMillis(Long.MAX_VALUE);
  private static Value clz =
      ContextInitializer.getPythonClass("/EvictionConfig.py", "EvictionConfig");
  private Value obj;

  public EvictionConfig(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder builder = new StringBuilder();
    // builder.append("EvictionConfig [idleEvictDuration=");
    // builder.append(idleEvictDuration);
    // builder.append(", idleSoftEvictDuration=");
    // builder.append(idleSoftEvictDuration);
    // builder.append(", minIdle=");
    // builder.append(minIdle);
    // builder.append("]");
    // return builder.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public Duration getIdleSoftEvictTimeDuration() {
    //
    // return idleSoftEvictDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIdleSoftEvictTimeDuration").as(Duration.class);
  }

  public long getIdleSoftEvictTime() {
    //
    // return idleSoftEvictDuration.toMillis();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIdleSoftEvictTime").as(long.class);
  }

  public Duration getIdleEvictTimeDuration() {
    //
    // return idleEvictDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIdleEvictTimeDuration").as(Duration.class);
  }

  public long getIdleEvictTime() {
    //
    // return idleEvictDuration.toMillis();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIdleEvictTime").as(long.class);
  }

  public static EvictionConfig EvictionConfig0(
      final long poolIdleEvictMillis, final long poolIdleSoftEvictMillis, final int minIdle) {
    //
    // return new EvictionConfig(
    // Duration.ofMillis(poolIdleEvictMillis),
    // Duration.ofMillis(poolIdleSoftEvictMillis),
    // minIdle);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember(
            "EvictionConfig0", poolIdleEvictMillis, poolIdleSoftEvictMillis, minIdle)
        .as(EvictionConfig.class);
  }

  public int getMinIdle() {
    //
    // return minIdle;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMinIdle").as(int.class);
  }

  public Duration getIdleSoftEvictDuration() {
    //
    // return idleSoftEvictDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIdleSoftEvictDuration").as(Duration.class);
  }

  public Duration getIdleEvictDuration() {
    //
    // return idleEvictDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIdleEvictDuration").as(Duration.class);
  }

  public EvictionConfig(
      final Duration idleEvictDuration, final Duration idleSoftEvictDuration, final int minIdle) {
    //
    // this.idleEvictDuration =
    // PoolImplUtils.isPositive(idleEvictDuration) ? idleEvictDuration : MAX_DURATION;
    // this.idleSoftEvictDuration =
    // PoolImplUtils.isPositive(idleSoftEvictDuration)
    // ? idleSoftEvictDuration
    // : MAX_DURATION;
    // this.minIdle = minIdle;
    //

    this.obj = clz.invokeMember("__init__", idleEvictDuration, idleSoftEvictDuration, minIdle);
  }
}
