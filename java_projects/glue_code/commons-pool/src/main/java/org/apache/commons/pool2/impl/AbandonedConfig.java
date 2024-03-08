package org.apache.commons.pool;

import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.nio.charset.Charset;
import java.time.Duration;
import org.graalvm.polyglot.Value;

public class AbandonedConfig {
  private PrintWriter logWriter =
      new PrintWriter(new OutputStreamWriter(System.out, Charset.defaultCharset()));
  private boolean requireFullStackTrace = true;
  private Duration removeAbandonedTimeoutDuration = DEFAULT_REMOVE_ABANDONED_TIMEOUT_DURATION;
  private static final Duration DEFAULT_REMOVE_ABANDONED_TIMEOUT_DURATION = Duration.ofMinutes(5);
  private static Value clz =
      ContextInitializer.getPythonClass("/AbandonedConfig.py", "AbandonedConfig");
  private Value obj;

  public AbandonedConfig(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder builder = new StringBuilder();
    // builder.append("AbandonedConfig [removeAbandonedOnBorrow=");
    // builder.append(removeAbandonedOnBorrow);
    // builder.append(", removeAbandonedOnMaintenance=");
    // builder.append(removeAbandonedOnMaintenance);
    // builder.append(", removeAbandonedTimeoutDuration=");
    // builder.append(removeAbandonedTimeoutDuration);
    // builder.append(", logAbandoned=");
    // builder.append(logAbandoned);
    // builder.append(", logWriter=");
    // builder.append(logWriter);
    // builder.append(", useUsageTracking=");
    // builder.append(useUsageTracking);
    // builder.append("]");
    // return builder.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public void setRemoveAbandonedTimeout1(final int removeAbandonedTimeoutSeconds) {
    //
    // setRemoveAbandonedTimeout0(Duration.ofSeconds(removeAbandonedTimeoutSeconds));
    //

    obj.invokeMember("setRemoveAbandonedTimeout1", removeAbandonedTimeoutSeconds);
  }

  public int getRemoveAbandonedTimeout() {
    //
    // return (int) this.removeAbandonedTimeoutDuration.getSeconds();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRemoveAbandonedTimeout").as(int.class);
  }

  public boolean getLogAbandoned() {
    //
    // return this.logAbandoned;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLogAbandoned").as(boolean.class);
  }

  public void setUseUsageTracking(final boolean useUsageTracking) {
    //
    // this.useUsageTracking = useUsageTracking;
    //

    obj.invokeMember("setUseUsageTracking", useUsageTracking);
  }

  public void setRequireFullStackTrace(final boolean requireFullStackTrace) {
    //
    // this.requireFullStackTrace = requireFullStackTrace;
    //

    obj.invokeMember("setRequireFullStackTrace", requireFullStackTrace);
  }

  public void setRemoveAbandonedTimeout0(final Duration removeAbandonedTimeout) {
    //
    // this.removeAbandonedTimeoutDuration =
    // PoolImplUtils.nonNull(
    // removeAbandonedTimeout, DEFAULT_REMOVE_ABANDONED_TIMEOUT_DURATION);
    //

    obj.invokeMember("setRemoveAbandonedTimeout0", removeAbandonedTimeout);
  }

  public void setRemoveAbandonedOnMaintenance(final boolean removeAbandonedOnMaintenance) {
    //
    // this.removeAbandonedOnMaintenance = removeAbandonedOnMaintenance;
    //

    obj.invokeMember("setRemoveAbandonedOnMaintenance", removeAbandonedOnMaintenance);
  }

  public void setRemoveAbandonedOnBorrow(final boolean removeAbandonedOnBorrow) {
    //
    // this.removeAbandonedOnBorrow = removeAbandonedOnBorrow;
    //

    obj.invokeMember("setRemoveAbandonedOnBorrow", removeAbandonedOnBorrow);
  }

  public void setLogWriter(final PrintWriter logWriter) {
    //
    // this.logWriter = logWriter;
    //

    obj.invokeMember("setLogWriter", logWriter);
  }

  public void setLogAbandoned(final boolean logAbandoned) {
    //
    // this.logAbandoned = logAbandoned;
    //

    obj.invokeMember("setLogAbandoned", logAbandoned);
  }

  public boolean getUseUsageTracking() {
    //
    // return useUsageTracking;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getUseUsageTracking").as(boolean.class);
  }

  public boolean getRequireFullStackTrace() {
    //
    // return requireFullStackTrace;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRequireFullStackTrace").as(boolean.class);
  }

  public Duration getRemoveAbandonedTimeoutDuration() {
    //
    // return this.removeAbandonedTimeoutDuration;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRemoveAbandonedTimeoutDuration").as(Duration.class);
  }

  public boolean getRemoveAbandonedOnMaintenance() {
    //
    // return this.removeAbandonedOnMaintenance;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRemoveAbandonedOnMaintenance").as(boolean.class);
  }

  public boolean getRemoveAbandonedOnBorrow() {
    //
    // return this.removeAbandonedOnBorrow;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRemoveAbandonedOnBorrow").as(boolean.class);
  }

  public PrintWriter getLogWriter() {
    //
    // return logWriter;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLogWriter").as(PrintWriter.class);
  }

  public AbandonedConfig(int constructorId, final AbandonedConfig abandonedConfig) {
    //
    // if (constructorId == 0) {
    //
    // this.setLogAbandoned(abandonedConfig.getLogAbandoned());
    // this.setLogWriter(abandonedConfig.getLogWriter());
    // this.setRemoveAbandonedOnBorrow(abandonedConfig.getRemoveAbandonedOnBorrow());
    // this.setRemoveAbandonedOnMaintenance(abandonedConfig.getRemoveAbandonedOnMaintenance());
    // this.setRemoveAbandonedTimeout0(abandonedConfig.getRemoveAbandonedTimeoutDuration());
    // this.setUseUsageTracking(abandonedConfig.getUseUsageTracking());
    // this.setRequireFullStackTrace(abandonedConfig.getRequireFullStackTrace());
    // } else {
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, abandonedConfig);
  }

  public static AbandonedConfig copy(final AbandonedConfig abandonedConfig) {
    //
    // return abandonedConfig == null ? null : new AbandonedConfig(0, abandonedConfig);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("copy", abandonedConfig).as(AbandonedConfig.class);
  }
}
