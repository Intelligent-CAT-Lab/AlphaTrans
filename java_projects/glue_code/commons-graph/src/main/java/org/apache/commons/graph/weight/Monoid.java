package org.apache.commons.graph.weight;

import java.io.Serializable;

public interface Monoid<E> extends Serializable {
  E inverse(E element);

  E identity();

  E append(E e1, E e2);
}
