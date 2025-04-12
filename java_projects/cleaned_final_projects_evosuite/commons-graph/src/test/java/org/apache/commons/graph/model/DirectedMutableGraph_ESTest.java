
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


package org.apache.commons.graph.model;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.sql.ClientInfoStatus;
import java.sql.SQLNonTransientConnectionException;
import java.util.ArrayDeque;
import java.util.Locale;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.lang.MockThrowable;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DirectedMutableGraph_ESTest extends DirectedMutableGraph_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DirectedMutableGraph<ArrayDeque<SQLNonTransientConnectionException>, Object> directedMutableGraph0 = new DirectedMutableGraph<ArrayDeque<SQLNonTransientConnectionException>, Object>();
      ArrayDeque<SQLNonTransientConnectionException> arrayDeque0 = new ArrayDeque<SQLNonTransientConnectionException>();
      directedMutableGraph0.decorateAddVertex(arrayDeque0);
      ArrayDeque<SQLNonTransientConnectionException> arrayDeque1 = new ArrayDeque<SQLNonTransientConnectionException>();
      // Undeclared exception!
      try { 
        directedMutableGraph0.decorateAddEdge(arrayDeque1, (Object) null, arrayDeque0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DirectedMutableGraph<Locale.Category, Locale.Category> directedMutableGraph0 = new DirectedMutableGraph<Locale.Category, Locale.Category>();
      Locale.Category locale_Category0 = Locale.Category.DISPLAY;
      directedMutableGraph0.decorateAddVertex(locale_Category0);
      int int0 = directedMutableGraph0.getOutDegree(locale_Category0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DirectedMutableGraph<ArrayDeque<SQLNonTransientConnectionException>, Object> directedMutableGraph0 = new DirectedMutableGraph<ArrayDeque<SQLNonTransientConnectionException>, Object>();
      ArrayDeque<SQLNonTransientConnectionException> arrayDeque0 = new ArrayDeque<SQLNonTransientConnectionException>();
      directedMutableGraph0.addVertex(arrayDeque0);
      int int0 = directedMutableGraph0.getInDegree(arrayDeque0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ArrayDeque<SQLNonTransientConnectionException> arrayDeque0 = new ArrayDeque<SQLNonTransientConnectionException>();
      DirectedMutableGraph<ArrayDeque<SQLNonTransientConnectionException>, Object> directedMutableGraph0 = new DirectedMutableGraph<ArrayDeque<SQLNonTransientConnectionException>, Object>();
      directedMutableGraph0.decorateAddVertex(arrayDeque0);
      directedMutableGraph0.decorateAddEdge(arrayDeque0, arrayDeque0, arrayDeque0);
      int int0 = directedMutableGraph0.getInDegree(arrayDeque0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DirectedMutableGraph<ClientInfoStatus, ArrayDeque<SQLNonTransientConnectionException>> directedMutableGraph0 = new DirectedMutableGraph<ClientInfoStatus, ArrayDeque<SQLNonTransientConnectionException>>();
      ClientInfoStatus clientInfoStatus0 = ClientInfoStatus.REASON_UNKNOWN;
      directedMutableGraph0.decorateAddVertex(clientInfoStatus0);
      directedMutableGraph0.decorateAddEdge(clientInfoStatus0, (ArrayDeque<SQLNonTransientConnectionException>) null, clientInfoStatus0);
      int int0 = directedMutableGraph0.getDegree(clientInfoStatus0);
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DirectedMutableGraph<ArrayDeque<SQLNonTransientConnectionException>, SQLNonTransientConnectionException> directedMutableGraph0 = new DirectedMutableGraph<ArrayDeque<SQLNonTransientConnectionException>, SQLNonTransientConnectionException>();
      ArrayDeque<SQLNonTransientConnectionException> arrayDeque0 = new ArrayDeque<SQLNonTransientConnectionException>();
      // Undeclared exception!
      try { 
        directedMutableGraph0.getOutDegree(arrayDeque0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DirectedMutableGraph<ArrayDeque<SQLNonTransientConnectionException>, Object> directedMutableGraph0 = new DirectedMutableGraph<ArrayDeque<SQLNonTransientConnectionException>, Object>();
      ArrayDeque<SQLNonTransientConnectionException> arrayDeque0 = new ArrayDeque<SQLNonTransientConnectionException>();
      // Undeclared exception!
      try { 
        directedMutableGraph0.getInDegree(arrayDeque0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DirectedMutableGraph<SQLNonTransientConnectionException, SQLNonTransientConnectionException> directedMutableGraph0 = new DirectedMutableGraph<SQLNonTransientConnectionException, SQLNonTransientConnectionException>();
      MockThrowable mockThrowable0 = new MockThrowable();
      SQLNonTransientConnectionException sQLNonTransientConnectionException0 = new SQLNonTransientConnectionException(mockThrowable0);
      directedMutableGraph0.decorateRemoveVertex(sQLNonTransientConnectionException0);
      assertNull(sQLNonTransientConnectionException0.getSQLState());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DirectedMutableGraph<ClientInfoStatus, ArrayDeque<SQLNonTransientConnectionException>> directedMutableGraph0 = new DirectedMutableGraph<ClientInfoStatus, ArrayDeque<SQLNonTransientConnectionException>>();
      ClientInfoStatus clientInfoStatus0 = ClientInfoStatus.REASON_UNKNOWN_PROPERTY;
      Iterable<ClientInfoStatus> iterable0 = directedMutableGraph0.getInbound(clientInfoStatus0);
      assertNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DirectedMutableGraph<ClientInfoStatus, ArrayDeque<SQLNonTransientConnectionException>> directedMutableGraph0 = new DirectedMutableGraph<ClientInfoStatus, ArrayDeque<SQLNonTransientConnectionException>>();
      ClientInfoStatus clientInfoStatus0 = ClientInfoStatus.REASON_UNKNOWN;
      directedMutableGraph0.decorateAddVertex(clientInfoStatus0);
      int int0 = directedMutableGraph0.getDegree(clientInfoStatus0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DirectedMutableGraph<Locale.Category, SQLNonTransientConnectionException> directedMutableGraph0 = new DirectedMutableGraph<Locale.Category, SQLNonTransientConnectionException>();
      Locale.Category locale_Category0 = Locale.Category.FORMAT;
      Iterable<Locale.Category> iterable0 = directedMutableGraph0.getOutbound(locale_Category0);
      assertNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DirectedMutableGraph<SQLNonTransientConnectionException, ArrayDeque<Object>> directedMutableGraph0 = new DirectedMutableGraph<SQLNonTransientConnectionException, ArrayDeque<Object>>();
      ArrayDeque<Object> arrayDeque0 = new ArrayDeque<Object>();
      // Undeclared exception!
      try { 
        directedMutableGraph0.decorateRemoveEdge(arrayDeque0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DirectedMutableGraph<ClientInfoStatus, ArrayDeque<SQLNonTransientConnectionException>> directedMutableGraph0 = new DirectedMutableGraph<ClientInfoStatus, ArrayDeque<SQLNonTransientConnectionException>>();
      ClientInfoStatus clientInfoStatus0 = ClientInfoStatus.REASON_UNKNOWN;
      // Undeclared exception!
      try { 
        directedMutableGraph0.getDegree(clientInfoStatus0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e);
      }
  }
}
