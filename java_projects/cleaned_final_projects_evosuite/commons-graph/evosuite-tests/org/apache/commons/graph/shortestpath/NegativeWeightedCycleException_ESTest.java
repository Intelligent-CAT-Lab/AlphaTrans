
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


package org.apache.commons.graph.shortestpath;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.UnknownFormatConversionException;
import org.apache.commons.graph.shortestpath.NegativeWeightedCycleException;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.lang.MockThrowable;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class NegativeWeightedCycleException_ESTest extends NegativeWeightedCycleException_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      MockThrowable mockThrowable0 = new MockThrowable("");
      Object[] objectArray0 = new Object[3];
      NegativeWeightedCycleException negativeWeightedCycleException0 = null;
      try {
        negativeWeightedCycleException0 = new NegativeWeightedCycleException("a%mGB+4,$>", mockThrowable0, objectArray0);
        fail("Expecting exception: UnknownFormatConversionException");
      
      } catch(UnknownFormatConversionException e) {
         //
         // Conversion = 'm'
         //
         verifyException("java.util.Formatter$FormatSpecifier", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Object[] objectArray0 = new Object[9];
      NegativeWeightedCycleException negativeWeightedCycleException0 = new NegativeWeightedCycleException((String) null, (Throwable) null, objectArray0);
      MockThrowable mockThrowable0 = new MockThrowable("qlp$", negativeWeightedCycleException0);
      NegativeWeightedCycleException negativeWeightedCycleException1 = null;
      try {
        negativeWeightedCycleException1 = new NegativeWeightedCycleException((String) null, mockThrowable0, objectArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }
}
