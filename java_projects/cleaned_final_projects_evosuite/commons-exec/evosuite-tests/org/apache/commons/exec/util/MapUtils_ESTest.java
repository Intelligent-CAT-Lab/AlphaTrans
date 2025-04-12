
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


package org.apache.commons.exec.util;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.AbstractMap;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.exec.util.MapUtils;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MapUtils_ESTest extends MapUtils_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      HashMap<String, String> hashMap1 = new HashMap<String, String>(hashMap0);
      hashMap1.put("", " e]+a{Rx(}+`z,");
      hashMap0.put((String) null, "xl!@i7$!oQ`");
      Map<String, String> map0 = MapUtils.merge((Map<String, String>) hashMap1, (Map<String, String>) hashMap0);
      assertEquals(1, hashMap1.size());
      assertEquals(2, map0.size());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Map<AbstractMap.SimpleImmutableEntry<AbstractMap.SimpleImmutableEntry, AbstractMap.SimpleImmutableEntry>, AbstractMap.SimpleImmutableEntry<String, String>> map0 = MapUtils.copy((Map<AbstractMap.SimpleImmutableEntry<AbstractMap.SimpleImmutableEntry, AbstractMap.SimpleImmutableEntry>, AbstractMap.SimpleImmutableEntry<String, String>>) null);
      assertNull(map0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Map<String, AbstractMap.SimpleImmutableEntry<AbstractMap.SimpleImmutableEntry, AbstractMap.SimpleImmutableEntry>> map0 = MapUtils.prefix((Map<AbstractMap.SimpleImmutableEntry<String, String>, AbstractMap.SimpleImmutableEntry<AbstractMap.SimpleImmutableEntry, AbstractMap.SimpleImmutableEntry>>) null, "");
      assertNull(map0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      hashMap0.put("+3Kon&-D", "+3Kon&-D");
      Map<String, String> map0 = MapUtils.merge((Map<String, String>) hashMap0, (Map<String, String>) null);
      assertEquals(1, map0.size());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      HashMap<AbstractMap.SimpleImmutableEntry<String, String>, String> hashMap0 = new HashMap<AbstractMap.SimpleImmutableEntry<String, String>, String>();
      Map<AbstractMap.SimpleImmutableEntry<String, String>, String> map0 = MapUtils.merge((Map<AbstractMap.SimpleImmutableEntry<String, String>, String>) hashMap0, (Map<AbstractMap.SimpleImmutableEntry<String, String>, String>) hashMap0);
      assertEquals(0, map0.size());
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Map<String, String> map0 = MapUtils.merge((Map<String, String>) null, (Map<String, String>) null);
      assertNull(map0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      HashMap<String, AbstractMap.SimpleImmutableEntry<String, String>> hashMap0 = new HashMap<String, AbstractMap.SimpleImmutableEntry<String, String>>();
      Map<String, AbstractMap.SimpleImmutableEntry<String, String>> map0 = MapUtils.merge((Map<String, AbstractMap.SimpleImmutableEntry<String, String>>) null, (Map<String, AbstractMap.SimpleImmutableEntry<String, String>>) hashMap0);
      assertEquals(0, map0.size());
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      MapUtils mapUtils0 = new MapUtils();
  }
}
