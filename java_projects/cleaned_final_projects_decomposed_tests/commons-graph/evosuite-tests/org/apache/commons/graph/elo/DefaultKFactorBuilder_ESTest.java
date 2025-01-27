/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 14:38:48 GMT 2024
 */

package org.apache.commons.graph.elo;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.elo.DefaultKFactorBuilder;
import org.apache.commons.graph.elo.GameResult;
import org.apache.commons.graph.elo.PlayersRank;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class DefaultKFactorBuilder_ESTest extends DefaultKFactorBuilder_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      DirectedMutableGraph<GameResult, GameResult> directedMutableGraph0 = new DirectedMutableGraph<GameResult, GameResult>();
      Double double0 = new Double(0.5);
      PlayersRank<GameResult> playersRank0 = (PlayersRank<GameResult>) mock(PlayersRank.class, new ViolatedAssumptionAnswer());
      doReturn(double0, double0, double0, double0).when(playersRank0).getRanking(any(org.apache.commons.graph.elo.GameResult.class));
      DefaultKFactorBuilder<GameResult> defaultKFactorBuilder0 = new DefaultKFactorBuilder<GameResult>(directedMutableGraph0, playersRank0);
      GameResult gameResult0 = GameResult.DRAW;
      directedMutableGraph0.addVertex(gameResult0);
      GameResult gameResult1 = GameResult.WIN;
      directedMutableGraph0.addVertex(gameResult1);
      directedMutableGraph0.addEdge(gameResult0, gameResult1, gameResult1);
      defaultKFactorBuilder0.withKFactor((-1));
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DirectedMutableGraph<GameResult, GameResult> directedMutableGraph0 = new DirectedMutableGraph<GameResult, GameResult>();
      Double double0 = new Double(2324.7);
      Double double1 = new Double((-1238.378389823641));
      PlayersRank<GameResult> playersRank0 = (PlayersRank<GameResult>) mock(PlayersRank.class, new ViolatedAssumptionAnswer());
      doReturn(double0, double1, double1, double0).when(playersRank0).getRanking(any(org.apache.commons.graph.elo.GameResult.class));
      DefaultKFactorBuilder<GameResult> defaultKFactorBuilder0 = new DefaultKFactorBuilder<GameResult>(directedMutableGraph0, playersRank0);
      GameResult gameResult0 = GameResult.DRAW;
      directedMutableGraph0.addVertex(gameResult0);
      directedMutableGraph0.addEdge(gameResult0, gameResult0, gameResult0);
      defaultKFactorBuilder0.withKFactor((-1250));
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      DefaultKFactorBuilder<Object> defaultKFactorBuilder0 = new DefaultKFactorBuilder<Object>((DirectedGraph<Object, GameResult>) null, (PlayersRank<Object>) null);
      // Undeclared exception!
      try { 
        defaultKFactorBuilder0.withDefaultKFactor();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.elo.DefaultKFactorBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      DirectedMutableGraph<GameResult, GameResult> directedMutableGraph0 = new DirectedMutableGraph<GameResult, GameResult>();
      GameResult gameResult0 = GameResult.WIN;
      directedMutableGraph0.addVertex(gameResult0);
      directedMutableGraph0.addEdge(gameResult0, gameResult0, gameResult0);
      PlayersRank<GameResult> playersRank0 = (PlayersRank<GameResult>) mock(PlayersRank.class, new ViolatedAssumptionAnswer());
      doReturn((Double) null).when(playersRank0).getRanking(any(org.apache.commons.graph.elo.GameResult.class));
      DefaultKFactorBuilder<GameResult> defaultKFactorBuilder0 = new DefaultKFactorBuilder<GameResult>(directedMutableGraph0, playersRank0);
      // Undeclared exception!
      try { 
        defaultKFactorBuilder0.withKFactor(1714);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.elo.DefaultKFactorBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      DirectedMutableGraph<Object, GameResult> directedMutableGraph0 = new DirectedMutableGraph<Object, GameResult>();
      DefaultKFactorBuilder<Object> defaultKFactorBuilder0 = new DefaultKFactorBuilder<Object>(directedMutableGraph0, (PlayersRank<Object>) null);
      defaultKFactorBuilder0.withDefaultKFactor();
  }
}
