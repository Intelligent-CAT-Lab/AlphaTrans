
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
import java.lang.reflect.Type;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.convert.StringConverter;
import org.joda.convert.TypeStringConverterFactory;
import org.joda.convert.Types;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class TypeStringConverterFactory_ESTest extends TypeStringConverterFactory_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Class<Types.WildcardTypeImpl> class0 = Types.WildcardTypeImpl.class;
      TypeStringConverterFactory.TypeStringConverter typeStringConverterFactory_TypeStringConverter0 = new TypeStringConverterFactory.TypeStringConverter(class0);
      String string0 = typeStringConverterFactory_TypeStringConverter0.convertToString((Type) class0);
      assertEquals("org.joda.convert.Types$WildcardTypeImpl", string0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      TypeStringConverterFactory typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        typeStringConverterFactory0.findConverter((Class<?>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      TypeStringConverterFactory typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE;
      Class<Types.WildcardTypeImpl> class0 = Types.WildcardTypeImpl.class;
      StringConverter<?> stringConverter0 = typeStringConverterFactory0.findConverter(class0);
      assertNotNull(stringConverter0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      TypeStringConverterFactory typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE;
      Class<Object> class0 = Object.class;
      StringConverter<?> stringConverter0 = typeStringConverterFactory0.findConverter(class0);
      assertNull(stringConverter0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      Class<Object> class0 = Object.class;
      TypeStringConverterFactory.TypeStringConverter typeStringConverterFactory_TypeStringConverter0 = new TypeStringConverterFactory.TypeStringConverter(class0);
      Class<Types.WildcardTypeImpl> class1 = Types.WildcardTypeImpl.class;
      // Undeclared exception!
      try { 
        typeStringConverterFactory_TypeStringConverter0.convertFromString(class1, "");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // java.lang.ClassNotFoundException: Class '.class' should be in target project, but could not be found!
         //
         verifyException("org.joda.convert.TypeUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Class<Object> class0 = Object.class;
      TypeStringConverterFactory.TypeStringConverter typeStringConverterFactory_TypeStringConverter0 = new TypeStringConverterFactory.TypeStringConverter(class0);
      Class<?> class1 = typeStringConverterFactory_TypeStringConverter0.getEffectiveType();
      assertFalse(class1.isPrimitive());
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      Class<Object> class0 = Object.class;
      TypeStringConverterFactory.TypeStringConverter typeStringConverterFactory_TypeStringConverter0 = new TypeStringConverterFactory.TypeStringConverter(class0);
      // Undeclared exception!
      try { 
        typeStringConverterFactory_TypeStringConverter0.convertToString((Type) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.System", e);
      }
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      TypeStringConverterFactory typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE;
      String string0 = typeStringConverterFactory0.toString();
      assertEquals("TypeStringConverterFactory", string0);
  }
}
