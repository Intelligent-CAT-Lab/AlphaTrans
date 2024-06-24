
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


package org.joda.convert;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.convert.AnnotationStringConverterFactory;
import org.joda.convert.StringConverter;
import org.joda.convert.TypedFromStringConverter;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class AnnotationStringConverterFactory_ESTest extends AnnotationStringConverterFactory_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      AnnotationStringConverterFactory annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        annotationStringConverterFactory0.findFromStringConverter((Class<AnnotationStringConverterFactory>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.AnnotationStringConverterFactory", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      AnnotationStringConverterFactory annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        annotationStringConverterFactory0.findConverter((Class<?>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.AnnotationStringConverterFactory", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      AnnotationStringConverterFactory annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE;
      Class<AnnotationStringConverterFactory> class0 = AnnotationStringConverterFactory.class;
      TypedFromStringConverter<AnnotationStringConverterFactory> typedFromStringConverter0 = annotationStringConverterFactory0.findFromStringConverter(class0);
      assertNull(typedFromStringConverter0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      AnnotationStringConverterFactory annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE;
      Class<AnnotationStringConverterFactory> class0 = AnnotationStringConverterFactory.class;
      StringConverter<?> stringConverter0 = annotationStringConverterFactory0.findConverter(class0);
      assertNull(stringConverter0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      AnnotationStringConverterFactory annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE;
      Class<Object> class0 = Object.class;
      TypedFromStringConverter<Object> typedFromStringConverter0 = annotationStringConverterFactory0.findFromStringConverter(class0);
      assertNull(typedFromStringConverter0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      AnnotationStringConverterFactory annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE;
      String string0 = annotationStringConverterFactory0.toString();
      assertEquals("AnnotationStringConverterFactory", string0);
  }
}
