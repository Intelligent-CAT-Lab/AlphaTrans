package org.apache.commons.pool;

import java.util.Set;

public interface GenericObjectPoolMXBean {
  Set<DefaultPooledObjectInfo> listAllObjects();

  boolean isClosed();

  boolean isAbandonedConfig();

  long getTimeBetweenEvictionRunsMillis();

  boolean getTestWhileIdle();

  boolean getTestOnReturn();

  boolean getTestOnCreate();

  boolean getTestOnBorrow();

  long getReturnedCount();

  int getRemoveAbandonedTimeout();

  boolean getRemoveAbandonedOnMaintenance();

  boolean getRemoveAbandonedOnBorrow();

  int getNumWaiters();

  int getNumTestsPerEvictionRun();

  int getNumIdle();

  int getNumActive();

  int getMinIdle();

  long getMinEvictableIdleTimeMillis();

  long getMeanIdleTimeMillis();

  long getMeanBorrowWaitTimeMillis();

  long getMeanActiveTimeMillis();

  long getMaxWaitMillis();

  int getMaxTotal();

  int getMaxIdle();

  long getMaxBorrowWaitTimeMillis();

  boolean getLogAbandoned();

  boolean getLifo();

  boolean getFairness();

  String getFactoryType();

  long getDestroyedCount();

  long getDestroyedByEvictorCount();

  long getDestroyedByBorrowValidationCount();

  String getCreationStackTrace();

  long getCreatedCount();

  long getBorrowedCount();

  boolean getBlockWhenExhausted();
}
