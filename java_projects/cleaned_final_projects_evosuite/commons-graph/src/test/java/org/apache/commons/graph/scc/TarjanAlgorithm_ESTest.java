
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


package org.apache.commons.graph.scc;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.LinkedHashSet;
import java.util.Set;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.scc.TarjanAlgorithm;
import org.apache.commons.graph.scc.TarjanVertexMetaInfo;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class TarjanAlgorithm_ESTest extends TarjanAlgorithm_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      DirectedMutableGraph<TarjanVertexMetaInfo, TarjanVertexMetaInfo> directedMutableGraph0 = new DirectedMutableGraph<TarjanVertexMetaInfo, TarjanVertexMetaInfo>();
      TarjanAlgorithm<TarjanVertexMetaInfo, TarjanVertexMetaInfo> tarjanAlgorithm0 = new TarjanAlgorithm<TarjanVertexMetaInfo, TarjanVertexMetaInfo>(directedMutableGraph0);
      Set<Set<TarjanVertexMetaInfo>> set0 = tarjanAlgorithm0.perform();
      assertTrue(set0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      TarjanAlgorithm<TarjanVertexMetaInfo, TarjanVertexMetaInfo> tarjanAlgorithm0 = new TarjanAlgorithm<TarjanVertexMetaInfo, TarjanVertexMetaInfo>((DirectedGraph<TarjanVertexMetaInfo, TarjanVertexMetaInfo>) null);
      // Undeclared exception!
      try { 
        tarjanAlgorithm0.perform();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.scc.TarjanAlgorithm", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      DirectedMutableGraph<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>>();
      LinkedHashSet<TarjanVertexMetaInfo> linkedHashSet0 = new LinkedHashSet<TarjanVertexMetaInfo>();
      directedMutableGraph0.addVertex(linkedHashSet0);
      TarjanVertexMetaInfo tarjanVertexMetaInfo0 = new TarjanVertexMetaInfo();
      linkedHashSet0.add(tarjanVertexMetaInfo0);
      directedMutableGraph0.addVertex(linkedHashSet0);
      TarjanAlgorithm<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>> tarjanAlgorithm0 = new TarjanAlgorithm<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>>(directedMutableGraph0);
      Set<Set<LinkedHashSet<TarjanVertexMetaInfo>>> set0 = tarjanAlgorithm0.perform();
      assertEquals(1, set0.size());
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      DirectedMutableGraph<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>>();
      LinkedHashSet<TarjanVertexMetaInfo> linkedHashSet0 = new LinkedHashSet<TarjanVertexMetaInfo>();
      TarjanVertexMetaInfo tarjanVertexMetaInfo0 = new TarjanVertexMetaInfo();
      linkedHashSet0.add(tarjanVertexMetaInfo0);
      directedMutableGraph0.addVertex(linkedHashSet0);
      LinkedHashSet<TarjanVertexMetaInfo> linkedHashSet1 = new LinkedHashSet<TarjanVertexMetaInfo>();
      directedMutableGraph0.addVertex(linkedHashSet1);
      directedMutableGraph0.addEdge(linkedHashSet0, linkedHashSet0, linkedHashSet1);
      TarjanAlgorithm<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>> tarjanAlgorithm0 = new TarjanAlgorithm<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>>(directedMutableGraph0);
      Set<Set<LinkedHashSet<TarjanVertexMetaInfo>>> set0 = tarjanAlgorithm0.perform();
      assertEquals(2, set0.size());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      DirectedMutableGraph<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>>();
      LinkedHashSet<TarjanVertexMetaInfo> linkedHashSet0 = new LinkedHashSet<TarjanVertexMetaInfo>();
      directedMutableGraph0.addVertex(linkedHashSet0);
      directedMutableGraph0.addEdge(linkedHashSet0, linkedHashSet0, linkedHashSet0);
      TarjanAlgorithm<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>> tarjanAlgorithm0 = new TarjanAlgorithm<LinkedHashSet<TarjanVertexMetaInfo>, LinkedHashSet<TarjanVertexMetaInfo>>(directedMutableGraph0);
      Set<Set<LinkedHashSet<TarjanVertexMetaInfo>>> set0 = tarjanAlgorithm0.perform();
      assertEquals(1, set0.size());
  }
}
