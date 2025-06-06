
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


package org.apache.commons.graph.export;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.export.DefaultExportSelector;
import org.apache.commons.graph.export.DotExporter;
import org.apache.commons.graph.export.ExportSelector;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.weight.Monoid;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultExportSelector_ESTest extends DefaultExportSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      UndirectedMutableGraph<String, String> undirectedMutableGraph0 = new UndirectedMutableGraph<String, String>();
      DefaultExportSelector<String, String> defaultExportSelector0 = new DefaultExportSelector<String, String>(undirectedMutableGraph0);
      // Undeclared exception!
      try { 
        defaultExportSelector0.withName((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Graph name cannot be null.
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Monoid<String> monoid0 = (Monoid<String>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(monoid0).identity();
      Mapper<String, String> mapper0 = (Mapper<String, String>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<String, String, String> mutableSpanningTree0 = new MutableSpanningTree<String, String, String>(monoid0, mapper0);
      DefaultExportSelector<String, String> defaultExportSelector0 = new DefaultExportSelector<String, String>(mutableSpanningTree0);
      DotExporter<String, String> dotExporter0 = defaultExportSelector0.usingDotNotation();
      assertNotNull(dotExporter0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      UndirectedMutableGraph<String, String> undirectedMutableGraph0 = new UndirectedMutableGraph<String, String>();
      DefaultExportSelector<String, String> defaultExportSelector0 = new DefaultExportSelector<String, String>(undirectedMutableGraph0);
      ExportSelector<String, String> exportSelector0 = defaultExportSelector0.withName("org.apache.commons.graph.export.DefaultExportSelector");
      assertNotNull(exportSelector0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      DefaultExportSelector<String, String> defaultExportSelector0 = new DefaultExportSelector<String, String>((Graph<String, String>) null);
      // Undeclared exception!
      try { 
        defaultExportSelector0.usingDotNotation();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.export.DotExporter", e);
      }
  }
}
