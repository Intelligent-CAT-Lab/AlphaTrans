package org.apache.commons.pool;

import java.time.Instant;

public interface TrackedUse {
  long getLastUsed();

  default Instant getLastUsedInstant() {
    //
    // return Instant.ofEpochMilli(getLastUsed());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastUsedInstant").as(Instant.class);
  }
}
