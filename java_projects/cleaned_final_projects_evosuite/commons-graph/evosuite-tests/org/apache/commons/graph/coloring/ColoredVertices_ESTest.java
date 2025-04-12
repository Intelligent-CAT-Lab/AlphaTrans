
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


package org.apache.commons.graph.coloring;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.coloring.ColoredVertices;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ColoredVertices_ESTest extends ColoredVertices_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      Integer integer0 = new Integer(0);
      Integer integer1 = coloredVertices0.getColor(integer0);
      coloredVertices0.addColor(integer0, integer0);
      coloredVertices0.addColor(integer1, integer0);
      assertEquals(1, coloredVertices0.getRequiredColors());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      Integer integer0 = new Integer((-1193));
      coloredVertices0.addColor(integer0, integer0);
      int int0 = coloredVertices0.getRequiredColors();
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      // Undeclared exception!
      try { 
        coloredVertices0.getColor((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to get the color for a null Vertex
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      Integer integer0 = new Integer((-1193));
      coloredVertices0.addColor(integer0, integer0);
      boolean boolean0 = coloredVertices0.containsColoredVertex(integer0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      Integer integer0 = new Integer((-1193));
      boolean boolean0 = coloredVertices0.containsColoredVertex(integer0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      Integer integer0 = new Integer((-1193));
      coloredVertices0.removeColor(integer0);
      assertEquals(0, coloredVertices0.getRequiredColors());
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      Integer integer0 = new Integer((-1193));
      Integer integer1 = coloredVertices0.getColor(integer0);
      coloredVertices0.addColor(integer0, integer1);
      assertEquals(1, coloredVertices0.getRequiredColors());
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      int int0 = coloredVertices0.getRequiredColors();
      assertEquals(0, int0);
  }
}
