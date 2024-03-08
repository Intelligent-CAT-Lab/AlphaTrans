package org.apache.commons.pool;

import org.apache.commons.pool2.PooledObject;
import org.graalvm.polyglot.Value;

public class DefaultEvictionPolicy<T> implements EvictionPolicy<T> {
  private static Value clz =
      ContextInitializer.getPythonClass("/DefaultEvictionPolicy.py", "DefaultEvictionPolicy");
  private Value obj;

  public DefaultEvictionPolicy(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean evict(
      final EvictionConfig config, final PooledObject<T> underTest, final int idleCount) {
    //
    // return (config.getIdleSoftEvictDuration().compareTo(underTest.getIdleDuration()) < 0
    // && config.getMinIdle() < idleCount)
    // || config.getIdleEvictDuration().compareTo(underTest.getIdleDuration()) < 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("evict", config, underTest, idleCount).as(boolean.class);
  }
}
