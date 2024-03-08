package org.apache.commons.pool;


public interface SwallowedExceptionListener {
  void onSwallowException(Exception e);
}
