package org.apache.commons.pool;

import java.io.PrintWriter;
import java.time.Duration;
import java.time.Instant;
import java.util.Deque;

public interface PooledObject<T> extends Comparable<PooledObject<T>> {
  void use();

  String toString();

  boolean startEvictionTest();

  void setLogAbandoned(boolean logAbandoned);

  void printStackTrace(PrintWriter writer);

  void markReturning();

  void markAbandoned();

  void invalidate();

  int hashCode();

  PooledObjectState getState();

  T getObject();

  long getLastUsedTime();

  long getLastReturnTime();

  long getLastBorrowTime();

  long getIdleTimeMillis();

  long getCreateTime();

  long getActiveTimeMillis();

  boolean equals(Object obj);

  boolean endEvictionTest(Deque<PooledObject<T>> idleQueue);

  boolean deallocate();

  int compareTo(PooledObject<T> other);

  boolean allocate();

  default void setRequireFullStackTrace(final boolean requireFullStackTrace) {
    //

    obj.invokeMember("setRequireFullStackTrace");
  }

  default Instant getLastUsedInstant() {
    //
    // return Instant.ofEpochMilli(getLastUsedTime());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastUsedInstant").as(Instant.class);
  }

  default Instant getLastReturnInstant() {
    //
    // return Instant.ofEpochMilli(getLastReturnTime());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastReturnInstant").as(Instant.class);
  }

  default Instant getLastBorrowInstant() {
    //
    // return Instant.ofEpochMilli(getLastBorrowTime());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastBorrowInstant").as(Instant.class);
  }

  default Duration getIdleTime() {
    //
    // return Duration.ofMillis(getIdleTimeMillis());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIdleTime").as(Duration.class);
  }

  default Duration getIdleDuration() {
    //
    // return Duration.ofMillis(getIdleTimeMillis());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIdleDuration").as(Duration.class);
  }

  default Instant getCreateInstant() {
    //
    // return Instant.ofEpochMilli(getCreateTime());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCreateInstant").as(Instant.class);
  }

  default long getBorrowedCount() {
    //
    // return -1;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getBorrowedCount").as(long.class);
  }

  default Duration getActiveTime() {
    //
    // return getActiveDuration();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getActiveTime").as(Duration.class);
  }

  default Duration getActiveDuration() {
    //
    // final Instant lastReturnInstant = getLastReturnInstant();
    // final Instant lastBorrowInstant = getLastBorrowInstant();
    // return lastReturnInstant.isAfter(lastBorrowInstant)
    // ? Duration.between(lastBorrowInstant, lastReturnInstant)
    // : Duration.between(lastBorrowInstant, Instant.now());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getActiveDuration").as(Duration.class);
  }
}
