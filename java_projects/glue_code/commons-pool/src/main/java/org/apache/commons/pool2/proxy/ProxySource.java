package org.apache.commons.pool;

import org.apache.commons.pool2.UsageTracking;

interface ProxySource<T> {
  T resolveProxy(T proxy);

  T createProxy(T pooledObject, UsageTracking<T> usageTracking);
}
