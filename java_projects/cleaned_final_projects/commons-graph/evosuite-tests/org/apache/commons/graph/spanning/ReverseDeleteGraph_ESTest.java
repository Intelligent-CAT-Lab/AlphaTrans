/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 14:54:13 GMT 2024
 */

package org.apache.commons.graph.spanning;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.Collection;
import java.util.LinkedList;
import java.util.List;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.spanning.ReverseDeleteGraph;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class ReverseDeleteGraph_ESTest extends ReverseDeleteGraph_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer1 = integerWeightBaseOperations0.identity();
      linkedList0.add(integer1);
      Integer integer2 = new Integer(0);
      VertexPair<Integer> vertexPair0 = reverseDeleteGraph0.getVertices1(integer2);
      assertNull(vertexPair0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      linkedList0.add(integer0);
      inMemoryPath0.addConnectionInTail(integer0, integer0, integer0);
      VertexPair<Integer> vertexPair0 = reverseDeleteGraph0.getVertices1(integer0);
      assertNotNull(vertexPair0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      linkedList0.add(integer0);
      int int0 = reverseDeleteGraph0.getSize();
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      inMemoryPath0.addConnectionInTail(integer0, integer0, integer0);
      int int0 = reverseDeleteGraph0.getOrder();
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      inMemoryPath0.addConnectionInTail(integer0, integer0, integer0);
      boolean boolean0 = reverseDeleteGraph0.containsVertex(integer0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      inMemoryPath0.addConnectionInTail(integer0, integer0, integer0);
      boolean boolean0 = reverseDeleteGraph0.containsEdge(integer0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(directedMutableGraph0, (Collection<Integer>) null, (Collection<Integer>) null);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getVertices1((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>((Graph<Integer, Integer>) null, linkedList0, linkedList0);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getVertices0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(undirectedMutableGraph0, (Collection<Integer>) null, (Collection<Integer>) null);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getSize();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>((Graph<Integer, Integer>) null, linkedList0, linkedList0);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getOrder();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(undirectedMutableGraph0, (Collection<Integer>) null, (Collection<Integer>) null);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getEdges();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.ArrayList", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      List<Integer> list0 = List.of();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(directedMutableGraph0, list0, list0);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getEdge((Integer) null, (Integer) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>((Graph<Integer, Integer>) null, linkedList0, linkedList0);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getEdge((Integer) null, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Integer integer0 = Integer.valueOf((-110));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getEdge(integer0, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to construct a Vertex with a null tail
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(directedMutableGraph0, linkedList0, linkedList0);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getConnectedVertices((Integer) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>((Graph<Integer, Integer>) null, linkedList0, linkedList0);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getConnectedVertices((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getConnectedVertices((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to get the degree of a null vertex
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer1 = integerWeightBaseOperations0.inverse(integer0);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getConnectedVertices(integer1);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Impossible to get the degree of input vertex; 1 not contained in this path
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>((Graph<Integer, Integer>) null, linkedList0, linkedList0);
      Integer integer0 = new Integer((-55));
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.containsVertex(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>((Graph<Integer, Integer>) null, linkedList0, linkedList0);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.containsEdge((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      Integer integer1 = reverseDeleteGraph0.getEdge(integer0, integer0);
      assertNull(integer1);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Integer integer0 = new Integer((-88));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      linkedList0.add((Integer) null);
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      Integer integer1 = reverseDeleteGraph0.getEdge(integer0, integer0);
      assertNull(integer1);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Integer integer0 = new Integer((-78));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      List<Integer> list0 = List.of(integer0, integer0, integer0, integer0, integer0, integer0);
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, list0);
      VertexPair<Integer> vertexPair0 = reverseDeleteGraph0.getVertices1(integer0);
      assertNull(vertexPair0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer1 = integerWeightBaseOperations0.identity();
      linkedList0.add(integer1);
      VertexPair<Integer> vertexPair0 = reverseDeleteGraph0.getVertices1(integer0);
      assertNull(vertexPair0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      int int0 = reverseDeleteGraph0.getOrder();
      assertFalse(linkedList0.contains(int0));
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(1);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, mapper0);
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryWeightedPath0, linkedList0, linkedList0);
      // Undeclared exception!
      try { 
        reverseDeleteGraph0.getDegree(integer0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Integer integer0 = new Integer((-78));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      int int0 = reverseDeleteGraph0.getSize();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      boolean boolean0 = reverseDeleteGraph0.containsVertex(integer0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Integer integer0 = new Integer((-87));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      ReverseDeleteGraph<Integer, Integer> reverseDeleteGraph0 = new ReverseDeleteGraph<Integer, Integer>(inMemoryPath0, linkedList0, linkedList0);
      boolean boolean0 = reverseDeleteGraph0.containsEdge(integer0);
      assertFalse(boolean0);
  }
}
