
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

package org.joda.convert;

/** Example class with no annotations. */
public class DistanceNoAnnotationsCharSequence {

    /** Amount. */
    final int amount;

    public static DistanceNoAnnotationsCharSequence parse(CharSequence amount) {
        return new DistanceNoAnnotationsCharSequence(0, amount, 0);
    }

    public DistanceNoAnnotationsCharSequence(int constructorId, CharSequence amount1, int amount) {
        if (constructorId == 0) {

            String amt = amount1.toString().substring(0, amount1.length() - 1);
            this.amount = Integer.parseInt(amt);
        } else {

            this.amount = amount;
        }
    }

    public String print() {
        return amount + "m";
    }

    @Override
    public String toString() {
        return "Distance[" + amount + "m]";
    }
}
