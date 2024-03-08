package org.apache.commons.pool;


public interface DefaultPooledObjectInfoMBean {
  String getPooledObjectType();

  String getPooledObjectToString();

  String getLastReturnTimeFormatted();

  long getLastReturnTime();

  String getLastBorrowTrace();

  String getLastBorrowTimeFormatted();

  long getLastBorrowTime();

  String getCreateTimeFormatted();

  long getCreateTime();

  long getBorrowedCount();
}
