package org.apache.commons.pool;

import org.apache.commons.pool2.PooledObject;

public interface EvictionPolicy<T> {
  boolean evict(EvictionConfig config, PooledObject<T> underTest, int idleCount);
}
