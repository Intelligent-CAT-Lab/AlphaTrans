
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


package org.apache.commons.graph.spanning;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.Comparator;
import java.util.function.Function;
import java.util.function.ToDoubleFunction;
import java.util.function.ToIntFunction;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.spanning.WeightedEdgesComparator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class WeightedEdgesComparator_ESTest extends WeightedEdgesComparator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      ToDoubleFunction<Integer> toDoubleFunction0 = (ToDoubleFunction<Integer>) mock(ToDoubleFunction.class, new ViolatedAssumptionAnswer());
      doReturn(0.0, 0.0).when(toDoubleFunction0).applyAsDouble(anyInt());
      Comparator<Integer> comparator0 = Comparator.comparingDouble((ToDoubleFunction<? super Integer>) toDoubleFunction0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null, (Object) null).when(mapper0).map(anyInt());
      WeightedEdgesComparator<Integer, Integer> weightedEdgesComparator0 = new WeightedEdgesComparator<Integer, Integer>(comparator0, mapper0);
      Integer integer0 = new Integer(0);
      int int0 = weightedEdgesComparator0.compare(integer0, integer0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      ToIntFunction<Integer> toIntFunction0 = (ToIntFunction<Integer>) mock(ToIntFunction.class, new ViolatedAssumptionAnswer());
      Comparator<Integer> comparator0 = Comparator.comparingInt((ToIntFunction<? super Integer>) toIntFunction0);
      Comparator<Integer> comparator1 = Comparator.nullsLast((Comparator<? super Integer>) comparator0);
      Integer integer0 = new Integer(0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(integer0, integer0).when(mapper0).map(anyInt());
      WeightedEdgesComparator<Integer, Integer> weightedEdgesComparator0 = new WeightedEdgesComparator<Integer, Integer>(comparator1, mapper0);
      int int0 = weightedEdgesComparator0.compare((Integer) null, integer0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Function<Integer, Integer> function0 = Function.identity();
      Comparator<Integer> comparator0 = Comparator.comparing((Function<? super Integer, ? extends Integer>) function0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null, (Object) null).when(mapper0).map(anyInt());
      WeightedEdgesComparator<Integer, Integer> weightedEdgesComparator0 = new WeightedEdgesComparator<Integer, Integer>(comparator0, mapper0);
      // Undeclared exception!
      try { 
        weightedEdgesComparator0.compare((Integer) null, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Comparator", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      ToDoubleFunction<Integer> toDoubleFunction0 = (ToDoubleFunction<Integer>) mock(ToDoubleFunction.class, new ViolatedAssumptionAnswer());
      doReturn((-555.198663509436), (-555.198663509436)).when(toDoubleFunction0).applyAsDouble(anyInt());
      Comparator<Integer> comparator0 = Comparator.comparingDouble((ToDoubleFunction<? super Integer>) toDoubleFunction0);
      Integer integer0 = new Integer(1);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(integer0, (Integer) null).when(mapper0).map(anyInt());
      WeightedEdgesComparator<Integer, Integer> weightedEdgesComparator0 = new WeightedEdgesComparator<Integer, Integer>(comparator0, mapper0);
      int int0 = weightedEdgesComparator0.compare(integer0, (Integer) null);
      assertEquals((-1), int0);
  }
}
