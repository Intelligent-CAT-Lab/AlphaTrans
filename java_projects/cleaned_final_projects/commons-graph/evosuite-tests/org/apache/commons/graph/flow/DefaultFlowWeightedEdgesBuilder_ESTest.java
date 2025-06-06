/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 14:58:50 GMT 2024
 */

package org.apache.commons.graph.flow;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.flow.DefaultFlowWeightedEdgesBuilder;
import org.apache.commons.graph.flow.FromHeadBuilder;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class DefaultFlowWeightedEdgesBuilder_ESTest extends DefaultFlowWeightedEdgesBuilder_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      DefaultFlowWeightedEdgesBuilder<Integer, Integer> defaultFlowWeightedEdgesBuilder0 = new DefaultFlowWeightedEdgesBuilder<Integer, Integer>(directedMutableGraph0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      FromHeadBuilder<Integer, Integer, Integer> fromHeadBuilder0 = defaultFlowWeightedEdgesBuilder0.whereEdgesHaveWeights(mapper0);
      assertNotNull(fromHeadBuilder0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DefaultFlowWeightedEdgesBuilder<Mapper<Integer, Integer>, Integer> defaultFlowWeightedEdgesBuilder0 = new DefaultFlowWeightedEdgesBuilder<Mapper<Integer, Integer>, Integer>((DirectedGraph<Mapper<Integer, Integer>, Integer>) null);
      // Undeclared exception!
      try { 
        defaultFlowWeightedEdgesBuilder0.whereEdgesHaveWeights((Mapper<Integer, Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Function to calculate edges weight can not be null.
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }
}
