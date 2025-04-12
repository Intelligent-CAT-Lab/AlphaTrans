
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


package org.apache.commons.cli;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.Collection;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import org.apache.commons.cli.AmbiguousOptionException;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class AmbiguousOptionException_ESTest extends AmbiguousOptionException_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      AmbiguousOptionException ambiguousOptionException0 = null;
      try {
        ambiguousOptionException0 = new AmbiguousOptionException("b+ypAm<DOx,Ai~yI", (Collection<String>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.AmbiguousOptionException", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Locale.IsoCountryCode locale_IsoCountryCode0 = Locale.IsoCountryCode.PART3;
      Set<String> set0 = Locale.getISOCountries(locale_IsoCountryCode0);
      AmbiguousOptionException ambiguousOptionException0 = new AmbiguousOptionException("'  (could be: ", set0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      List<String> list0 = List.of("d=7 pDtt,nCa");
      AmbiguousOptionException ambiguousOptionException0 = new AmbiguousOptionException("d=7 pDtt,nCa", list0);
      Collection<String> collection0 = ambiguousOptionException0.getMatchingOptions();
      assertTrue(collection0.contains("d=7 pDtt,nCa"));
  }
}
