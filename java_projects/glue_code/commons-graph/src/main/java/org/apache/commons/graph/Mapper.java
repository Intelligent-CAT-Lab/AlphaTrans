package org.apache.commons.graph;

import java.io.Serializable;

public interface Mapper<I, O> extends Serializable {
  O map(I input);
}
