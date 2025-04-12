
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
import org.apache.commons.graph.scc.TarjanVertexMetaInfo;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class TarjanVertexMetaInfo_ESTest extends TarjanVertexMetaInfo_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      TarjanVertexMetaInfo tarjanVertexMetaInfo0 = new TarjanVertexMetaInfo();
      tarjanVertexMetaInfo0.setIndex((-1184));
      boolean boolean0 = tarjanVertexMetaInfo0.hasUndefinedIndex();
      assertEquals((-1184), tarjanVertexMetaInfo0.getIndex());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      TarjanVertexMetaInfo tarjanVertexMetaInfo0 = new TarjanVertexMetaInfo();
      tarjanVertexMetaInfo0.setLowLink(2901);
      int int0 = tarjanVertexMetaInfo0.getLowLink();
      assertEquals(2901, int0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      TarjanVertexMetaInfo tarjanVertexMetaInfo0 = new TarjanVertexMetaInfo();
      assertTrue(tarjanVertexMetaInfo0.hasUndefinedIndex());
      
      tarjanVertexMetaInfo0.setIndex(0);
      int int0 = tarjanVertexMetaInfo0.getIndex();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      TarjanVertexMetaInfo tarjanVertexMetaInfo0 = new TarjanVertexMetaInfo();
      tarjanVertexMetaInfo0.setIndex(877);
      int int0 = tarjanVertexMetaInfo0.getIndex();
      assertEquals(877, int0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      TarjanVertexMetaInfo tarjanVertexMetaInfo0 = new TarjanVertexMetaInfo();
      boolean boolean0 = tarjanVertexMetaInfo0.hasUndefinedIndex();
      assertTrue(boolean0);
      assertEquals((-1), tarjanVertexMetaInfo0.getLowLink());
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      TarjanVertexMetaInfo tarjanVertexMetaInfo0 = new TarjanVertexMetaInfo();
      assertEquals((-1), tarjanVertexMetaInfo0.getIndex());
      
      tarjanVertexMetaInfo0.setIndex(0);
      boolean boolean0 = tarjanVertexMetaInfo0.hasUndefinedIndex();
      assertEquals(0, tarjanVertexMetaInfo0.getIndex());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      TarjanVertexMetaInfo tarjanVertexMetaInfo0 = new TarjanVertexMetaInfo();
      assertEquals((-1), tarjanVertexMetaInfo0.getLowLink());
      
      tarjanVertexMetaInfo0.setLowLink(0);
      int int0 = tarjanVertexMetaInfo0.getLowLink();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      TarjanVertexMetaInfo tarjanVertexMetaInfo0 = new TarjanVertexMetaInfo();
      int int0 = tarjanVertexMetaInfo0.getLowLink();
      assertEquals((-1), tarjanVertexMetaInfo0.getIndex());
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      TarjanVertexMetaInfo tarjanVertexMetaInfo0 = new TarjanVertexMetaInfo();
      int int0 = tarjanVertexMetaInfo0.getIndex();
      assertEquals((-1), int0);
      assertEquals((-1), tarjanVertexMetaInfo0.getLowLink());
  }
}
