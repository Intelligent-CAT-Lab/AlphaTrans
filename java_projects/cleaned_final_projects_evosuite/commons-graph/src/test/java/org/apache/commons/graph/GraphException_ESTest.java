
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


package org.apache.commons.graph;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.UnknownFormatConversionException;
import org.apache.commons.graph.GraphException;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.lang.MockThrowable;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class GraphException_ESTest extends GraphException_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      MockThrowable mockThrowable0 = new MockThrowable((String) null, (Throwable) null);
      Throwable[] throwableArray0 = mockThrowable0.getSuppressed();
      GraphException graphException0 = new GraphException("", mockThrowable0, throwableArray0);
      GraphException graphException1 = null;
      try {
        graphException1 = new GraphException("%?A?(S~uPlt", graphException0, throwableArray0);
        fail("Expecting exception: UnknownFormatConversionException");
      
      } catch(UnknownFormatConversionException e) {
         //
         // Conversion = '?'
         //
         verifyException("java.util.Formatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      MockThrowable mockThrowable0 = new MockThrowable("org.apache.commons.graph.GraphException");
      Object[] objectArray0 = new Object[1];
      GraphException graphException0 = new GraphException("org.apache.commons.graph.GraphException", mockThrowable0, objectArray0);
      GraphException graphException1 = null;
      try {
        graphException1 = new GraphException((String) null, graphException0, objectArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Object[] objectArray0 = new Object[8];
      GraphException graphException0 = new GraphException("3yD", (Throwable) null, objectArray0);
      GraphException graphException1 = new GraphException("\"WaDD1~$b_0", graphException0, objectArray0);
      assertFalse(graphException1.equals((Object)graphException0));
  }
}
