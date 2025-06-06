package org.apache.commons.graph.model;


/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */


import static org.apache.commons.graph.utils.Assertions.checkNotNull;
import static org.apache.commons.graph.utils.Objects.eq;
import static org.apache.commons.graph.utils.Objects.hash;

import static java.lang.String.format;

/** */
public class BaseLabeledWeightedEdge<W> extends BaseLabeledEdge {

    private static final long serialVersionUID = 5935967858178091436L;

    private final W weight;

    public BaseLabeledWeightedEdge(String label, W weight) {
        super(label);
        this.weight = checkNotNull(weight, "Argument 'weight' must not be null");
    }

    /** {@inheritDoc} */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }

        if (!super.equals(obj)) {
            return false;
        }

        if (getClass() != obj.getClass()) {
            return false;
        }
        @SuppressWarnings("unchecked")
        BaseLabeledWeightedEdge<W> other = (BaseLabeledWeightedEdge<W>) obj;
        return eq(weight, other.getWeight());
    }

    /** {@inheritDoc} */
    public W getWeight() {
        return weight;
    }

    /** {@inheritDoc} */
    @Override
    public int hashCode() {
        return hash(super.hashCode(), 31, weight);
    }

    /** {@inheritDoc} */
    @Override
    public String toString() {
        return format("%s( %s )", getLabel(), weight);
    }
}
