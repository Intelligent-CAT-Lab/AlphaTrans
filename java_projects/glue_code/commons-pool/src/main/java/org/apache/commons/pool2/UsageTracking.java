package org.apache.commons.pool;


public interface UsageTracking<T> {
  void use(T pooledObject);
}
