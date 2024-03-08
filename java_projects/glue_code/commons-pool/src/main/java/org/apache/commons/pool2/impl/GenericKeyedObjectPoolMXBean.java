package org.apache.commons.pool;

import java.util.List;
import java.util.Map;

public interface GenericKeyedObjectPoolMXBean<K> {
  Map<String, List<DefaultPooledObjectInfo>> listAllObjects();

  boolean isClosed();

  long getTimeBetweenEvictionRunsMillis();

  boolean getTestWhileIdle();

  boolean getTestOnReturn();

  boolean getTestOnCreate();

  boolean getTestOnBorrow();

  long getReturnedCount();

  Map<String, Integer> getNumWaitersByKey();

  int getNumWaiters();

  int getNumTestsPerEvictionRun();

  int getNumIdle();

  Map<String, Integer> getNumActivePerKey();

  int getNumActive();

  int getMinIdlePerKey();

  long getMinEvictableIdleTimeMillis();

  long getMeanIdleTimeMillis();

  long getMeanBorrowWaitTimeMillis();

  long getMeanActiveTimeMillis();

  long getMaxWaitMillis();

  int getMaxTotalPerKey();

  int getMaxTotal();

  int getMaxIdlePerKey();

  long getMaxBorrowWaitTimeMillis();

  boolean getLifo();

  boolean getFairness();

  long getDestroyedCount();

  long getDestroyedByEvictorCount();

  long getDestroyedByBorrowValidationCount();

  String getCreationStackTrace();

  long getCreatedCount();

  long getBorrowedCount();

  boolean getBlockWhenExhausted();

  default boolean isAbandonedConfig() {
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isAbandonedConfig").as(boolean.class);
  }

  default int getRemoveAbandonedTimeout() {
    //
    // return 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRemoveAbandonedTimeout").as(int.class);
  }

  default boolean getRemoveAbandonedOnMaintenance() {
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRemoveAbandonedOnMaintenance").as(boolean.class);
  }

  default boolean getRemoveAbandonedOnBorrow() {
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRemoveAbandonedOnBorrow").as(boolean.class);
  }

  default boolean getLogAbandoned() {
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLogAbandoned").as(boolean.class);
  }
}
